#!/usr/bin/env python3
"""
Quick Fix Script for Vercel 404 Issues
Yakkai Neri Yoga Academy
"""

import json
import os
from pathlib import Path

def fix_vercel_config():
    """Fix common Vercel configuration issues"""
    print("🔧 Fixing Vercel Configuration...")
    
    # Updated vercel.json with better configuration
    vercel_config = {
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
            "FLASK_ENV": "production",
            "PYTHONPATH": "/var/task"
        },
        "functions": {
            "wsgi.py": {
                "includeFiles": "**"
            }
        }
    }
    
    # Write the fixed configuration
    with open("vercel.json", "w") as f:
        json.dump(vercel_config, f, indent=2)
    
    print("✅ vercel.json updated with optimized configuration")

def fix_wsgi():
    """Ensure WSGI is properly configured"""
    print("🔧 Fixing WSGI Configuration...")
    
    wsgi_content = '''"""
WSGI Entry Point for Vercel Deployment
Yakkai Neri Yoga Academy Web Application
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Set production environment
os.environ['FLASK_ENV'] = 'production'

# Import the Flask application
from app import app

# Configure for production
app.config['ENV'] = 'production'
app.config['DEBUG'] = False

# Ensure database tables are created
with app.app_context():
    from app import db
    db.create_all()

# Vercel expects the WSGI application to be named 'app'
# This is the entry point for Vercel
if __name__ == "__main__":
    app.run()
'''
    
    with open("wsgi.py", "w") as f:
        f.write(wsgi_content)
    
    print("✅ wsgi.py updated with production optimizations")

def create_vercel_ignore():
    """Create or update .vercelignore to exclude unnecessary files"""
    print("🔧 Updating .vercelignore...")
    
    vercelignore_content = '''# Vercel ignore file
# Exclude files that don't need to be deployed

# Environment files (contains sensitive data)
.env
.env.local

# Development files
*.pyc
__pycache__/
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git/
.gitignore
.mypy_cache
.pytest_cache
.hypothesis

# Local development files
*.db
*.sqlite
*.sqlite3
wellness.db
app.py.bak
test_database.py
reset_db.py
debug_vercel.py
fix_404.py

# IDE files
.vscode/
.idea/
*.swp
*.swo
*~

# OS files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Instance folder
instance/
'''
    
    with open(".vercelignore", "w") as f:
        f.write(vercelignore_content)
    
    print("✅ .vercelignore updated")

def create_deployment_guide():
    """Create step-by-step deployment guide"""
    print("📖 Creating deployment guide...")
    
    guide_content = '''# 🚀 Vercel Deployment Fix Guide
## Yakkai Neri Yoga Academy

## 🔧 **Quick Fix Steps**

### 1. **Redeploy with Latest Configuration**
```bash
# If using Vercel CLI
vercel --prod

# Or push to connected Git repository for auto-deployment
```

### 2. **Set Environment Variables in Vercel Dashboard**
Go to your Vercel project dashboard and add these environment variables:

**Required:**
- `SECRET_KEY` = Any random string (e.g., `your-super-secret-key-here`)
- `FLASK_ENV` = `production`

**Optional (for Neon database):**
- `DATABASE_URL` = Your Neon PostgreSQL connection string

### 3. **Common 404 Fixes**

#### **A. Force Redeploy**
```bash
# Delete .vercel folder and redeploy
rm -rf .vercel
vercel --prod
```

#### **B. Check Function Logs**
1. Go to Vercel Dashboard
2. Click on your project
3. Go to "Functions" tab
4. Check logs for errors

#### **C. Verify Build Output**
1. Check if build completed successfully
2. Verify all files are uploaded
3. Check function runtime logs

### 4. **Environment Variables Setup**

#### **In Vercel Dashboard:**
1. Go to Settings > Environment Variables
2. Add these variables:

```
SECRET_KEY = flask-secret-key-change-this-in-production
FLASK_ENV = production
DATABASE_URL = postgresql://... (if using Neon)
```

### 5. **Test Deployment**

After deployment, test these URLs:
- `https://your-app.vercel.app/` (Home page)
- `https://your-app.vercel.app/corporate-yoga` (Corporate page)
- `https://your-app.vercel.app/wellness` (Wellness page)

### 6. **Troubleshooting**

#### **If still getting 404:**

1. **Check Build Logs:**
   ```
   Vercel Dashboard > Project > Deployments > Latest > View Logs
   ```

2. **Verify Function is Created:**
   ```
   Vercel Dashboard > Project > Functions
   Should show wsgi.py function
   ```

3. **Check Domain/DNS:**
   ```
   Vercel Dashboard > Project > Settings > Domains
   Verify domain is properly configured
   ```

#### **If getting 500 errors:**
1. Check function logs for Python errors
2. Verify all dependencies in requirements.txt
3. Check database connection

### 7. **Manual Verification**

Run this locally to ensure everything works:
```bash
python app.py
# Should start without errors
# Test all routes in browser
```

## 🎯 **Most Common Solutions**

1. **Environment Variables Missing** → Add SECRET_KEY and FLASK_ENV
2. **Build Cache Issues** → Delete .vercel folder and redeploy  
3. **Function Timeout** → Check for infinite loops in code
4. **Database Connection** → Verify DATABASE_URL or use SQLite fallback

## 🆘 **If Nothing Works**

1. Create a new Vercel project
2. Import from GitHub repository
3. Add environment variables
4. Deploy fresh

---

**Your app should now work perfectly on Vercel!** 🎉
'''
    
    with open("VERCEL_404_FIX.md", "w") as f:
        f.write(guide_content)
    
    print("✅ VERCEL_404_FIX.md created with step-by-step guide")

def main():
    """Apply all fixes"""
    print("🚀 Applying Vercel 404 Fixes...")
    print("=" * 50)
    
    try:
        fix_vercel_config()
        fix_wsgi()
        create_vercel_ignore()
        create_deployment_guide()
        
        print("\n🎉 All fixes applied successfully!")
        print("\n📋 Next Steps:")
        print("1. Commit these changes to Git")
        print("2. Push to your repository (triggers auto-deploy)")
        print("3. OR run: vercel --prod")
        print("4. Add environment variables in Vercel dashboard")
        print("5. Check VERCEL_404_FIX.md for detailed steps")
        
    except Exception as e:
        print(f"❌ Error applying fixes: {e}")

if __name__ == "__main__":
    main()