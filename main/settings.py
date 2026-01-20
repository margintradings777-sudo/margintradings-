from pathlib import Path
import os
import dj_database_url

# =========================
# BASE
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# SECURITY
# =========================
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-secret-key")

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "margintradings.in",
    "www.margintradings.in",
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'django_filters',
    'import_export',

    'apis',
    'tables',
]

# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URL / WSGI
# =========================
ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# =========================
# DATABASE (POSTGRES - RENDER)
# =========================
DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =========================
# REST FRAMEWORK
# =========================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# =========================
# CORS / CSRF
# =========================
CORS_ALLOWED_ORIGINS = [
    "https://margintradings.in",
    "https://www.margintradings.in",
    "https://margintradings-backend.onrender.com",
]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
CORS_ALLOW_CREDENTIALS = True

# =========================
# STATIC FILES
# =========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# DEFAULT PK
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

IMPORT_EXPORT_USE_TRANSACTIONS = True
