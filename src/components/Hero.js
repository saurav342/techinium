import React, { useEffect, useState, useMemo } from 'react';
import { Link } from 'react-router-dom';
import './Hero.css';

const Hero = () => {
  const [currentText, setCurrentText] = useState('');
  const [isDeleting, setIsDeleting] = useState(false);
  const [loopNum, setLoopNum] = useState(0);
  const [typingSpeed, setTypingSpeed] = useState(150);

  const texts = useMemo(() => [
    'AI-Powered Digital Solutions',
    'Intelligent Web Development',
    'Smart Mobile Applications',
    'Future-Ready Technology'
  ], []);

  useEffect(() => {
    const handleTyping = () => {
      const current = loopNum % texts.length;
      const fullText = texts[current];

      if (isDeleting) {
        setTypingSpeed(50);
        setCurrentText(prev => prev.substring(0, prev.length - 1));
      } else {
        setTypingSpeed(150);
        setCurrentText(prev => fullText.substring(0, prev.length + 1));
      }

      if (!isDeleting && currentText === fullText) {
        setTimeout(() => setIsDeleting(true), 2000);
      } else if (isDeleting && currentText === '') {
        setIsDeleting(false);
        setLoopNum(prev => prev + 1);
      }
    };

    const timer = setTimeout(handleTyping, typingSpeed);
    return () => clearTimeout(timer);
  }, [currentText, isDeleting, loopNum, typingSpeed, texts]);

  return (
    <section className="hero" id="home">
      <div className="hero__container container">
        <div className="hero__content">
          <h1 className="hero__title">
            <span className="typing-text">{currentText}</span>
            <span className="typing-cursor">|</span>
            <br />
            <span className="hero__subtitle">for Tomorrow's Businesses</span>
          </h1>
          <p className="hero__description">
            Transform your business with intelligent web and app development solutions that leverage cutting-edge artificial intelligence to deliver exceptional results.
          </p>
          <div className="hero__buttons">
            <Link to="/contact" className="btn btn-primary">Get Started</Link>
            <Link to="/services" className="btn btn-secondary">View Services</Link>
          </div>
        </div>
        <div className="hero__image">
          <div className="hero__ai-elements">
            <div className="ai-circle ai-circle--1"></div>
            <div className="ai-circle ai-circle--2"></div>
            <div className="ai-circle ai-circle--3"></div>
            <div className="ai-shape ai-shape--1"></div>
            <div className="ai-shape ai-shape--2"></div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero; 