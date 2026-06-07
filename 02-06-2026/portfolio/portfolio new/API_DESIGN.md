# REST API Design

Base URL: `/api`

Authentication uses the same secure Flask session as the web app. Login once with `/api/auth/login`, then call protected endpoints with the returned session cookie.

## Authentication

- `POST /api/auth/register`
  - Body: `{ "name": "GOKULARASU K", "email": "user@example.com", "password": "secret" }`
- `POST /api/auth/login`
  - Body: `{ "email": "admin@gokularasu.dev", "password": "Admin@12345" }`
- `GET /api/auth/me`
  - Protected. Returns current user profile.

## Projects

- `GET /api/projects`
- `POST /api/projects`
- `GET /api/projects/<id>`
- `PUT /api/projects/<id>`
- `DELETE /api/projects/<id>`

Fields: `title`, `description`, `tech_stack`, `github_url`, `live_url`, `status`.

## Certifications

- `GET /api/certifications`
- `POST /api/certifications`

Fields: `title`, `issuer`, `issue_date`, `credential_url`.

## Contact Messages

- `POST /api/contact-messages`
- `GET /api/contact-messages`

Fields: `name`, `email`, `subject`, `message`.

## Analytics

- `GET /api/analytics`

Returns total visitors, daily visitors, most viewed pages, contact status counts, and project views.

## Career Assistant

- `POST /api/career-assistant`

Body: `{ "prompt": "How do I prepare for interviews?" }`
