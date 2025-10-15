import React from 'react';
import { render } from '@testing-library/react';
import App from '../src/App';

test('App renders without crashing', () => {
  const { container } = render(<App />);
  expect(container).toBeTruthy();
});

test('App displays main heading', () => {
  const { getByText } = render(<App />);
  expect(getByText('AI Cage-Driven Development')).toBeInTheDocument();
});

test('App displays subtitle', () => {
  const { getByText } = render(<App />);
  expect(getByText(/Claude Code × Codex CLI/)).toBeInTheDocument();
});
