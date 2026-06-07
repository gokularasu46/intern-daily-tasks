"""
AI-Powered Professional Portfolio & Career Management System
Owner: GOKULARASU K

Run:
    flask --app app init-db
    flask --app app run --debug
"""

from __future__ import annotations

import os
import re
import secrets
from collections import Counter
from datetime import datetime, timedelta
from functools import wraps
from pathlib import Path

from flask import Flask, abort, flash, jsonify, redirect, render_template, request, send_from_directory, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
db = SQLAlchemy()

SKILL_KEYWORDS = {
    "python", "flask", "django", "sql", "sqlite", "mysql", "postgresql", "html", "css",
    "javascript", "bootstrap", "react", "git", "github", "rest api", "machine learning",
    "data analytics", "pandas", "numpy", "power bi", "tableau", "excel", "nlp",
    "tensorflow", "scikit-learn",
}
CAREER_TRACKS = {
    "AI Full Stack Developer": {"python", "flask", "sql", "javascript", "machine learning", "rest api"},
    "Data Analyst": {"python", "sql", "excel", "power bi", "tableau", "data analytics"},
    "Backend Developer": {"python", "flask", "django", "sql", "rest api", "git"},
}
ALLOWED_DOCS = {"pdf", "doc", "docx", "txt"}
ALLOWED_IMAGES = {"png", "jpg", "jpeg", "webp"}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(30), default="user", index=True)
    headline = db.Column(db.String(180), default="AI & Data Analytics Enthusiast")
    bio = db.Column(db.Text, default="")
    skills = db.Column(db.Text, default="Python, Flask, SQL, HTML, CSS, JavaScript, Bootstrap, Data Analytics")
    education = db.Column(db.Text, default="Computer Science and Business Systems")
    reset_token = db.Column(db.String(120), nullable=True, index=True)
    reset_expires_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def skill_list(self) -> list[str]:
        return [item.strip() for item in self.skills.split(",") if item.strip()]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "headline": self.headline,
            "skills": self.skill_list(),
            "created_at": self.created_at.isoformat(),
        }


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(255), default="")
    github_url = db.Column(db.String(255), default="")
    live_url = db.Column(db.String(255), default="")
    image_file = db.Column(db.String(255), default="")
    status = db.Column(db.String(40), default="Published")
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "tech_stack": self.tech_stack,
            "github_url": self.github_url,
            "live_url": self.live_url,
            "status": self.status,
            "views": self.views,
            "created_at": self.created_at.isoformat(),
        }


class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    issuer = db.Column(db.String(180), nullable=False)
    issue_date = db.Column(db.String(40), default="")
    credential_url = db.Column(db.String(255), default="")
    certificate_file = db.Column(db.String(255), default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "issuer": self.issuer, "issue_date": self.issue_date, "credential_url": self.credential_url}


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), nullable=False, index=True)
    subject = db.Column(db.String(180), default="Portfolio inquiry")
    message = db.Column(db.Text, nullable=False)
    reply = db.Column(db.Text, default="")
    status = db.Column(db.String(30), default="New", index=True)
    ip_address = db.Column(db.String(80), default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    replied_at = db.Column(db.DateTime, nullable=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "message": self.message,
            "status": self.status,
            "reply": self.reply,
            "created_at": self.created_at.isoformat(),
        }


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    summary = db.Column(db.String(255), default="")
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default="Draft", index=True)
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship("BlogComment", cascade="all, delete-orphan", backref="blog")

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "slug": self.slug, "summary": self.summary, "status": self.status, "views": self.views}


