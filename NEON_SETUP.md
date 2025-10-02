# Neon Database Setup Guide
## Yakkai Neri Yoga Academy

This guide explains how to set up and use Neon Tech's serverless PostgreSQL database with your Yakkai Neri application.

## 🐘 What is Neon?

[Neon](https://neon.tech/) is a serverless PostgreSQL database that's perfect for:
- **Serverless applications** (like Vercel deployments)
- **Auto-scaling** based on usage
- **Branching databases** for development/testing
- **Free tier** with generous limits

## 🚀 Quick Setup

### Step 1: Create Neon Account

1. Go to [console.neon.tech](https://console.neon.tech/)
2. Sign up with GitHub, Google, or email
3. Create your first project

### Step 2: Get Database Connection String

1. In your Neon dashboard, go to **Connection Details**
2. Copy the connection string (looks like):
   ```
   postgresql://username:password@hostname/database?sslmode=require
   ```

### Step 3: Configure Local Environment

1. **Copy the environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file with your Neon connection string:**
   ```env
   DATABASE_URL=postgresql://your_username:your_password@your_host.neon.tech/your_database?sslmode=require
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   ```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Test Connection

```bash
python test_neon.py
```

## 🌐 Vercel Deployment with Neon

### Configure Environment Variables in Vercel

1. Go to your project in [Vercel Dashboard](https://vercel.com/dashboard)
2. Navigate to **Settings** → **Environment Variables**
3. Add these variables:

| Variable | Value | Environment |
|----------|-------|-------------|
| `DATABASE_URL` | Your Neon connection string | Production, Preview, Development |
| `SECRET_KEY` | Random secret key for Flask | Production, Preview, Development |

### Deploy to Vercel

```bash
# Option 1: Vercel CLI
vercel --prod

# Option 2: Push to Git (auto-deploy)
git add .
git commit -m "Add Neon database support"
git push origin main
```

## 🔧 Database Features

### Automatic Table Creation

The application automatically creates tables when it starts:
- `wellness_assessments` - Stores wellness form submissions
- `companies` - Stores corporate client information

### Data Persistence

✅ **With Neon**: All data persists between deployments and restarts
❌ **Without Neon**: Data is lost on each restart (in-memory database)

## 📊 Database Schema

### WellnessSubmission Table
```sql
CREATE TABLE wellness_assessments (
    id SERIAL PRIMARY KEY,
    company_code VARCHAR(50),
    q1 VARCHAR(10),
    q2 VARCHAR(10),
    -- ... q3 to q12
    name VARCHAR(100),
    mobile VARCHAR(20),
    email VARCHAR(120),
    designation VARCHAR(100),
    total_score INTEGER,
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Company Table
```sql
CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    employee_count INTEGER,
    industry VARCHAR(100),
    company_code VARCHAR(50) UNIQUE NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔄 Database Operations

### View Data in Neon Console

1. Go to [console.neon.tech](https://console.neon.tech/)
2. Select your project
3. Go to **SQL Editor**
4. Run queries like:
   ```sql
   SELECT * FROM wellness_assessments ORDER BY submission_date DESC LIMIT 10;
   SELECT * FROM companies ORDER BY created_date DESC;
   ```

### Backup and Restore

Neon automatically handles:
- **Point-in-time recovery**
- **Automated backups**
- **Database branching** for testing

## 🌿 Database Branching (Advanced)

Neon allows you to create database branches for different environments:

```bash
# Create a branch for testing
neonctl branches create --name testing

# Get connection string for testing branch
neonctl connection-string --branch testing
```

## 🚨 Troubleshooting

### Connection Issues

1. **Check connection string format:**
   ```
   postgresql://username:password@hostname/database?sslmode=require
   ```

2. **Verify SSL mode is included:** `?sslmode=require`

3. **Check environment variables are set:**
   ```bash
   echo $DATABASE_URL
   ```

### Common Errors

**Error**: `could not connect to server`
- **Solution**: Check if connection string is correct and Neon instance is running

**Error**: `relation does not exist`
- **Solution**: Tables are created automatically. Restart the application.

**Error**: `SSL connection required`
- **Solution**: Ensure connection string includes `?sslmode=require`

## 💰 Pricing

### Neon Free Tier Includes:
- 3 projects
- 10 branches per project
- 3 GB storage
- 100 hours of compute per month

### Perfect for:
- Development and testing
- Small to medium applications
- Prototypes and MVPs

## 📞 Support

- [Neon Documentation](https://neon.tech/docs/)
- [Neon Discord Community](https://discord.gg/92vNTzKDGp)
- [GitHub Issues](https://github.com/neondatabase/neon/issues)

## 🎉 Benefits of Using Neon

✅ **Serverless**: No server management required
✅ **Auto-scaling**: Scales with your application
✅ **Persistent data**: Unlike SQLite, data survives deployments
✅ **PostgreSQL**: Full PostgreSQL compatibility
✅ **Free tier**: Generous limits for development
✅ **Fast cold starts**: Optimized for serverless environments
✅ **Database branching**: Create isolated environments
✅ **Automatic backups**: Built-in data protection

---

**Ready to use Neon with your Yakkai Neri application!** 🐘✨