const { Pool } = require('pg');
require('dotenv').config();

// Database configuration with connection pooling
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.DATABASE_URL ? { rejectUnauthorized: false } : false,
  max: 20, // Maximum number of connections in pool
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 10000,
});

// Initialize database tables
async function initializeDatabase() {
  const client = await pool.connect();
  try {
    // Create wellness_assessments table
    await client.query(`
      CREATE TABLE IF NOT EXISTS wellness_assessments (
        id SERIAL PRIMARY KEY,
        company_code VARCHAR(50),
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
        total_score INTEGER,
        submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `);

    // Create companies table
    await client.query(`
      CREATE TABLE IF NOT EXISTS companies (
        id SERIAL PRIMARY KEY,
        company_name VARCHAR(100) NOT NULL,
        contact_person VARCHAR(100) NOT NULL,
        email VARCHAR(120) UNIQUE NOT NULL,
        phone VARCHAR(20) NOT NULL,
        employee_count INTEGER,
        industry VARCHAR(100),
        company_code VARCHAR(50) UNIQUE NOT NULL,
        created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `);

    console.log('✅ Database tables initialized successfully');
  } catch (error) {
    console.error('❌ Error initializing database:', error);
    throw error;
  } finally {
    client.release();
  }
}

// Query helper function
async function query(text, params) {
  const start = Date.now();
  try {
    const res = await pool.query(text, params);
    const duration = Date.now() - start;
    console.log('Executed query', { text, duration, rows: res.rowCount });
    return res;
  } catch (error) {
    console.error('Database query error:', error);
    throw error;
  }
}

module.exports = {
  query,
  pool,
  initializeDatabase
};
