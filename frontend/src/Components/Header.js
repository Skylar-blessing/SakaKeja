import React from 'react';
import { Link } from 'react-scroll';

const Header = () => {
  return (
    <header>
      <div className="header-container">
        <div className="logo-container">
          <span className="logo-name">SakaKeja</span>
        </div>
        <nav className="navbar">
          <ul>
            <li>
              <Link
                activeClass="active"
                to="home"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Home
              </Link>
            </li>
            <li>
              <Link
                activeClass="active"
                to="about-us"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Our Company
              </Link>
            </li>
            <li>
              <Link
                activeClass="active"
                to="properties"
                spy={true}
                smooth={true}
                offset={-70}
                duration={1000}
              >
                Properties
              </Link>
            </li>
            <li>
              <Link
                activeClass="active"
                to="blog"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Blog
              </Link>
            </li>
            <li>
              <Link
                activeClass="active"
                to="contact-us"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Contact Us
              </Link>
            </li>
          </ul>
        </nav>
        <div className="auth-buttons">
          <Link to="/login" className="auth">Login</Link>
          <Link to="/signup" className="auth-button">Sign Up</Link>
        </div>
      </div>
    </header>
  );
};

export default Header;
