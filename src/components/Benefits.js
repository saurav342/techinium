import React from 'react';
import './Benefits.css';

const Benefits = () => {
  const benefits = [
    {
      title: "AI-First Approach",
      description: "Every solution is built with artificial intelligence at its core, ensuring smarter, more efficient results.",
      icon: "🤖"
    },
    {
      title: "Cutting-Edge Technology",
      description: "We leverage the latest AI frameworks and technologies to deliver future-ready solutions.",
      icon: "⚡"
    },
    {
      title: "Expert Team",
      description: "Our team combines deep technical expertise with AI specialization to drive exceptional outcomes.",
      icon: "👥"
    },
    {
      title: "Proven Results",
      description: "Delivered 200+ AI-powered projects with 98% client satisfaction and measurable business impact.",
      icon: "🏆"
    }
  ];

  return (
    <section className="benefits">
      <div className="container">
        <div className="section__header">
          <h2 className="section__title">Why Choose Techinium</h2>
          <p className="section__subtitle">
            Leading the future of development with AI-first solutions
          </p>
        </div>
        
        <div className="benefits__grid">
          {benefits.map((benefit, index) => (
            <div 
              key={index} 
              className="benefit-card"
              style={{ animationDelay: `${index * 0.2}s` }}
            >
              <div className="benefit-card__icon">{benefit.icon}</div>
              <h3 className="benefit-card__title">{benefit.title}</h3>
              <p className="benefit-card__description">{benefit.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Benefits; 