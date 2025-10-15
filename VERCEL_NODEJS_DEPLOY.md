# 🚀 Vercel Deployment Guide - Node.js/Express

## ✅ Project Successfully Converted to Node.js!

Your Flask application has been converted to Node.js/Express and optimized for Vercel deployment.

## 📋 What Changed

### Added Files:
- `package.json` - Node.js dependencies
- `api/index.js` - Express.js application (converted from app.py)
- `api/db.js` - PostgreSQL database connection
- `scripts/convert-templates.js` - Template conversion utility
- `.gitignore` - Updated for Node.js

### Updated Files:
- `vercel.json` - Now configured for Node.js (@vercel/node)
- `.env.example` - Updated for Node.js environment variables

### Files to Remove (Optional):
- `app.py`, `app.py.bak`, `wsgi.py` - Old Python files
- `requirements.txt` - Python dependencies
- All `.py` test files
- `__pycache__/` directory

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
npm install
```

### 2. Update HTML Templates

Run the template conversion script to update Jinja2 syntax to EJS:

```bash
node scripts/convert-templates.js
```

This will:
- Convert `{{ url_for('static', filename='...') }}` to `/static/...`
- Convert route references to direct paths
- Rename `.html` files to `.ejs`

### 3. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` and add your Neon PostgreSQL connection string:

```
DATABASE_URL=postgresql://your_user:your_password@your_host.neon.tech/your_database?sslmode=require
NODE_ENV=development
PORT=3000
```

### 4. Test Locally

```bash
npm run dev
```

Visit: http://localhost:3000

### 5. Deploy to Vercel

#### Option A: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

#### Option B: Using GitHub

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "Import Project"
4. Select your GitHub repository
5. Vercel will auto-detect the Node.js configuration

### 6. Configure Environment Variables in Vercel

In your Vercel dashboard:
1. Go to Project Settings → Environment Variables
2. Add:
   - `DATABASE_URL` = Your Neon PostgreSQL connection string
   - `NODE_ENV` = `production`

## 📁 Project Structure

```
├── api/
│   ├── index.js          # Main Express app (serverless function)
│   └── db.js            # Database configuration
├── templates/           # EJS templates (converted from HTML)
├── static/             # CSS, JS, images
├── scripts/
│   └── convert-templates.js  # Template conversion utility
├── package.json        # Node.js dependencies
├── vercel.json        # Vercel configuration
└── .env.example       # Environment variables template
```

## 🎯 API Endpoints

All your original Flask routes are preserved:

- `GET /` - Home page
- `GET /corporate-yoga` - Corporate yoga page
- `GET /wellness_form` - Individual wellness form
- `GET /corporate_onboard` - HR registration
- `POST /submit_wellness/:company_code` - Submit wellness assessment
- `POST /submit_corporate_wellness` - Submit corporate wellness
- `POST /submit_company` - Submit company registration
- `GET /debug_submissions` - Debug endpoint (JSON)
- `GET /health` - Health check endpoint

And all other page routes (courses, contact, etc.)

## 🔍 Testing After Deployment

1. Visit your Vercel URL
2. Test the wellness form submission
3. Check `/health` endpoint: `https://your-app.vercel.app/health`
4. Check `/debug_submissions` to verify database connectivity

## ⚡ Performance Optimizations

1. **Connection Pooling**: Database uses connection pooling (max 20 connections)
2. **Serverless-Ready**: All functions optimized for serverless deployment
3. **Static Assets**: Served directly by Vercel CDN
4. **Auto-scaling**: Vercel handles scaling automatically

## 🐛 Troubleshooting

### Templates not loading
- Make sure you ran `node scripts/convert-templates.js`
- Check that `.ejs` files exist in `templates/` folder

### Database connection issues
- Verify `DATABASE_URL` in Vercel environment variables
- Check Neon database is active and accessible
- View logs: `vercel logs your-project-url`

### Static files not loading
- Check paths in templates use `/static/...` format
- Verify files exist in `static/` directory

## 📊 Monitoring

View real-time logs:
```bash
vercel logs --follow
```

## 🎉 Done!

Your application is now running on Node.js/Express and optimized for Vercel!

For support, check:
- [Vercel Documentation](https://vercel.com/docs)
- [Express.js Documentation](https://expressjs.com/)
- [Neon PostgreSQL Documentation](https://neon.tech/docs)
