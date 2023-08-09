import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './compononents/Login';
import SignUp from './compononents/SignUp';
import OwnerDashboard from './compononents/OwnerDashboard';
import TenantDashboard from './compononents/TenantDashboard';
import PropertyList from './compononents/PropertyList'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/owner-dashboard" element={<OwnerDashboard />} />
        <Route path="/tenant-dashboard" element={<TenantDashboard />} />
        <Route path="/rent" element={<PropertyList />} />
      </Routes>
    </Router>
  );
}

export default App;