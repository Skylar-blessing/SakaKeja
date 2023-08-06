// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './Main';
import LoginPage from './LoginPage';
import SignupPage from './SignupPage';
import PropertiesPage from './PropertiesPage';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/properties" element={<PropertiesPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
