from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# --- UPDATED LINE ---
# This tells Flask to look for HTML files in the 'templates' folder
# and static files in the 'static' folder (proper Flask structure).
app = Flask(__name__, template_folder='templates', static_folder='static')


# --- Database Configuration ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wellness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True  # Logs all SQL statements to the console

db = SQLAlchemy(app)

# --- Models ---
# Defining the database tables as Python classes.

class WellnessSubmission(db.Model):
    __tablename__ = 'wellness_assessments'
    id = db.Column(db.Integer, primary_key=True)
    company_code = db.Column(db.String(50))
    q1 = db.Column(db.String(10))
    q2 = db.Column(db.String(10))
    q3 = db.Column(db.String(10))
    q4 = db.Column(db.String(10))
    q5 = db.Column(db.String(10))
    q6 = db.Column(db.String(10))
    q7 = db.Column(db.String(10))
    q8 = db.Column(db.String(10))
    q9 = db.Column(db.String(10))
    q10 = db.Column(db.String(10))
    q11 = db.Column(db.String(10))
    q12 = db.Column(db.String(10))
    name = db.Column(db.String(100))
    mobile = db.Column(db.String(20))
    email = db.Column(db.String(120))
    designation = db.Column(db.String(100))
    total_score = db.Column(db.Integer)
    submission_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    employee_count = db.Column(db.Integer)
    industry = db.Column(db.String(100))
    company_code = db.Column(db.String(50), unique=True, nullable=False)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

# --- Routes ---

# This now serves index.html as the home page from your root folder.
@app.route("/")
def home():
    return render_template("index.html")

# This route serves the corporate-yoga.html page from your root folder.
@app.route("/corporate-yoga")
def corporate_yoga():
    return render_template("corporate-yoga.html", company_code="ABC123")


@app.route("/wellness_form")
def wellness_form():
    return render_template("individual-wellness.html", company_code='self')

@app.route("/corporate_onboard")
def corporate_onboard():
    return render_template("hr-register.html")

@app.route("/submission_success")
def submission_success():
    return render_template("submission-success.html")

# Additional page routes
@app.route("/courses")
def courses():
    return render_template("Courses.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/meet-the-trainer")
def meet_the_trainer():
    return render_template("meet-the-trainer.html")

@app.route("/workshops")
def workshops():
    return render_template("Workshops.html")

@app.route("/adolescence")
def adolescence():
    return render_template("Adolescence.html")

@app.route("/prenatal-postnatal")
def prenatal_postnatal():
    return render_template("Prenatal & Postnatal.html")

@app.route("/professional")
def professional():
    return render_template("professional.html")

@app.route("/tech-supported-yoga")
def tech_supported_yoga():
    return render_template("Tech-supported Yoga.html")

@app.route("/therapy")
def therapy():
    return render_template("therapy.html")

@app.route("/women-wellness")
def women_wellness():
    return render_template("Women-Wellness.html")

@app.route("/women-seniors")
def women_seniors():
    return render_template("women-seniors.html")

@app.route("/yoga-as-sport")
def yoga_as_sport():
    return render_template("yoga-as-sport.html")

@app.route("/yoga-for-sport")
def yoga_for_sport():
    return render_template("yoga-for-sport.html")

@app.route("/wellness")
def wellness():
    return render_template("wellness.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/submit_wellness/<company_code>", methods=["POST"])
