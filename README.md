# Ashes to New Detailing Monorepo

This repository contains the frontend and backend for **Ashes to New Detailing LLC**.

## Project Structure

- `backend/` – Django REST API
- `frontend/` – React 18 + Vite + TypeScript + Tailwind CSS

## Backend Setup

```bash
cd backend/ashes_api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r ../../requirements.txt
python manage.py migrate
python manage.py seed_initial_data
python manage.py runserver  # http://localhost:8000
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev  # http://localhost:5173
```

## Environment

- Copy `.env.example` to `.env` in `backend/ashes_api` and adjust values if needed.
- `SECRET_KEY`, `DEBUG`, and database variables are supported. SQLite is the default.

## CORS

The backend allows requests from `http://localhost:5173` and `http://127.0.0.1:5173`.

## Admin

Run `python manage.py createsuperuser` inside `backend/ashes_api` to create an admin account. All services, packages, add-ons, and settings can be edited in the Django admin.

## Deployment

For production, set `DEBUG=False` and provide a strong `SECRET_KEY`. Configure `ALLOWED_HOSTS` and use a production-ready server (e.g., Gunicorn) behind a reverse proxy. Build the frontend with `npm run build` and serve the files via a static host.