class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(180), nullable=False)
    role = db.Column(db.String(180), nullable=False)
    source = db.Column(db.String(120), default="")
    status = db.Column(db.String(60), default="Applied", index=True)
    applied_on = db.Column(db.String(40), default="")
    interview_at = db.Column(db.String(80), default="")
    notes = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class VisitorAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(180), nullable=False, index=True)
    ip_address = db.Column(db.String(80), default="")
    user_agent = db.Column(db.String(255), default="")
    visited_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    body = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(60), default="Admin")
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ResumeAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255), nullable=False)
    detected_skills = db.Column(db.Text, default="")
    missing_skills = db.Column(db.Text, default="")
    suggestions = db.Column(db.Text, default="")
    score = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def create_app() -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.update(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-change-this-secret"),
        SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'portfolio.db'}"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MAX_CONTENT_LENGTH=20 * 1024 * 1024,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        UPLOAD_FOLDER=str(UPLOAD_DIR),
    )
    db.init_app(flask_app)

    @flask_app.context_processor
    def inject_globals() -> dict:
        return {"current_user": current_user(), "csrf_token": session.get("csrf_token", "")}

    @flask_app.before_request
    def before_request() -> None:
        session.setdefault("csrf_token", secrets.token_urlsafe(32))
        if request.endpoint not in {"static", "uploaded_file"} and not request.path.startswith("/api"):
            db.session.add(VisitorAnalytics(page=request.path, ip_address=request.headers.get("X-Forwarded-For", request.remote_addr or ""), user_agent=(request.user_agent.string or "")[:255]))
            db.session.commit()

    register_cli(flask_app)
    register_routes(flask_app)
    return flask_app


def current_user() -> User | None:
    user_id = session.get("user_id")
    return db.session.get(User, user_id) if user_id else None


def register_cli(flask_app: Flask) -> None:
    @flask_app.cli.command("init-db")
    def init_db_command() -> None:
        init_database()
        print("Database initialized. Admin: admin@gokularasu.dev / Admin@12345")


def register_routes(flask_app: Flask) -> None:
    routes = [
        ("/", "home", home, ["GET"]), ("/register", "register", register, ["GET", "POST"]),
        ("/login", "login", login, ["GET", "POST"]), ("/logout", "logout", logout, ["GET"]),
        ("/forgot-password", "forgot_password", forgot_password, ["GET", "POST"]),
        ("/reset-password/<token>", "reset_password", reset_password, ["GET", "POST"]),
        ("/profile", "profile", profile, ["GET", "POST"]), ("/dashboard", "dashboard", dashboard, ["GET"]),
        ("/resume-analyzer", "resume_analyzer", resume_analyzer, ["GET", "POST"]),
        ("/projects", "projects", projects, ["GET"]), ("/project/add", "project_add", project_form, ["GET", "POST"]),
        ("/project/<int:project_id>/edit", "project_edit", project_form, ["GET", "POST"]),
        ("/project/<int:project_id>/delete", "project_delete", project_delete, ["POST"]),
        ("/certifications", "certifications", certifications, ["GET", "POST"]),
        ("/certification/<int:cert_id>/delete", "certification_delete", certification_delete, ["POST"]),
        ("/contact", "contact", contact, ["GET", "POST"]), ("/messages", "messages", messages, ["GET"]),
        ("/message/<int:message_id>/reply", "message_reply", message_reply, ["POST"]),
        ("/analytics", "analytics", analytics, ["GET"]), ("/blogs", "blogs", blogs, ["GET"]),
        ("/blog/add", "blog_form", blog_form, ["GET", "POST"]), ("/blog/<slug>", "blog_detail", blog_detail, ["GET", "POST"]),
        ("/blog/<int:blog_id>/edit", "blog_edit", blog_form, ["GET", "POST"]),
        ("/blog/<int:blog_id>/delete", "blog_delete", blog_delete, ["POST"]),
        ("/career-assistant", "career_assistant", career_assistant, ["GET", "POST"]),
        ("/jobs", "jobs", jobs, ["GET", "POST"]), ("/job/<int:job_id>/delete", "job_delete", job_delete, ["POST"]),
        ("/admin", "admin", admin, ["GET"]), ("/admin/users", "admin_users", admin_users, ["GET"]),
        ("/uploads/<path:filename>", "uploaded_file", uploaded_file, ["GET"]),
    ]
    for rule, endpoint, view, methods in routes:
        flask_app.add_url_rule(rule, endpoint, view, methods=methods)
    register_api_routes(flask_app)


def register_api_routes(flask_app: Flask) -> None:
    api_routes = [
        ("/api/auth/register", "api_register", api_register, ["POST"]),
        ("/api/auth/login", "api_login", api_login, ["POST"]),
        ("/api/auth/me", "api_me", api_me, ["GET"]),
        ("/api/projects", "api_projects", api_projects, ["GET", "POST"]),
        ("/api/projects/<int:project_id>", "api_project_detail", api_project_detail, ["GET", "PUT", "DELETE"]),
        ("/api/certifications", "api_certifications", api_certifications, ["GET", "POST"]),
        ("/api/contact-messages", "api_contact_messages", api_contact_messages, ["GET", "POST"]),
        ("/api/analytics", "api_analytics", api_analytics, ["GET"]),
        ("/api/career-assistant", "api_career_assistant", api_career_assistant, ["POST"]),
    ]
    for rule, endpoint, view, methods in api_routes:
        flask_app.add_url_rule(rule, endpoint, view, methods=methods)


