import { BrowserRouter, Routes, Route } from 'react-router-dom';
import UserChat from './pages/UserChat';
import AdminDashboard from './pages/AdminDashboard';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* User interface */}
        <Route path="/" element={<UserChat />} />

        {/* Admin interface */}
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}