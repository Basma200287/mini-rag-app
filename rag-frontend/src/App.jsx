import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import UserChat from "./UserChat";
import AdminDashboard from "./AdminDashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<UserChat />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}