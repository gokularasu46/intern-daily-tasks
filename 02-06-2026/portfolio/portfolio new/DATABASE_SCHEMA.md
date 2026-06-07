# Database Schema

The app uses SQLAlchemy and defaults to SQLite. Set `DATABASE_URL` to a MySQL connection string for MySQL deployment.

## Tables

- `user`: authentication, profile, role, password hash, reset token, skills, education.
- `project`: project CRUD, uploaded image filename, links, status, view statistics.
- `certification`: certificate records, issuer, date, credential URL, uploaded file.
- `contact_message`: visitor messages, reply text, status, IP, timestamps.
- `blog`: blog posts, slug, summary, content, status, views.
- `blog_comment`: comments attached to blog posts.
- `job_application`: company, role, status, source, interview schedule, offer tracking notes.
- `visitor_analytics`: page path, IP, user agent, timestamp.
- `notification`: admin alerts, email/contact notification placeholders.
- `resume_analysis`: uploaded resume path, detected skills, missing skills, score, suggestions.

Security features include password hashing with Werkzeug, session cookies, CSRF tokens on HTML forms, SQLAlchemy query binding for SQL injection prevention, and upload extension validation.
