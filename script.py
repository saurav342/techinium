# Create the main HTML file for Netlify deployment
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Techinium - AI-Powered Digital Solutions</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <!-- Header -->
    <header class="header" id="header">
        <nav class="nav container">
            <div class="nav__brand">
                <i class="fas fa-robot nav__logo"></i>
                <span class="nav__title">Techinium</span>
            </div>
            <div class="nav__menu" id="nav-menu">
                <ul class="nav__list">
                    <li class="nav__item"><a href="#home" class="nav__link active">Home</a></li>
                    <li class="nav__item"><a href="#services" class="nav__link">Services</a></li>
                    <li class="nav__item"><a href="#about" class="nav__link">About</a></li>
                    <li class="nav__item"><a href="#portfolio" class="nav__link">Portfolio</a></li>
                    <li class="nav__item"><a href="#contact" class="nav__link">Contact</a></li>
                </ul>
                <div class="nav__close" id="nav-close">
                    <i class="fas fa-times"></i>
                </div>
            </div>
            <div class="nav__toggle" id="nav-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero__container container">
            <div class="hero__content">
                <h1 class="hero__title">
                    <span class="typing-text">AI-Powered Digital Solutions</span>
                    <br>for Tomorrow's Businesses
                </h1>
                <p class="hero__description">
                    Transform your business with intelligent web and app development solutions that leverage cutting-edge artificial intelligence to deliver exceptional results.
                </p>
                <div class="hero__buttons">
                    <a href="#contact" class="btn btn-primary">Get Started</a>
                    <a href="#services" class="btn btn-secondary">View Services</a>
                </div>
            </div>
            <div class="hero__image">
                <div class="hero__ai-elements">
                    <div class="ai-circle ai-circle--1"></div>
                    <div class="ai-circle ai-circle--2"></div>
                    <div class="ai-circle ai-circle--3"></div>
                    <div class="ai-shape ai-shape--1"></div>
                    <div class="ai-shape ai-shape--2"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services" id="services">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">AI-Enhanced Services</h2>
                <p class="section__subtitle">
                    Comprehensive digital solutions powered by artificial intelligence
                </p>
            </div>
            <div class="services__grid" id="services-grid">
                <!-- Services will be dynamically loaded -->
            </div>
        </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="about" id="about">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Why Choose Techinium</h2>
                <p class="section__subtitle">
                    Leading the future of development with AI-first solutions
                </p>
            </div>
            <div class="benefits__grid" id="benefits-grid">
                <!-- Benefits will be dynamically loaded -->
            </div>
            <div class="stats">
                <div class="stats__item">
                    <div class="stats__number" data-target="200">0</div>
                    <div class="stats__label">AI Projects Delivered</div>
                </div>
                <div class="stats__item">
                    <div class="stats__number" data-target="98">0</div>
                    <div class="stats__label">Client Satisfaction %</div>
                </div>
                <div class="stats__item">
                    <div class="stats__number" data-target="50">0</div>
                    <div class="stats__label">Expert Developers</div>
                </div>
                <div class="stats__item">
                    <div class="stats__number" data-target="24">0</div>
                    <div class="stats__label">Hours Support</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section class="process">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Our AI-Driven Process</h2>
                <p class="section__subtitle">
                    Five intelligent steps to transform your digital presence
                </p>
            </div>
            <div class="process__timeline" id="process-timeline">
                <!-- Process steps will be dynamically loaded -->
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section class="portfolio" id="portfolio">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Featured Projects</h2>
                <p class="section__subtitle">
                    Showcase of our AI-powered development solutions
                </p>
            </div>
            <div class="portfolio__filters">
                <button class="filter-btn active" data-filter="all">All Projects</button>
                <button class="filter-btn" data-filter="web-app">Web Apps</button>
                <button class="filter-btn" data-filter="mobile-app">Mobile Apps</button>
                <button class="filter-btn" data-filter="e-commerce">E-commerce</button>
            </div>
            <div class="portfolio__grid" id="portfolio-grid">
                <!-- Portfolio items will be dynamically loaded -->
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Client Success Stories</h2>
                <p class="section__subtitle">
                    What our clients say about our AI-driven solutions
                </p>
            </div>
            <div class="testimonials__slider" id="testimonials-slider">
                <!-- Testimonials will be dynamically loaded -->
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact" id="contact">
        <div class="container">
            <div class="section__header">
                <h2 class="section__title">Let's Build Something Amazing</h2>
                <p class="section__subtitle">
                    Ready to transform your business with AI-powered solutions?
                </p>
            </div>
            <div class="contact__content">
                <div class="contact__info">
                    <div class="contact__item">
                        <i class="fas fa-map-marker-alt"></i>
                        <div>
                            <h4>Address</h4>
                            <p>123 Innovation Street<br>Tech City, TC 12345</p>
                        </div>
                    </div>
                    <div class="contact__item">
                        <i class="fas fa-phone"></i>
                        <div>
                            <h4>Phone</h4>
                            <p>+1 (555) 123-4567</p>
                        </div>
                    </div>
                    <div class="contact__item">
                        <i class="fas fa-envelope"></i>
                        <div>
                            <h4>Email</h4>
                            <p>hello@techinium.com</p>
                        </div>
                    </div>
                    <div class="contact__item">
                        <i class="fas fa-clock"></i>
                        <div>
                            <h4>Office Hours</h4>
                            <p>Mon - Fri: 9:00 AM - 6:00 PM</p>
                        </div>
                    </div>
                </div>
                <form class="contact__form" id="contact-form">
                    <div class="form__group">
                        <input type="text" name="name" placeholder="Your Name" required>
                    </div>
                    <div class="form__group">
                        <input type="email" name="email" placeholder="Your Email" required>
                    </div>
                    <div class="form__group">
                        <input type="text" name="company" placeholder="Company Name">
                    </div>
                    <div class="form__group">
                        <select name="service" required>
                            <option value="">Select a Service</option>
                            <option value="web-development">Web Development</option>
                            <option value="mobile-development">Mobile Development</option>
                            <option value="ai-solutions">AI Solutions</option>
                            <option value="consulting">Consulting</option>
                        </select>
                    </div>
                    <div class="form__group">
                        <textarea name="message" placeholder="Tell us about your project..." rows="5" required></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer__content">
                <div class="footer__section">
                    <div class="footer__brand">
                        <i class="fas fa-robot"></i>
                        <span>Techinium</span>
                    </div>
                    <p>AI-powered digital solutions for tomorrow's businesses. Transform your ideas into intelligent applications.</p>
                    <div class="footer__social">
                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                        <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                <div class="footer__section">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="#services">Web Development</a></li>
                        <li><a href="#services">Mobile Apps</a></li>
                        <li><a href="#services">AI Solutions</a></li>
                        <li><a href="#services">Digital Transformation</a></li>
                    </ul>
                </div>
                <div class="footer__section">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="#about">About Us</a></li>
                        <li><a href="#portfolio">Portfolio</a></li>
                        <li><a href="#contact">Contact</a></li>
                        <li><a href="#">Careers</a></li>
                    </ul>
                </div>
                <div class="footer__section">
                    <h4>Newsletter</h4>
                    <p>Subscribe to get updates on AI trends and our latest projects.</p>
                    <form class="newsletter__form">
                        <input type="email" placeholder="Your email">
                        <button type="submit">Subscribe</button>
                    </form>
                </div>
            </div>
            <div class="footer__bottom">
                <p>&copy; 2025 Techinium. All rights reserved.</p>
                <div class="footer__links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Floating Action Button -->
    <div class="fab" id="fab">
        <i class="fas fa-comments"></i>
        <div class="fab__tooltip">Chat with us</div>
    </div>

    <!-- Scripts -->
    <script src="app.js"></script>
</body>
</html>"""

# Save HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ index.html created successfully")