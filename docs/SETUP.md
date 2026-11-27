# Sonika setup and deployment

## Local setup

### Backend
1. Use Python 3.12+.
2. `cd backend`, create and activate a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Copy `.env.example` to `.env`; set a strong `DJANGO_SECRET_KEY`. SQLite is used automatically if DATABASE_URL is omitted.
5. Run `python manage.py migrate`, then `python manage.py createsuperuser`, then `python manage.py runserver`.

### Frontend
1. In another terminal, `cd frontend`.
2. Run `npm install`.
3. Copy `.env.example` to `.env` and set `VITE_API_URL=http://127.0.0.1:8000/api`.
4. Run `npm run dev`.

## Render backend and PostgreSQL
1. Create a Render Blueprint from this repository and review the service settings before confirming.
2. The Blueprint creates only the Django web service. It deliberately does not provision a database automatically, so you can choose your own PostgreSQL provider and avoid an unexpected charge or expiring free database.
3. Create a PostgreSQL database with your preferred provider (for example, Render PostgreSQL or Neon), then add its connection string as the Render `DATABASE_URL` environment variable. Check the provider's current free-tier limits, expiry and backup policy before using it for business data.
4. Set `FRONTEND_URL` and `CORS_ALLOWED_ORIGINS` to the exact Vercel URL (including https://).
5. Set `IMAGEKIT_PUBLIC_KEY` and `IMAGEKIT_PRIVATE_KEY` after creating the separate ImageKit account. Keep the private key only in Render.
6. Optionally set `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`, and `DJANGO_SUPERUSER_PASSWORD` in Render before first deploy. The build command creates that admin once; it will not overwrite an existing account. Remove the password environment variable after the first successful deployment.
7. Health check: `/api/health/`.

## Vercel frontend
1. Import the repository into Vercel. Keep project root at repository root.
2. Root `vercel.json` builds `frontend` and publishes `frontend/dist`.
3. Set `VITE_API_URL=https://YOUR-RENDER-SERVICE.onrender.com/api` and redeploy.

## ImageKit
Create a separate ImageKit account. Add the public and private keys to Render only. The admin obtains a short-lived signed upload token from Django, then uploads directly to ImageKit. Never expose the private key or commit credentials.

## Admin dashboard
Visit `/admin/login` on the Vercel site. Sign in with a Django staff/superuser account. The dashboard manages products, categories, shop settings/map, About content and FAQs. Django's built-in admin is at `/django-admin/`.

## Google Maps
In Admin → Shop settings, paste a Google Maps embed URL (Google Maps → Share → Embed a map) in the Google Maps URL field to display the interactive map. A regular share URL works for directions but is not embeddable. Address, coordinates, contact numbers and opening hours are editable there.

## Before launch
- Use a strong unique Django secret key and keep DEBUG=false.
- Restrict ALLOWED_HOSTS and CORS to actual domains.
- Verify admin CRUD, image uploads, map embed and product browsing on deployed services.
- Back up PostgreSQL regularly and confirm the provider's data retention and recovery options.
