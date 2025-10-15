@echo off
echo ========================================
echo Deploy to Vercel - Yakkai Neri
echo ========================================
echo.

echo Checking if Vercel CLI is installed...
where vercel >nul 2>&1
if %errorlevel% neq 0 (
    echo Vercel CLI not found. Installing...
    call npm install -g vercel
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install Vercel CLI
        echo Please run: npm install -g vercel
        pause
        exit /b 1
    )
    echo ✅ Vercel CLI installed!
) else (
    echo ✅ Vercel CLI already installed
)
echo.

echo ========================================
echo Starting Vercel Deployment...
echo ========================================
echo.
echo IMPORTANT: Make sure you have:
echo   1. Created a .env file with DATABASE_URL
echo   2. Added DATABASE_URL to Vercel dashboard
echo.
pause

call vercel

echo.
echo ========================================
echo Deployment initiated!
echo ========================================
echo.
echo Next steps:
echo 1. Go to Vercel dashboard
echo 2. Add environment variables:
echo    - DATABASE_URL (your Neon connection string)
echo    - NODE_ENV = production
echo 3. Redeploy if needed
echo.
echo Monitor logs: vercel logs --follow
echo.
pause
