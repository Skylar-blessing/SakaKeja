import React from 'react';
import { FaHome, FaBuilding, FaMapMarkerAlt, FaNewspaper, FaFacebook, FaLinkedin, FaTwitter, FaInstagram, FaEnvelope, FaUser, FaSignInAlt } from 'react-icons/fa';

const Footer = () => {
    return (
        <footer className="footer-container">
            <div className="footer-section">
                <div className="social-icons">
                    <div className="eco-icon">
                        <FaHome /> EcoHaven Reality
                    </div>
                    <div className="social-links">
                        <FaFacebook />
                        <FaLinkedin />
                        <FaTwitter />
                        <FaInstagram />
                    </div>
                    <div className="contact-button">
                        <button>Contact Us</button>
                    </div>
                </div>
            </div>
            <div className="footer-section">
                <ul className="footer-list">
                   <li className='Nav'>Navigation</li>
                    <li><FaHome /> Home</li>
                    <li><FaBuilding /> Our Company</li>
                    <li><FaMapMarkerAlt /> Properties</li>
                    <li><FaNewspaper /> Blog</li>
                </ul>
            </div>
            <div className="footer-section">
                <ul className="footer-list">
                    <li className='Nav'>Company</li>
                    <li>About Us</li>
                    <li>Our Mission</li>
                    <li>Our Team</li>
                </ul>
            </div>
            <div className="footer-section">
                <ul className="footer-list">
                    <li className='Nav'>Support</li>
                    <li>+254710203050</li>
                    <li><FaUser /> Login</li>
                </ul>
            </div>
        </footer>
    );
};

export default Footer;
