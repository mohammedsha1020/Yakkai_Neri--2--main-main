#!/usr/bin/env python3
"""
Neon Database Test Script
Tests the connection and functionality with Neon PostgreSQL database
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add current directory to path
sys.path.insert(0, str(Path.cwd()))

def test_neon_connection():
    """Test if we can connect to Neon database"""
    database_url = os.environ.get('DATABASE_URL')
    
    if not database_url:
        print("❌ DATABASE_URL environment variable not set")
        print("💡 Create a .env file with your Neon connection string")
        print("📖 See NEON_SETUP.md for instructions")
        return False
    
    if 'neon.tech' not in database_url and 'postgresql://' not in database_url:
        print("⚠️  DATABASE_URL doesn't look like a Neon connection string")
        print(f"   Current: {database_url[:50]}...")
        return False
    
    print(f"✅ DATABASE_URL configured")
    print(f"🌐 Host: {database_url.split('@')[1].split('/')[0] if '@' in database_url else 'Unknown'}")
    return True

def test_app_with_neon():
    """Test Flask app with Neon database"""
    try:
        from app import app, db, WellnessSubmission, Company
        
        print("✅ Flask app imported successfully")
        
        with app.app_context():
            # Test database connection
            try:
                db.create_all()
                print("✅ Database tables created/verified")
            except Exception as e:
                print(f"❌ Error creating tables: {e}")
                return False
            
            # Test a simple query
            try:
                wellness_count = db.session.query(db.func.count(WellnessSubmission.id)).scalar()
                company_count = db.session.query(db.func.count(Company.id)).scalar()
                print(f"✅ Database queries working")
                print(f"📊 Found {wellness_count} wellness submissions and {company_count} companies")
            except Exception as e:
                print(f"❌ Error querying database: {e}")
                return False
            
            return True
            
    except Exception as e:
        print(f"❌ Error importing Flask app: {e}")
        return False

def test_neon_write_read():
    """Test writing and reading data to/from Neon"""
    try:
        from app import app, db, WellnessSubmission, Company
        
        with app.app_context():
            # Test writing data
            test_submission = WellnessSubmission(
                company_code="NEON_TEST",
                q1="5", q2="4", q3="3", q4="5", q5="4", q6="3",
                q7="5", q8="4", q9="3", q10="5", q11="4", q12="3",
                name="Neon Test User",
                mobile="1234567890",
                email="neon.test@example.com",
                designation="Test Position",
                total_score=50
            )
            
            db.session.add(test_submission)
            db.session.commit()
            print("✅ Test data written to Neon database")
            
            # Test reading data
            saved_submission = WellnessSubmission.query.filter_by(email="neon.test@example.com").first()
            if saved_submission:
                print("✅ Test data read from Neon database")
                print(f"📝 Submission ID: {saved_submission.id}")
                print(f"👤 Name: {saved_submission.name}")
                print(f"🏢 Company: {saved_submission.company_code}")
                
                # Clean up test data
                db.session.delete(saved_submission)
                db.session.commit()
                print("✅ Test data cleaned up")
                return True
            else:
                print("❌ Could not read test data from database")
                return False
                
    except Exception as e:
        print(f"❌ Error in write/read test: {e}")
        return False

def display_connection_info():
    """Display information about the current database connection"""
    database_url = os.environ.get('DATABASE_URL', '')
    
    if 'postgresql://' in database_url:
        try:
            # Parse connection string safely
            parts = database_url.replace('postgresql://', '').split('@')
            if len(parts) == 2:
                host_db = parts[1].split('/')
                host = host_db[0]
                database = host_db[1].split('?')[0] if len(host_db) > 1 else 'unknown'
                
                print(f"🐘 Database Type: PostgreSQL (Neon)")
                print(f"🌐 Host: {host}")
                print(f"🗄️  Database: {database}")
                print(f"🔒 SSL: {'Required' if 'sslmode=require' in database_url else 'Not specified'}")
            else:
                print("🐘 Database Type: PostgreSQL")
                
        except Exception:
            print("🐘 Database Type: PostgreSQL (connection string parsing failed)")
    elif 'sqlite' in database_url:
        print("📁 Database Type: SQLite (fallback)")
    else:
        print("❓ Database Type: Unknown")

def main():
    """Run all Neon database tests"""
    print("🧪 Neon Database Connection Test")
    print("=" * 50)
    print()
    
    # Display connection info
    display_connection_info()
    print()
    
    tests = [
        ("Neon Connection Check", test_neon_connection),
        ("Flask App with Neon", test_app_with_neon),
        ("Write/Read Test", test_neon_write_read),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"🔍 Testing: {test_name}")
        print("-" * 30)
        
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASSED")
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
        
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Neon database is working perfectly!")
        print("✅ Your application is ready for production deployment")
    elif passed == 0:
        print("⚠️  No tests passed. Check your Neon setup:")
        print("📖 See NEON_SETUP.md for configuration instructions")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        
    print("\n📋 Next steps:")
    if passed == total:
        print("1. Deploy to Vercel with DATABASE_URL environment variable")
        print("2. Enjoy persistent data storage! 🎉")
    else:
        print("1. Check your .env file has correct DATABASE_URL")
        print("2. Verify your Neon database is running")
        print("3. Re-run this test: python test_neon.py")

if __name__ == "__main__":
    main()