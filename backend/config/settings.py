import os
from pathlib import Path
from datetime import timedelta
import dj_database_url
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.getenv("DJANGO_SECRET_KEY","unsafe-dev-key-change-me")
DEBUG=os.getenv("DJANGO_DEBUG","false").lower()=="true"
ALLOWED_HOSTS=[x.strip() for x in os.getenv("ALLOWED_HOSTS","*").split(",") if x.strip()]
FRONTEND_URL=os.getenv("FRONTEND_URL","http://localhost:5173")
INSTALLED_APPS=["django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles","corsheaders","rest_framework","rest_framework_simplejwt","shop"]
MIDDLEWARE=["django.middleware.security.SecurityMiddleware","whitenoise.middleware.WhiteNoiseMiddleware","corsheaders.middleware.CorsMiddleware","django.contrib.sessions.middleware.SessionMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware","django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware","django.middleware.clickjacking.XFrameOptionsMiddleware"]
ROOT_URLCONF="config.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.debug","django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION="config.wsgi.application"
DATABASES={"default":dj_database_url.config(default=f"sqlite:///{BASE_DIR/'db.sqlite3'}",conn_max_age=600)}
AUTH_PASSWORD_VALIDATORS=[{"NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},{"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"}]
LANGUAGE_CODE="en-us"; TIME_ZONE="Asia/Kathmandu"; USE_I18N=True; USE_TZ=True
STATIC_URL="static/"; STATIC_ROOT=BASE_DIR/"staticfiles"
STORAGES={"staticfiles":{"BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage"},"default":{"BACKEND":"django.core.files.storage.FileSystemStorage"}}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
CORS_ALLOWED_ORIGINS=[x.strip() for x in os.getenv("CORS_ALLOWED_ORIGINS",FRONTEND_URL).split(",") if x.strip()]
CSRF_TRUSTED_ORIGINS=[x.strip() for x in os.getenv("CSRF_TRUSTED_ORIGINS",FRONTEND_URL).split(",") if x.strip()]
REST_FRAMEWORK={"DEFAULT_AUTHENTICATION_CLASSES":("rest_framework_simplejwt.authentication.JWTAuthentication",),"DEFAULT_PERMISSION_CLASSES":("rest_framework.permissions.AllowAny",),"DEFAULT_RENDERER_CLASSES":("rest_framework.renderers.JSONRenderer",)}
SIMPLE_JWT={"ACCESS_TOKEN_LIFETIME":timedelta(minutes=45),"REFRESH_TOKEN_LIFETIME":timedelta(days=7)}
IMAGEKIT_PUBLIC_KEY=os.getenv("IMAGEKIT_PUBLIC_KEY",""); IMAGEKIT_PRIVATE_KEY=os.getenv("IMAGEKIT_PRIVATE_KEY","")
