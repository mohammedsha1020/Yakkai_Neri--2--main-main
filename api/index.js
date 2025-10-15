const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const cors = require('cors');
require('dotenv').config();

const { query, initializeDatabase } = require('./db');

const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '../static')));

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../templates'));

// Initialize database on startup
let dbInitialized = false;

async function ensureDbInitialized() {
  if (!dbInitialized) {
    try {
      await initializeDatabase();
      dbInitialized = true;
    } catch (error) {
      console.error('Failed to initialize database:', error);
    }
  }
}

// Call this on app startup
ensureDbInitialized();

// ==================== ROUTES ====================

// Home page
app.get('/', (req, res) => {
  res.render('index');
});

// Corporate yoga page
app.get('/corporate-yoga', (req, res) => {
  res.render('corporate-yoga', { company_code: 'ABC123' });
});

// Wellness form
app.get('/wellness_form', (req, res) => {
  res.render('individual-wellness', { company_code: 'self' });
});

// Corporate onboarding
app.get('/corporate_onboard', (req, res) => {
  res.render('hr-register');
});

// Submission success
app.get('/submission_success', (req, res) => {
  res.render('submission-success');
});

// Additional page routes
app.get('/courses', (req, res) => res.render('Courses'));
app.get('/contact', (req, res) => res.render('contact'));
app.get('/meet-the-trainer', (req, res) => res.render('meet-the-trainer'));
app.get('/workshops', (req, res) => res.render('Workshops'));
app.get('/adolescence', (req, res) => res.render('Adolescence'));
app.get('/prenatal-postnatal', (req, res) => res.render('Prenatal & Postnatal'));
app.get('/professional', (req, res) => res.render('professional'));
app.get('/tech-supported-yoga', (req, res) => res.render('Tech-supported Yoga'));
app.get('/therapy', (req, res) => res.render('therapy'));
app.get('/women-wellness', (req, res) => res.render('Women-Wellness'));
app.get('/women-seniors', (req, res) => res.render('women-seniors'));
app.get('/yoga-as-sport', (req, res) => res.render('yoga-as-sport'));
app.get('/yoga-for-sport', (req, res) => res.render('yoga-for-sport'));
app.get('/wellness', (req, res) => res.render('wellness'));
app.get('/admin', (req, res) => res.render('admin'));

// ==================== FORM SUBMISSIONS ====================

// Submit wellness assessment
app.post('/submit_wellness/:company_code', async (req, res) => {
  const { company_code } = req.params;
  const formData = req.body;

  console.log(`\nAttempting to submit wellness form for company_code: ${company_code}`);
  console.log(`Received form data:`, formData);

  try {
    // Calculate total score
    let totalScore = 0;
    for (let i = 1; i <= 12; i++) {
      const value = formData[`q${i}`];
      if (value && !isNaN(parseInt(value))) {
        totalScore += parseInt(value);
      }
    }

    // Insert into database
    const result = await query(
      `INSERT INTO wellness_assessments 
       (company_code, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, 
        name, mobile, email, designation, total_score)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, 
               $14, $15, $16, $17, $18)
       RETURNING id`,
      [
        company_code,
        formData.q1, formData.q2, formData.q3, formData.q4,
        formData.q5, formData.q6, formData.q7, formData.q8,
        formData.q9, formData.q10, formData.q11, formData.q12,
        formData.name, formData.mobile, formData.email,
        formData.designation, totalScore
      ]
    );

    console.log('✅ Wellness submission saved successfully! ID:', result.rows[0].id);
    res.redirect('/submission_success');
  } catch (error) {
    console.error('\n--- DATABASE ERROR ---');
    console.error('Error saving wellness submission:', error);
    console.error('----------------------\n');
    res.status(500).send(`Error submitting form. Please check the console for details. Error: ${error.message}`);
  }
});

// Submit corporate wellness
app.post('/submit_corporate_wellness', async (req, res) => {
  const company_code = req.body.company_code || 'corporate_page';
  const formData = req.body;

  console.log(`\nAttempting to submit wellness form from CORPORATE page for company_code: ${company_code}`);
  console.log(`Received form data:`, formData);

  try {
    // Calculate total score
    let totalScore = 0;
    for (let i = 1; i <= 12; i++) {
      const value = formData[`q${i}`];
      if (value && !isNaN(parseInt(value))) {
        totalScore += parseInt(value);
      }
    }

    // Insert into database
    const result = await query(
      `INSERT INTO wellness_assessments 
       (company_code, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, 
        name, mobile, email, designation, total_score)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, 
               $14, $15, $16, $17, $18)
       RETURNING id`,
      [
        company_code,
        formData.q1, formData.q2, formData.q3, formData.q4,
        formData.q5, formData.q6, formData.q7, formData.q8,
        formData.q9, formData.q10, formData.q11, formData.q12,
        formData.name, formData.mobile, formData.email,
        formData.designation, totalScore
      ]
    );

    console.log('✅ Corporate wellness submission saved successfully! ID:', result.rows[0].id);
    res.redirect('/submission_success');
  } catch (error) {
    console.error('\n--- DATABASE ERROR ---');
    console.error('Error saving corporate wellness submission:', error);
    console.error('----------------------\n');
    res.status(500).send(`Error submitting form. Please check the console for details. Error: ${error.message}`);
  }
});

// Submit company registration
app.post('/submit_company', async (req, res) => {
  const formData = req.body;

  console.log('\nAttempting to submit new company form.');
  console.log('Received form data:', formData);

  try {
    const result = await query(
      `INSERT INTO companies 
       (company_name, contact_person, email, phone, employee_count, industry, company_code)
       VALUES ($1, $2, $3, $4, $5, $6, $7)
       RETURNING id`,
      [
        formData.company_name,
        formData.contact_person,
        formData.email,
        formData.phone,
        formData.employee_count,
        formData.industry,
        formData.company_code
      ]
    );

    console.log('✅ Company data saved successfully! ID:', result.rows[0].id);
    res.redirect('/submission_success');
  } catch (error) {
    console.error('\n--- DATABASE ERROR ---');
    console.error('Error saving company:', error);
    console.error('----------------------\n');
    res.status(500).send(`An error occurred while saving company data. Error: ${error.message}`);
  }
});

// Debug endpoint
app.get('/debug_submissions', async (req, res) => {
  try {
    const result = await query(
      'SELECT id, company_code, name, total_score, submission_date FROM wellness_assessments ORDER BY id DESC LIMIT 10'
    );

    const countResult = await query('SELECT COUNT(*) as count FROM wellness_assessments');
    const count = parseInt(countResult.rows[0].count);

    const data = result.rows.map(row => ({
      id: row.id,
      company_code: row.company_code,
      name: row.name,
      total_score: row.total_score,
      submission_date: row.submission_date
    }));

    res.json({
      count: count,
      samples: data
    });
  } catch (error) {
    console.error('Error fetching submissions:', error);
    res.status(500).json({ error: error.message });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    timestamp: new Date().toISOString(),
    dbInitialized: dbInitialized 
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).send('Page not found');
});

// Error handler
app.use((err, req, res, next) => {
  console.error('Server error:', err);
  res.status(500).send('Internal server error');
});

// For local development
if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
    console.log(`📊 Admin panel: http://localhost:${PORT}/admin`);
    console.log(`🧘 Wellness form: http://localhost:${PORT}/wellness_form`);
  });
}

// Export for Vercel serverless
module.exports = app;
