# Yakkai Neri Yoga Academy - Web Application

A comprehensive Flask-based web application for Yakkai Neri Yoga Academy offering various yoga courses, wellness assessments, and corporate training programs.

## 🌟 Features

- **Home Page**: Introduction to Yakkai Neri Yoga Academy
- **Corporate Yoga**: Specialized programs for corporate wellness
- **Individual Wellness**: Personal wellness assessment and programs
- **Course Catalog**: Various yoga courses including:
  - Adolescence programs
  - Prenatal & Postnatal yoga
  - Professional development
  - Tech-supported yoga
  - Therapy and wellness
  - Women's wellness programs
  - Yoga as sport
- **Trainer Profile**: Meet the experienced trainers
- **Contact & Registration**: Easy contact and corporate onboarding
- **Admin Panel**: Administrative functions and data management

## 🏗️ Project Structure

```
Yakkai_Neri--1/
├── app.py                  # Main Flask application
├── app.py.bak             # Backup of original app
├── reset_db.py            # Database reset utility
├── wellness.db            # SQLite database
├── README.md              # This file
├── templates/             # HTML templates
│   ├── index.html         # Home page
│   ├── corporate-yoga.html
│   ├── individual-wellness.html
│   ├── hr-register.html
│   ├── admin.html
│   ├── contact.html
│   ├── meet-the-trainer.html
│   ├── Courses.html
│   ├── Workshops.html
│   ├── Adolescence.html
│   ├── Prenatal & Postnatal.html
│   ├── professional.html
│   ├── Tech-supported Yoga.html
│   ├── therapy.html
│   ├── Women-Wellness.html
│   ├── women-seniors.html
│   ├── yoga-as-sport.html
│   ├── yoga-for-sport.html
│   ├── wellness.html
│   ├── submission-success.html
│   └── base.html
├── static/               # Static files
│   ├── css/             # Stylesheets
│   │   ├── style.css
│   │   ├── admin-style.css
│   │   ├── corporate-yoga.css
│   │   ├── custom-index.css
│   │   └── submission-success.css
│   ├── js/              # JavaScript files
│   │   ├── script.js
│   │   ├── admin-script.js
│   │   └── corporate-yoga.js
│   └── images/          # Image assets
│       ├── banner.jpg
│       ├── award.jpg
│       ├── victory.jpg
│       ├── Champion-award.jpg
│       └── [other images...]
└── instance/            # Instance-specific files
    └── [database files]
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   cd "d:\mini projects\praveen\Yakkai_Neri--1\Yakkai_Neri--1"
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up database (Choose one option):**

   **Option A: Neon Database (Recommended for production)**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env with your Neon connection string
   # Get it from: https://console.neon.tech/
   # See NEON_SETUP.md for detailed instructions
   
   # Test connection
   python test_neon.py
   ```

   **Option B: Local SQLite (Development only)**
   ```bash
   # No setup needed - SQLite file created automatically
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser and visit**
   ```
   http://127.0.0.1:5000
   ```

## 🌐 Available Routes

- `/` - Home page
- `/corporate-yoga` - Corporate yoga programs
- `/wellness_form` - Individual wellness assessment
- `/corporate_onboard` - Corporate registration
- `/courses` - Course catalog
- `/contact` - Contact information
- `/meet-the-trainer` - Trainer profiles
- `/workshops` - Workshop information
- `/adolescence` - Adolescence programs
- `/prenatal-postnatal` - Prenatal & postnatal programs
- `/professional` - Professional development
- `/tech-supported-yoga` - Technology-supported yoga
- `/therapy` - Therapy programs
- `/women-wellness` - Women's wellness
- `/women-seniors` - Programs for senior women
- `/yoga-as-sport` - Yoga as sport
- `/yoga-for-sport` - Yoga for sports performance
- `/wellness` - General wellness information
- `/admin` - Admin panel

## 💾 Database

The application supports multiple database configurations:

### 🐘 Neon PostgreSQL (Recommended for Production)
- **Serverless PostgreSQL** optimized for modern applications
- **Persistent data** that survives deployments
- **Auto-scaling** with usage-based pricing
- **Free tier** with generous limits
- **Perfect for Vercel** deployment

**Setup**: See `NEON_SETUP.md` for complete instructions
**Test**: Run `python test_neon.py` to verify connection

### 📁 SQLite (Local Development)
- **File-based database** for local development
- **Automatic setup** - no configuration needed
- **Development only** - not suitable for production

### Database Tables

#### WellnessSubmission
- Individual wellness assessment responses
- Stores questionnaire answers (q1-q12)
- Personal information (name, email, mobile, designation)
- Total score calculation
- Company code tracking

#### Company
- Corporate client information
- Contact details
- Employee count and industry
- Unique company codes for tracking

## 🔧 Development

### Debug Mode
The application runs in debug mode by default, which provides:
- Auto-reload on file changes
- Detailed error messages
- Interactive debugger

### Database Reset
To reset the database, run:
```bash
python reset_db.py
```

## 📁 File Organization

- **Templates**: All HTML files are in the `templates/` folder following Flask conventions
- **Static Files**: CSS, JavaScript, and images are in the `static/` folder with proper subdirectories
- **Database**: SQLite database files are created automatically
- **Configuration**: Database and Flask configuration in `app.py`

## 🎨 Styling

The application uses:
- **Tailwind CSS** (CDN) for utility-first styling
- **Font Awesome** for icons
- **Google Fonts** (Poppins) for typography
- **Custom CSS** for specific styling needs

## 📱 Responsive Design

All pages are designed to be responsive and work well on:
- Desktop computers
- Tablets
- Mobile devices

## 🚀 Production Deployment

### Vercel + Neon Deployment (Recommended)

The application is optimized for Vercel deployment with Neon database:

1. **Set up Neon Database:**
   - Create account at [neon.tech](https://neon.tech/)
   - Get your connection string
   - See `NEON_SETUP.md` for detailed instructions

2. **Deploy to Vercel:**
   - Push code to GitHub/GitLab/Bitbucket
   - Go to [vercel.com](https://vercel.com/) and import your repository
   - Add `DATABASE_URL` environment variable in Vercel settings

3. **Environment Variables for Vercel:**
   - `DATABASE_URL` - Your Neon connection string
   - `SECRET_KEY` - Random secret key for Flask

4. **Files for Vercel Deployment:**
   - `vercel.json` - Vercel configuration
   - `wsgi.py` - WSGI entry point
   - `.vercelignore` - Deployment exclusions
   - `VERCEL_DEPLOY.md` - Detailed deployment guide
   - `NEON_SETUP.md` - Database setup guide

**📖 Read `VERCEL_DEPLOY.md` and `NEON_SETUP.md` for complete instructions.**

### Other Production Options

For traditional hosting:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Configure environment variables for sensitive data
4. Use a production database (PostgreSQL, MySQL)
5. Set up proper static file serving

## 🤝 Contributing

1. Follow the existing code structure
2. Test all functionality before submitting
3. Ensure responsive design compatibility
4. Update documentation as needed

## 📞 Support

For support or questions about the Yakkai Neri Yoga Academy web application, please contact the development team.

---

**Yakkai Neri Yoga Academy** - Transforming lives through yoga and wellness.