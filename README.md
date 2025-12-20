# TrekMate Project

A Django-based booking application for treks (project package: `trekbook_manager`).

This README provides a complete step-by-step setup and run guide for a development environment on Linux/macOS. Follow the commands exactly in a shell (your default shell is `sh`).

---

## Prerequisites

- Python 3.11+ (the project was created with Django 5.2.x)
- git (optional, for cloning)
- pip
- MySQL Client Libraries (e.g., `libmysqlclient-dev` on Debian/Ubuntu, `mysql-client` on macOS with Homebrew)
- Recommended: use a virtual environment

Note: the project uses SQLite by default (`db.sqlite3`) so there is no extra database server required for development. If your app uses ImageField you'll need the Pillow package.

---


## 1. Clone the GitHub repository

Clone the project from GitHub using:

```sh
git clone https://github.com/arthurr455565/TrekMate.git
cd TrekMate
```

---

## 2. Create & activate a virtual environment

It's recommended to create a project-level virtual environment. This example will create `.venv` in the project root.

**Linux/macOS (sh/bash):**

```sh
python -m venv .venv
. .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

You should see your shell prompt change to indicate the virtualenv is active.

---

## 3. Install dependencies

If the repository contains a `requirements.txt`, install it. Otherwise install Django and recommended packages.

sh commands:

```sh
# If requirements.txt exists
pip install -r requirements.txt
```

---

## 4. Environment Variables Setup

Create a `.env` file in the project root (the same directory as `manage.py`) by copying the `.env.sample` (if provided) or creating a new one.

```sh
cp .env.sample .env # If .env.sample exists
# OR create a new .env file with the following content:
# touch .env
```

Edit the `.env` file and set the following variables:

```ini
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

- `SECRET_KEY`: A unique secret key for your Django project. You can generate one using Python:
  ```python
  import os
  import secrets
  print(secrets.token_urlsafe(50))
  ```
- `DEBUG`: Set to `True` for development, `False` for production.
- `DB_NAME`: The name of your MySQL database.
- `DB_USER`: The username for your MySQL database.
- `DB_PASSWORD`: The password for your MySQL database user.
- `DB_HOST`: The host where your MySQL database is running (e.g., `127.0.0.1` for local).
- `DB_PORT`: The port your MySQL database is listening on (default is `3306`).

---

## 5. Database Setup (MySQL)

Ensure you have a MySQL server running and create a database for the project. For example, if your `DB_NAME` in `.env` is `trekbook`, you would do:

sh commands:

```sh
mysql -u your_database_user -p
CREATE DATABASE trekbook CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

---

## 6. Configure project settings (one-time checks)

Before running migrations, ensure the project settings are configured correctly. Open `trekbook_manager/settings.py` and check:

- INSTALLED_APPS includes your apps, e.g.:
  - 'accounts', 'bookings', 'core', 'guides', 'treks'

- TEMPLATES['DIRS'] includes the top-level `templates/` directory, for example:

  import os
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')],
          ...
      }
  ]

- STATIC and MEDIA configuration for development:

  STATIC_URL = '/static/'
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

  # Optional: where collectstatic will place files
  STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

If you add or change settings, save the file.

---

## 7. Serve media files in development (urls)

If you use ImageField (guides, etc.), add the following when DEBUG=True in `trekbook_manager/urls.py` (at the bottom of the file):

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

This allows Django's runserver to serve uploaded images in development.

---

## 8. Create migrations and migrate the database

Run the following commands from the project root with the virtualenv active:

sh commands:

python manage.py makemigrations
python manage.py migrate

If you see errors during `makemigrations` or `migrate`, read the traceback carefully — common issues include:
- Model/form mismatches (forms referencing non-existent model fields)
- Missing imports in models/forms
Fix the code then re-run the commands.

---

## 9. Create a superuser (optional but recommended)

sh commands:

python manage.py createsuperuser

Follow the prompts to create an admin account.

---

## 10. (Optional) Collect static files

If you plan to use `collectstatic` (for production or testing), run:

sh commands:

python manage.py collectstatic

This places static files into `STATIC_ROOT`.

---

## 11. Run the development server

sh commands:

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

---

## 12. Common gotchas and troubleshooting

- If templates look unstyled or Tailwind classes have no effect:
  - Confirm Tailwind is loaded in `templates/base.html`. This project includes a CDN-tailwind setup by default. If you prefer local build, follow `TAILWIND_SETUP.md`.
  - Check browser devtools console for errors or blocked resources (CSP, offline, adblockers).

- If image uploads don't appear:
  - Ensure `MEDIA_ROOT` exists and is writable.
  - Ensure `MEDIA_URL` serving is configured in `trekbook_manager/urls.py` (see step 5).

- If named URL reversing fails (reverse or `{% url %}`):
  - Ensure app `urls.py` defines `app_name = 'your_app'` when you intend to use namespaced URLs (e.g. `bookings:booking_list`).
  - Ensure `trekbook_manager/urls.py` includes the app with include(..., namespace='...') or without namespace if you use the non-namespaced names.

- If migrations fail with model/form field errors:
  - Make sure your `forms.py` lists only fields that exist on the model.
  - If you add fields to models (e.g. `bio`, `profile_image`), create migrations and migrate.

- If you have a folder name with spaces (e.g. `Booking Project`) you may encounter tooling issues; consider renaming the folder to `booking_project`.

---

## 13. Tailwind / frontend workflow (optional)

This project includes `TAILWIND_SETUP.md`. If you want to compile Tailwind locally (recommended for production and better performance):

- Install Node.js and npm
- Follow `TAILWIND_SETUP.md` for registering Tailwind via npm and building a CSS file to include in `base.html` instead of CDN

---
