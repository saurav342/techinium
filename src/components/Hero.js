import React from 'react';
import { Link } from 'react-router-dom';
import './Hero.css';

const Hero = () => {
  return (
    <section className="hero" id="home">
      {/* background gradient + vignette */}
      <div className="hero__bg" aria-hidden="true" />

      <div className="hero__container container">
        <div className="hero__content">
          <h1 className="hero__title">
            <span className="hero__headline hero__headline--top">
              AI-Powered Digital
            </span>
            <br />
            <span className="hero__headline hero__headline--bottom">
              Solutions
            </span>
          </h1>

          {/* faint oversized line */}
          <div className="hero__ghost-title">
            for Tomorrow&apos;s<br />Businesses
          </div>

          <p className="hero__description">
            Transform your business with intelligent web and app development
            powered by cutting-edge artificial intelligence technology.
          </p>

          <div className="hero__buttons">
            <Link to="/contact" className="btn btn-primary hero__cta">
              Get Started
            </Link>
            <Link to="/services" className="btn btn-secondary hero__cta hero__cta--ghost">
              View Services
            </Link>
          </div>
        </div>

        {/* right-side floating dots */}
        <div className="hero__art" aria-hidden="true">
          <span className="dot dot--pink" />
          <span className="dot dot--purple" />
          {/* <span className="dot dot--green" /> */}
          <span className="dot dot--yellow" />
        </div>
      </div>
    </section>
  );
};

export default Hero;