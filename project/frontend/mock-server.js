// Spring Boot 없이 화면만 먼저 확인하는 가짜 서버 (의존성 없음)
//   실행: npm run mock
//   GET  http://localhost:8080/api/predict/subscribe  (SSE 구독)
//   POST http://localhost:8080/api/predict            (접수 후 즉시 응답, 결과는 SSE로)
import http from 'node:http';

const PORT = process.env.PORT || 8080;
const cors = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Accept',
};
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const subscribers = new Set();
const sendAll = (event, data) => {
  for (const res of subscribers) res.write(`event: ${event}\ndata: ${data}\n\n`);
};

http
  .createServer(async (req, res) => {
    if (req.method === 'OPTIONS') {
      res.writeHead(204, cors);
      return res.end();
    }

    if (req.method === 'GET' && req.url === '/api/predict/subscribe') {
      res.writeHead(200, {
        ...cors,
        'Content-Type': 'text/event-stream; charset=utf-8',
        'Cache-Control': 'no-cache',
        Connection: 'keep-alive',
      });
      res.write(': connected\n\n');
      subscribers.add(res);
      req.on('close', () => subscribers.delete(res));
      return;
    }

    if (req.method === 'POST' && req.url === '/api/predict') {
      let body = '';
      for await (const chunk of req) body += chunk;
      const x = JSON.parse(body || '{}');
      console.log('요청:', x);

      res.writeHead(200, { ...cors, 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('추론 요청 접수'); // 2단계: 즉시 리턴

      await sleep(1500); // 추론 중이라고 가정
      const fuelAdj = { Z: 6, X: 0, D: 12, E: -8, N: -15 }[x.fuel_type] ?? 0;
      const pred = 55 + Number(x.engine_size) * 38 + Number(x.cylinders) * 6 + fuelAdj;
      sendAll('result', JSON.stringify({ prediction: Math.round(pred * 10) / 10, r2: 0.9312 }));
      return;
    }

    res.writeHead(404, cors);
    res.end();
  })
  .listen(PORT, () => console.log(`mock server: http://localhost:${PORT}/api/predict`));
