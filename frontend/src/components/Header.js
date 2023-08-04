import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="Header">
      <div className="LogoContainer">
        <span className="LogoName">Saka-Keja</span>
      </div>
      <nav className="Navbar">
        <ul>
          <li>
            <a href="#home">Home</a>
          </li>
          <li>
            <a href="#about">About Us</a>
          </li>
          <li>
            <a href="#properties">Properties</a>
          </li>
          <li>
            <a href="#blog">Blog</a>
          </li>
          <li>
            <a href="#contact">Contact Us</a>
          </li>
        </ul>
      </nav>
      <div className="AuthButtons">
        <Link to="/login">
          <button className="loginButton">Login</button>
        </Link>
        <Link to="/signup">
          <button className="signupButton">Sign Up</button>
        </Link>
      </div>
    </header>
  );
};

export default Header;
