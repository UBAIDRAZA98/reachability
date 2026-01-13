import React, { useState } from 'react';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';

export default function App() {
  // Simple state-based routing to avoid React Router bloat
  const [view, setView] = useState('login');

  const handleLogin = () => {
    // In a real app, check creds. Here, just let them in.
    setView('dashboard');
  };

  return (
    <div className="app-container">
      {view === 'login' && <Login onLogin={handleLogin} />}
      {view === 'dashboard' && <Dashboard />}
    </div>
  );
}
