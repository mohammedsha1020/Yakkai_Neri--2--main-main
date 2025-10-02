"""
WSGI Entry Point for Vercel Deployment
Yakkai Neri Yoga Academy Web Application
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import the Flask application
from app import app

# Configure for production
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

# Vercel expects the WSGI application to be named 'app'
# This is the entry point for Vercel
if __name__ == "__main__":
    app.run()