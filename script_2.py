# Create the JavaScript file for Netlify deployment
js_content = """// Application data
const appData = {
  "services": [
    {
      "title": "AI-Enhanced Web Application Development",
      "description": "Custom web applications powered by artificial intelligence, featuring responsive design, intelligent user interfaces, and automated optimization.",
      "technologies": ["HTML5", "CSS3", "JavaScript", "React", "Angular", "Vue.js", "Node.js", "Python", "AI/ML APIs"],
      "icon": "🌐"
    },
    {
      "title": "Intelligent Mobile App Development",
      "description": "Native and cross-platform mobile apps with AI-driven features, predictive analytics, and smart user experiences.",
      "technologies": ["Swift", "Kotlin", "Flutter", "React Native", "TensorFlow Lite", "Core ML"],
      "icon": "📱"
    },
    {
      "title": "AI-Driven Full Stack Development",
      "description": "End-to-end development solutions with intelligent backend systems, automated deployments, and AI-enhanced databases.",
      "technologies": ["MEAN Stack", "MERN Stack", "Django", "Laravel", "Microservices", "AI Frameworks"],
      "icon": "⚡"
    },
    {
      "title": "Smart API Development & Integration",
      "description": "Intelligent APIs with automated documentation, smart routing, and AI-powered data processing capabilities.",
      "technologies": ["REST APIs", "GraphQL", "OAuth", "JWT", "AI APIs", "Machine Learning Models"],
      "icon": "🔗"
    },
    {
      "title": "AI-Powered E-commerce Development",
      "description": "Intelligent online stores with recommendation engines, automated inventory management, and predictive analytics.",
      "technologies": ["Shopify", "Magento", "WooCommerce", "AI Recommendation Systems", "Payment AI"],
      "icon": "🛒"
    },
    {
      "title": "Intelligent UI/UX Design Services",
      "description": "AI-driven design processes with user behavior analysis, automated A/B testing, and personalized experiences.",
      "technologies": ["Figma", "Adobe XD", "User Analytics AI", "Design Systems", "Personalization Engines"],
      "icon": "🎨"
    },
    {
      "title": "AI-Driven Digital Transformation",
      "description": "Comprehensive business transformation using AI technologies, automation, and intelligent process optimization.",
      "technologies": ["Cloud AI", "Automation Tools", "ML Pipelines", "Data Analytics", "Process Mining"],
      "icon": "🚀"
    },
    {
      "title": "Smart Web Development Consulting",
      "description": "Strategic consulting with AI-powered architecture recommendations, performance optimization, and security analysis.",
      "technologies": ["Architecture AI", "Performance Tools", "Security AI", "Code Analysis", "Optimization Algorithms"],
      "icon": "💡"
    },
    {
      "title": "Automated Website Maintenance & Support",
      "description": "AI-powered monitoring, automated updates, predictive maintenance, and intelligent issue resolution.",
      "technologies": ["Monitoring AI", "Automated Tools", "Predictive Analytics", "Security Bots", "Performance AI"],
      "icon": "🔧"
    },
    {
      "title": "AI-Enhanced Quality Assurance & Testing",
      "description": "Intelligent testing with automated test generation, AI-powered bug detection, and predictive quality metrics.",
      "technologies": ["Test Automation AI", "Selenium", "AI Testing Tools", "Quality Prediction", "Smart Debugging"],
      "icon": "✅"
    },
    {
      "title": "Intelligent Digital Marketing Integration",
      "description": "AI-driven marketing automation, intelligent SEO, predictive analytics, and personalized campaign optimization.",
      "technologies": ["Marketing AI", "SEO Tools", "Analytics AI", "Automation Platforms", "Predictive Models"],
      "icon": "📈"
    },
    {
      "title": "AI-Optimized Cloud Services & DevOps",
      "description": "Intelligent cloud infrastructure with automated scaling, AI-powered monitoring, and smart deployment strategies.",
      "technologies": ["AWS AI", "Azure AI", "Google Cloud AI", "Kubernetes", "DevOps Automation", "ML Ops"],
      "icon": "☁️"
    }
  ],
  "benefits": [
    {
      "title": "AI-First Approach",
      "description": "Every solution is built with artificial intelligence at its core, ensuring smarter, more efficient results.",
      "icon": "🤖"
    },
    {
      "title": "Cutting-Edge Technology",
      "description": "We leverage the latest AI frameworks and technologies to deliver future-ready solutions.",
      "icon": "⚡"
    },
    {
      "title": "Expert Team",
      "description": "Our team combines deep technical expertise with AI specialization to drive exceptional outcomes.",
      "icon": "👥"
    },
    {
      "title": "Proven Results",
      "description": "Delivered 200+ AI-powered projects with 98% client satisfaction and measurable business impact.",
      "icon": "🏆"
    }
  ],
  "process": [
    {
      "step": 1,
      "title": "AI-Powered Discovery",
      "description": "We use intelligent analysis tools to understand your business needs and identify optimization opportunities."
    },
    {
      "step": 2,
      "title": "Intelligent Design",
      "description": "AI-driven design processes create user-centric interfaces with predictive user experience optimization."
    },
    {
      "step": 3,
      "title": "Smart Development",
      "description": "Our development process integrates AI capabilities from the ground up, ensuring intelligent functionality."
    },
    {
      "step": 4,
      "title": "AI-Enhanced Testing",
      "description": "Automated testing with AI-powered quality assurance ensures robust, reliable solutions."
    },
    {
      "step": 5,
      "title": "Automated Deployment",
      "description": "Intelligent deployment and ongoing support with predictive maintenance and optimization."
    }
  ],
  "portfolio": [
    {
      "title": "E-commerce AI Platform",
      "description": "Intelligent online marketplace with AI-powered recommendations and automated inventory management.",
      "category": "e-commerce",
      "technologies": ["React", "Node.js", "TensorFlow", "AWS"],
      "icon": "🛒"
    },
    {
      "title": "Smart Healthcare App",
      "description": "Mobile health application with AI diagnostics and personalized treatment recommendations.",
      "category": "mobile-app",
      "technologies": ["React Native", "Python", "ML Models", "Cloud AI"],
      "icon": "🏥"
    },
    {
      "title": "Financial Analytics Dashboard",
      "description": "Real-time financial dashboard with predictive analytics and automated risk assessment.",
      "category": "web-app",
      "technologies": ["Vue.js", "Python", "AI Analytics", "Data Visualization"],
      "icon": "📊"
    },
    {
      "title": "AI-Powered CRM System",
      "description": "Customer relationship management system with intelligent lead scoring and automated workflows.",
      "category": "web-app",
      "technologies": ["Angular", "Django", "Machine Learning", "PostgreSQL"],
      "icon": "👥"
    }
  ],
  "testimonials": [
    {
      "name": "Sarah Johnson",
      "company": "TechStart Inc.",
      "position": "CEO",
      "review": "Techinium's AI-driven approach transformed our e-commerce platform. Sales increased by 150% within 6 months!",
      "rating": 5
    },
    {
      "name": "Michael Chen",
      "company": "Digital Innovations",
      "position": "CTO",
      "review": "The intelligent automation they built saved us 40 hours per week. Outstanding technical expertise!",
      "rating": 5
    },
    {
      "name": "Emily Rodriguez",
      "company": "Growth Dynamics",
      "position": "Marketing Director",
      "review": "Their AI-powered marketing integration delivered a 300% improvement in lead conversion rates.",
      "rating": 5
    }
  ]
};

// DOM Elements
const navMenu = document.getElementById('nav-menu');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');
const navLinks = document.querySelectorAll('.nav__link');

// Mobile menu toggle
navToggle?.addEventListener('click', () => {
  navMenu?.classList.add('show');
});

navClose?.addEventListener('click', () => {
  navMenu?.classList.remove('show');
});

// Close menu when clicking on a link
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    navMenu?.classList.remove('show');
  });
});

// Header scroll effect
window.addEventListener('scroll', () => {
  const header = document.getElementById('header');
  if (window.scrollY > 50) {
    header?.classList.add('scroll');
  } else {
    header?.classList.remove('scroll');
  }
});

// Active navigation link
const sections = document.querySelectorAll('section[id]');

const scrollActive = () => {
  const scrollY = window.pageYOffset;

  sections.forEach(current => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 50;
    const sectionId = current.getAttribute('id');
    const sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']');

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      sectionsClass?.classList.add('active');
    } else {
      sectionsClass?.classList.remove('active');
    }
  });
};

window.addEventListener('scroll', scrollActive);

// Typing effect for hero title
const typingText = document.querySelector('.typing-text');
if (typingText) {
  const text = typingText.textContent;
  typingText.textContent = '';
  
  let i = 0;
  const typing = () => {
    if (i < text.length) {
      typingText.textContent += text.charAt(i);
      i++;
      setTimeout(typing, 100);
    }
  };
  
  setTimeout(typing, 500);
}

// Load services
const loadServices = () => {
  const servicesGrid = document.getElementById('services-grid');
  if (!servicesGrid) return;

  servicesGrid.innerHTML = appData.services.map(service => `
    <div class="service__card fade-in">
      <span class="service__icon">${service.icon}</span>
      <h3 class="service__title">${service.title}</h3>
      <p class="service__description">${service.description}</p>
      <div class="service__technologies">
        ${service.technologies.map(tech => `<span class="tech__tag">${tech}</span>`).join('')}
      </div>
    </div>
  `).join('');
};

// Load benefits
const loadBenefits = () => {
  const benefitsGrid = document.getElementById('benefits-grid');
  if (!benefitsGrid) return;

  benefitsGrid.innerHTML = appData.benefits.map(benefit => `
    <div class="benefit__card fade-in">
      <span class="benefit__icon">${benefit.icon}</span>
      <h3 class="benefit__title">${benefit.title}</h3>
      <p class="benefit__description">${benefit.description}</p>
    </div>
  `).join('');
};

// Load process
const loadProcess = () => {
  const processTimeline = document.getElementById('process-timeline');
  if (!processTimeline) return;

  processTimeline.innerHTML = appData.process.map(step => `
    <div class="process__step fade-in">
      <div class="process__number">${step.step}</div>
      <div class="process__content">
        <h3>${step.title}</h3>
        <p>${step.description}</p>
      </div>
    </div>
  `).join('');
};

// Load portfolio
const loadPortfolio = () => {
  const portfolioGrid = document.getElementById('portfolio-grid');
  if (!portfolioGrid) return;

  portfolioGrid.innerHTML = appData.portfolio.map(item => `
    <div class="portfolio__item fade-in" data-category="${item.category}">
      <div class="portfolio__image">
        <span>${item.icon}</span>
      </div>
      <div class="portfolio__content">
        <h3 class="portfolio__title">${item.title}</h3>
        <p class="portfolio__description">${item.description}</p>
        <div class="portfolio__technologies">
          ${item.technologies.map(tech => `<span class="portfolio__tech">${tech}</span>`).join('')}
        </div>
      </div>
    </div>
  `).join('');
};

// Portfolio filter
const portfolioFilters = document.querySelectorAll('.filter-btn');
portfolioFilters.forEach(filter => {
  filter.addEventListener('click', () => {
    // Remove active class from all filters
    portfolioFilters.forEach(btn => btn.classList.remove('active'));
    // Add active class to clicked filter
    filter.classList.add('active');
    
    const filterValue = filter.getAttribute('data-filter');
    const portfolioItems = document.querySelectorAll('.portfolio__item');
    
    portfolioItems.forEach(item => {
      if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
        item.style.display = 'block';
        setTimeout(() => item.style.opacity = '1', 10);
      } else {
        item.style.opacity = '0';
        setTimeout(() => item.style.display = 'none', 300);
      }
    });
  });
});

// Load testimonials
const loadTestimonials = () => {
  const testimonialsSlider = document.getElementById('testimonials-slider');
  if (!testimonialsSlider) return;

  testimonialsSlider.innerHTML = appData.testimonials.map(testimonial => `
    <div class="testimonial__item fade-in">
      <div class="testimonial__stars">
        ${'★'.repeat(testimonial.rating)}
      </div>
      <p class="testimonial__text">"${testimonial.review}"</p>
      <div class="testimonial__author">${testimonial.name}</div>
      <div class="testimonial__position">${testimonial.position}, ${testimonial.company}</div>
    </div>
  `).join('');
};

// Counter animation
const animateCounters = () => {
  const counters = document.querySelectorAll('.stats__number');
  
  counters.forEach(counter => {
    const target = parseInt(counter.getAttribute('data-target'));
    const increment = target / 100;
    let current = 0;
    
    const updateCounter = () => {
      if (current < target) {
        current += increment;
        counter.textContent = Math.ceil(current);
        setTimeout(updateCounter, 20);
      } else {
        counter.textContent = target;
      }
    };
    
    updateCounter();
  });
};

// Intersection Observer for animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      
      // Start counter animation when stats section is visible
      if (entry.target.querySelector('.stats__number')) {
        animateCounters();
      }
    }
  });
}, observerOptions);

// Observe elements for animation
const observeElements = () => {
  const elementsToObserve = document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right');
  elementsToObserve.forEach(el => observer.observe(el));
};

// Contact form handling
const contactForm = document.getElementById('contact-form');
contactForm?.addEventListener('submit', (e) => {
  e.preventDefault();
  
  // Get form data
  const formData = new FormData(contactForm);
  const data = Object.fromEntries(formData);
  
  // Simple validation
  if (!data.name || !data.email || !data.message) {
    alert('Please fill in all required fields.');
    return;
  }
  
  // Email validation
  const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  if (!emailRegex.test(data.email)) {
    alert('Please enter a valid email address.');
    return;
  }
  
  // Simulate form submission
  alert('Thank you for your message! We\\'ll get back to you soon.');
  contactForm.reset();
});

// Newsletter form handling
const newsletterForm = document.querySelector('.newsletter__form');
newsletterForm?.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const email = e.target.querySelector('input[type="email"]').value;
  
  if (!email) {
    alert('Please enter your email address.');
    return;
  }
  
  const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  if (!emailRegex.test(email)) {
    alert('Please enter a valid email address.');
    return;
  }
  
  alert('Thank you for subscribing to our newsletter!');
  e.target.reset();
});

// Floating Action Button
const fab = document.getElementById('fab');
fab?.addEventListener('click', () => {
  // Simulate opening chat
  alert('Chat feature coming soon! For now, please use the contact form or email us at hello@techinium.com');
});

// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Preloader (if needed)
window.addEventListener('load', () => {
  const preloader = document.querySelector('.preloader');
  if (preloader) {
    preloader.style.opacity = '0';
    setTimeout(() => {
      preloader.style.display = 'none';
    }, 300);
  }
});

// Initialize all functions when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  loadServices();
  loadBenefits();
  loadProcess();
  loadPortfolio();
  loadTestimonials();
  observeElements();
  
  // Add initial animation classes
  setTimeout(() => {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach((el, index) => {
      setTimeout(() => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      }, index * 100);
    });
  }, 100);
});

// Handle window resize
let resizeTimeout;
window.addEventListener('resize', () => {
  clearTimeout(resizeTimeout);
  resizeTimeout = setTimeout(() => {
    // Recalculate any layout-dependent features
    scrollActive();
  }, 250);
});

// Service worker registration for PWA (optional)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(registration => {
        console.log('SW registered: ', registration);
      })
      .catch(registrationError => {
        console.log('SW registration failed: ', registrationError);
      });
  });
}

// Performance monitoring
const logPerformance = () => {
  if ('performance' in window) {
    window.addEventListener('load', () => {
      setTimeout(() => {
        const perfData = performance.getEntriesByType('navigation')[0];
        console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
      }, 0);
    });
  }
};

logPerformance();

// Add some interactive hover effects
document.addEventListener('DOMContentLoaded', () => {
  // Add hover effect to service cards
  const serviceCards = document.querySelectorAll('.service__card');
  serviceCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-10px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0) scale(1)';
    });
  });
  
  // Add hover effect to portfolio items
  const portfolioItems = document.querySelectorAll('.portfolio__item');
  portfolioItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
      item.style.transform = 'translateY(-5px) scale(1.02)';
    });
    
    item.addEventListener('mouseleave', () => {
      item.style.transform = 'translateY(0) scale(1)';
    });
  });
});

// Add parallax effect to hero section
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const parallax = document.querySelector('.hero__ai-elements');
  
  if (parallax) {
    const speed = scrolled * 0.5;
    parallax.style.transform = `translateY(${speed}px)`;
  }
});

// Add loading animation
const addLoadingAnimation = () => {
  const style = document.createElement('style');
  style.textContent = `
    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }
    
    .loading {
      animation: pulse 1.5s ease-in-out infinite;
    }
  `;
  document.head.appendChild(style);
};

addLoadingAnimation();

// Export functions for potential testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    appData,
    loadServices,
    loadBenefits,
    loadProcess,
    loadPortfolio,
    loadTestimonials
  };
}"""

# Save JavaScript file
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✓ app.js created successfully")