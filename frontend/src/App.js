import React, { useState, useEffect} from "react";
import Properties from "./Properties";
import Home from "./Home";
import ContactUs from "./ContactUs";

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  const [isDarkMode, setIsDarkMode] = useState('light');
 
  const themeClass = isDarkMode ? "light" : "dark";

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

useEffect(() => {
    document.body.className = themeClass;
     }, [themeClass]);
  return (
    <div className={`App ${themeClass}`}>
      <header>
      <button onClick={toggleTheme} className="mode">
        {isDarkMode ? "Dark mode" : "Light mode"}
      </button>
      </header>

      <Router>
        <Routes> 
          <Route path="/" element={<Home />} />
          <Route path="/properties" element={<Properties />} />
          <Route path="/contactus" element={<ContactUs />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