def init_database() -> None:
    db.create_all()
    if not User.query.filter_by(email="admin@gokularasu.dev").first():
        admin_user = User(name="GOKULARASU K", email="admin@gokularasu.dev", role="admin")
        admin_user.set_password("Admin@12345")
        db.session.add(admin_user)
    if Project.query.count() == 0:
        db.session.add_all([
            Project(title="AI Resume Analyzer", description="NLP-assisted resume scoring and career suggestion system.", tech_stack="Python, Flask, SQLite, Bootstrap, NLP", github_url="https://github.com/", views=18),
            Project(title="Visitor Intelligence Dashboard", description="Portfolio analytics module with page reports and engagement metrics.", tech_stack="Flask, SQLAlchemy, Chart.js", views=31),
        ])
    if Certification.query.count() == 0:
        db.session.add(Certification(title="Python Full Stack Development", issuer="Professional Training", issue_date="2026"))
    if Blog.query.count() == 0:
        db.session.add(Blog(title="Building Career Systems Instead of Static Portfolios", slug="building-career-systems", summary="Why an intelligent portfolio can manage proof, progress, and opportunities.", content="A modern portfolio should do more than introduce a person. It should collect signals, present proof, and help its owner make better career decisions.", status="Published"))
    db.session.commit()


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not current_user():
            flash("Please login to continue.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped


def admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        user = current_user()
        if not user or user.role != "admin":
            abort(403)
        return view(*args, **kwargs)
    return wrapped


def validate_csrf() -> None:
    if request.method in {"POST", "PUT", "DELETE"} and not request.path.startswith("/api"):
        if request.form.get("csrf_token") != session.get("csrf_token"):
            abort(400, "Invalid CSRF token")


def allowed_file(filename: str, allowed: set[str]) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed


def save_upload(file_storage, folder: str, allowed: set[str]) -> str:
    if not file_storage or not file_storage.filename:
        return ""
    if not allowed_file(file_storage.filename, allowed):
        raise ValueError("Unsupported file type")
    target_dir = UPLOAD_DIR / folder
    target_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{secure_filename(file_storage.filename)}"
    file_storage.save(target_dir / filename)
    return f"{folder}/{filename}"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or secrets.token_hex(4)


def extract_resume_text(path: Path) -> str:
    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8", errors="ignore")
    return path.read_bytes().decode("latin-1", errors="ignore")


def analyze_resume_text(text: str) -> dict:
    normalized = text.lower()
    detected = sorted(skill for skill in SKILL_KEYWORDS if skill in normalized)
    target_skills = set().union(*CAREER_TRACKS.values())
    missing = sorted(target_skills.difference(detected))
    best_track = max(CAREER_TRACKS, key=lambda track: len(CAREER_TRACKS[track].intersection(detected)))
    score = min(100, int((len(detected) / max(len(target_skills), 1)) * 100) + 25)
    suggestions = [
        f"Prioritize {', '.join(missing[:5]) or 'advanced project proof'} for stronger role alignment.",
        f"Best current match: {best_track}. Add quantified project outcomes to improve recruiter scanning.",
        "Create one deployed Flask or analytics project with a short case-study blog post.",
    ]
    return {"detected": detected, "missing": missing[:10], "score": score, "suggestions": suggestions}


def analytics_summary() -> dict:
    today = datetime.utcnow().date()
    total = VisitorAnalytics.query.count()
    daily = VisitorAnalytics.query.filter(VisitorAnalytics.visited_at >= datetime.combine(today, datetime.min.time())).count()
    pages = Counter(row.page for row in VisitorAnalytics.query.all()).most_common(8)
    contacts_by_status = dict(db.session.query(ContactMessage.status, db.func.count(ContactMessage.id)).group_by(ContactMessage.status).all())
    return {"total_visitors": total, "daily_visitors": daily, "most_viewed_pages": pages, "contacts_by_status": contacts_by_status, "project_views": sum(project.views for project in Project.query.all())}


def career_reply(prompt: str) -> str:
    text = prompt.lower()
    if "interview" in text:
        return "Prepare STAR stories for projects, revise Python/SQL basics, and practice explaining one AI project from problem to deployment."
    if "skill" in text:
        return "Recommended skill path: Flask REST APIs, SQL joins, pandas analysis, GitHub documentation, and one cloud deployment on Render or PythonAnywhere."
    if "resume" in text:
        return "Keep the resume achievement-led: action verb, technology, measurable result. Add links to GitHub, live demos, certifications, and the strongest two projects."
    return "Focus on a clear target role, build proof projects, publish short technical notes, and track every application with follow-up dates."


def home():
    return render_template("home.html", projects=Project.query.order_by(Project.created_at.desc()).limit(4).all(), certifications=Certification.query.order_by(Certification.created_at.desc()).limit(4).all(), blogs=Blog.query.filter_by(status="Published").order_by(Blog.created_at.desc()).limit(3).all(), owner=User.query.filter_by(role="admin").first())


def register():
    validate_csrf()
    if request.method == "POST":
        email = request.form["email"].lower().strip()
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "danger")
        else:
            user = User(name=request.form["name"].strip(), email=email)
            user.set_password(request.form["password"])
            db.session.add(user)
            db.session.commit()
            flash("Account created. Please login.", "success")
            return redirect(url_for("login"))
    return render_template("auth.html", mode="register")


