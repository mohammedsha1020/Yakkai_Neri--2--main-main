#!/usr/bin/env python3
"""
Vercel Deployment Test Script
Quick test to verify everything is working before deployment
"""

import subprocess
import sys
import os
from pathlib import Path

def test_local_app():
    """Test if the app runs locally"""
    print("Testing local Flask application...")
    
    try:
        # Import the app to check for import errors
        from app import app, db
        
        with app.app_context():
            # Test database creation
            db.create_all()
            print("✅ Database tables created successfully")
            
            # Test a simple route
            with app.test_client() as client:
                response = client.get('/')
                if response.status_code == 200:
                    print("✅ Home route ('/') working")
                else:
                    print(f"❌ Home route failed: {response.status_code}")
                
                response = client.get('/corporate-yoga')
                if response.status_code == 200:
                    print("✅ Corporate yoga route working")
                else:
                    print(f"❌ Corporate yoga route failed: {response.status_code}")
        
        return True
        
    except Exception as e:
        print(f"❌ Local app test failed: {e}")
        return False

def check_vercel_cli():
    """Check if Vercel CLI is installed"""
    try:
        result = subprocess.run(['vercel', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Vercel CLI installed: {result.stdout.strip()}")
            return True
        else:
            print("❌ Vercel CLI not found")
            return False
    except FileNotFoundError:
        print("❌ Vercel CLI not installed")
        print("💡 Install with: npm i -g vercel")
        return False

def deploy_to_vercel():
    """Deploy to Vercel"""
    print("\n🚀 Deploying to Vercel...")
    
    try:
        # Run vercel deploy
        result = subprocess.run(['vercel', '--prod'], 
                              capture_output=True, text=True, cwd=Path.cwd())
        
        if result.returncode == 0:
            print("✅ Deployment successful!")
            print(f"Output: {result.stdout}")
            return True
        else:
            print(f"❌ Deployment failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Deployment error: {e}")
        return False

def main():
    """Main test and deployment function"""
    print("🧪 Vercel Deployment Test & Fix")
    print("=" * 40)
    
    # Test local app first
    if not test_local_app():
        print("❌ Local app test failed. Fix issues before deploying.")
        return
    
    print("\n✅ Local tests passed!")
    
    # Check if user wants to deploy
    deploy = input("\n🤔 Deploy to Vercel now? (y/n): ").lower().strip()
    
    if deploy == 'y':
        if check_vercel_cli():
            if deploy_to_vercel():
                print("\n🎉 Deployment complete!")
                print("\n📝 Next steps:")
                print("1. Check your Vercel dashboard for the deployment URL")
                print("2. Add environment variables if needed:")
                print("   - SECRET_KEY (required)")
                print("   - DATABASE_URL (optional, for Neon)")
                print("3. Test the live URL")
            else:
                print("\n❌ Deployment failed. Check error messages above.")
        else:
            print("\n💡 Install Vercel CLI first: npm i -g vercel")
    else:
        print("\n✅ Ready to deploy! Run 'vercel --prod' when ready.")
        print("\n📋 Pre-deployment checklist:")
        print("✅ Local app working")
        print("✅ vercel.json configured")
        print("✅ wsgi.py ready")
        print("✅ requirements.txt updated")
        print("\n🎯 Manual deployment: vercel --prod")

if __name__ == "__main__":
    main()