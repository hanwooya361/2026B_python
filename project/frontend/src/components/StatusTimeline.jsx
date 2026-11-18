export default function StatusTimeline({ messages, loading, error }) {
  if (messages.length === 0 && !loading && !error) return null;

  return (
    <div className="card status">
      <h2>진행 상황</h2>
      <ul>
        {messages.map((m, i) => {
          const isLast = i === messages.length - 1;
          const running = loading && isLast;
          return (
            <li key={i} className={running ? 'running' : 'done'}>
              <span className="dot">{running ? <i className="spinner" /> : '✓'}</span>
              <span>{m}</span>
            </li>
          );
        })}
        {loading && messages.length === 0 && (
          <li className="running">
            <span className="dot"><i className="spinner" /></span>
            <span>서버에 연결하는 중...</span>
          </li>
        )}
        {error && (
          <li className="fail">
            <span className="dot">!</span>
            <span>{error}</span>
          </li>
        )}
      </ul>
    </div>
  );
}
