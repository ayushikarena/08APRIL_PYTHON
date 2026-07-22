# MyPlaylistApp 🎵

This is a simple Django web application built as an academic assignment. It allows administrators to create and manage music or video playlists (including cover images) from the Django Admin panel, and allows users to browse playlists and view detailed information about each playlist.

---

## Project Overview

* **Developer:** Student
* **Framework:** Django (Python)
* **Database:** SQLite (default Django database)
* **Frontend:** Standard HTML5 and custom CSS (no external frameworks like Bootstrap, Tailwind, or React)
* **Design Philosophy:** Keep it clean, simple, and easy to understand for beginners.

---

## Features

1. **Home Page:** A simple welcoming landing page introducing the application.
2. **Playlist List Page:** Displays a list of all playlists with their title, short description, and upload cover photo.
3. **Playlist Detail Page:** Shows full-size cover photo, title, creation date, and detailed description.
4. **Admin Panel:** Enables adding, editing, and deleting playlists with cover images.
5. **Custom CSS:** Basic custom styled responsive layout without any external frameworks.
6. **JSON API Endpoint:** A simple built-in JSON API endpoint (`/api/playlists/`) returning all playlists for external apps.

---

## Project Structure

```text
MyPlaylistApp/
├── manage.py                # Django CLI tool
├── db.sqlite3               # SQLite database file
├── requirements.txt         # Project dependencies
├── MyPlaylistApp/           # Project configuration folder
│   ├── __init__.py
│   ├── settings.py          # Django project settings
│   ├── urls.py              # Main URL router
│   └── wsgi.py              # Web server gateway interface
├── playlists/               # Django application folder
│   ├── __init__.py
│   ├── admin.py             # Admin panel configurations
│   ├── apps.py
│   ├── models.py            # Playlist database model
│   ├── urls.py              # Application-specific URLs
│   ├── views.py             # Function-based views
│   ├── migrations/          # Database migrations history
│   ├── static/              # Static files (CSS)
│   │   └── playlists/
│   │       └── css/
│   │           └── style.css
│   └── templates/           # HTML templates
│       └── playlists/
│           ├── base.html
│           ├── home.html
│           ├── playlist_list.html
│           └── playlist_detail.html
└── media/                   # Folder for uploaded covers (auto-created)
```

---

## Installation & Running Locally

Follow these steps to run the application on your computer:

1. **Clone or Download the Project:**
   Make sure you are in the project folder `MyPlaylistApp`.

2. **Create a Virtual Environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment:**
   * **Windows (Command Prompt):**
     ```cmd
     .venv\Scripts\activate
     ```
   * **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   * **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (Admin account):**
   ```bash
   python manage.py createsuperuser
   ```
   *(Enter username, email, and password. Note: you can use `admin` / `admin` for development)*

7. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

---

## Testing Guide

To verify that the project is working correctly, perform the following test cases:

### 1. Test the Home Page
* Open your browser and go to `http://127.0.0.1:8000/`
* Verify that you see the welcome header and a button labeled "Browse Playlists".
* Verify the navigation links work.

### 2. Test the Admin Panel
* Go to `http://127.0.0.1:8000/admin/`
* Log in using the superuser credentials you created.
* Click on **Playlists** under the **Playlists** section.
* Click **Add Playlist** to create a new one. Enter a title, description, and upload a cover photo, then save it.
* Verify that the new playlist is displayed in the list view showing its title and creation date.

### 3. Test the Playlist List Page
* Go to `http://127.0.0.1:8000/playlists/`
* Verify that the newly added playlist is listed, displaying its cover photo, title, first few words of the description, and a "View Details" button.

### 4. Test the Playlist Detail Page
* Click the "View Details" button on one of the playlists in the list.
* Verify that the URL changes to `http://127.0.0.1:8000/playlists/<id>/` where `<id>` is the playlist number.
* Verify that the full description and large cover photo are displayed.

### 5. Test the JSON API Endpoint
* Go to `http://127.0.0.1:8000/api/playlists/`
* Verify that it returns a JSON list containing the title, description, and details of all database playlists.

---

## Git Commands for GitHub

To push your project to a GitHub repository named `MyPlaylistApp`, run these commands in order in your local project terminal:

```bash
# 1. Initialize a git repository
git init

# 2. Add all project files to staging (except virtual env or database if ignored)
# Create a .gitignore file with: .venv/, db.sqlite3, media/, staticfiles/
git add .

# 3. Commit the files
git commit -m "Initial commit of MyPlaylistApp student project"

# 4. Rename the default branch to main
git branch -M main

# 5. Link to your remote GitHub repository (Replace your-username with your actual username)
git remote add origin https://github.com/your-username/MyPlaylistApp.git

# 6. Push to GitHub
git push -u origin main
```

---

## PythonAnywhere Deployment Steps

Follow these instructions to host your project live on PythonAnywhere:

