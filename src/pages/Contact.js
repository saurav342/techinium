import React, { useState } from 'react';
import './Contact.css';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    company: '',
    service: '',
    message: ''
  });

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    setTimeout(() => {
      setIsSubmitting(false);
      setSubmitStatus('success');
      setFormData({
        name: '',
        email: '',
        company: '',
        service: '',
        message: ''
      });
    }, 2000);
  };

  const services = [
    "AI-Enhanced Web Development",
    "Intelligent Mobile Apps",
    "AI-Powered E-commerce",
    "Smart API Development",
    "UI/UX Design Services",
    "Digital Transformation",
    "Web Development Consulting",
    "Website Maintenance",
    "Quality Assurance",
    "Digital Marketing",
    "Cloud Services & DevOps",
    "Other"
  ];

  return (
    <div className="contact-page">
      <div className="contact-hero">
        <div className="container">
          <h1 className="contact-hero__title">Get In Touch</h1>
          <p className="contact-hero__description">
            Ready to transform your business with AI? Let's discuss your project and explore how we can help.
          </p>
        </div>
      </div>
      
      <div className="contact-content">
        <div className="container">
          <div className="contact__grid">
            <div className="contact__info">
              <h2>Let's Start a Conversation</h2>
              <p>
                Whether you have a specific project in mind or just want to explore the possibilities 
                of AI-powered solutions, we're here to help. Our team of experts is ready to discuss 
                your needs and provide personalized recommendations.
              </p>
              
              <div className="contact__details">
                <div className="contact__detail">
                  <div className="contact__icon">📧</div>
                  <div>
                    <h3>Email</h3>
                    <p>hello@techinium.com</p>
                  </div>
                </div>
                
                <div className="contact__detail">
                  <div className="contact__icon">📱</div>
                  <div>
                    <h3>Phone</h3>
                    <p>+1 (555) 123-4567</p>
                  </div>
                </div>
                
                <div className="contact__detail">
                  <div className="contact__icon">🌍</div>
                  <div>
                    <h3>Location</h3>
                    <p>San Francisco, CA</p>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="contact__form">
              <h2>Send us a Message</h2>
              
              {submitStatus === 'success' ? (
                <div className="success-message">
                  <div className="success-icon">✅</div>
                  <h3>Thank you!</h3>
                  <p>Your message has been sent successfully. We'll get back to you within 24 hours.</p>
                </div>
              ) : (
                <form onSubmit={handleSubmit}>
                  <div className="form-group">
                    <label htmlFor="name">Full Name *</label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      required
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="email">Email Address *</label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="company">Company</label>
                    <input
                      type="text"
                      id="company"
                      name="company"
                      value={formData.company}
                      onChange={handleChange}
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="service">Service of Interest</label>
                    <select
                      id="service"
                      name="service"
                      value={formData.service}
                      onChange={handleChange}
                    >
                      <option value="">Select a service</option>
                      {services.map((service, index) => (
                        <option key={index} value={service}>{service}</option>
                      ))}
                    </select>
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="message">Message *</label>
                    <textarea
                      id="message"
                      name="message"
                      rows="5"
                      value={formData.message}
                      onChange={handleChange}
                      required
                      placeholder="Tell us about your project and how we can help..."
                    ></textarea>
                  </div>
                  
                  <button 
                    type="submit" 
                    className="btn btn-primary"
                    disabled={isSubmitting}
                  >
                    {isSubmitting ? 'Sending...' : 'Send Message'}
                  </button>
                </form>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact; 