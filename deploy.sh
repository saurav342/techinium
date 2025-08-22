#!/bin/bash

echo "🚀 Deploying Techinium React App to Netlify..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Build the project
echo "🔨 Building the project..."
npm run build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    
    # Check if Netlify CLI is installed
    if command -v netlify &> /dev/null; then
        echo "🌐 Deploying to Netlify..."
        netlify deploy --prod --dir=build
    else
        echo "📁 Build completed successfully!"
        echo "📋 To deploy to Netlify:"
        echo "   1. Install Netlify CLI: npm install -g netlify-cli"
        echo "   2. Run: netlify deploy --prod --dir=build"
        echo "   3. Or drag the 'build' folder to Netlify's deploy area"
    fi
else
    echo "❌ Build failed. Please check the error messages above."
    exit 1
fi

echo "🎉 Deployment process completed!" 