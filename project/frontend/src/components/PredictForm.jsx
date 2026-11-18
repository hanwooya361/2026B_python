import { OPTIONS, brandLabel, classLabel, fuelLabel, transLabel } from '../options.js';

const [ENGINE_MIN, ENGINE_MAX] = OPTIONS.engine_size;

function Field({ label, hint, children }) {
  return (
    <div className="field">
      <div className="field-head">
        <label>{label}</label>
        {hint && <span className="hint">{hint}</span>}
      </div>
      {children}
    </div>
  );
}

export default function PredictForm({ form, setForm, onSubmit, loading }) {
  const set = (key) => (e) => setForm((f) => ({ ...f, [key]: e.target.value }));

  const submit = (e) => {
    e.preventDefault();
    onSubmit();
  };

  return (
    <form className="card form" onSubmit={submit}>
      <h2>차량 사양 입력</h2>

      <div className="grid-2">
        <Field label="제조사">
          <select value={form.make} onChange={set('make')}>
            {OPTIONS.make.map((v) => (
              <option key={v} value={v}>{brandLabel(v)}</option>
            ))}
          </select>
        </Field>

        <Field label="차종">
          <select value={form.vehicle_class} onChange={set('vehicle_class')}>
            {OPTIONS.vehicle_class.map((v) => (
              <option key={v} value={v}>{classLabel(v)}</option>
            ))}
          </select>
        </Field>
      </div>

      <Field label="배기량" hint={`${Number(form.engine_size).toFixed(1)} L`}>
        <input
          type="range"
          min={ENGINE_MIN}
          max={ENGINE_MAX}
          step="0.1"
          value={form.engine_size}
          onChange={set('engine_size')}
        />
        <div className="range-scale">
          <span>{ENGINE_MIN} L</span>
          <span>{ENGINE_MAX} L</span>
        </div>
      </Field>

      <Field label="실린더 수" hint={`${form.cylinders}기통`}>
        <div className="chips">
          {OPTIONS.cylinders.map((n) => (
            <button
              type="button"
              key={n}
              className={`chip ${Number(form.cylinders) === n ? 'on' : ''}`}
              onClick={() => setForm((f) => ({ ...f, cylinders: n }))}
            >
              {n}
            </button>
          ))}
        </div>
      </Field>

      <div className="grid-2">
        <Field label="변속기">
          <select value={form.transmission} onChange={set('transmission')}>
            {OPTIONS.transmission.map((v) => (
              <option key={v} value={v}>{transLabel(v)}</option>
            ))}
          </select>
        </Field>

        <Field label="연료">
          <select value={form.fuel_type} onChange={set('fuel_type')}>
            {OPTIONS.fuel_type.map((v) => (
              <option key={v} value={v}>{fuelLabel(v)}</option>
            ))}
          </select>
        </Field>
      </div>

      <button className="submit" type="submit" disabled={loading}>
        {loading ? '예측 중...' : 'CO₂ 배출량 예측하기'}
      </button>
    </form>
  );
}
