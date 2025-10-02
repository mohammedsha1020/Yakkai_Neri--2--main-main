@echo off
echo.
echo =========================================
echo  Yakkai Neri - Neon Database Setup
echo =========================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Setting up environment file...
if not exist ".env" (
    copy ".env.example" ".env"
    echo ✅ Created .env file from template
    echo.
    echo ⚠️  IMPORTANT: Edit .env file with your Neon database URL
    echo    1. Go to https://console.neon.tech/
    echo    2. Create account and project
    echo    3. Copy connection string to .env file
) else (
    echo ✅ .env file already exists
)

echo.
echo =========================================
echo  Setup Instructions:
echo =========================================
echo.
echo 1. Create Neon account: https://console.neon.tech/
echo 2. Get your connection string
echo 3. Edit .env file with your DATABASE_URL
echo 4. Run: python test_neon.py
echo 5. Run: python app.py
echo.
echo 📖 Read NEON_SETUP.md for detailed instructions
echo.
echo =========================================
pause