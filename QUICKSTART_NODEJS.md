# 🚀 Quick Start - Node.js Migration

## Your Flask app has been converted to Node.js/Express!

### 🎯 Quick Deploy to Vercel (3 steps)

#### 1️⃣ Install Dependencies & Convert Templates
```bash
.\setup-nodejs.bat
```

#### 2️⃣ Add Database URL
Edit `.env` file and add your Neon PostgreSQL connection string:
```
DATABASE_URL=postgresql://user:password@host.neon.tech/db?sslmode=require
```

#### 3️⃣ Deploy to Vercel
```bash
npm i -g vercel
vercel login
vercel
```

### 🧪 Test Locally First
```bash
npm run dev
```
Visit: http://localhost:3000

---

## 📚 Full Documentation
See [VERCEL_NODEJS_DEPLOY.md](VERCEL_NODEJS_DEPLOY.md) for complete instructions.

## 🆘 Need Help?

### Common Issues:

**Templates not loading?**
→ Run: `node scripts/convert-templates.js`

**Database errors?**
→ Check `DATABASE_URL` in `.env` and Vercel dashboard

**Static files 404?**
→ Verify files are in `static/` folder

### Check Logs:
```bash
vercel logs --follow
```

---

## 🎉 What's New

- ✅ **Language**: Python → JavaScript/Node.js
- ✅ **Framework**: Flask → Express.js
- ✅ **Templates**: Jinja2 → EJS
- ✅ **Deployment**: Optimized for Vercel serverless
- ✅ **Database**: PostgreSQL with connection pooling
- ✅ **Performance**: Auto-scaling & CDN for static files

**All your routes, forms, and database operations are preserved!**
