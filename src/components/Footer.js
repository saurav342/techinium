import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  const handleSocialClick = (platform) => {
    // Placeholder for social media functionality
    console.log(`Navigate to ${platform}`);
  };

  const handleServiceClick = (service) => {
    // Placeholder for service navigation
    console.log(`Navigate to ${service} service`);
  };

  const handleLegalClick = (policy) => {
    // Placeholder for legal page navigation
    console.log(`Navigate to ${policy}`);
  };

  return (
    <footer className="footer">
      <div className="footer__container">
        {/* Main Footer Content */}
        <div className="footer__main">
          {/* Company Info Section */}
          <div className="footer__section">
            <div className="footer__brand">
              <i className="fas fa-robot footer__logo"></i>
              <span className="footer__title">Techinium</span>
            </div>
            <p className="footer__description">
              Empowering businesses with cutting-edge technology solutions. 
              We transform ideas into digital reality with innovation and expertise.
            </p>
            <div className="footer__social">
              <button 
                type="button"
                className="footer__social-link" 
                aria-label="Facebook"
                onClick={() => handleSocialClick('Facebook')}
              >
                <i className="fab fa-facebook-f"></i>
              </button>
              <button 
                type="button"
                className="footer__social-link" 
                aria-label="Twitter"
                onClick={() => handleSocialClick('Twitter')}
              >
                <i className="fab fa-twitter"></i>
              </button>
              <button 
                type="button"
                className="footer__social-link" 
                aria-label="LinkedIn"
                onClick={() => handleSocialClick('LinkedIn')}
              >
                <i className="fab fa-linkedin-in"></i>
              </button>
              <button 
                type="button"
                className="footer__social-link" 
                aria-label="Instagram"
                onClick={() => handleSocialClick('Instagram')}
              >
                <i className="fab fa-instagram"></i>
              </button>
            </div>
          </div>

          {/* Quick Links Section */}
          <div className="footer__section">
            <h3 className="footer__heading">Quick Links</h3>
            <ul className="footer__links">
              <li><Link to="/" className="footer__link">Home</Link></li>
              <li><Link to="/about" className="footer__link">About Us</Link></li>
              <li><Link to="/services" className="footer__link">Services</Link></li>
              <li><Link to="/portfolio" className="footer__link">Portfolio</Link></li>
              <li><Link to="/contact" className="footer__link">Contact</Link></li>
            </ul>
          </div>

          {/* Services Section */}
          <div className="footer__section">
            <h3 className="footer__heading">Our Services</h3>
            <ul className="footer__links">
              <li><button type="button" className="footer__link" onClick={() => handleServiceClick('Web Development')}>Web Development</button></li>
              <li><button type="button" className="footer__link" onClick={() => handleServiceClick('Mobile Apps')}>Mobile Apps</button></li>
              <li><button type="button" className="footer__link" onClick={() => handleServiceClick('Cloud Solutions')}>Cloud Solutions</button></li>
              <li><button type="button" className="footer__link" onClick={() => handleServiceClick('Digital Marketing')}>Digital Marketing</button></li>
              <li><button type="button" className="footer__link" onClick={() => handleServiceClick('Consulting')}>Consulting</button></li>
            </ul>
          </div>

          {/* Contact Section */}
          <div className="footer__section">
            <h3 className="footer__heading">Get In Touch</h3>
            <div className="footer__contact">
              <div className="footer__contact-item">
                <i className="fas fa-map-marker-alt"></i>
                <span>123 Tech Street, Digital City, DC 12345</span>
              </div>
              <div className="footer__contact-item">
                <i className="fas fa-phone"></i>
                <span>+1 (555) 123-4567</span>
              </div>
              <div className="footer__contact-item">
                <i className="fas fa-envelope"></i>
                <span>hello@techinium.com</span>
              </div>
            </div>
          </div>
        </div>

        {/* Footer Bottom */}
        <div className="footer__bottom">
          <div className="footer__bottom-content">
            <p className="footer__copyright">
              © {currentYear} Techinium. All rights reserved.
            </p>
            <div className="footer__legal">
              <button type="button" className="footer__legal-link" onClick={() => handleLegalClick('Privacy Policy')}>Privacy Policy</button>
              <button type="button" className="footer__legal-link" onClick={() => handleLegalClick('Terms of Service')}>Terms of Service</button>
              <button type="button" className="footer__legal-link" onClick={() => handleLegalClick('Cookie Policy')}>Cookie Policy</button>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
