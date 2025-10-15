import { render } from '@testing-library/react';
import App from '../src/App';

test('App renders without crashing', () => {
  const { container } = render(<App />);
  expect(container).toBeTruthy();
});

test('App displays main heading', () => {
  const { getByText } = render(<App />);
  expect(getByText('Rune')).toBeInTheDocument();
});

test('App displays subtitle', () => {
  const { getByText } = render(<App />);
  expect(getByText(/Claude Code × Codex CLI による自動開発環境/)).toBeInTheDocument();
});
