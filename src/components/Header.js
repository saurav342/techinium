import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Header.css';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <header className={`header ${isScrolled ? 'header--scrolled' : ''}`} id="header">
      <nav className="nav container">
        <div className="nav__brand">
          <Link to="/" className="nav__logo-link">
            <i className="fas fa-robot nav__logo"></i>
            <span className="nav__title">Techinium</span>
          </Link>
        </div>
        
        <div className={`nav__menu ${isMenuOpen ? 'nav__menu--open' : ''}`} id="nav-menu">
          <ul className="nav__list">
            <li className="nav__item">
              <Link 
                to="/" 
                className={`nav__link ${isActive('/') ? 'active' : ''}`}
                onClick={closeMenu}
              >
                Home
              </Link>
            </li>
            <li className="nav__item">
              <Link 
                to="/services" 
                className={`nav__link ${isActive('/services') ? 'active' : ''}`}
                onClick={closeMenu}
              >
                Services
              </Link>
            </li>
            <li className="nav__item">
              <Link 
                to="/about" 
                className={`nav__link ${isActive('/about') ? 'active' : ''}`}
                onClick={closeMenu}
              >
                About
              </Link>
            </li>
            <li className="nav__item">
              <Link 
                to="/portfolio" 
                className={`nav__link ${isActive('/portfolio') ? 'active' : ''}`}
                onClick={closeMenu}
              >
                Portfolio
              </Link>
            </li>
            <li className="nav__item">
              <Link 
                to="/contact" 
                className={`nav__link ${isActive('/contact') ? 'active' : ''}`}
                onClick={closeMenu}
              >
                Contact
              </Link>
            </li>
          </ul>
          
          <div className="nav__close" id="nav-close" onClick={closeMenu}>
            <i className="fas fa-times"></i>
          </div>
        </div>
        
        <div className="nav__toggle" id="nav-toggle" onClick={toggleMenu}>
          <i className="fas fa-bars"></i>
        </div>
      </nav>
    </header>
  );
};

export default Header; 