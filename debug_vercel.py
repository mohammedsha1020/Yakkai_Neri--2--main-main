#!/usr/bin/env python3
"""
Vercel Deployment Debug Script
This script helps diagnose and fix 404 issues with Vercel deployment
"""

import os
import json
from pathlib import Path

def check_vercel_config():
    """Check if vercel.json configuration is correct"""
    print("🔍 Checking Vercel Configuration...")
    
    vercel_file = Path("vercel.json")
    if not vercel_file.exists():
        print("❌ vercel.json not found!")
        return False
    
    try:
        with open(vercel_file, 'r') as f:
            config = json.load(f)
        
        print("✅ vercel.json found and valid JSON")
        print(f"   - Version: {config.get('version', 'Not specified')}")
        print(f"   - Name: {config.get('name', 'Not specified')}")
        
        # Check builds
        builds = config.get('builds', [])
        print(f"   - Builds: {len(builds)} configured")
        for build in builds:
            print(f"     • {build.get('src')} -> {build.get('use')}")
        
        # Check routes
        routes = config.get('routes', [])
        print(f"   - Routes: {len(routes)} configured")
        for route in routes:
            print(f"     • {route.get('src')} -> {route.get('dest')}")
        
        return True
    except json.JSONDecodeError as e:
        print(f"❌ vercel.json has invalid JSON: {e}")
        return False

def check_wsgi_file():
    """Check if wsgi.py exists and is properly configured"""
    print("\n🔍 Checking WSGI Configuration...")
    
    wsgi_file = Path("wsgi.py")
    if not wsgi_file.exists():
        print("❌ wsgi.py not found!")
        return False
    
    print("✅ wsgi.py found")
    
    # Check if it imports app correctly
    try:
        with open(wsgi_file, 'r') as f:
            content = f.read()
        
        if "from app import app" in content:
            print("✅ WSGI correctly imports Flask app")
        else:
            print("⚠️  WSGI might not import Flask app correctly")
        
        return True
    except Exception as e:
        print(f"❌ Error reading wsgi.py: {e}")
        return False

def check_templates_structure():
    """Check if templates are in the correct directory"""
    print("\n🔍 Checking Templates Structure...")
    
    templates_dir = Path("templates")
    if not templates_dir.exists():
        print("❌ templates/ directory not found!")
        return False
    
    templates = list(templates_dir.glob("*.html"))
    print(f"✅ templates/ directory found with {len(templates)} HTML files")
    
    # Check for critical templates
    critical_templates = ["index.html", "corporate-yoga.html"]
    for template in critical_templates:
        if (templates_dir / template).exists():
            print(f"✅ {template} found")
        else:
            print(f"❌ {template} missing!")
    
    return True

def check_static_structure():
    """Check if static files are in the correct directory"""
    print("\n🔍 Checking Static Files Structure...")
    
    static_dir = Path("static")
    if not static_dir.exists():
        print("❌ static/ directory not found!")
        return False
    
    print("✅ static/ directory found")
    
    # Check subdirectories
    subdirs = ["css", "js", "images"]
    for subdir in subdirs:
        subdir_path = static_dir / subdir
        if subdir_path.exists():
            files = list(subdir_path.glob("*"))
            print(f"✅ static/{subdir}/ found with {len(files)} files")
        else:
            print(f"⚠️  static/{subdir}/ not found")
    
    return True

def check_requirements():
    """Check if requirements.txt exists and has necessary packages"""
    print("\n🔍 Checking Requirements...")
    
    req_file = Path("requirements.txt")
    if not req_file.exists():
        print("❌ requirements.txt not found!")
        return False
    
    with open(req_file, 'r') as f:
        requirements = f.read()
    
    essential_packages = ["Flask", "Flask-SQLAlchemy"]
    for package in essential_packages:
        if package in requirements:
            print(f"✅ {package} found in requirements")
        else:
            print(f"❌ {package} missing from requirements!")
    
    return True

def generate_fixes():
    """Generate potential fixes for common 404 issues"""
    print("\n🔧 Potential Fixes for 404 Errors:")
    print("="*50)
    
    fixes = [
        {
            "issue": "WSGI Entry Point",
            "fix": "Ensure wsgi.py correctly imports and exposes the Flask app",
            "code": """# wsgi.py
from app import app

if __name__ == "__main__":
    app.run()
"""
        },
        {
            "issue": "Vercel Routes Configuration",
            "fix": "Update vercel.json to properly route requests",
            "code": """// vercel.json routes section
"routes": [
    {
        "src": "/static/(.*)",
        "dest": "/static/$1"
    },
    {
        "src": "/(.*)",
        "dest": "/wsgi.py"
    }
]"""
        },
        {
            "issue": "Flask Template/Static Configuration",
            "fix": "Ensure Flask app is configured with correct folders",
            "code": """# In app.py
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')
"""
        },
        {
            "issue": "Missing Environment Variables",
            "fix": "Set required environment variables in Vercel dashboard",
            "code": """Required Environment Variables:
- SECRET_KEY: Random secret key for Flask
- DATABASE_URL: Neon PostgreSQL connection string (optional)
- FLASK_ENV: production
"""
        }
    ]
    
    for i, fix in enumerate(fixes, 1):
        print(f"{i}. {fix['issue']}")
        print(f"   Solution: {fix['fix']}")
        print(f"   Code/Config:")
        print("   " + "\n   ".join(fix['code'].split('\n')))
        print()

def main():
    """Main diagnostic function"""
    print("🚀 Yakkai Neri Vercel Deployment Diagnostics")
    print("=" * 50)
    
    # Run all checks
    checks = [
        check_vercel_config,
        check_wsgi_file,
        check_templates_structure,
        check_static_structure,
        check_requirements
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Error running check: {e}")
            results.append(False)
    
    # Summary
    print(f"\n📊 Summary: {sum(results)}/{len(results)} checks passed")
    
    if all(results):
        print("✅ All checks passed! Your configuration looks good.")
        print("\n💡 If you're still getting 404 errors, try:")
        print("   1. Redeploy to Vercel")
        print("   2. Check Vercel function logs")
        print("   3. Verify environment variables in Vercel dashboard")
    else:
        print("⚠️  Some issues found. See fixes below:")
        generate_fixes()

if __name__ == "__main__":
    main()