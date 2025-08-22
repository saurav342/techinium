# Techinium - React.js Website

AI-powered digital solutions agency website built with modern React.js technologies.

## 🚀 Features

- **Modern React Architecture**: Built with React 18, React Router, and modern hooks
- **Responsive Design**: Mobile-first approach with CSS Grid and Flexbox
- **AI-Focused Content**: Showcases AI-enhanced services and solutions
- **Interactive Components**: Smooth animations and user-friendly navigation
- **Performance Optimized**: Fast loading with code splitting and optimization
- **Netlify Ready**: Optimized for deployment on Netlify

## 🛠️ Technologies Used

- **Frontend**: React 18, React Router DOM
- **Styling**: CSS3 with CSS Grid, Flexbox, and animations
- **Icons**: Font Awesome
- **Build Tool**: Create React App
- **Deployment**: Netlify

## 🎨 Color Palette

- **Primary**: Pink (#FF69B4, #FFB6C1)
- **Secondary**: Green (#32CD32, #90EE90) 
- **Accent**: Purple (#9370DB, #DDA0DD)
- **Warning**: Golden Yellow (#FFD700, #FFF8DC)

## 📁 Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── Header.js       # Navigation header
│   ├── Hero.js         # Hero section with typing animation
│   ├── ServicesPreview.js # Services preview cards
│   ├── Benefits.js     # Why choose us section
│   ├── Stats.js        # Animated statistics
│   ├── Process.js      # Development workflow timeline
│   └── ContactCTA.js   # Call-to-action section
├── pages/              # Page components
│   ├── Home.js         # Home page
│   ├── Services.js     # All services page
│   ├── About.js        # About us page
│   ├── Portfolio.js    # Portfolio/projects page
│   └── Contact.js      # Contact form page
├── App.js              # Main app component with routing
├── index.js            # React entry point
└── index.css           # Global styles
```

## 🚀 Getting Started

### Prerequisites

- Node.js (version 18 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd techinium-react
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Available Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App

## 🌐 Deployment to Netlify

### Option 1: Git Repository (Recommended)
1. Push your code to GitHub/GitLab
2. Connect your Netlify account to your Git provider
3. Select the repository and deploy
4. Netlify will automatically build and deploy your React app

### Option 2: Netlify CLI
1. Install Netlify CLI: `npm install -g netlify-cli`
2. Build your project: `npm run build`
3. Deploy: `netlify deploy --prod --dir=build`

### Option 3: Drag and Drop
1. Run `npm run build`
2. Drag the `build` folder to Netlify's deploy area

## 🔧 Configuration

### Netlify Configuration
The project includes:
- `netlify.toml` - Build and redirect configuration
- `_redirects` - SPA routing support

### Environment Variables
Create a `.env` file in the root directory for any environment-specific variables.

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (320px - 767px)

## 🎭 Components

### Header Component
- Fixed navigation with smooth scrolling
- Mobile-responsive hamburger menu
- Active route highlighting

### Hero Section
- Animated typing text effect
- AI-themed visual elements
- Call-to-action buttons

### Services Preview
- Grid layout of featured services
- Technology tags
- Hover animations

### Benefits Section
- Why choose Techinium
- Icon-based presentation
- Responsive grid layout

### Statistics
- Animated counters
- Intersection Observer for performance
- Smooth number counting

### Process Timeline
- Step-by-step development workflow
- Visual timeline design
- Hover effects

## 🚀 Performance Features

- **Code Splitting**: Automatic route-based code splitting
- **Lazy Loading**: Components load when needed
- **Optimized Images**: Efficient image handling
- **CSS Animations**: Hardware-accelerated animations
- **Responsive Images**: Optimized for different screen sizes

## 🔒 Security

- **Content Security Policy**: Configured for security
- **HTTPS**: Enforced on Netlify
- **Input Validation**: Form validation and sanitization

## 📈 Analytics & Monitoring

- **Web Vitals**: Performance monitoring
- **Error Boundaries**: Graceful error handling
- **Loading States**: User feedback during operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

© 2025 Techinium. All rights reserved.

## 📞 Contact

For questions or support:
- Email: hello@techinium.com
- Website: [techinium.com](https://techinium.com)

## 🔄 Migration from Static HTML

This React.js version is a complete rewrite of the original static HTML website, featuring:
- **Component-based architecture** instead of monolithic HTML
- **React Router** for client-side navigation
- **State management** with React hooks
- **Modern build system** with Create React App
- **Optimized performance** with code splitting
- **Better maintainability** with modular components 