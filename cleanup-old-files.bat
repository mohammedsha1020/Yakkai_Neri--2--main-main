@echo off
echo ========================================
echo Cleaning Up Old Python Files
echo ========================================
echo.
echo This will remove all old Python files and documentation.
echo Node.js files and templates will be preserved.
echo.
pause

echo Removing Python application files...
if exist app.py del /Q app.py
if exist app.py.bak del /Q app.py.bak
if exist wsgi.py del /Q wsgi.py
if exist requirements.txt del /Q requirements.txt

echo Removing Python test files...
if exist test_*.py del /Q test_*.py
if exist debug_vercel.py del /Q debug_vercel.py
if exist fix_404.py del /Q fix_404.py
if exist fix_404_urgent.py del /Q fix_404_urgent.py
if exist reset_db.py del /Q reset_db.py

echo Removing Python directories...
if exist __pycache__ rd /S /Q __pycache__
if exist instance rd /S /Q instance

echo Removing old batch scripts...
if exist run.bat del /Q run.bat
if exist setup.bat del /Q setup.bat
if exist setup-neon.bat del /Q setup-neon.bat
if exist deploy-to-vercel.bat del /Q deploy-to-vercel.bat

echo Removing old documentation...
if exist DEPLOYMENT_404_FIX.md del /Q DEPLOYMENT_404_FIX.md
if exist URGENT_FIX.txt del /Q URGENT_FIX.txt
if exist VERCEL_404_FIX.md del /Q VERCEL_404_FIX.md
if exist VERCEL_DEPLOY.md del /Q VERCEL_DEPLOY.md
if exist VERCEL_OPTIMIZATION.md del /Q VERCEL_OPTIMIZATION.md
if exist NEON_INTEGRATION.md del /Q NEON_INTEGRATION.md
if exist NEON_SETUP.md del /Q NEON_SETUP.md

echo.
echo ========================================
echo ✅ Cleanup Complete!
echo ========================================
echo.
echo Old Python files have been removed.
echo Your Node.js application files are safe.
echo.
pause
