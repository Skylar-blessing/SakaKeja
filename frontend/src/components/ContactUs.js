import React from 'react';
import { Link } from 'react-router-dom';
import { FaPhone, FaEnvelope, FaWhatsapp } from 'react-icons/fa';
import { Element } from 'react-scroll';

const ContactUs = () => {
  return (
    <Element name="contact-us">
      <div className="contact-us-container">
        <h2>Contact Us</h2>
        <div className="contact-options">
          <div className="contact-option">
            <FaPhone className="contact-icon" />
            <p>Call us: +123 456 7890</p>
          </div>
          <div className="contact-option">
            <FaEnvelope className="contact-icon" />
            <p>Email us: info@sakakeja.com</p>
          </div>
          <div className="contact-option">
            <FaWhatsapp className="contact-icon" />
            <p>WhatsApp: +123 456 7890</p>
          </div>
        </div>
        <div className="contact-form">
          <h3>Send us a message</h3>
          <form>
            <input type="text" placeholder="Your Name" />
            <input type="email" placeholder="Your Email" />
            <textarea placeholder="Your Message" rows="5" />
            <button type="submit">Send</button>
          </form>
        </div>
      </div>
    </Element>
  );
};

export default ContactUs;
