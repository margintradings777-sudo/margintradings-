from pathlib import Path
import os
import dj_database_url

# --------------------------------------------------

# BASE

# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------

# SECURITY

# --------------------------------------------------

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-change-this")
DEBUG = False

ALLOWED_HOSTS = [
"margintradings-backend.onrender.com",
"margintradings.in",
"[www.margintradings.in](http://www.margintradings.in)",
]

# --------------------------------------------------

# APPS

# --------------------------------------------------

INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",

```
# third-party
"rest_framework",
"corsheaders",
"import_export",

# local apps
"tables",
```

]

# --------------------------------------------------

# MIDDLEWARE (ORDER IS VERY IMPORTANT)

# --------------------------------------------------

MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"whitenoise.middleware.WhiteNoiseMiddleware",

```
"corsheaders.middleware.CorsMiddleware",

"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",

"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
```

]

# --------------------------------------------------

# URLS / WSGI

# --------------------------------------------------

ROOT_URLCONF = "main.urls"

TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [BASE_DIR / "templates"],
"APP_DIRS": True,
"OPTIONS": {
"context_processors": [
"django.template.context_processors.debug",
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
],
},
},
]

WSGI_APPLICATION = "main.wsgi.application"

# --------------------------------------------------

# DATABASE (PostgreSQL — Render)

# --------------------------------------------------

DATABASES = {
"default": dj_database_url.config(
default=os.environ.get("DATABASE_URL"),
conn_max_age=600,
ssl_require=True,
)
}

# --------------------------------------------------

# AUTH / PASSWORDS

# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
{"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
{"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
{"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
{"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------

# LANGUAGE / TIME

# --------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------

# STATIC FILES

# --------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------------------

# DEFAULTS

# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------

# 🔥 CORS + CSRF + SESSION (MAIN FIX)

# --------------------------------------------------

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
"[https://margintradings.in](https://margintradings.in)",
"[https://www.margintradings.in](https://www.margintradings.in)",
"[https://696cc85c5cbdd589e335890c--friendly-madeleine-935be3.netlify.app](https://696cc85c5cbdd589e335890c--friendly-madeleine-935be3.netlify.app)",
]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

SESSION_ENGINE = "django.contrib.sessions.backends.db"

SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True

# --------------------------------------------------

# REST FRAMEWORK (Session based auth)

# --------------------------------------------------

REST_FRAMEWORK = {
"DEFAULT_AUTHENTICATION_CLASSES": [
"rest_framework.authentication.SessionAuthentication",
],
"DEFAULT_PERMISSION_CLASSES": [
"rest_framework.permissions.AllowAny",
],
}

# --------------------------------------------------

# LOGGING (OPTIONAL — SAFE)

# --------------------------------------------------

LOGGING = {
"version": 1,
"disable_existing_loggers": False,
"handlers": {
"console": {"class": "logging.StreamHandler"},
},
"root": {
"handlers": ["console"],
"level": "INFO",
},
}
