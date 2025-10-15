@echo off
echo ========================================
echo Yakkai Neri - Node.js Setup Script
echo ========================================
echo.

echo Step 1: Installing Node.js dependencies...
call npm install
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✅ Dependencies installed successfully!
echo.

echo Step 2: Converting templates from Flask to Express...
call node scripts/convert-templates.js
if %errorlevel% neq 0 (
    echo ERROR: Failed to convert templates
    pause
    exit /b 1
)
echo ✅ Templates converted successfully!
echo.

echo Step 3: Checking environment variables...
if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo.
    echo ⚠️  IMPORTANT: Edit .env file and add your DATABASE_URL
    echo.
) else (
    echo ℹ️  .env file already exists
)
echo.

echo ========================================
echo ✅ Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your Neon DATABASE_URL
echo 2. Run 'npm run dev' to start the development server
echo 3. Visit http://localhost:3000
echo.
echo To deploy to Vercel:
echo   - Install Vercel CLI: npm i -g vercel
echo   - Run: vercel
echo.
pause