def login():
    validate_csrf()
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"].lower().strip()).first()
        if user and user.check_password(request.form["password"]):
            session["user_id"] = user.id
            flash("Welcome back.", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid email or password.", "danger")
    return render_template("auth.html", mode="login")


def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("home"))


def forgot_password():
    validate_csrf()
    token = None
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"].lower().strip()).first()
        if user:
            token = secrets.token_urlsafe(24)
            user.reset_token = token
            user.reset_expires_at = datetime.utcnow() + timedelta(hours=1)
            db.session.add(Notification(title="Password reset requested", body=f"Reset requested for {user.email}"))
            db.session.commit()
        flash("If the email exists, a reset link has been generated.", "info")
    return render_template("auth.html", mode="forgot", reset_token=token)


def reset_password(token: str):
    validate_csrf()
    user = User.query.filter_by(reset_token=token).first_or_404()
    if not user.reset_expires_at or user.reset_expires_at < datetime.utcnow():
        abort(410)
    if request.method == "POST":
        user.set_password(request.form["password"])
        user.reset_token = None
        user.reset_expires_at = None
        db.session.commit()
        flash("Password updated.", "success")
        return redirect(url_for("login"))
    return render_template("auth.html", mode="reset")


@login_required
def profile():
    validate_csrf()
    user = current_user()
    if request.method == "POST":
        for field in ["name", "headline", "bio", "skills", "education"]:
            setattr(user, field, request.form[field].strip())
        db.session.commit()
        flash("Profile updated.", "success")
    return render_template("profile.html", user=user)


@login_required
def dashboard():
    return render_template("dashboard.html", projects=Project.query.count(), certifications=Certification.query.count(), messages=ContactMessage.query.count(), blogs=Blog.query.count(), jobs=JobApplication.query.order_by(JobApplication.created_at.desc()).limit(5).all(), analytics=analytics_summary(), notifications=Notification.query.order_by(Notification.created_at.desc()).limit(6).all())


@login_required
def resume_analyzer():
    validate_csrf()
    analysis = None
    if request.method == "POST":
        try:
            stored = save_upload(request.files.get("resume"), "resumes", ALLOWED_DOCS)
            analysis = analyze_resume_text(extract_resume_text(UPLOAD_DIR / stored))
            db.session.add(ResumeAnalysis(file_name=stored, detected_skills=", ".join(analysis["detected"]), missing_skills=", ".join(analysis["missing"]), suggestions="\n".join(analysis["suggestions"]), score=analysis["score"]))
            db.session.commit()
        except ValueError as exc:
            flash(str(exc), "danger")
    return render_template("resume.html", analysis=analysis, history=ResumeAnalysis.query.order_by(ResumeAnalysis.created_at.desc()).limit(8).all())


def projects():
    return render_template("projects.html", projects=Project.query.order_by(Project.created_at.desc()).all())


