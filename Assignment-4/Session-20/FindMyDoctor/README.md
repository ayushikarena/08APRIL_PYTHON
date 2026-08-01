# FoodieFinder - Django Restaurant Search & Discovery Web App

A beginner-friendly, full-stack Python Django web application developed for a college assignment capstone project.

## 📌 Project Overview
FoodieFinder allows users to register, log in, manage their personal profile with custom profile picture uploads, search and filter nearby restaurants by cuisine and location, receive a 6-digit email OTP for secure password recovery, and view interactive pins on Google Maps with automatic reverse geocoding address lookup.

---

## ✨ Features
1. **User Authentication & Security**:
   - User Registration (Username, First Name, Last Name, Email, Password verification)
   - Secure Login & Logout with Django Authentication
   - Forgot Password module with random 6-digit OTP sent via email
   - 3-Minute OTP expiration rule and verification logic

2. **User Profile Management**:
   - Update user details (Name, Email, Phone, Address)
   - Profile picture upload with ImageField (displays default avatar if none uploaded)

3. **Restaurant Directory & Search**:
   - Search restaurants by Cuisine (Indian, Italian, Japanese, Mexican, American, Chinese)
   - Search restaurants by Location (Downtown, Westside, Eastside, Uptown)
   - Displays matching results using Bootstrap 5 cards
   - Displays "No restaurants found" message if no match exists

4. **Google Maps & Geolocation Integration**:
   - HTML5 Geolocation API to auto-detect browser location
   - Interactive Google Maps pin marker
   - Reverse Geocoding API to display Latitude, Longitude, and formatted address on pin click

5. **Student Dashboard**:
   - Profile summary, activity list, quick metrics, and navigation shortcuts

6. **Admin Panel**:
   - Registered models (`UserProfile`, `Restaurant`, `OTPVerification`) with search fields and list filters.

---

## 🛠️ Technologies Used
- **Backend**: Python 3.x, Django 4.2+, SQLite3
- **Frontend**: HTML5, CSS3 (`static/css/style.css`), Bootstrap 5 CDN, Bootstrap Icons CDN
- **JavaScript**: Vanilla JS (`static/js/map.js`)
- **APIs**: Google Maps JavaScript API, Browser Geolocation API, Google Geocoding API

---

## 📂 Project Directory Structure

```
FindMyDoctor/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── seed_data.py
├── restaurant_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── restaurants/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── map.js
│   └── images/
│       └── default_profile.png
└── templates/
    ├── base.html
    ├── navbar.html
    ├── footer.html
    ├── home.html
    ├── register.html
    ├── login.html
    ├── forgot_password.html
    ├── otp_verify.html
    ├── reset_password.html
    ├── dashboard.html
    ├── profile.html
    ├── restaurant_search.html
    └── map.html
```

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure Python 3.8+ and pip are installed on your system.

### 2. Install Dependencies
Open terminal/command prompt in the project root folder and run:
```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations
Create the SQLite database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin Superuser (Optional)
To log in to the Django Admin panel:
```bash
python manage.py createsuperuser
```

### 5. Seed Sample Restaurant Data
Populate the database with dummy restaurants:
```bash
python seed_data.py
```

### 6. Start the Development Server
```bash
python manage.py runserver
```
Open your browser and navigate to: `http://127.0.0.1:8000/`

---

## 🔑 Google Maps API Key Setup
1. Get a Google Maps API Key from [Google Cloud Console](https://console.cloud.google.com/).
2. Enable **Maps JavaScript API** and **Geocoding API**.
3. Open `templates/map.html` and replace `YOUR_GOOGLE_MAPS_API_KEY` on line 57 with your key:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_ACTUAL_API_KEY&callback=initMap&async=defer" async defer></script>
```

---

## 📧 Email Backend Configuration (OTP)

### Testing Mode (Console Email)
By default in `restaurant_project/settings.py`, the console email backend is configured:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
When a user requests a password reset OTP, the 6-digit OTP code will print directly in your terminal command line output.

### Production Mode (Gmail SMTP)
To send actual emails to users' inboxes via Gmail, update `restaurant_project/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_gmail_app_password'
```

---

## ☁️ PythonAnywhere Deployment Guide

1. **Sign up**: Create an account on [PythonAnywhere](https://www.pythonanywhere.com/).
2. **Open Bash Console**: Pull your code or upload project files.
3. **Set up Virtual Environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```
4. **Static Files Collection**:
   ```bash
   python manage.py collectstatic
   ```
5. **Configure Web App**:
   - Go to the **Web** tab.
   - Set **Source Code Path**: `/home/yourusername/FindMyDoctor`
   - Set **Virtualenv Path**: `/home/yourusername/.virtualenvs/myenv`
   - Edit **WSGI Configuration File**:
     ```python
     import os
     import sys
     path = '/home/yourusername/FindMyDoctor'
     if path not in sys.path:
         sys.path.append(path)
     os.environ['DJANGO_SETTINGS_MODULE'] = 'restaurant_project.settings'
     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```
6. **Set Static & Media Mappings**:
   - URL: `/static/` -> Path: `/home/yourusername/FindMyDoctor/staticfiles`
   - URL: `/media/` -> Path: `/home/yourusername/FindMyDoctor/media`
7. Click **Reload yourusername.pythonanywhere.com**.

---

## 🐙 Git Commands to Push to GitHub

Run these commands in your project terminal to push code to your personal GitHub repository:

```bash
# Initialize git repository
git init

# Add all project files
git add .

# Create initial commit
git commit -m "Initial commit of Django Restaurant Finder assignment project"

# Rename branch to main
git branch -M main

# Link your remote GitHub repository (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push code to GitHub
git push -u origin main
```

---

## 📸 Screenshots Placeholder
- **Homepage**: `[Insert Homepage Screenshot]`
- **Restaurant Search**: `[Insert Restaurant Search Screenshot]`
- **Google Maps Explorer**: `[Insert Google Maps Screenshot]`
- **Dashboard**: `[Insert Dashboard Screenshot]`
- **OTP Verification**: `[Insert OTP Verification Screenshot]`

---

## 🔮 Future Improvements
- Add online restaurant table booking system.
- Add user reviews and star rating submission module.
- Add payment gateway integration for food orders.
