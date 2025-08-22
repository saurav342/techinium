# Create Netlify configuration files

# Create _redirects file for single page application routing
redirects_content = """# Redirects for Netlify
/*    /index.html   200

# Security headers
/*
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; font-src 'self' https://cdnjs.cloudflare.com; img-src 'self' data: https:; connect-src 'self';
"""

with open('_redirects', 'w', encoding='utf-8') as f:
    f.write(redirects_content)

# Create netlify.toml for additional configuration
toml_content = """[build]
  publish = "."
  
[build.environment]
  NODE_VERSION = "18"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "max-age=31536000"

[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "max-age=31536000"

[[headers]]
  for = "/*.png"
  [headers.values]
    Cache-Control = "max-age=31536000"

[[headers]]
  for = "/*.jpg"
  [headers.values]
    Cache-Control = "max-age=31536000"

[[headers]]
  for = "/*.svg"
  [headers.values]
    Cache-Control = "max-age=31536000"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
"""

with open('netlify.toml', 'w', encoding='utf-8') as f:
    f.write(toml_content)

# Create a README file with deployment instructions
readme_content = """# Techinium Website

AI-powered digital solutions agency website built with modern web technologies.

## Features

- **Modern Design**: Clean, professional layout with light color theme
- **AI-Focused Content**: Showcases AI-enhanced services and solutions
- **Responsive**: Works perfectly on all devices
- **Interactive**: Smooth animations and user-friendly navigation
- **Performance Optimized**: Fast loading and optimized assets

## Technologies Used

- HTML5
- CSS3 (Custom CSS with CSS Grid and Flexbox)
- Vanilla JavaScript (ES6+)
- Font Awesome Icons
- Responsive Design

## Color Palette

- Primary: Pink (#FF69B4, #FFB6C1)
- Secondary: Green (#32CD32, #90EE90) 
- Accent: Purple (#9370DB, #DDA0DD)
- Warning: Golden Yellow (#FFD700, #FFF8DC)

## Deployment to Netlify

### Option 1: Drag and Drop
1. Create a folder with all the files: `index.html`, `style.css`, `app.js`, `_redirects`, `netlify.toml`
2. Go to [Netlify](https://netlify.com)
3. Drag the folder to the deploy area
4. Your site will be deployed automatically

### Option 2: Git Repository
1. Create a new repository on GitHub
2. Upload all files to the repository
3. Connect your Netlify account to GitHub
4. Select the repository and deploy

### Option 3: Netlify CLI
1. Install Netlify CLI: `npm install -g netlify-cli`
2. Run `netlify login` to authenticate
3. Run `netlify deploy` for preview
4. Run `netlify deploy --prod` for production

## File Structure

```
techinium-website/
├── index.html          # Main HTML file
├── style.css           # Stylesheet with custom CSS
├── app.js              # JavaScript functionality
├── _redirects          # Netlify redirects configuration
├── netlify.toml        # Netlify build configuration
└── README.md           # This file
```

## Services Offered

The website showcases 12 AI-enhanced services:

1. AI-Enhanced Web Application Development
2. Intelligent Mobile App Development
3. AI-Driven Full Stack Development
4. Smart API Development & Integration
5. AI-Powered E-commerce Development
6. Intelligent UI/UX Design Services
7. AI-Driven Digital Transformation
8. Smart Web Development Consulting
9. Automated Website Maintenance & Support
10. AI-Enhanced Quality Assurance & Testing
11. Intelligent Digital Marketing Integration
12. AI-Optimized Cloud Services & DevOps

## Contact

For any questions or modifications, please contact the development team.

## License

© 2025 Techinium. All rights reserved.
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✓ _redirects file created successfully")
print("✓ netlify.toml file created successfully") 
print("✓ README.md file created successfully")

# Create a simple deployment checklist
checklist_content = """# Netlify Deployment Checklist for Techinium Website

## Files to Upload:
- [ ] index.html
- [ ] style.css  
- [ ] app.js
- [ ] _redirects
- [ ] netlify.toml
- [ ] README.md

## Deployment Steps:

### Method 1: Drag & Drop (Easiest)
1. [ ] Zip all files together OR create a folder with all files
2. [ ] Go to https://app.netlify.com/drop
3. [ ] Drag the folder/zip file to deploy
4. [ ] Wait for deployment to complete
5. [ ] Test the live website

### Method 2: Git Integration (Recommended for updates)
1. [ ] Create new repository on GitHub
2. [ ] Upload all files to the repository
3. [ ] Go to https://app.netlify.com
4. [ ] Click "New site from Git"
5. [ ] Connect GitHub and select repository
6. [ ] Deploy settings should be automatic due to netlify.toml
7. [ ] Deploy site

## After Deployment:
- [ ] Test all navigation links
- [ ] Verify contact form (will show alert)
- [ ] Check responsive design on mobile
- [ ] Test all interactive elements
- [ ] Verify all sections load properly
- [ ] Check performance with Lighthouse

## Domain Setup (Optional):
- [ ] Purchase domain (e.g., techinium.com)
- [ ] In Netlify dashboard, go to Domain settings
- [ ] Add custom domain
- [ ] Configure DNS settings
- [ ] Enable HTTPS (automatic with Netlify)

## Post-Deployment:
- [ ] Set up Google Analytics (add tracking code to index.html)
- [ ] Set up contact form handling (use Netlify Forms or external service)
- [ ] Consider adding real testimonials and portfolio items
- [ ] Optimize images if added later
- [ ] Set up monitoring and backups

## Notes:
- The website is fully responsive and optimized for performance
- All animations and interactions are included
- Contact form currently shows alerts (integrate with Netlify Forms for real functionality)
- Color scheme uses pink, green, purple, and golden yellow as requested
- All 12 AI-enhanced services are included from the provided document
"""

with open('deployment_checklist.txt', 'w', encoding='utf-8') as f:
    f.write(checklist_content)

print("✓ deployment_checklist.txt created successfully")
print("\n🎉 All files ready for Netlify deployment!")
print("\nFiles created:")
print("- index.html (Main website)")
print("- style.css (Styling)")  
print("- app.js (Functionality)")
print("- _redirects (Netlify routing)")
print("- netlify.toml (Build config)")
print("- README.md (Documentation)")
print("- deployment_checklist.txt (Deployment guide)")