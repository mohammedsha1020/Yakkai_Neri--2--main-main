# 🧘 Yakkai Neri Yoga Academy - Node.js/Express

> **Enterprise Wellness Platform** - Now powered by Node.js and optimized for Vercel!

[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![Express](https://img.shields.io/badge/Express-4.18-blue.svg)](https://expressjs.com/)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-black.svg)](https://vercel.com)

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
npm install

# 2. Setup environment
copy .env.example .env
# Edit .env and add your DATABASE_URL

# 3. Start development server
npm run dev
```

Visit: **http://localhost:3000**

---

## 📦 Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel
```

**Don't forget to add `DATABASE_URL` in Vercel Environment Variables!**

---

## 📚 Documentation

- **[Quick Start Guide](QUICKSTART_NODEJS.md)** - Get started in 3 steps
- **[Deployment Guide](VERCEL_NODEJS_DEPLOY.md)** - Complete Vercel deployment instructions
- **[Migration Summary](MIGRATION_SUMMARY.md)** - See what changed from Python to Node.js

---

## ✨ Features

- ✅ **Corporate Wellness Assessments** - 12-question wellness evaluation
- ✅ **Individual Wellness Forms** - Personal health tracking
- ✅ **HR Registration Portal** - Company onboarding system
- ✅ **Admin Dashboard** - Submission management
- ✅ **PostgreSQL Database** - Powered by Neon.tech
- ✅ **Responsive Design** - Works on all devices
- ✅ **Serverless Ready** - Auto-scaling on Vercel

---

## 🏗️ Project Structure

```
├── api/
│   ├── index.js          # Express application
│   └── db.js            # Database configuration
├── templates/           # EJS templates (HTML)
├── static/
│   ├── css/            # Stylesheets
│   ├── js/             # Client-side JavaScript
│   └── images/         # Images and assets
├── scripts/
│   └── convert-templates.js  # Template converter
├── package.json        # Dependencies
└── vercel.json        # Vercel configuration
```

---

## 🔧 Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@host.neon.tech/db?sslmode=require
NODE_ENV=development
PORT=3000
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/corporate-yoga` | Corporate wellness page |
| GET | `/wellness_form` | Individual wellness form |
| GET | `/corporate_onboard` | HR registration |
| POST | `/submit_wellness/:code` | Submit wellness assessment |
| POST | `/submit_corporate_wellness` | Submit corporate wellness |
| POST | `/submit_company` | Register company |
| GET | `/debug_submissions` | View submissions (JSON) |
| GET | `/health` | Health check |

---

## 🛠️ Tech Stack

- **Runtime**: Node.js 18+
- **Framework**: Express.js 4.18
- **Database**: PostgreSQL (Neon.tech)
- **Templates**: EJS
- **Deployment**: Vercel Serverless
- **CSS**: Tailwind CSS (CDN)

---

## 🐛 Troubleshooting

### Templates not loading?
```bash
node scripts/convert-templates.js
```

### Database connection error?
Check `DATABASE_URL` in `.env` and Vercel dashboard

### View deployment logs:
```bash
vercel logs --follow
```

---

## 📊 Database Schema

### `wellness_assessments`
Stores wellness assessment submissions with 12 questions, personal info, and scores.

### `companies`
Stores registered company information and HR contact details.

---

## 🎯 Migration from Python

This project was migrated from Flask (Python) to Express (Node.js):
- ✅ All routes preserved
- ✅ Database operations converted to pg
- ✅ Templates converted from Jinja2 to EJS
- ✅ Performance optimized for Vercel

See [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md) for details.

---

## 📝 License

© 2025 Yakkai Neri Yoga Academy. All rights reserved.

---

## 🆘 Support

For issues or questions:
1. Check the [documentation](VERCEL_NODEJS_DEPLOY.md)
2. Review [migration notes](MIGRATION_SUMMARY.md)
3. Check Vercel deployment logs

---

**Built with ❤️ and optimized for Vercel** 🚀
