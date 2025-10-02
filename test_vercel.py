#!/usr/bin/env python3
"""
Vercel Configuration Test Script
Tests if the application is ready for Vercel deployment
"""

import os
import sys
import json
from pathlib import Path

def check_file_exists(filename, description):
    """Check if a required file exists"""
    if Path(filename).exists():
        print(f"✅ {description}: {filename}")
        return True
    else:
        print(f"❌ {description}: {filename} - NOT FOUND")
        return False

def check_vercel_config():
    """Check vercel.json configuration"""
    try:
        with open('vercel.json', 'r') as f:
            config = json.load(f)
        
        required_keys = ['version', 'builds', 'routes']
        for key in required_keys:
            if key in config:
                print(f"✅ vercel.json has '{key}' configuration")
            else:
                print(f"❌ vercel.json missing '{key}' configuration")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Error reading vercel.json: {e}")
        return False

def check_wsgi_entry():
    """Check if wsgi.py can import the app"""
    try:
        # Add current directory to path
        sys.path.insert(0, str(Path.cwd()))
        
        # Try to import from wsgi
        from wsgi import app
        print("✅ WSGI entry point working - app can be imported")
        return True
    except Exception as e:
        print(f"❌ WSGI entry point error: {e}")
        return False

def check_requirements():
    """Check if requirements.txt has necessary packages"""
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
        
        required_packages = ['Flask', 'Flask-SQLAlchemy']
        for package in required_packages:
            if package in requirements:
                print(f"✅ {package} found in requirements.txt")
            else:
                print(f"❌ {package} missing from requirements.txt")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def check_project_structure():
    """Check if project structure is correct for Vercel"""
    structure_checks = [
        ('templates', 'Templates directory'),
        ('static', 'Static files directory'),
        ('static/css', 'CSS directory'),
        ('static/js', 'JavaScript directory'),
        ('static/images', 'Images directory'),
    ]
    
    all_good = True
    for path, description in structure_checks:
        if Path(path).exists():
            print(f"✅ {description}: {path}")
        else:
            print(f"❌ {description}: {path} - NOT FOUND")
            all_good = False
    
    return all_good

def test_app_import():
    """Test if the Flask app can be imported without errors"""
    try:
        # Set environment variable to simulate Vercel
        os.environ['VERCEL'] = '1'
        
        # Try to import the app
        from app import app, db
        
        print("✅ Flask app imports successfully")
        print("✅ Database configuration working")
        
        # Test app context
        with app.app_context():
            print("✅ Flask app context working")
        
        return True
    except Exception as e:
        print(f"❌ Flask app import error: {e}")
        return False
    finally:
        # Clean up environment
        os.environ.pop('VERCEL', None)

def main():
    """Run all Vercel readiness tests"""
    print("🧪 Vercel Deployment Readiness Test")
    print("=" * 50)
    print()
    
    tests = [
        ("Required Files", lambda: all([
            check_file_exists('vercel.json', 'Vercel config'),
            check_file_exists('wsgi.py', 'WSGI entry point'),
            check_file_exists('requirements.txt', 'Python requirements'),
            check_file_exists('app.py', 'Flask application'),
        ])),
        ("Vercel Configuration", check_vercel_config),
        ("Requirements Check", check_requirements),
        ("Project Structure", check_project_structure),
        ("WSGI Entry Point", check_wsgi_entry),
        ("Flask App Import", test_app_import),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing: {test_name}")
        print("-" * 30)
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASSED")
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Ready for Vercel deployment!")
        print("\n📋 Next steps:")
        print("1. Push your code to Git repository")
        print("2. Connect repository to Vercel")
        print("3. Deploy!")
        print("\n📖 See VERCEL_DEPLOY.md for detailed instructions")
    else:
        print("⚠️  Some issues need to be fixed before deployment")
        print("Please resolve the failed tests above")

if __name__ == "__main__":
    main()