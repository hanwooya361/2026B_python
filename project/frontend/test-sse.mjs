// node test-sse.mjs : SSE 파서 단위 테스트 (서버/브라우저 불필요)
import assert from 'node:assert/strict';
import { parseSse } from './src/sse.js';

// 1) 완성된 이벤트 2개
let r = parseSse('event: status\ndata: 모델 로딩\n\nevent: result\ndata: {"prediction":196.3,"r2":0.93}\n\n');
assert.equal(r.events.length, 2);
assert.deepEqual(r.events[0], { event: 'status', data: '모델 로딩' });
assert.equal(JSON.parse(r.events[1].data).prediction, 196.3);
assert.equal(r.rest, '');

// 2) 조각난 입력: 이벤트 중간에서 끊겨도 rest로 이어붙이면 복원
let a = parseSse('event: status\ndata: 입력 검');
assert.equal(a.events.length, 0);
let b = parseSse(a.rest + '증 중\n\n');
assert.deepEqual(b.events, [{ event: 'status', data: '입력 검증 중' }]);

// 3) 이벤트 이름이 없으면 message, \r\n, 주석, 여러 줄 data
r = parseSse(': keep-alive\r\n\r\ndata: 안녕\r\n\r\ndata: a\ndata: b\n\n');
assert.deepEqual(r.events, [
  { event: 'message', data: '안녕' },
  { event: 'message', data: 'a\nb' },
]);

// 4) \r\n 이 청크 경계에서 갈라져도 정상 처리
a = parseSse('event: status\r');
b = parseSse(a.rest + '\ndata: ok\r\n\r\n');
assert.deepEqual(b.events, [{ event: 'status', data: 'ok' }]);

console.log('SSE 파서 테스트 통과 (4/4)');
