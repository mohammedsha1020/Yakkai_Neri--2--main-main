#!/usr/bin/env python3
"""
Direct Flask App Test - Tests routes without external requests
"""

import os
import sys
from pathlib import Path

def test_flask_app_directly():
    """Test Flask app by importing and using test_client"""
    print("🧪 Testing Flask Application Directly")
    print("=" * 40)
    
    try:
        # Import the app
        from app import app
        
        print("✅ Flask app imported successfully")
        
        # Create test client
        with app.test_client() as client:
            # Test routes
            routes_to_test = [
                "/",
                "/corporate-yoga", 
                "/wellness",
                "/courses",
                "/contact",
                "/meet-the-trainer",
                "/workshops"
            ]
            
            results = []
            
            for route in routes_to_test:
                try:
                    response = client.get(route)
                    if response.status_code == 200:
                        print(f"✅ {route} - Working ({response.status_code})")
                        results.append(True)
                    elif response.status_code == 404:
                        print(f"❌ {route} - 404 NOT FOUND")
                        results.append(False)
                    else:
                        print(f"⚠️  {route} - Status: {response.status_code}")
                        results.append(False)
                except Exception as e:
                    print(f"❌ {route} - Error: {e}")
                    results.append(False)
            
            print(f"\n📊 Results: {sum(results)}/{len(results)} routes working")
            
            # Test static files
            print("\n🎨 Testing Static Files:")
            static_files = [
                "/static/css/style.css",
                "/static/js/script.js"
            ]
            
            static_results = []
            for static_file in static_files:
                try:
                    response = client.get(static_file)
                    if response.status_code == 200:
                        print(f"✅ {static_file} - Working")
                        static_results.append(True)
                    else:
                        print(f"❌ {static_file} - Status: {response.status_code}")
                        static_results.append(False)
                except Exception as e:
                    print(f"❌ {static_file} - Error: {e}")
                    static_results.append(False)
            
            total_working = sum(results) + sum(static_results)
            total_tests = len(results) + len(static_results)
            
            print(f"\n🎯 Overall Results: {total_working}/{total_tests} working")
            
            if total_working == total_tests:
                print("✅ All tests passed! No 404 issues.")
                return True
            else:
                print("❌ Some routes/files have 404 errors.")
                print("\n🔧 Next steps:")
                print("   1. Check templates/ folder for missing HTML files")
                print("   2. Check static/ folder structure")
                print("   3. Verify route definitions in app.py")
                return False
                
    except Exception as e:
        print(f"❌ Failed to test Flask app: {e}")
        return False

def check_file_structure():
    """Check if required files exist"""
    print("\n📁 Checking File Structure:")
    print("=" * 30)
    
    required_dirs = ["templates", "static", "static/css", "static/js", "static/images"]
    required_files = ["app.py", "wsgi.py", "vercel.json", "requirements.txt"]
    
    all_good = True
    
    for directory in required_dirs:
        if Path(directory).exists():
            print(f"✅ {directory}/ exists")
        else:
            print(f"❌ {directory}/ missing!")
            all_good = False
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing!")
            all_good = False
    
    # Check templates
    templates_dir = Path("templates")
    if templates_dir.exists():
        html_files = list(templates_dir.glob("*.html"))
        print(f"📄 Found {len(html_files)} HTML templates")
        
        critical_templates = ["index.html", "corporate-yoga.html"]
        for template in critical_templates:
            if (templates_dir / template).exists():
                print(f"✅ {template} found")
            else:
                print(f"❌ {template} missing!")
                all_good = False
    
    return all_good

if __name__ == "__main__":
    print("🚀 Flask App Diagnostics")
    print("=" * 50)
    
    # Check file structure first
    structure_ok = check_file_structure()
    
    if structure_ok:
        print("\n✅ File structure looks good!")
    else:
        print("\n❌ File structure issues found!")
    
    # Test the app
    app_ok = test_flask_app_directly()
    
    print("\n" + "=" * 50)
    if structure_ok and app_ok:
        print("🎉 Everything working perfectly!")
        print("💡 If getting 404 on Vercel, check environment variables.")
    else:
        print("🚨 Issues found that need to be fixed.")