// SSE 텍스트 파서 (브라우저/Node 어디서든 동작하는 순수 함수)
// buffer: 지금까지 받은 미처리 텍스트. 반환: 완성된 이벤트들 + 아직 덜 온 꼬리(rest)
export function parseSse(buffer) {
  const normalized = buffer.replace(/\r\n/g, '\n');
  const blocks = normalized.split('\n\n');
  const rest = blocks.pop(); // 마지막 조각은 이벤트가 끝나지 않았을 수 있음
  const events = [];

  for (const block of blocks) {
    if (!block.trim()) continue;
    let event = 'message';
    const data = [];
    for (const line of block.split('\n')) {
      if (line.startsWith(':')) continue; // 주석(keep-alive)
      const idx = line.indexOf(':');
      const field = idx === -1 ? line : line.slice(0, idx);
      let value = idx === -1 ? '' : line.slice(idx + 1);
      if (value.startsWith(' ')) value = value.slice(1);
      if (field === 'event') event = value;
      else if (field === 'data') data.push(value);
    }
    if (data.length) events.push({ event, data: data.join('\n') });
  }
  return { events, rest };
}