def submit_wellness(company_code):
    print(f"\nAttempting to submit wellness form for company_code: {company_code}")
    print(f"Received form data: {request.form}")

    submission = WellnessSubmission(
        company_code=company_code,
        q1=request.form.get("q1"),
        q2=request.form.get("q2"),
        q3=request.form.get("q3"),
        q4=request.form.get("q4"),
        q5=request.form.get("q5"),
        q6=request.form.get("q6"),
        q7=request.form.get("q7"),
        q8=request.form.get("q8"),
        q9=request.form.get("q9"),
        q10=request.form.get("q10"),
        q11=request.form.get("q11"),
        q12=request.form.get("q12"),
        name=request.form.get("name"),
        mobile=request.form.get("mobile"),
        email=request.form.get("email"),
        designation=request.form.get("designation")
    )

    total = 0
    for i in range(1, 13):
        v = request.form.get(f"q{i}")
        if v and v.isdigit():
            total += int(v)
    submission.total_score = total

    try:
        db.session.add(submission)
        db.session.commit()
        print("Wellness submission saved successfully!")
        return redirect(url_for('submission_success'))
    except Exception as e:
        db.session.rollback()
        print(f"\n--- DATABASE ERROR ---")
        print(f"Error saving wellness submission: {e}")
        print(f"----------------------\n")
        return f"Error submitting form. Please check the console for details. Error: {e}", 500

@app.route("/submit_corporate_wellness", methods=["POST"])
def submit_corporate_wellness():
    """Handles submission from the corporate yoga page wellness form."""
    company_code = request.form.get("company_code", "corporate_page")
    print(f"\nAttempting to submit wellness form from CORPORATE page for company_code: {company_code}")
    print(f"Received form data: {request.form}")

    submission = WellnessSubmission(
        company_code=company_code,
        q1=request.form.get("q1"),
        q2=request.form.get("q2"),
        q3=request.form.get("q3"),
        q4=request.form.get("q4"),
        q5=request.form.get("q5"),
        q6=request.form.get("q6"),
        q7=request.form.get("q7"),
        q8=request.form.get("q8"),
        q9=request.form.get("q9"),
        q10=request.form.get("q10"),
        q11=request.form.get("q11"),
        q12=request.form.get("q12"),
        name=request.form.get("name"),
        mobile=request.form.get("mobile"),
        email=request.form.get("email"),
        designation=request.form.get("designation")
    )

    total = 0
    for i in range(1, 13):
        v = request.form.get(f"q{i}")
        if v and v.isdigit():
            total += int(v)
    submission.total_score = total

    try:
        db.session.add(submission)
        db.session.commit()
        print("Corporate wellness submission saved successfully!")
        return redirect(url_for('submission_success'))
    except Exception as e:
        db.session.rollback()
        print(f"\n--- DATABASE ERROR ---")
        print(f"Error saving corporate wellness submission: {e}")
        print(f"----------------------\n")
        return f"Error submitting form. Please check the console for details. Error: {e}", 500


@app.route("/submit_company", methods=["POST"])
def submit_company():
    print(f"\nAttempting to submit new company form.")
    print(f"Received form data: {request.form}")

    try:
        new_company = Company(
            company_name=request.form.get("company_name"),
            contact_person=request.form.get("contact_person"),
            email=request.form.get("email"),
            phone=request.form.get("phone"),
            employee_count=request.form.get("employee_count"),
            industry=request.form.get("industry"),
            company_code=request.form.get("company_code")
        )
        db.session.add(new_company)
        db.session.commit()
        print("Company data saved successfully!")
        return redirect(url_for('submission_success'))
    except Exception as e:
        db.session.rollback()
        print(f"\n--- DATABASE ERROR ---")
        print(f"Error saving company: {e}")
        print(f"----------------------\n")
        return f"An error occurred while saving company data. Error: {e}", 500
        
@app.route('/debug_submissions')
def debug_submissions():
    """Return count and a small sample of wellness submissions as JSON for debugging."""
    try:
        subs = WellnessSubmission.query.order_by(WellnessSubmission.id.desc()).limit(10).all()
        data = []
        for s in subs:
            data.append({
                'id': s.id,
                'company_code': s.company_code,
                'name': s.name,
                'total_score': s.total_score,
                'submission_date': s.submission_date.isoformat() if s.submission_date else None
            })
        total = db.session.query(db.func.count(WellnessSubmission.id)).scalar()
        return jsonify({'count': total, 'samples': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    with app.app_context():
        print("Creating database tables if they don't exist...")
        db.create_all()
        print("Tables created/verified.")
    app.run(debug=True)
