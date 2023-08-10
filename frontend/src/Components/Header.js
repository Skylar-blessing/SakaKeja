import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Link as ScrollLink } from 'react-scroll';
import { FaHome } from 'react-icons/fa'; // Import the FaHome icon

const Header = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login')
  };

  const handleSignupClick = () => {
    navigate('/signup')
  };

  return (
    <header>
      <div className="header-container">
        <div className="logo-container">
          <span className="home-icon"><FaHome /></span> {/* Add the home icon */}
          <span className="logo-name">SakaKeja</span>
        </div>
        <nav className="navbar">
          <ul>
            <li>
              <ScrollLink
                to="home"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Home
              </ScrollLink>
            </li>
            <li>
              <ScrollLink
                to="about-us"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Our Company
              </ScrollLink>
            </li>
            <li>
              <ScrollLink
                to="property-explore"
                spy={true}
                smooth={true}
                offset={-70}
                duration={1000}
              >
                Properties
              </ScrollLink>
            </li>
            <li>
              <ScrollLink
                to="blog"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Blog
              </ScrollLink>
            </li>
            <li>
              <ScrollLink
                to="contact-us"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Contact Us
              </ScrollLink>
            </li>
          </ul>
        </nav>
        <div className="auth-buttons">
          <button className="auth-button" onClick={handleLoginClick}>Login</button>
          <button className="auth-button" onClick={handleSignupClick}>Sign Up</button>
        </div>
      </div>
    </header>
  );
};

export default Header;
