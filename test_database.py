#!/usr/bin/env python3
"""
Database Test Script for Yakkai Neri Yoga Academy

This script tests the database functionality to ensure all forms and data storage work correctly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, WellnessSubmission, Company

def test_database_connection():
    """Test if database connection works"""
    try:
        with app.app_context():
            db.create_all()
            print("✅ Database connection successful!")
            return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_wellness_submission():
    """Test wellness submission functionality"""
    try:
        with app.app_context():
            # Create a test wellness submission
            test_submission = WellnessSubmission(
                company_code="TEST123",
                q1="5", q2="4", q3="3", q4="5", q5="4", q6="3",
                q7="5", q8="4", q9="3", q10="5", q11="4", q12="3",
                name="Test User",
                mobile="1234567890",
                email="test@example.com",
                designation="Test Position",
                total_score=50
            )
            
            db.session.add(test_submission)
            db.session.commit()
            
            # Verify the submission was saved
            saved_submission = WellnessSubmission.query.filter_by(email="test@example.com").first()
            if saved_submission:
                print("✅ Wellness submission test passed!")
                
                # Clean up test data
                db.session.delete(saved_submission)
                db.session.commit()
                return True
            else:
                print("❌ Wellness submission test failed - data not saved")
                return False
                
    except Exception as e:
        print(f"❌ Wellness submission test failed: {e}")
        return False

def test_company_registration():
    """Test company registration functionality"""
    try:
        with app.app_context():
            # Create a test company
            test_company = Company(
                company_name="Test Company Ltd",
                contact_person="Test Contact",
                email="test@testcompany.com",
                phone="1234567890",
                employee_count=100,
                industry="Technology",
                company_code="TESTCO123"
            )
            
            db.session.add(test_company)
            db.session.commit()
            
            # Verify the company was saved
            saved_company = Company.query.filter_by(email="test@testcompany.com").first()
            if saved_company:
                print("✅ Company registration test passed!")
                
                # Clean up test data
                db.session.delete(saved_company)
                db.session.commit()
                return True
            else:
                print("❌ Company registration test failed - data not saved")
                return False
                
    except Exception as e:
        print(f"❌ Company registration test failed: {e}")
        return False

def test_database_queries():
    """Test database query functionality"""
    try:
        with app.app_context():
            # Test counting records
            wellness_count = db.session.query(db.func.count(WellnessSubmission.id)).scalar()
            company_count = db.session.query(db.func.count(Company.id)).scalar()
            
            print(f"✅ Database queries work! Found {wellness_count} wellness submissions and {company_count} companies")
            return True
            
    except Exception as e:
        print(f"❌ Database query test failed: {e}")
        return False

def main():
    """Run all database tests"""
    print("🧪 Starting Database Tests for Yakkai Neri Yoga Academy\n")
    
    tests = [
        ("Database Connection", test_database_connection),
        ("Wellness Submission", test_wellness_submission),
        ("Company Registration", test_company_registration),
        ("Database Queries", test_database_queries)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name} test...")
        if test_func():
            passed += 1
        print()
    
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Database functionality is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the database configuration.")

if __name__ == "__main__":
    main()