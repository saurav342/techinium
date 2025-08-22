import React from 'react';
import './Process.css';

const Process = () => {
  const processSteps = [
    {
      step: "01",
      title: "Discovery & Analysis",
      description: "We analyze your requirements and create a comprehensive project roadmap with AI-powered insights.",
      icon: "🔍"
    },
    {
      step: "02",
      title: "AI-Powered Design",
      description: "Our AI-driven design process creates intuitive interfaces based on user behavior analysis.",
      icon: "🎨"
    },
    {
      step: "03",
      title: "Intelligent Development",
      description: "We build your solution using cutting-edge AI technologies and best practices.",
      icon: "⚡"
    },
    {
      step: "04",
      title: "Testing & Optimization",
      description: "AI-powered testing ensures quality and performance optimization for the best user experience.",
      icon: "✅"
    },
    {
      step: "05",
      title: "Deployment & Support",
      description: "Seamless deployment with ongoing AI-powered monitoring and support.",
      icon: "🚀"
    }
  ];

  return (
    <section className="process">
      <div className="container">
        <div className="section__header">
          <h2 className="section__title">Our AI-Powered Process</h2>
          <p className="section__subtitle">
            A streamlined workflow that leverages artificial intelligence at every step
          </p>
        </div>
        
        <div className="process__timeline">
          {processSteps.map((step, index) => (
            <div 
              key={index} 
              className="process__step"
              style={{ animationDelay: `${index * 0.3}s` }}
            >
              <div className="process__step-number">{step.step}</div>
              <div className="process__step-content">
                <div className="process__step-icon">{step.icon}</div>
                <h3 className="process__step-title">{step.title}</h3>
                <p className="process__step-description">{step.description}</p>
              </div>
              {index < processSteps.length - 1 && (
                <div className="process__step-connector"></div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Process; 