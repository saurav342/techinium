import React from 'react';
import './Services.css';

const Services = () => {
  const services = [
    {
      title: "AI-Enhanced Web Application Development",
      description: "Custom web applications powered by artificial intelligence, featuring responsive design, intelligent user interfaces, and automated optimization.",
      technologies: ["HTML5", "CSS3", "JavaScript", "React", "Angular", "Vue.js", "Node.js", "Python", "AI/ML APIs"],
      icon: "🌐"
    },
    {
      title: "Intelligent Mobile App Development",
      description: "Native and cross-platform mobile apps with AI-driven features, predictive analytics, and smart user experiences.",
      technologies: ["Swift", "Kotlin", "Flutter", "React Native", "TensorFlow Lite", "Core ML"],
      icon: "📱"
    },
    {
      title: "AI-Driven Full Stack Development",
      description: "End-to-end development solutions with intelligent backend systems, automated deployments, and AI-enhanced databases.",
      technologies: ["MEAN Stack", "MERN Stack", "Django", "Laravel", "Microservices", "AI Frameworks"],
      icon: "⚡"
    },
    {
      title: "Smart API Development & Integration",
      description: "Intelligent APIs with automated documentation, smart routing, and AI-powered data processing capabilities.",
      technologies: ["REST APIs", "GraphQL", "OAuth", "JWT", "AI APIs", "Machine Learning Models"],
      icon: "🔗"
    },
    {
      title: "AI-Powered E-commerce Development",
      description: "Intelligent online stores with recommendation engines, automated inventory management, and predictive analytics.",
      technologies: ["Shopify", "Magento", "WooCommerce", "AI Recommendation Systems", "Payment AI"],
      icon: "🛒"
    },
    {
      title: "Intelligent UI/UX Design Services",
      description: "AI-driven design processes with user behavior analysis, automated A/B testing, and personalized experiences.",
      technologies: ["Figma", "Adobe XD", "User Analytics AI", "Design Systems", "Personalization Engines"],
      icon: "🎨"
    },
    {
      title: "AI-Driven Digital Transformation",
      description: "Comprehensive business transformation using AI technologies, automation, and intelligent process optimization.",
      technologies: ["Cloud AI", "Automation Tools", "ML Pipelines", "Data Analytics", "Process Mining"],
      icon: "🚀"
    },
    {
      title: "Smart Web Development Consulting",
      description: "Strategic consulting with AI-powered architecture recommendations, performance optimization, and security analysis.",
      technologies: ["Architecture AI", "Performance Tools", "Security AI", "Code Analysis", "Optimization Algorithms"],
      icon: "💡"
    },
    {
      title: "Automated Website Maintenance & Support",
      description: "AI-powered monitoring, automated updates, predictive maintenance, and intelligent issue resolution.",
      technologies: ["Monitoring AI", "Automated Tools", "Predictive Analytics", "Security Bots", "Performance AI"],
      icon: "🔧"
    },
    {
      title: "AI-Enhanced Quality Assurance & Testing",
      description: "Intelligent testing with automated test generation, AI-powered bug detection, and predictive quality metrics.",
      technologies: ["Test Automation AI", "Selenium", "AI Testing Tools", "Quality Prediction", "Smart Debugging"],
      icon: "✅"
    },
    {
      title: "Intelligent Digital Marketing Integration",
      description: "AI-driven marketing automation, intelligent SEO, predictive analytics, and personalized campaign optimization.",
      technologies: ["Marketing AI", "SEO Tools", "Analytics AI", "Automation Platforms", "Predictive Models"],
      icon: "📈"
    },
    {
      title: "AI-Optimized Cloud Services & DevOps",
      description: "Intelligent cloud infrastructure with automated scaling, AI-powered monitoring, and smart deployment strategies.",
      technologies: ["AWS AI", "Azure AI", "Google Cloud AI", "Kubernetes", "DevOps Automation", "ML Ops"],
      icon: "☁️"
    }
  ];

  return (
    <div className="services-page">
      <div className="services-hero">
        <div className="container">
          <h1 className="services-hero__title">Our AI-Enhanced Services</h1>
          <p className="services-hero__description">
            Comprehensive digital solutions powered by artificial intelligence to transform your business
          </p>
        </div>
      </div>
      
      <div className="services-content">
        <div className="container">
          <div className="services__grid">
            {services.map((service, index) => (
              <div 
                key={index} 
                className="service-item"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="service-item__header">
                  <div className="service-item__icon">{service.icon}</div>
                  <h3 className="service-item__title">{service.title}</h3>
                </div>
                <p className="service-item__description">{service.description}</p>
                <div className="service-item__technologies">
                  <h4>Technologies:</h4>
                  <div className="tech-tags">
                    {service.technologies.map((tech, techIndex) => (
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

export default Services; 