@login_required
def project_form(project_id: int | None = None):
    validate_csrf()
    project = db.session.get(Project, project_id) if project_id else Project()
    if project_id and not project:
        abort(404)
    if request.method == "POST":
        for field in ["title", "description", "tech_stack", "github_url", "live_url", "status"]:
            setattr(project, field, request.form.get(field, "").strip())
        image = save_upload(request.files.get("image"), "projects", ALLOWED_IMAGES)
        if image:
            project.image_file = image
        db.session.add(project)
        db.session.commit()
        flash("Project saved.", "success")
        return redirect(url_for("projects"))
    return render_template("project_form.html", project=project)


@login_required
def project_delete(project_id: int):
    validate_csrf()
    project = db.session.get(Project, project_id) or abort(404)
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted.", "info")
    return redirect(url_for("projects"))


@login_required
def certifications():
    validate_csrf()
    if request.method == "POST":
        try:
            db.session.add(Certification(title=request.form["title"].strip(), issuer=request.form["issuer"].strip(), issue_date=request.form.get("issue_date", "").strip(), credential_url=request.form.get("credential_url", "").strip(), certificate_file=save_upload(request.files.get("certificate"), "certificates", ALLOWED_DOCS | ALLOWED_IMAGES)))
            db.session.commit()
            flash("Certification added.", "success")
        except ValueError as exc:
            flash(str(exc), "danger")
    return render_template("certifications.html", certifications=Certification.query.order_by(Certification.created_at.desc()).all())


@login_required
def certification_delete(cert_id: int):
    validate_csrf()
    cert = db.session.get(Certification, cert_id) or abort(404)
    db.session.delete(cert)
    db.session.commit()
    flash("Certification deleted.", "info")
    return redirect(url_for("certifications"))


def contact():
    validate_csrf()
    if request.method == "POST":
        msg = ContactMessage(name=request.form["name"].strip(), email=request.form["email"].strip(), subject=request.form.get("subject", "Portfolio inquiry").strip(), message=request.form["message"].strip(), ip_address=request.headers.get("X-Forwarded-For", request.remote_addr or ""))
        db.session.add(msg)
        db.session.add(Notification(title="New contact message", body=f"{msg.name} sent: {msg.subject}", category="Contact"))
        db.session.commit()
        flash("Message received. Thank you.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")


@login_required
def messages():
    return render_template("messages.html", messages=ContactMessage.query.order_by(ContactMessage.created_at.desc()).all())


@login_required
def message_reply(message_id: int):
    validate_csrf()
    msg = db.session.get(ContactMessage, message_id) or abort(404)
    msg.reply = request.form["reply"].strip()
    msg.status = "Replied"
    msg.replied_at = datetime.utcnow()
    db.session.add(Notification(title="Reply saved", body=f"Reply drafted for {msg.email}", category="Email"))
    db.session.commit()
    flash("Reply saved. Configure SMTP to send it as email.", "success")
    return redirect(url_for("messages"))


@login_required
def analytics():
    return render_template("analytics.html", analytics=analytics_summary())


def blogs():
    query = Blog.query if current_user() else Blog.query.filter_by(status="Published")
    return render_template("blogs.html", blogs=query.order_by(Blog.created_at.desc()).all())


@login_required
def blog_form(blog_id: int | None = None):
    validate_csrf()
    blog = db.session.get(Blog, blog_id) if blog_id else Blog()
    if blog_id and not blog:
        abort(404)
    if request.method == "POST":
        blog.title = request.form["title"].strip()
        blog.slug = slugify(request.form.get("slug") or blog.title)
        blog.summary = request.form.get("summary", "").strip()
        blog.content = request.form["content"].strip()
        blog.status = request.form.get("status", "Draft")
        db.session.add(blog)
        db.session.commit()
        flash("Blog saved.", "success")
        return redirect(url_for("blogs"))
    return render_template("blog_form.html", blog=blog)


def blog_detail(slug: str):
    blog = Blog.query.filter_by(slug=slug).first_or_404()
    if blog.status != "Published" and not current_user():
        abort(404)
    validate_csrf()
    if request.method == "POST":
        db.session.add(BlogComment(blog=blog, name=request.form["name"].strip(), comment=request.form["comment"].strip()))
        flash("Comment added.", "success")
    blog.views += 1
    db.session.commit()
    return render_template("blog_detail.html", blog=blog)


