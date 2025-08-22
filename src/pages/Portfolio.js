import React from 'react';
import './Portfolio.css';

const Portfolio = () => {
  const projects = [
    {
      title: "AI-Powered E-commerce Platform",
      description: "A comprehensive online store with intelligent product recommendations, automated inventory management, and AI-driven customer insights.",
      technologies: ["React", "Node.js", "MongoDB", "TensorFlow", "AWS"],
      image: "🛒",
      category: "E-commerce"
    },
    {
      title: "Intelligent Healthcare Dashboard",
      description: "A healthcare analytics platform that uses machine learning to predict patient outcomes and optimize treatment plans.",
      technologies: ["Python", "React", "FastAPI", "Scikit-learn", "PostgreSQL"],
      image: "🏥",
      category: "Healthcare"
    },
    {
      title: "Smart Financial Analytics Tool",
      description: "An AI-driven financial platform that provides real-time market analysis, risk assessment, and investment recommendations.",
      technologies: ["Vue.js", "Python", "Django", "Pandas", "NumPy"],
      image: "📊",
      category: "Finance"
    },
    {
      title: "AI-Enhanced Learning Management System",
      description: "An intelligent educational platform that personalizes learning experiences and tracks student progress using AI algorithms.",
      technologies: ["Angular", "Node.js", "TensorFlow.js", "MongoDB", "Redis"],
      image: "🎓",
      category: "Education"
    },
    {
      title: "Intelligent Supply Chain Platform",
      description: "A supply chain optimization system that uses AI to predict demand, optimize routes, and reduce operational costs.",
      technologies: ["React", "Python", "Flask", "Scikit-learn", "PostgreSQL"],
      image: "🚚",
      category: "Logistics"
    },
    {
      title: "AI-Powered Customer Service Bot",
      description: "An intelligent chatbot that handles customer inquiries, provides personalized support, and learns from interactions.",
      technologies: ["Python", "TensorFlow", "NLP", "FastAPI", "Redis"],
      image: "🤖",
      category: "Customer Service"
    }
  ];

  return (
    <div className="portfolio-page">
      <div className="portfolio-hero">
        <div className="container">
          <h1 className="portfolio-hero__title">Our Portfolio</h1>
          <p className="portfolio-hero__description">
            Showcasing innovative AI-powered solutions that drive business transformation
          </p>
        </div>
      </div>
      
      <div className="portfolio-content">
        <div className="container">
          <div className="portfolio__grid">
            {projects.map((project, index) => (
              <div 
                key={index} 
                className="portfolio-item"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="portfolio-item__image">{project.image}</div>
                <div className="portfolio-item__content">
                  <div className="portfolio-item__category">{project.category}</div>
                  <h3 className="portfolio-item__title">{project.title}</h3>
                  <p className="portfolio-item__description">{project.description}</p>
                  <div className="portfolio-item__technologies">
                    {project.technologies.map((tech, techIndex) => (
                      <span key={techIndex} className="tech-tag">{tech}</span>
                    ))}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Portfolio; 