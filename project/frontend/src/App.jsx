import { useEffect, useRef, useState } from 'react';
import axios from 'axios';
import PredictForm from './components/PredictForm.jsx';
import StatusTimeline from './components/StatusTimeline.jsx';
import ResultCard from './components/ResultCard.jsx';
import { streamPredict, describeError } from './api.js';
import './App.css';

const DEFAULTS = {
  make: 'HYUNDAI',
  vehicle_class: 'COMPACT',
  engine_size: 2.0,
  cylinders: 4,
  transmission: 'AS6',
  fuel_type: 'X',
};

export default function App() {
  const [form, setForm] = useState(DEFAULTS);
  const [messages, setMessages] = useState([]);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const abortRef = useRef(null);

  // 화면을 떠날 때 진행 중인 요청 정리
  useEffect(() => () => abortRef.current?.abort(), []);

  const handleSubmit = async () => {
    abortRef.current?.abort(); // 이전 요청이 남아 있으면 취소
    const controller = new AbortController();
    abortRef.current = controller;

    setMessages([]);
    setResult(null);
    setError('');
    setLoading(true);

    // 백엔드(FastAPI)가 기대하는 키 이름과 동일 — 학습 때 쓴 특성과 같아야 함
    const payload = {
      make: form.make,
      vehicle_class: form.vehicle_class,
      engine_size: Number(form.engine_size),
      cylinders: Number(form.cylinders),
      transmission: form.transmission,
      fuel_type: form.fuel_type,
    };

    try {
      await streamPredict(payload, {
        signal: controller.signal,
        onStatus: (msg) => setMessages((prev) => [...prev, msg]),
        onResult: (r) => setResult(r),
        onError: (msg) => setError(msg),
      });
    } catch (e) {
      if (!axios.isCancel(e)) setError(describeError(e));
    } finally {
      if (abortRef.current === controller) setLoading(false);
    }
  };

  return (
    <div className="page">
      <header className="hero">
        <h1>자동차 CO₂ 배출량 예측</h1>
        <p>차량 사양을 입력하면 LightGBM 모델이 1km당 CO₂ 배출량(g/km)을 예측합니다.</p>
      </header>

      <main className="layout">
        <PredictForm form={form} setForm={setForm} onSubmit={handleSubmit} loading={loading} />
        <div className="side">
          <StatusTimeline messages={messages} loading={loading} error={error} />
          <ResultCard result={result} />
          {!loading && !error && messages.length === 0 && !result && (
            <div className="card empty">왼쪽에서 사양을 고르고 예측하기를 눌러 보세요.</div>
          )}
        </div>
      </main>

      <footer className="foot">
        React · axios(SSE) → Spring Boot(WebClient) → FastAPI(LightGBM) · 데이터: 캐나다 정부 연료소비등급
      </footer>
    </div>
  );
}
