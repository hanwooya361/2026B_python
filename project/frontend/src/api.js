import axios from 'axios';

// Spring Boot 게이트웨이 기본 주소
//   GET  {API_URL}/subscribe  → SSE 구독 (EventSource)
//   POST {API_URL}            → 추론 요청 접수 (axios, 즉시 응답)
export const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8080/api/predict';

const tryJson = (text) => {
  try {
    return JSON.parse(text);
  } catch {
    return null;
  }
};

/**
 * 흐름
 *  1) EventSource로 SSE를 먼저 구독한다 (결과를 놓치지 않기 위해 구독이 먼저)
 *  2) 연결이 열리면 axios로 POST → Spring은 "접수"만 응답하고 바로 리턴 (2단계: 추론 중)
 *  3) 추론이 끝나면 Spring이 SSE로 보낸다 (3단계)
 *       event: result  data: {"prediction": 196.3, "r2": 0.93}
 *       event: fail    data: 오류 메시지
 */
export function streamPredict(payload, { onStatus, onResult, onError, signal }) {
  return new Promise((resolve, reject) => {
    const es = new EventSource(`${API_URL}/subscribe`);
    let sent = false; // POST를 이미 보냈는지 (재연결 시 중복 방지)
    let finished = false; // result 또는 fail을 받았는지

    const close = () => {
      es.close();
      signal?.removeEventListener('abort', onAbort);
    };
    const onAbort = () => {
      finished = true;
      close();
      reject(new axios.CanceledError('canceled'));
    };
    signal?.addEventListener('abort', onAbort);

    es.addEventListener('result', (e) => {
      const parsed = tryJson(e.data);
      finished = true;
      close();
      if (parsed && 'prediction' in parsed) {
        onResult?.({
          prediction: Number(parsed.prediction),
          r2: parsed.r2 ?? null,
        });
      } else {
        onError?.('결과 형식이 올바르지 않습니다.');
      }
      resolve();
    });

    es.addEventListener('fail', (e) => {
      finished = true;
      close();
      onError?.(e.data);
      resolve();
    });

    es.onopen = async () => {
      if (sent) return;
      sent = true;
      onStatus?.('SSE 연결 완료, 추론을 요청하는 중...');
      try {
        await axios.post(API_URL, payload, { signal });
        onStatus?.('추론 중입니다...');
      } catch (err) {
        finished = true;
        close();
        reject(err);
      }
    };

    es.onerror = () => {
      if (finished) return;
      finished = true;
      close();
      const err = new Error('SSE 연결이 끊어졌습니다.');
      err.code = 'ERR_NETWORK';
      reject(err);
    };
  });
}

export function describeError(e) {
  if (e?.response) {
    return `서버 오류 (HTTP ${e.response.status}). Spring Boot와 FastAPI 로그를 확인하세요.`;
  }
  if (e?.code === 'ERR_NETWORK' || e?.request) {
    return '서버에 연결할 수 없습니다. Spring Boot가 켜져 있는지, 주소와 CORS 설정을 확인하세요.';
  }
  return e?.message ?? '알 수 없는 오류가 발생했습니다.';
}
