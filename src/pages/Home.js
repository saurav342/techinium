import React, { useEffect, useState } from 'react';
import Hero from '../components/Hero';
import ServicesPreview from '../components/ServicesPreview';
import Benefits from '../components/Benefits';
import Stats from '../components/Stats';
import Process from '../components/Process';
import ContactCTA from '../components/ContactCTA';
import './Home.css';

const Home = () => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  return (
    <div className={`home ${isVisible ? 'fade-in' : ''}`}>
      <Hero />
      <ServicesPreview />
      <Benefits />
      <Stats />
      <Process />
      <ContactCTA />
    </div>
  );
};

export default Home; 