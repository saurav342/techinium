import React from 'react';
import { Link } from 'react-router-dom';
import './ServicesPreview.css';

const ServicesPreview = () => {
  const previewServices = [
    {
      title: "AI-Enhanced Web Development",
      description: "Custom web applications powered by artificial intelligence with responsive design and intelligent interfaces.",
      icon: "🌐",
      technologies: ["React", "Node.js", "AI/ML APIs"]
    },
    {
      title: "Intelligent Mobile Apps",
      description: "Native and cross-platform mobile apps with AI-driven features and predictive analytics.",
      icon: "📱",
      technologies: ["Flutter", "React Native", "TensorFlow Lite"]
    },
    {
      title: "AI-Powered E-commerce",
      description: "Intelligent online stores with recommendation engines and automated inventory management.",
      icon: "🛒",
      technologies: ["Shopify", "AI Recommendations", "Payment AI"]
    }
  ];

  return (
    <section className="services-preview">
      <div className="container">
        <div className="section__header">
          <h2 className="section__title">Our AI-Enhanced Services</h2>
          <p className="section__subtitle">
            Comprehensive digital solutions powered by artificial intelligence
          </p>
        </div>
        
        <div className="services-preview__grid">
          {previewServices.map((service, index) => (
            <div 
              key={index} 
              className="service-card"
              style={{ animationDelay: `${index * 0.2}s` }}
            >
              <div className="service-card__icon">{service.icon}</div>
              <h3 className="service-card__title">{service.title}</h3>
              <p className="service-card__description">{service.description}</p>
              <div className="service-card__technologies">
                {service.technologies.map((tech, techIndex) => (
                  <span key={techIndex} className="tech-tag">{tech}</span>
                ))}
              </div>
            </div>
          ))}
        </div>
        
        <div className="services-preview__cta">
          <Link to="/services" className="btn btn-primary">View All Services</Link>
        </div>
      </div>
    </section>
  );
};

export default ServicesPreview; 