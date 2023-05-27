import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';

const rootElement = document.getElementById('root');

// Use createRoot to render the root component
ReactDOM.createRoot(rootElement).render(
  <Router>
    <App />
  </Router>
);
