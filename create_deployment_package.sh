#!/bin/bash
echo "Creating Techinium Website deployment package..."
if [ -f "techinium-website.zip" ]; then
    rm techinium-website.zip
fi
zip -r techinium-website.zip index.html style.css app.js _redirects netlify.toml manifest.json README.md deployment_checklist.txt
echo
echo "✓ techinium-website.zip created successfully!"
echo
echo "You can now upload this zip file to Netlify:"
echo "1. Go to https://app.netlify.com/drop"
echo "2. Drag and drop techinium-website.zip"
echo "3. Your site will be deployed automatically!"
echo
