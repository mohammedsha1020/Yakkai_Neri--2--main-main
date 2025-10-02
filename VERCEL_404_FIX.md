# Vercel Deployment Fix Guide
## Yakkai Neri Yoga Academy

## Quick Fix Steps

### 1. Redeploy with Latest Configuration
```bash
# If using Vercel CLI
vercel --prod

# Or push to connected Git repository for auto-deployment
```

### 2. Set Environment Variables in Vercel Dashboard
Go to your Vercel project dashboard and add these environment variables:

**Required:**
- `SECRET_KEY` = Any random string (e.g., `your-super-secret-key-here`)
- `FLASK_ENV` = `production`

**Optional (for Neon database):**
- `DATABASE_URL` = Your Neon PostgreSQL connection string

### 3. Common 404 Fixes

#### A. Force Redeploy
```bash
# Delete .vercel folder and redeploy
rm -rf .vercel
vercel --prod
```

#### B. Check Function Logs
1. Go to Vercel Dashboard
2. Click on your project
3. Go to "Functions" tab
4. Check logs for errors

#### C. Verify Build Output
1. Check if build completed successfully
2. Verify all files are uploaded
3. Check function runtime logs

### 4. Environment Variables Setup

#### In Vercel Dashboard:
1. Go to Settings > Environment Variables
2. Add these variables:

```
SECRET_KEY = flask-secret-key-change-this-in-production
FLASK_ENV = production
DATABASE_URL = postgresql://... (if using Neon)
```

### 5. Test Deployment

After deployment, test these URLs:
- `https://your-app.vercel.app/` (Home page)
- `https://your-app.vercel.app/corporate-yoga` (Corporate page)
- `https://your-app.vercel.app/wellness` (Wellness page)

### 6. Troubleshooting

#### If still getting 404:

1. **Check Build Logs:**
   ```
   Vercel Dashboard > Project > Deployments > Latest > View Logs
   ```

2. **Verify Function is Created:**
   ```
   Vercel Dashboard > Project > Functions
   Should show wsgi.py function
   ```

3. **Check Domain/DNS:**
   ```
   Vercel Dashboard > Project > Settings > Domains
   Verify domain is properly configured
   ```

#### If getting 500 errors:
1. Check function logs for Python errors
2. Verify all dependencies in requirements.txt
3. Check database connection

### 7. Manual Verification

Run this locally to ensure everything works:
```bash
python app.py
# Should start without errors
# Test all routes in browser
```

## Most Common Solutions

1. **Environment Variables Missing** → Add SECRET_KEY and FLASK_ENV
2. **Build Cache Issues** → Delete .vercel folder and redeploy  
3. **Function Timeout** → Check for infinite loops in code
4. **Database Connection** → Verify DATABASE_URL or use SQLite fallback

## If Nothing Works

1. Create a new Vercel project
2. Import from GitHub repository
3. Add environment variables
4. Deploy fresh

---

**Your app should now work perfectly on Vercel!**
