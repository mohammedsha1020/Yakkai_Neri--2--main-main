#!/usr/bin/env python3
"""
Quick Test Script for Local Flask App
Tests if routes are working and identifies 404 issues
"""

import requests
import time

def test_local_routes():
    """Test local Flask routes"""
    print("🧪 Testing Local Flask Application")
    print("=" * 40)
    
    base_url = "http://127.0.0.1:5000"
    
    routes_to_test = [
        "/",
        "/corporate-yoga", 
        "/wellness",
        "/courses",
        "/contact",
        "/static/css/style.css",
        "/static/images/banner.jpg"
    ]
    
    print(f"Testing routes on: {base_url}")
    print("Waiting 2 seconds for Flask app to be ready...")
    time.sleep(2)
    
    results = []
    
    for route in routes_to_test:
        try:
            url = f"{base_url}{route}"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"✅ {route} - Working ({response.status_code})")
                results.append(True)
            elif response.status_code == 404:
                print(f"❌ {route} - 404 NOT FOUND")
                results.append(False)
            else:
                print(f"⚠️  {route} - Status: {response.status_code}")
                results.append(False)
                
        except requests.exceptions.ConnectionError:
            print(f"❌ {route} - Connection Error (Flask app not running?)")
            results.append(False)
        except Exception as e:
            print(f"❌ {route} - Error: {e}")
            results.append(False)
    
    print(f"\n📊 Results: {sum(results)}/{len(results)} routes working")
    
    if all(results):
        print("✅ All routes working! No 404 issues locally.")
    else:
        print("❌ Some routes have 404 errors. Check configuration.")
        print("\n🔧 Common fixes for 404 errors:")
        print("   1. Check if templates/ folder has all HTML files")
        print("   2. Check if static/ folder has CSS/JS/images")
        print("   3. Verify Flask app configuration in app.py")
    
    return all(results)

if __name__ == "__main__":
    try:
        success = test_local_routes()
        if success:
            print("\n🎉 Local app is working perfectly!")
            print("💡 If getting 404 on deployment, check Vercel environment variables.")
        else:
            print("\n🚨 Local app has issues that need to be fixed first.")
    except Exception as e:
        print(f"❌ Test script error: {e}")
        print("💡 Make sure Flask app is running: python app.py")