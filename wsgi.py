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

# Set production environment if not set
if not os.environ.get('FLASK_ENV'):
    os.environ['FLASK_ENV'] = 'production'

# Set fallback secret key if not provided
if not os.environ.get('SECRET_KEY'):
    os.environ['SECRET_KEY'] = 'yakkai-neri-fallback-secret-key'

try:
    # Import the Flask application
    from app import app
    
    # Configure for production
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    
    # Ensure database tables are created for serverless
    with app.app_context():
        from app import db
        db.create_all()
        print("✅ Database tables created/verified")
        
except Exception as e:
    print(f"❌ Error in WSGI setup: {e}")
    # Create a minimal Flask app as fallback
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def error_page():
        return f"<h1>Application Error</h1><p>Error: {e}</p><p>Check logs for details.</p>"

# Vercel expects the WSGI application to be named 'app'
# This is the entry point for Vercel
if __name__ == "__main__":
    app.run()