@login_required
def blog_delete(blog_id: int):
    validate_csrf()
    blog = db.session.get(Blog, blog_id) or abort(404)
    db.session.delete(blog)
    db.session.commit()
    flash("Blog deleted.", "info")
    return redirect(url_for("blogs"))


@login_required
def career_assistant():
    validate_csrf()
    reply = career_reply(request.form["prompt"]) if request.method == "POST" else None
    return render_template("assistant.html", reply=reply)


@login_required
def jobs():
    validate_csrf()
    if request.method == "POST":
        db.session.add(JobApplication(company=request.form["company"].strip(), role=request.form["role"].strip(), source=request.form.get("source", "").strip(), status=request.form.get("status", "Applied"), applied_on=request.form.get("applied_on", "").strip(), interview_at=request.form.get("interview_at", "").strip(), notes=request.form.get("notes", "").strip()))
        db.session.commit()
        flash("Job application tracked.", "success")
    return render_template("jobs.html", jobs=JobApplication.query.order_by(JobApplication.created_at.desc()).all())


@login_required
def job_delete(job_id: int):
    validate_csrf()
    job = db.session.get(JobApplication, job_id) or abort(404)
    db.session.delete(job)
    db.session.commit()
    flash("Job deleted.", "info")
    return redirect(url_for("jobs"))


@admin_required
def admin():
    return render_template("admin.html", users=User.query.count(), analytics=analytics_summary())


@admin_required
def admin_users():
    return render_template("admin_users.html", users=User.query.order_by(User.created_at.desc()).all())


def uploaded_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)


def json_payload() -> dict:
    return request.get_json(silent=True) or {}


def api_user_required() -> User:
    user = current_user()
    if not user:
        abort(401)
    return user


def api_register():
    data = json_payload()
    if User.query.filter_by(email=data.get("email", "").lower()).first():
        return jsonify({"error": "Email already registered"}), 409
    user = User(name=data["name"], email=data["email"].lower())
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


def api_login():
    data = json_payload()
    user = User.query.filter_by(email=data.get("email", "").lower()).first()
    if not user or not user.check_password(data.get("password", "")):
        return jsonify({"error": "Invalid credentials"}), 401
    session["user_id"] = user.id
    return jsonify({"message": "Logged in", "user": user.to_dict()})


def api_me():
    return jsonify(api_user_required().to_dict())


def api_projects():
    if request.method == "POST":
        api_user_required()
        data = json_payload()
        project = Project(title=data["title"], description=data["description"], tech_stack=data.get("tech_stack", ""), github_url=data.get("github_url", ""), live_url=data.get("live_url", ""), status=data.get("status", "Published"))
        db.session.add(project)
        db.session.commit()
        return jsonify(project.to_dict()), 201
    return jsonify([project.to_dict() for project in Project.query.order_by(Project.created_at.desc()).all()])


def api_project_detail(project_id: int):
    project = db.session.get(Project, project_id) or abort(404)
    if request.method == "GET":
        project.views += 1
        db.session.commit()
        return jsonify(project.to_dict())
    api_user_required()
    if request.method == "DELETE":
        db.session.delete(project)
        db.session.commit()
        return jsonify({"message": "Deleted"})
    for field, value in json_payload().items():
        if field in {"title", "description", "tech_stack", "github_url", "live_url", "status"}:
            setattr(project, field, value)
    db.session.commit()
    return jsonify(project.to_dict())


def api_certifications():
    if request.method == "POST":
        api_user_required()
        data = json_payload()
        cert = Certification(title=data["title"], issuer=data["issuer"], issue_date=data.get("issue_date", ""), credential_url=data.get("credential_url", ""))
        db.session.add(cert)
        db.session.commit()
        return jsonify(cert.to_dict()), 201
    return jsonify([cert.to_dict() for cert in Certification.query.order_by(Certification.created_at.desc()).all()])


def api_contact_messages():
    if request.method == "POST":
        data = json_payload()
        msg = ContactMessage(name=data["name"], email=data["email"], subject=data.get("subject", ""), message=data["message"])
        db.session.add(msg)
        db.session.commit()
        return jsonify(msg.to_dict()), 201
    api_user_required()
    return jsonify([msg.to_dict() for msg in ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()])


def api_analytics():
    api_user_required()
    return jsonify(analytics_summary())


def api_career_assistant():
    api_user_required()
    return jsonify({"reply": career_reply(json_payload().get("prompt", ""))})


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        init_database()
    app.run(debug=True)
