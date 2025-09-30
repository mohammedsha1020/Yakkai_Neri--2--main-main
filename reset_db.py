import pymysql

def reset_database():
    try:
        # Connect to MySQL
        print("Connecting to MySQL...")
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        with connection.cursor() as cursor:
            # Drop and recreate database
            print("Dropping existing database if it exists...")
            cursor.execute('DROP DATABASE IF EXISTS yakkai_neri')
            
            print("Creating new database...")
            cursor.execute('CREATE DATABASE yakkai_neri')
            
            print("Selecting database...")
            cursor.execute('USE yakkai_neri')
            
            print("Creating wellness_assessments table...")
            cursor.execute('''
                CREATE TABLE wellness_assessments (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    company_code VARCHAR(50) NOT NULL,
                    q1 VARCHAR(10),
                    q2 VARCHAR(10),
                    q3 VARCHAR(10),
                    q4 VARCHAR(10),
                    q5 VARCHAR(10),
                    q6 VARCHAR(10),
                    q7 VARCHAR(10),
                    q8 VARCHAR(10),
                    q9 VARCHAR(10),
                    q10 VARCHAR(10),
                    q11 VARCHAR(10),
                    q12 VARCHAR(10),
                    name VARCHAR(100),
                    mobile VARCHAR(20),
                    email VARCHAR(120),
                    designation VARCHAR(100),
                    total_score INT,
                    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            print("Creating companies table...")
            cursor.execute('''
                CREATE TABLE companies (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    company_name VARCHAR(100) NOT NULL,
                    contact_person VARCHAR(100) NOT NULL,
                    email VARCHAR(120) NOT NULL UNIQUE,
                    phone VARCHAR(20) NOT NULL,
                    employee_count INT,
                    industry VARCHAR(100),
                    company_code VARCHAR(50) NOT NULL UNIQUE,
                    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            connection.commit()
            print("Database and tables created successfully!")
            
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        connection.close()

if __name__ == "__main__":
    print("Starting database reset...")
    reset_database()
    print("Database reset complete")