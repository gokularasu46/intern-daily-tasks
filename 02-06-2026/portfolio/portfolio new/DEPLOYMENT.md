# Deployment Guide

## Local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask --app app init-db
flask --app app run --debug
```

Default admin:

- Email: `admin@gokularasu.dev`
- Password: `Admin@12345`

## GitHub

```bash
git init
git add .
git commit -m "Build AI career portfolio system"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Render

1. Create a new Web Service from the GitHub repository.
2. Build command: `pip install -r requirements.txt`
3. Start command: `gunicorn app:app`
4. Add environment variables from `.env.example`.
5. Run `flask --app app init-db` in the Render shell after first deploy.

## PythonAnywhere

1. Upload the project folder.
2. Create a virtual environment and install `requirements.txt`.
3. Configure the WSGI file to import `app` from `app.py`.
4. Set `SECRET_KEY` in the web app environment.
5. Run `flask --app app init-db` from a Bash console.

## MySQL

Install a MySQL driver, then set:

```bash
DATABASE_URL=mysql+pymysql://user:password@host/database
```

Then run:

```bash
flask --app app init-db
```
