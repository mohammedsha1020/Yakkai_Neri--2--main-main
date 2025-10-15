# ✅ Deployment Checklist

## Pre-Deployment

- [x] ✅ Node.js dependencies installed (`npm install`)
- [x] ✅ Templates converted to EJS format
- [ ] ⚠️ `.env` file created with `DATABASE_URL`
- [ ] ⚠️ Tested locally with `npm run dev`
- [ ] ⚠️ Verified all routes work locally

## Vercel Setup

- [ ] ⚠️ Vercel CLI installed (`npm i -g vercel`)
- [ ] ⚠️ Logged into Vercel (`vercel login`)
- [ ] ⚠️ Connected to GitHub (optional but recommended)

## Deploy

- [ ] ⚠️ Run `vercel` command
- [ ] ⚠️ Follow prompts to link/create project
- [ ] ⚠️ Confirm deployment

## Post-Deployment

- [ ] ⚠️ Add `DATABASE_URL` in Vercel dashboard
  - Go to: Project Settings → Environment Variables
  - Add: `DATABASE_URL` = Your Neon PostgreSQL connection string
  - Add: `NODE_ENV` = `production`
- [ ] ⚠️ Redeploy after adding env vars (if needed)
- [ ] ⚠️ Test deployment:
  - [ ] Homepage loads: `https://your-app.vercel.app/`
  - [ ] Health check: `https://your-app.vercel.app/health`
  - [ ] Wellness form: `https://your-app.vercel.app/wellness_form`
  - [ ] Submit a test form
  - [ ] Check debug endpoint: `https://your-app.vercel.app/debug_submissions`

## Verification

- [ ] ⚠️ All pages load without errors
- [ ] ⚠️ Static files (CSS/JS/images) load correctly
- [ ] ⚠️ Forms submit successfully
- [ ] ⚠️ Database records are saved
- [ ] ⚠️ No console errors in browser

## Monitoring

- [ ] ⚠️ Check Vercel logs: `vercel logs --follow`
- [ ] ⚠️ Monitor function execution time in Vercel dashboard
- [ ] ⚠️ Verify database connections in Neon dashboard

## Optional Cleanup

- [ ] Delete old Python files:
  - [ ] `app.py`, `app.py.bak`
  - [ ] `wsgi.py`
  - [ ] `requirements.txt`
  - [ ] All `.py` test files
  - [ ] `__pycache__/` directory
  - [ ] `instance/` directory

---

## Quick Commands Reference

```bash
# Install dependencies
npm install

# Test locally
npm run dev

# Deploy to Vercel
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs --follow

# View project info
vercel ls
```

---

## Environment Variables Needed

### Local (`.env` file)
```
DATABASE_URL=postgresql://user:password@host.neon.tech/db?sslmode=require
NODE_ENV=development
PORT=3000
```

### Vercel Dashboard
```
DATABASE_URL=postgresql://user:password@host.neon.tech/db?sslmode=require
NODE_ENV=production
```

---

## Troubleshooting

### ❌ Templates not found
**Fix**: Templates already converted to `.ejs` format in `templates/` folder

### ❌ Database connection error
**Fix**: Check `DATABASE_URL` in Vercel environment variables

### ❌ 404 on static files
**Fix**: Verify files exist in `static/` directory and paths use `/static/...`

### ❌ Form submission fails
**Fix**: Check Vercel function logs: `vercel logs --follow`

### ❌ Cold start timeout
**Fix**: Connection pooling is already configured. Should resolve after warmup.

---

## Success Indicators ✅

When everything works, you should see:

1. ✅ Homepage loads instantly
2. ✅ All navigation links work
3. ✅ Forms submit successfully
4. ✅ Success page shows after submission
5. ✅ `/debug_submissions` shows data
6. ✅ `/health` returns healthy status
7. ✅ No errors in browser console
8. ✅ No errors in Vercel logs

---

## 🎉 Once Complete

Your app is live and running on:
- **Node.js 18+**
- **Express.js**
- **Vercel Serverless**
- **PostgreSQL (Neon)**

**Auto-scaling enabled!** 🚀

---

## Support

- 📚 [VERCEL_NODEJS_DEPLOY.md](VERCEL_NODEJS_DEPLOY.md) - Full guide
- 📊 [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md) - What changed
- 🚀 [QUICKSTART_NODEJS.md](QUICKSTART_NODEJS.md) - Quick reference
