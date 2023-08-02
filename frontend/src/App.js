import "./App.css";
// import React, {useEffect} from 'react';
import Login from "./Login";
import SignUp from "./SignUp";
import { Link } from "react-router-dom";
import { NavBar } from "./NavBar";
import Home from "./Home";
import { BrowserRouter, Route, Router, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <NavBar />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
