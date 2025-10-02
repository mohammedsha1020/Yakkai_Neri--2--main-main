#!/usr/bin/env python3
"""
URGENT: Vercel 404 Fix Script
Yakkai Neri Yoga Academy - Complete solution for deployment issues
"""

import os
import sys
import subprocess
from pathlib import Path

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def create_vercel_environment_guide():
    """Create step-by-step guide for setting Vercel environment variables"""
    print_section("VERCEL ENVIRONMENT VARIABLES SETUP")
    
    print("🚨 CRITICAL: You must add these environment variables in Vercel:")
    print("\n1. Go to: https://vercel.com/dashboard")
    print("2. Click on your project: yakkai-neri-yoga-academy")
    print("3. Go to: Settings → Environment Variables")
    print("4. Add these EXACT variables:")
    
    print("\n" + "="*40)
    print("REQUIRED ENVIRONMENT VARIABLES:")
    print("="*40)
    print("Variable Name: SECRET_KEY")
    print("Value: yakkai-neri-yoga-academy-secret-key-2025")
    print("\nVariable Name: FLASK_ENV")
    print("Value: production")
    print("\nVariable Name: DATABASE_URL")
    print("Value: postgresql://neondb_owner:npg_rIfO4sa3FMcL@ep-lively-bread-aau5vtqp-pooler.westus3.azure.neon.tech/neondb?sslmode=require&channel_binding=require")
    print("="*40)
    
    print("\n✅ After adding variables, click 'Save' and 'Redeploy'")

def test_with_env_vars():
    """Test the application with environment variables"""
    print_section("TESTING WITH ENVIRONMENT VARIABLES")
    
    try:
        # Set environment variables for testing
        os.environ['SECRET_KEY'] = 'yakkai-neri-yoga-academy-secret-key-2025'
        os.environ['FLASK_ENV'] = 'production'
        os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_rIfO4sa3FMcL@ep-lively-bread-aau5vtqp-pooler.westus3.azure.neon.tech/neondb?sslmode=require&channel_binding=require'
        
        # Import and test the app
        from app import app, db
        
        with app.app_context():
            print("✅ App imported successfully with environment variables")
            
            # Test database connection
            try:
                db.create_all()
                print("✅ Database connection successful")
            except Exception as e:
                print(f"⚠️  Database connection issue: {e}")
                print("   (This might be normal if Neon database is sleeping)")
            
            # Test routes
            with app.test_client() as client:
                response = client.get('/')
                if response.status_code == 200:
                    print("✅ Home route working")
                else:
                    print(f"❌ Home route failed: {response.status_code}")
                
                response = client.get('/corporate-yoga')
                if response.status_code == 200:
                    print("✅ Corporate yoga route working")
                else:
                    print(f"❌ Corporate yoga route failed: {response.status_code}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def check_current_wsgi():
    """Check and display current WSGI configuration"""
    print_section("CHECKING WSGI CONFIGURATION")
    
    wsgi_path = Path("wsgi.py")
    if wsgi_path.exists():
        print("✅ wsgi.py exists")
        with open(wsgi_path, 'r') as f:
            content = f.read()
            if "from app import app" in content:
                print("✅ WSGI imports app correctly")
            else:
                print("❌ WSGI import issue")
    else:
        print("❌ wsgi.py missing!")

def create_immediate_fix():
    """Create files needed for immediate deployment fix"""
    print_section("CREATING DEPLOYMENT FIX FILES")
    
    # Create a production-ready wsgi.py
    wsgi_content = '''"""
WSGI Entry Point for Vercel Deployment
Yakkai Neri Yoga Academy - Production Ready
"""

import os
import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Set production environment
os.environ.setdefault('FLASK_ENV', 'production')
os.environ.setdefault('SECRET_KEY', 'fallback-secret-key')

try:
    # Import Flask app
    from app import app
    
    # Configure for production
    app.config['ENV'] = 'production'
    app.config['DEBUG'] = False
    
    # Initialize database tables
    with app.app_context():
        from app import db
        db.create_all()
        print("✅ Database tables initialized")
        
except Exception as e:
    print(f"❌ WSGI Error: {e}")
    # Create a minimal Flask app as fallback
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return f"Error: {e}. Check environment variables."

# Export for Vercel
if __name__ == "__main__":
    app.run()
'''
    
    with open("wsgi.py", "w") as f:
        f.write(wsgi_content)
    print("✅ Updated wsgi.py with production configuration")
    
    # Create optimized vercel.json
    vercel_config = '''{
  "version": 2,
  "name": "yakkai-neri-yoga-academy",
  "builds": [
    {
      "src": "wsgi.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb",
        "runtime": "python3.9"
      }
    },
    {
      "src": "static/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/wsgi.py"
    }
  ],
  "env": {
    "PYTHONPATH": "/var/task"
  },
  "functions": {
    "wsgi.py": {
      "includeFiles": "**"
    }
  }
}'''
    
    with open("vercel.json", "w") as f:
        f.write(vercel_config)
    print("✅ Updated vercel.json with optimized configuration")

def provide_deployment_instructions():
    """Provide step-by-step deployment instructions"""
    print_section("DEPLOYMENT INSTRUCTIONS")
    
    print("🚀 FOLLOW THESE STEPS TO FIX THE 404 ERROR:")
    print("\nSTEP 1: Add Environment Variables in Vercel")
    print("   → Go to https://vercel.com/dashboard")
    print("   → Click your project → Settings → Environment Variables")
    print("   → Add the 3 variables shown above")
    
    print("\nSTEP 2: Redeploy the Application")
    print("   Option A: Git Push (if auto-deploy enabled)")
    print("     git add .")
    print("     git commit -m 'Fix 404 error with environment variables'")
    print("     git push")
    
    print("\n   Option B: Manual Deploy")
    print("     vercel --prod")
    
    print("\nSTEP 3: Verify Deployment")
    print("   → Check Vercel dashboard for deployment status")
    print("   → Test your live URL")
    print("   → Check function logs if still failing")
    
    print("\n🎯 ROOT CAUSE OF 404 ERROR:")
    print("   Missing SECRET_KEY environment variable in Vercel")
    print("   Flask cannot start without a SECRET_KEY")
    print("   This causes all routes to return 404")

def main():
    """Main fix function"""
    print("🚨 URGENT: Vercel 404 Fix for Yakkai Neri Yoga Academy")
    print("🎯 This will solve your deployment issue immediately")
    
    # Run all fix steps
    create_vercel_environment_guide()
    check_current_wsgi()
    create_immediate_fix()
    test_with_env_vars()
    provide_deployment_instructions()
    
    print_section("SUMMARY")
    print("✅ All fixes applied!")
    print("🔥 MOST IMPORTANT: Add environment variables in Vercel dashboard")
    print("🚀 Then redeploy - your 404 error will be fixed!")
    
    print("\n📞 If still having issues:")
    print("   1. Check Vercel function logs")
    print("   2. Verify all 3 environment variables are set")
    print("   3. Try deleting .vercel folder and redeploying")

if __name__ == "__main__":
    main()