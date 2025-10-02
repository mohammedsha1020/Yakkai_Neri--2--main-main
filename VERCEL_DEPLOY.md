# Vercel Deployment Guide
## Yakkai Neri Yoga Academy

This guide explains how to deploy the Yakkai Neri Yoga Academy application to Vercel.

## 🚀 Quick Deployment

### Prerequisites
- [Vercel account](https://vercel.com/) (free)
- [Git repository](https://github.com/) with your code
- [Vercel CLI](https://vercel.com/cli) (optional but recommended)

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push to Git Repository**
   ```bash
   git add .
   git commit -m "Optimize for Vercel deployment"
   git push origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com/)
   - Sign in with your GitHub account
   - Click "New Project"
   - Import your repository
   - Vercel will automatically detect the Flask app

3. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy your application
   - You'll get a live URL like `https://your-app.vercel.app`

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy from Project Directory**
   ```bash
   cd "d:\mini projects\praveen\Yakkai_Neri--1\Yakkai_Neri--1"
   vercel --prod
   ```

## 📁 Project Structure for Vercel

```
Yakkai_Neri--1/
├── vercel.json           # Vercel configuration
├── wsgi.py              # WSGI entry point
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── .vercelignore       # Files to ignore during deployment
├── templates/          # HTML templates
├── static/            # CSS, JS, Images
└── VERCEL_DEPLOY.md   # This file
```

## ⚙️ Configuration Files

### vercel.json
- Configures Python runtime and routing
- Sets up static file serving
- Defines environment variables

### wsgi.py
- Entry point for Vercel
- Imports the Flask application
- Configures production settings

### .vercelignore
- Excludes development files
- Reduces deployment size
- Improves build performance

## 🗄️ Database Configuration

The application automatically switches between:
- **Local Development**: SQLite file database (`wellness.db`)
- **Vercel Production**: In-memory SQLite database

⚠️ **Note**: Since Vercel is serverless, data doesn't persist between requests. For production, consider:
- [PlanetScale](https://planetscale.com/) (MySQL)
- [Supabase](https://supabase.com/) (PostgreSQL)
- [MongoDB Atlas](https://www.mongodb.com/atlas)

## 🌍 Environment Variables

You can set environment variables in Vercel dashboard:
1. Go to your project in Vercel dashboard
2. Navigate to Settings → Environment Variables
3. Add variables like:
   - `FLASK_ENV=production`
   - `DATABASE_URL=your_database_url` (if using external DB)

## 🔧 Build Settings

Vercel automatically detects the Flask app, but you can customize:

**Build Command**: (Leave empty - Vercel handles this)
**Output Directory**: (Leave empty)
**Install Command**: `pip install -r requirements.txt`

## 📱 Features Supported on Vercel

✅ **Working Features:**
- All static pages and routes
- Form submissions (temporary storage)
- CSS, JavaScript, and image serving
- Responsive design
- Contact forms

⚠️ **Limited Features:**
- Database persistence (data resets between deployments)
- File uploads (use cloud storage services)

## 🚀 Performance Optimizations

The application is optimized for Vercel with:
- Minimal dependencies
- Efficient static file serving
- Production-ready Flask configuration
- Proper error handling
- Fast cold start times

## 🔄 Updates and Redeployment

To update your deployed application:
1. Make changes to your code
2. Commit and push to Git
3. Vercel automatically redeploys

Or use CLI:
```bash
vercel --prod
```

## 🌐 Custom Domain

To use a custom domain:
1. Go to your project in Vercel dashboard
2. Navigate to Settings → Domains
3. Add your domain
4. Configure DNS settings as instructed

## 📞 Support

- [Vercel Documentation](https://vercel.com/docs)
- [Flask on Vercel Guide](https://vercel.com/guides/using-flask-with-vercel)
- [Vercel Community](https://github.com/vercel/community)

## 🎉 That's It!

Your Yakkai Neri Yoga Academy application is now ready for Vercel deployment!

Live URL: `https://your-app.vercel.app`