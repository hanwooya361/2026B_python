# CO₂ 배출량 예측 — React 프론트엔드

## 실행
```bash
npm install
npm run dev        # http://localhost:5173
```
Spring Boot가 아직 없으면 가짜 서버로 화면만 먼저 확인:
```bash
npm run mock       # http://localhost:8080/api/predict/stream  (별도 터미널)
npm run test:sse   # SSE 파서 단위 테스트
```
서버 주소를 바꾸려면 `.env.example`을 `.env`로 복사해 `VITE_API_URL`을 수정.

## 백엔드와의 약속 (Spring Boot가 지켜야 할 것)
- `POST /api/predict/stream`, 본문(JSON):
  `{ "make", "vehicle_class", "engine_size", "cylinders", "transmission", "fuel_type" }`
  (키 이름은 학습 때 쓴 특성 이름과 같음)
- 응답: `Content-Type: text/event-stream`
  ```
  event: status
  data: 모델이 배출량을 계산하는 중...

  event: result
  data: {"prediction": 196.3, "r2": 0.93}

  event: error
  data: 오류 메시지
  ```
- 브라우저(5173)에서 호출하므로 Spring 쪽 CORS에서 `http://localhost:5173` 허용 필요.

## 구조
- `src/api.js` axios POST + `onDownloadProgress`로 SSE 스트림 수신
- `src/sse.js` SSE 텍스트 파서(순수 함수)
- `src/options.js` 입력 선택지(데이터에서 추출) + 한글 라벨
- `src/components/` PredictForm / StatusTimeline / ResultCard
