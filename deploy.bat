@echo off
echo 🚀 Deploying Techinium React App to Netlify...

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed. Please install Node.js first.
    pause
    exit /b 1
)

REM Check if npm is installed
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ npm is not installed. Please install npm first.
    pause
    exit /b 1
)

REM Install dependencies
echo 📦 Installing dependencies...
npm install

REM Build the project
echo 🔨 Building the project...
npm run build

REM Check if build was successful
if %errorlevel% equ 0 (
    echo ✅ Build successful!
    
    REM Check if Netlify CLI is installed
    netlify --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo 🌐 Deploying to Netlify...
        netlify deploy --prod --dir=build
    ) else (
        echo 📁 Build completed successfully!
        echo 📋 To deploy to Netlify:
        echo    1. Install Netlify CLI: npm install -g netlify-cli
        echo    2. Run: netlify deploy --prod --dir=build
        echo    3. Or drag the 'build' folder to Netlify's deploy area
    )
) else (
    echo ❌ Build failed. Please check the error messages above.
    pause
    exit /b 1
)

echo 🎉 Deployment process completed!
pause 