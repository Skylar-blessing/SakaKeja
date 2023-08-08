import React from 'react';
import Main from './Main';
import OurCompany from './OurCompany';
import PropertyExplore from './PropertyExplore';
import Login from './Login'; 
import SignupPage from './SignupPage';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


const App = () => {
  return (
    <Router>
      <div>
        <Routes>
        <Route path="/" element={<Main />} />
        </Routes>
        
        <Routes> 
          <Route path="/login" element={<Login />} /> 
          <Route path="/signup" element={<SignupPage />} />
        </Routes>

        {/* Render additional components */}
        <OurCompany />
        <PropertyExplore />
      </div>
    </Router>
  );
};

export default App;
