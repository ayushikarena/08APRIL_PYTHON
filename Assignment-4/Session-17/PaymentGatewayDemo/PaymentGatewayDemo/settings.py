"""
============================================================
PaymentGatewayDemo/settings.py
============================================================
This is the MAIN CONFIGURATION FILE for the entire Django project.

Think of it as the "control center" — it tells Django:
  - Which apps are installed
  - Where to find templates (HTML files)
  - Which database to use
  - Where to read secret API keys from
  - Language, timezone, and many other settings

We use 'python-decouple' to read sensitive values from .env file.
This means NO passwords or API keys are written in this file.
============================================================
"""

from pathlib import Path

# python-decouple's 'config' function reads values from the .env file
# Usage: config('KEY_NAME', default='fallback_value', cast=data_type)
from decouple import config

# ─── BASE DIRECTORY ──────────────────────────────────────────────────────────
# Path(__file__) = full path to this settings.py file
# .resolve()     = makes it an absolute path (no ".." shortcuts)
# .parent.parent = go up two folders (settings.py → PaymentGatewayDemo/ → project root)
# Result: BASE_DIR = e:/Tops-Course/TASK/.../PaymentGatewayDemo/
BASE_DIR = Path(__file__).resolve().parent.parent


# ─── SECURITY SETTINGS ───────────────────────────────────────────────────────
# SECRET_KEY is read from .env file — NEVER hardcode this!
# Django uses it to sign cookies, tokens, and password reset links.
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me-in-production')

# DEBUG=True shows friendly error pages with full stack traces.
# ALWAYS set DEBUG=False in a real production server.
# cast=bool converts the string "True" from .env to Python True
DEBUG = config('DEBUG', default=True, cast=bool)

# ALLOWED_HOSTS = list of hostnames Django will respond to.
# For local development, we allow localhost and 127.0.0.1
# The split(',') converts the comma-separated string from .env into a Python list
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost').split(',')


# ─── INSTALLED APPS ──────────────────────────────────────────────────────────
# Django works like LEGO blocks — each "app" adds features.
# We must list EVERY app here to activate it.
INSTALLED_APPS = [
    # ── Django's built-in apps ────────────────────────────────────────────────
    'django.contrib.admin',         # The /admin/ panel for managing data
    'django.contrib.auth',          # User login/logout/authentication system
    'django.contrib.contenttypes',  # Tracks all models in all apps
    'django.contrib.sessions',      # Manages user sessions (shopping cart, login state)
    'django.contrib.messages',      # Flash messages (success/error notifications)
    'django.contrib.staticfiles',   # Serves CSS, JS, image files

    # ── Our custom app ────────────────────────────────────────────────────────
    'payments',  # Our app that handles ticket booking, food orders, and payments
]


# ─── MIDDLEWARE ──────────────────────────────────────────────────────────────
# Middleware = code that runs on EVERY request before it reaches your view.
# Think of it as "security guards" at the entrance.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # Adds security headers (HTTPS, etc.)
    'django.contrib.sessions.middleware.SessionMiddleware',     # Enables sessions (login state)
    'django.middleware.common.CommonMiddleware',                 # Adds trailing slashes, etc.
    'django.middleware.csrf.CsrfViewMiddleware',                # CSRF protection (prevents fake form submissions)
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Links requests to logged-in users
    'django.contrib.messages.middleware.MessageMiddleware',     # Enables flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Prevents your site from being embedded in iframes
]


# ─── URL CONFIGURATION ───────────────────────────────────────────────────────
# Tells Django which file contains the main URL patterns (routing table)
ROOT_URLCONF = 'PaymentGatewayDemo.urls'


# ─── TEMPLATES CONFIGURATION ─────────────────────────────────────────────────
# Tells Django WHERE to look for HTML template files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # DIRS = list of folders to search for templates
        # BASE_DIR / 'templates' = our project-level templates/ folder
        'DIRS': [BASE_DIR / 'templates'],

        # APP_DIRS=True also looks for templates inside each app's templates/ folder
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                # These inject variables into EVERY template automatically:
                'django.template.context_processors.request',  # Adds 'request' object
                'django.contrib.auth.context_processors.auth',  # Adds 'user' object
                'django.contrib.messages.context_processors.messages',  # Adds flash messages
            ],
        },
    },
]


# ─── WSGI APPLICATION ────────────────────────────────────────────────────────
# WSGI = Web Server Gateway Interface
# This is how a production web server (like Gunicorn) talks to Django
WSGI_APPLICATION = 'PaymentGatewayDemo.wsgi.application'


# ─── DATABASE CONFIGURATION ──────────────────────────────────────────────────
# We use SQLite — it stores everything in a single file (db.sqlite3).
# Perfect for development! No separate database server needed.
# For production, switch to PostgreSQL or MySQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # File will be created here automatically
    }
}


# ─── PASSWORD VALIDATION ─────────────────────────────────────────────────────
# Rules for creating strong passwords in the admin panel
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ─── INTERNATIONALISATION ────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'     # English language
TIME_ZONE = 'Asia/Kolkata'  # India Standard Time (IST) for correct timestamps
USE_I18N = True             # Enable translations
USE_TZ = True               # Store dates in UTC, display in TIME_ZONE


# ─── STATIC FILES ────────────────────────────────────────────────────────────
# Static files = CSS, JavaScript, images that don't change per user
STATIC_URL = '/static/'  # URL prefix for static files


# ─── DEFAULT AUTO FIELD ──────────────────────────────────────────────────────
# When Django creates a model, every table needs a primary key (unique ID).
# BigAutoField = auto-incrementing 64-bit integer (good for large datasets)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# PAYMENT GATEWAY SETTINGS
# ============================================================
# All values are read from .env — no secrets in this file!
# ============================================================

# ─── PAYTM SETTINGS (Task 2) ─────────────────────────────────────────────────
PAYTM_MERCHANT_ID    = config('PAYTM_MERCHANT_ID',    default='')
PAYTM_MERCHANT_KEY   = config('PAYTM_MERCHANT_KEY',   default='')
PAYTM_WEBSITE        = config('PAYTM_WEBSITE',        default='WEBSTAGING')
PAYTM_CHANNEL_ID     = config('PAYTM_CHANNEL_ID',     default='WEB')
PAYTM_INDUSTRY_TYPE  = config('PAYTM_INDUSTRY_TYPE',  default='Retail')
PAYTM_CALLBACK_URL   = config('PAYTM_CALLBACK_URL',   default='http://127.0.0.1:8000/payment-callback/')
PAYTM_ENVIRONMENT    = config('PAYTM_ENVIRONMENT',    default='STAGING')

# ─── STRIPE SETTINGS (Task 4) ────────────────────────────────────────────────
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY', default='')
STRIPE_SECRET_KEY      = config('STRIPE_SECRET_KEY',      default='')
STRIPE_WEBHOOK_SECRET  = config('STRIPE_WEBHOOK_SECRET',  default='')

# ─── PAYPAL SETTINGS (Task 5) ────────────────────────────────────────────────
PAYPAL_CLIENT_ID     = config('PAYPAL_CLIENT_ID',     default='')
PAYPAL_CLIENT_SECRET = config('PAYPAL_CLIENT_SECRET', default='')
PAYPAL_MODE          = config('PAYPAL_MODE',          default='sandbox')
PAYPAL_RETURN_URL    = config('PAYPAL_RETURN_URL',    default='http://127.0.0.1:8000/paypal/success/')
PAYPAL_CANCEL_URL    = config('PAYPAL_CANCEL_URL',    default='http://127.0.0.1:8000/paypal/cancel/')
