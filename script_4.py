# Create manifest.json for PWA capabilities
manifest_content = """{
  "name": "Techinium - AI-Powered Digital Solutions",
  "short_name": "Techinium",
  "description": "Leading AI-driven service agency specializing in intelligent web, app, and mobile development solutions.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFFFFF",
  "theme_color": "#FF69B4",
  "orientation": "portrait-primary",
  "icons": [
    {
      "src": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTkyIiBoZWlnaHQ9IjE5MiIgdmlld0JveD0iMCAwIDE5MiAxOTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSIxOTIiIGhlaWdodD0iMTkyIiByeD0iMjQiIGZpbGw9InVybCgjZ3JhZGllbnQwX2xpbmVhcikiLz4KPHBhdGggZD0iTTk2IDQ4QzEyMC44NTMgNDggMTQ0IDcxLjE0NzIgMTQ0IDk2QzE0NCAxMjAuODUzIDEyMC44NTMgMTQ0IDk2IDE0NEM3MS4xNDcyIDE0NCA0OCAxMjAuODUzIDQ4IDk2QzQ4IDcxLjE0NzIgNzEuMTQ3MiA0OCA5NiA0OFoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik05NiA3MkMxMDkuMjU1IDcyIDEyMCA4Mi43NDUyIDEyMCA5NkMxMjAgMTA5LjI1NSAxMDkuMjU1IDEyMCA5NiAxMjBDODIuNzQ1MiAxMjAgNzIgMTA5LjI1NSA3MiA5NkM3MiA4Mi43NDUyIDgyLjc0NTIgNzIgOTYgNzJaIiBmaWxsPSJ1cmwoI2dyYWRpZW50MV9saW5lYXIpIi8+CjxkZWZzPgo8bGluZWFyR3JhZGllbnQgaWQ9ImdyYWRpZW50MF9saW5lYXIiIHgxPSIwIiB5MT0iMCIgeDI9IjE5MiIgeTI9IjE5MiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPgo8c3RvcCBzdG9wLWNvbG9yPSIjRkY2OUI0Ii8+CjxzdG9wIG9mZnNldD0iMC41IiBzdG9wLWNvbG9yPSIjMzJDRDMyIi8+CjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzkzNzBEQiIvPgo8L2xpbmVhckdyYWRpZW50Pgo8bGluZWFyR3JhZGllbnQgaWQ9ImdyYWRpZW50MV9saW5lYXIiIHgxPSI3MiIgeTE9IjcyIiB4Mj0iMTIwIiB5Mj0iMTIwIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiNGRkQ3MDAiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRkY2OUI0Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjwvZGVmcz4KPC9zdmc+",
      "sizes": "192x192",
      "type": "image/svg+xml"
    },
    {
      "src": "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgdmlld0JveD0iMCAwIDUxMiA1MTIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxyZWN0IHdpZHRoPSI1MTIiIGhlaWdodD0iNTEyIiByeD0iNjQiIGZpbGw9InVybCgjZ3JhZGllbnQwX2xpbmVhcikiLz4KPHBhdGggZD0iTTI1NiAxMjhDMzIyLjI3NCAxMjggMzg0IDE4OS43MjYgMzg0IDI1NkMzODQgMzIyLjI3NCAzMjIuMjc0IDM4NCAyNTYgMzg0QzE4OS43MjYgMzg0IDEyOCAzMjIuMjc0IDEyOCAyNTZDMTI4IDE4OS43MjYgMTg5LjcyNiAxMjggMjU2IDEyOFoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0yNTYgMTkyQzI5MC41MSAxOTIgMzIwIDIyMS40OSAzMjAgMjU2QzMyMCAyOTAuNTEgMjkwLjUxIDMyMCAyNTYgMzIwQzIyMS40OSAzMjAgMTkyIDI5MC41MSAxOTIgMjU2QzE5MiAyMjEuNDkgMjIxLjQ5IDE5MiAyNTYgMTkyWiIgZmlsbD0idXJsKCNncmFkaWVudDFfbGluZWFyKSIvPgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJncmFkaWVudDBfbGluZWFyIiB4MT0iMCIgeTE9IjAiIHgyPSI1MTIiIHkyPSI1MTIiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agc3RvcC1jb2xvcj0iI0ZGNjlCNCIvPgo8c3RvcCBvZmZzZXQ9IjAuNSIgc3RvcC1jb2xvcj0iIzMyQ0QzMiIvPgo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiM5MzcwREIiLz4KPC9saW5lYXJHcmFkaWVudD4KPGxpbmVhckdyYWRpZW50IGlkPSJncmFkaWVudDFfbGluZWFyIiB4MT0iMTkyIiB5MT0iMTkyIiB4Mj0iMzIwIiB5Mj0iMzIwIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiNGRkQ3MDAiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRkY2OUI0Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjwvZGVmcz4KPC9zdmc+",
      "sizes": "512x512",
      "type": "image/svg+xml"
    }
  ],
  "categories": ["business", "productivity", "developer"],
  "lang": "en",
  "dir": "ltr"
}"""

with open('manifest.json', 'w', encoding='utf-8') as f:
    f.write(manifest_content)

print("✓ manifest.json created successfully")

# Update the HTML file to include the manifest
print("\n📝 Remember to add the following line to the <head> section of index.html:")
print('<link rel="manifest" href="/manifest.json">')
print("\nI'll update the HTML file to include this...")

# Read the current HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Add the manifest link to the head section
if 'manifest.json' not in html_content:
    html_content = html_content.replace(
        '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">',
        '''<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link rel="manifest" href="/manifest.json">'''
    )

# Save the updated HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ Updated index.html to include manifest.json")

print("\n🎉 Complete Netlify deployment package ready!")
print("\nFinal file list:")
print("1. index.html - Main website file")
print("2. style.css - All styling")
print("3. app.js - JavaScript functionality")
print("4. _redirects - Netlify routing rules")
print("5. netlify.toml - Build configuration")
print("6. manifest.json - PWA manifest")
print("7. README.md - Documentation")
print("8. deployment_checklist.txt - Step-by-step guide")

print("\n📦 To deploy to Netlify:")
print("1. Create a new folder called 'techinium-website'")
print("2. Copy all 8 files into that folder")
print("3. Either:")
print("   - Drag the folder to https://app.netlify.com/drop")
print("   - Or create a GitHub repo and connect to Netlify")
print("4. Your site will be live immediately!")

# Create a simple batch file for Windows users to easily zip the files
if True:  # Always create this for convenience
    batch_content = """@echo off
echo Creating Techinium Website deployment package...
if exist techinium-website.zip del techinium-website.zip
powershell -command "Compress-Archive -Path 'index.html','style.css','app.js','_redirects','netlify.toml','manifest.json','README.md','deployment_checklist.txt' -DestinationPath 'techinium-website.zip' -Force"
echo.
echo ✓ techinium-website.zip created successfully!
echo.
echo You can now upload this zip file to Netlify:
echo 1. Go to https://app.netlify.com/drop
echo 2. Drag and drop techinium-website.zip
echo 3. Your site will be deployed automatically!
echo.
pause
"""
    
    with open('create_deployment_package.bat', 'w', encoding='utf-8') as f:
        f.write(batch_content)
    
    print("9. create_deployment_package.bat - Windows zip utility")
    
# Create shell script for Mac/Linux users
shell_content = """#!/bin/bash
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
"""

with open('create_deployment_package.sh', 'w', encoding='utf-8') as f:
    f.write(shell_content)

print("10. create_deployment_package.sh - Mac/Linux zip utility")
print("\nYour Techinium website is ready for deployment! 🚀")