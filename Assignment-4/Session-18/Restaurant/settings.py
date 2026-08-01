"""
Django settings for the Maps and Geolocation student assignment project.
This file contains the configuration for database, templates, static files, and APIs.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-student-maps-assignment-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
# We include 'django.contrib.staticfiles' for styling and our custom 'app' application.
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Our custom app containing views and templates
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Look for templates in app/templates/
        'DIRS': [BASE_DIR / 'app' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

# Database
# Using simple SQLite database for beginner project.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'app' / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================================
# Google Maps and Geolocation Settings
# ==========================================
# Instructions to enable APIs in Google Cloud Console:
# 1. Go to Google Cloud Console (https://console.cloud.google.com/).
# 2. Create a project (or select an existing one).
# 3. Go to API & Services -> Library.
# 4. Search for "Geocoding API" and click "Enable".
# 5. Search for "Maps Embed API" and click "Enable".
# 6. Go to API & Services -> Credentials to create/copy your API key.
# 7. Replace "YOUR_API_KEY" below with your actual API key.
GOOGLE_MAPS_API_KEY = "AIzaSyDIKHdUtvHkx0_AI4fKYGnG2PLfskmC1Z0"
