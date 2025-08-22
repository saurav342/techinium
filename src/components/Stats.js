import React, { useEffect, useState, useRef } from 'react';
import './Stats.css';

const Stats = () => {
  const [isVisible, setIsVisible] = useState(false);
  const statsRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.5 }
    );

    if (statsRef.current) {
      observer.observe(statsRef.current);
    }

    return () => observer.disconnect();
  }, []);

  const stats = [
    { number: 200, label: "AI Projects Delivered", suffix: "+" },
    { number: 98, label: "Client Satisfaction %", suffix: "%" },
    { number: 50, label: "Team Members", suffix: "+" },
    { number: 5, label: "Years of Excellence", suffix: "+" }
  ];

  return (
    <section className="stats" ref={statsRef}>
      <div className="container">
        <div className="stats__grid">
          {stats.map((stat, index) => (
            <div 
              key={index} 
              className="stats__item"
              style={{ animationDelay: `${index * 0.2}s` }}
            >
              <div className="stats__number">
                {isVisible ? (
                  <AnimatedCounter 
                    target={stat.number} 
                    suffix={stat.suffix}
                  />
                ) : (
                  `0${stat.suffix}`
                )}
              </div>
              <div className="stats__label">{stat.label}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

const AnimatedCounter = ({ target, suffix }) => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const duration = 2000; // 2 seconds
    const increment = target / (duration / 16); // 60fps
    let current = 0;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        setCount(target);
        clearInterval(timer);
      } else {
        setCount(Math.floor(current));
      }
    }, 16);

    return () => clearInterval(timer);
  }, [target]);

  return <span>{count}{suffix}</span>;
};

export default Stats; 