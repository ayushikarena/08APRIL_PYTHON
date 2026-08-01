# SmartCityHub

SmartCityHub is a complete Django project that unifies multiple city services into a single platform. It features a professional Bootstrap 5 responsive UI and includes four main applications:

## Features
1. **Restaurant Finder**: Search for restaurants by cuisine and location (similar to Zomato).
2. **Movie Booking Authentication**: Secure user registration, login, and OTP verification (3-minute expiry).
3. **Shopping Profile**: Manage your personal profile, contact information, and profile picture.
4. **Cab Booking Map**: Interactive Google Maps integration for selecting and saving pickup locations.

## Technologies Used
- Python 3.x
- Django 5.x
- SQLite (Default Database)
- HTML, CSS, JavaScript
- Bootstrap 5
- Google Maps JavaScript API

## Installation Steps

1. **Clone the repository** (if downloaded from GitHub):
   ```bash
   git clone <repository_url>
   cd SmartCityHub
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000` in your web browser.

## Configuration

### Google Maps API
To enable the cab booking map feature, you need a Google Maps API Key.
Open `templates/map.html` and replace `YOUR_GOOGLE_MAPS_API_KEY` with your actual API key:
```html
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&libraries=places"></script>
```

### Email Settings (for OTP)
By default, the project uses the console email backend which prints OTPs to your terminal. To use a real email service, update `SmartCityHub/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## Deployment Steps (PythonAnywhere)

1. Sign up/Log in to [PythonAnywhere](https://www.pythonanywhere.com/).
2. Upload your code to PythonAnywhere (e.g., using GitHub or the Files tab).
3. Open a Bash console and install requirements in a virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv
   pip install -r requirements.txt
   ```
4. Run migrations and collect static files:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
5. Go to the "Web" tab, add a new web app, choose manual configuration.
6. Set the Virtualenv path to your created virtual environment.
7. Edit the WSGI configuration file to point to your `SmartCityHub` project.
8. Set up Static files mapping (URL `/static/` -> Directory `/path/to/staticfiles/`).
9. Set up Media files mapping (URL `/media/` -> Directory `/path/to/media/`).
10. Reload the web app.

## GitHub Push Commands

To initialize a new repository and push:
```bash
git init
git add .
git commit -m "Initial commit for SmartCityHub"
git branch -M main
git remote add origin https://github.com/yourusername/SmartCityHub.git
git push -u origin main
```
