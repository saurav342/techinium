import React from 'react';
import { Link } from 'react-router-dom';
import './ContactCTA.css';

const ContactCTA = () => {
  return (
    <section className="contact-cta">
      <div className="container">
        <div className="contact-cta__content">
          <h2 className="contact-cta__title">
            Ready to Transform Your Business with AI?
          </h2>
          <p className="contact-cta__description">
            Let's discuss how our AI-powered solutions can drive innovation and growth for your organization.
          </p>
          <div className="contact-cta__buttons">
            <Link to="/contact" className="btn btn-primary">Get Started Today</Link>
            <Link to="/services" className="btn btn-secondary">Explore Services</Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactCTA; 