import React from 'react';
import './About.css';

const About = () => {
  return (
    <div className="about-page">
      <div className="about-hero">
        <div className="container">
          <h1 className="about-hero__title">About Techinium</h1>
          <p className="about-hero__description">
            Leading the future of development with AI-first solutions
          </p>
        </div>
      </div>
      
      <div className="about-content">
        <div className="container">
          <div className="about__grid">
            <div className="about__section">
              <h2>Our Mission</h2>
              <p>
                At Techinium, we believe that artificial intelligence is the key to unlocking the full potential of digital solutions. 
                Our mission is to empower businesses with intelligent, scalable, and future-ready technology that drives innovation 
                and growth in an increasingly AI-driven world.
              </p>
            </div>
            
            <div className="about__section">
              <h2>Our Vision</h2>
              <p>
                We envision a future where every business can leverage the power of AI to create exceptional digital experiences, 
                optimize operations, and deliver value to their customers. Through our expertise and innovative approach, 
                we're making this vision a reality for organizations worldwide.
              </p>
            </div>
            
            <div className="about__section">
              <h2>Our Approach</h2>
              <p>
                Our AI-first approach means that artificial intelligence is integrated into every aspect of our development process. 
                From initial concept to final deployment, we use intelligent algorithms, machine learning models, and automated 
                systems to create solutions that are not just functional, but truly intelligent.
              </p>
            </div>
            
            <div className="about__section">
              <h2>Why AI-First?</h2>
              <p>
                In today's competitive landscape, businesses need more than just digital solutions—they need intelligent systems 
                that can learn, adapt, and evolve. Our AI-first methodology ensures that every solution we deliver is built with 
                intelligence at its core, providing ongoing value and competitive advantage.
              </p>
            </div>
          </div>
          
          <div className="about__values">
            <h2>Our Core Values</h2>
            <div className="values__grid">
              <div className="value-item">
                <div className="value-icon">🚀</div>
                <h3>Innovation</h3>
                <p>Constantly pushing boundaries with cutting-edge AI technologies</p>
              </div>
              <div className="value-item">
                <div className="value-icon">💎</div>
                <h3>Quality</h3>
                <p>Delivering excellence in every project and solution</p>
              </div>
              <div className="value-item">
                <div className="value-icon">🤝</div>
                <h3>Partnership</h3>
                <p>Building long-term relationships based on trust and results</p>
              </div>
              <div className="value-item">
                <div className="value-icon">🌱</div>
                <h3>Growth</h3>
                <p>Fostering continuous learning and development</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About; 