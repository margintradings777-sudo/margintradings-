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
    "www.margintradings.in",
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

    # third-party
    "rest_framework",
    "corsheaders",
    "import_export",

    # local apps
    "tables",
]

# --------------------------------------------------
# MIDDLEWARE (ORDER VERY IMPORTANT)
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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
# DATABASE (PostgreSQL - Render)
# --------------------------------------------------

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# --------------------------------------------------
# PASSWORD VALIDATION
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
# RENDER / HTTPS FIX
# --------------------------------------------------

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

# --------------------------------------------------
# SESSION FIX (LOGIN ISSUE SOLVED)
# --------------------------------------------------

SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True

# --------------------------------------------------
# CSRF FIX (REACT + DJANGO)
# --------------------------------------------------

CSRF_TRUSTED_ORIGINS = [
    "https://margintradings.in",
    "https://www.margintradings.in",
    "https://696cc85c5cbdd589e335890c--friendly-madeleine-935be3.netlify.app",
]

CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False

# --------------------------------------------------
# CORS FIX
# --------------------------------------------------

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "https://margintradings.in",
    "https://www.margintradings.in",
    "https://696cc85c5cbdd589e335890c--friendly-madeleine-935be3.netlify.app",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# --------------------------------------------------
# REST FRAMEWORK
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
# LOGGING
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
