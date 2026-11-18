import { CO2_STATS } from '../options.js';

const pct = (v, lo, hi) => Math.max(0, Math.min(100, ((v - lo) / (hi - lo)) * 100));

export default function ResultCard({ result }) {
  if (!result) return null;

  const { prediction, r2 } = result;
  const diff = prediction - CO2_STATS.mean;
  const r2Num = r2 === null || r2 === undefined ? null : Number(r2);

  return (
    <div className="card result">
      <h2>예측 결과</h2>

      <div className="big">
        {prediction.toFixed(1)}
        <small> g/km</small>
      </div>
      <p className="sub">
        데이터 평균({CO2_STATS.mean} g/km)보다{' '}
        <b>{Math.abs(diff).toFixed(1)} g/km {diff >= 0 ? '많은' : '적은'}</b> 수준입니다.
      </p>

      <div className="meter" aria-hidden="true">
        <div className="meter-fill" style={{ width: `${pct(prediction, CO2_STATS.min, CO2_STATS.max)}%` }} />
        <div className="meter-mean" style={{ left: `${pct(CO2_STATS.mean, CO2_STATS.min, CO2_STATS.max)}%` }} />
      </div>
      <div className="range-scale">
        <span>{CO2_STATS.min}</span>
        <span>평균 {CO2_STATS.mean}</span>
        <span>{CO2_STATS.max}</span>
      </div>

      {r2Num !== null && !Number.isNaN(r2Num) && (
        <div className="metric">
          <div className="metric-head">
            <span>모델 성능 (R² Score)</span>
            <b>{r2Num.toFixed(4)}</b>
          </div>
          <div className="bar"><div style={{ width: `${pct(r2Num, 0, 1)}%` }} /></div>
          <p className="note">
            학습에 쓰지 않은 테스트 데이터 기준으로, 모델이 배출량 변동의 약{' '}
            {(r2Num * 100).toFixed(1)}%를 설명합니다.
          </p>
        </div>
      )}

      <p className="note">
        ※ 예측값은 입력한 사양과 비슷한 차량들의 통계적 추정이며, 실제 인증 수치와 다를 수 있습니다.
      </p>
    </div>
  );
}
