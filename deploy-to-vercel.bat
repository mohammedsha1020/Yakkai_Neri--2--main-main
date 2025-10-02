@echo off
echo.
echo ========================================
echo  Yakkai Neri - Vercel Deployment Prep
echo ========================================
echo.

echo Checking project structure...
echo.

if exist "vercel.json" (
    echo ✅ vercel.json found
) else (
    echo ❌ vercel.json missing
)

if exist "wsgi.py" (
    echo ✅ wsgi.py found
) else (
    echo ❌ wsgi.py missing
)

if exist "requirements.txt" (
    echo ✅ requirements.txt found
) else (
    echo ❌ requirements.txt missing
)

if exist "templates" (
    echo ✅ templates folder found
) else (
    echo ❌ templates folder missing
)

if exist "static" (
    echo ✅ static folder found
) else (
    echo ❌ static folder missing
)

echo.
echo ========================================
echo  Deployment Instructions:
echo ========================================
echo.
echo 1. Push your code to GitHub/GitLab/Bitbucket:
echo    git add .
echo    git commit -m "Deploy to Vercel"
echo    git push origin main
echo.
echo 2. Go to vercel.com and import your repository
echo.
echo 3. Or use Vercel CLI:
echo    npm i -g vercel
echo    vercel --prod
echo.
echo 📖 Read VERCEL_DEPLOY.md for detailed instructions
echo.
echo ========================================
pause