### Step 1: Clone the GitHub Repository
1. Log in to PythonAnywhere.
2. Open a **Bash Console**.
3. Clone your repository:
   ```bash
   git clone https://github.com/your-username/MyPlaylistApp.git
   ```
4. Move into the project directory:
   ```bash
   cd MyPlaylistApp
   ```

### Step 2: Set Up Virtual Environment and Install Requirements
1. Create a virtual environment inside your folder:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 playlist-venv
   ```
   *(Alternatively, use `python3 -m venv .venv` and activate it)*
2. Install the packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Run Database Migrations & Collect Static Files
1. Create and run database tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Create your administrator account:
   ```bash
   python manage.py createsuperuser
   ```
3. Gather all static files into one place so PythonAnywhere can serve them:
   ```bash
   python manage.py collectstatic
   ```

### Step 4: Configure Web App on PythonAnywhere
1. Go to the **Web** tab in PythonAnywhere and click **Add a new web app**.
2. Select **Manual Configuration** (do not select Django) and choose Python 3.10.
3. In the **Virtualenv** section, enter the path to your virtual environment (e.g., `/home/your-username/.virtualenvs/playlist-venv` or the path of your `.venv` directory).
4. In the **Code** section, set the **Source code** path to your project folder (e.g., `/home/your-username/MyPlaylistApp`).

### Step 5: Configure the WSGI File
Click on the WSGI configuration file link (e.g. `/var/www/your-username_pythonanywhere_com_wsgi.py`) on the Web tab, delete all its content, and replace it with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/your-username/MyPlaylistApp'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module for Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'MyPlaylistApp.settings'

# Initialize the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(Make sure to replace `your-username` with your actual PythonAnywhere username!)*

### Step 6: Configure Static & Media Files in Web Tab
In the **Static files** section of the Web tab, add these mappings:

| URL | Directory |
|---|---|
| `/static/` | `/home/your-username/MyPlaylistApp/staticfiles/` |
| `/media/` | `/home/your-username/MyPlaylistApp/media/` |

*(Again, replace `your-username` with your username)*

### Step 7: Reload the Web App
Scroll to the top of the **Web** tab and click **Reload**. Your site is now live!

---

## Challenges Faced & Solutions

During development, several challenges were encountered:
1. **Challenge:** Django didn't serve uploaded cover images automatically in development.
   * **Solution:** We added `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` to the `MyPlaylistApp/urls.py` file to handle image routing in development.
2. **Challenge:** Keeping the CSS responsive without styling packages.
   * **Solution:** Used CSS Grid with `repeat(auto-fill, minmax(280px, 1fr))` for a clean layout that automatically adjusts to screen size.
3. **Challenge:** Displaying descriptions with paragraphs correctly.
   * **Solution:** Applied the `{{ playlist.description|linebreaks }}` template filter, which preserves newlines entered in the admin panel by converting them to `<p>` tags.

---

## Error Resolution (Common Issues & Fixes)

### 1. Static Files Not Loading (Styles are missing)
* **Cause:** The web server doesn't know where to look for CSS files, or `collectstatic` was not run.
* **Fix:** 
  1. Ensure `python manage.py collectstatic` was run.
  2. Verify that `STATIC_ROOT` and `STATIC_URL` are defined in `settings.py`.
  3. Ensure the static file mappings in PythonAnywhere's **Web** tab are correct.

### 2. Images Not Displaying
* **Cause:** Uploaded cover images are not in the folder mapped by PythonAnywhere, or media URLs are not configured.
* **Fix:**
  1. Ensure you have the `MEDIA_URL` and `MEDIA_ROOT` paths correctly defined in `settings.py`.
  2. Ensure you added the media static routing helper at the end of `urls.py`.
  3. Ensure that `/media/` is configured in the static mapping of PythonAnywhere pointing to the full path of the `media` directory.

### 3. ModuleNotFoundError (No module named 'django' or 'PIL')
* **Cause:** The virtual environment is either not activated, or python is searching the global space.
* **Fix:**
  1. Verify your virtual environment path is specified correctly under the **Web** tab on PythonAnywhere.
  2. Run `pip install pillow django` while the virtual environment is activated.

### 4. DisallowedHost (Invalid HTTP_HOST header)
* **Cause:** Django blocks request headers from domains not listed in the `ALLOWED_HOSTS` setting.
* **Fix:**
  * Open `settings.py` and set `ALLOWED_HOSTS = ['*']` or specify your PythonAnywhere site: `ALLOWED_HOSTS = ['your-username.pythonanywhere.com']`.

### 5. Migration Errors (Table already exists or relation doesn't exist)
* **Cause:** Database structure is out of sync with migration history files.
* **Fix:**
  * If it's a new setup, delete `db.sqlite3` and files inside `playlists/migrations/` (except `__init__.py`), then run `makemigrations` and `migrate` fresh.

### 6. 404 Page Errors
* **Cause:** The requested page URL path does not match any pattern in the project's `urls.py`.
* **Fix:**
  * Check the spelling of paths in `playlists/urls.py` and verify you included `<int:playlist_id>` parameter for details view.
