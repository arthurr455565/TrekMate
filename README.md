# TrekMate Project

A Django-based booking application for treks (project package: `trekbook_manager`).

This README provides a complete step-by-step setup and run guide for development environments on **Linux/macOS/Windows**. Follow the commands for your operating system.

---

## Prerequisites

- Python 3.11+ (the project was created with Django 5.2.x)
- git (optional, for cloning)
- pip
- MySQL Server (for MySQL setup) or SQLite (default, no installation needed)
- Recommended: use a virtual environment

**Database Options:**
- **SQLite** (default): No additional setup required. The project uses SQLite by default (`db.sqlite3`) for easy development.
- **MySQL**: Requires MySQL server. On Windows, the project uses PyMySQL (no compilation needed). On Linux/macOS, you can use `mysqlclient` or PyMySQL.

**Note:** If your app uses ImageField, you'll need the Pillow package (included in requirements.txt).

---


## 1. Clone the GitHub repository

Clone the project from GitHub using:

**Linux/macOS/Windows:**

```sh
git clone https://github.com/arthurr455565/TrekMate.git
cd TrekMate
```

**Note:** If you don't have git installed, you can download the repository as a ZIP file from GitHub and extract it.

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

Install dependencies from `requirements.txt`:

**Linux/macOS/Windows:**

```sh
pip install -r requirements.txt
```

**Note for Windows users:** If `mysqlclient` fails to install (requires Visual C++ Build Tools), the project will automatically use PyMySQL when `USE_MYSQL=True` is set in your `.env` file. PyMySQL is a pure Python MySQL client that works on Windows without compilation.

**Note for Linux/macOS users:** If you prefer PyMySQL over `mysqlclient`, you can install it separately:
```sh
pip install PyMySQL cryptography
```

---

## 4. Environment Variables Setup

Create a `.env` file in the project root (the same directory as `manage.py`) by copying the `.env.sample` (if provided) or creating a new one.

**Linux/macOS:**
```sh
cp .env.sample .env # If .env.sample exists
# OR create a new .env file:
touch .env
```

**Windows (PowerShell):**
```powershell
Copy-Item .env.sample .env # If .env.sample exists
# OR create a new .env file:
New-Item -Path .env -ItemType File
```

Edit the `.env` file and set the following variables:

**For SQLite (default):**
```ini
SECRET_KEY=your_secret_key_here
DEBUG=True
```

**For MySQL:**
```ini
SECRET_KEY=your_secret_key_here
DEBUG=True
USE_MYSQL=True
DB_NAME=trekbook
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

**Environment Variables Explained:**
- `SECRET_KEY`: A unique secret key for your Django project. Generate one using:
  ```sh
  python -c "import secrets; print(secrets.token_urlsafe(50))"
  ```
- `DEBUG`: Set to `True` for development, `False` for production.
- `USE_MYSQL`: Set to `True` to use MySQL, `False` or omit to use SQLite (default).
- `DB_NAME`: The name of your MySQL database (e.g., `trekbook`).
- `DB_USER`: The username for your MySQL database (e.g., `root`).
- `DB_PASSWORD`: The password for your MySQL database user.
- `DB_HOST`: The host where your MySQL database is running (e.g., `127.0.0.1` or `localhost`).
- `DB_PORT`: The port your MySQL database is listening on (default is `3306`).

---

## 5. Database Setup

### Option A: SQLite (Default - No Setup Required)

If you're using SQLite (default), no database setup is needed. Django will automatically create `db.sqlite3` when you run migrations.

### Option B: MySQL Setup

If you want to use MySQL, ensure you have a MySQL server running and create a database for the project.

**Linux/macOS - Using Command Line:**

```sh
mysql -u root -p
CREATE DATABASE trekbook CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

**Windows - Using MySQL Workbench (Recommended):**

1. Open MySQL Workbench and connect to your MySQL server.
2. Click on a connection (e.g., "Local instance MySQL95") to open a SQL editor.
3. Run the following SQL command:
   ```sql
   CREATE DATABASE IF NOT EXISTS trekbook CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
4. Click the "Execute" button (⚡) or press `Ctrl+Enter`.
5. Refresh the SCHEMAS panel - you should see `trekbook` appear.

**Alternative - Using Command Line (Windows):**

```powershell
mysql -u root -p
# Enter your password when prompted, then run:
CREATE DATABASE trekbook CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

**Note:** Make sure your `.env` file has `USE_MYSQL=True` and the correct database credentials before proceeding to migrations.

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

**Linux/macOS/Windows:**

```sh
python manage.py makemigrations
python manage.py migrate
```

If you see errors during `makemigrations` or `migrate`, read the traceback carefully — common issues include:
- Model/form mismatches (forms referencing non-existent model fields)
- Missing imports in models/forms
- Database connection errors (check your `.env` file and MySQL server status)
- MySQL authentication errors (verify username/password in `.env`)

Fix the code then re-run the commands.

---

## 9. Create a superuser (optional but recommended)

**Linux/macOS/Windows:**

```sh
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## 10. (Optional) Collect static files

If you plan to use `collectstatic` (for production or testing), run:

**Linux/macOS/Windows:**

```sh
python manage.py collectstatic
```

This places static files into `STATIC_ROOT`.

---

## 11. Run the development server

**Linux/macOS/Windows:**

```sh
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

---

## 12. Common gotchas and troubleshooting

### General Issues

- **If templates look unstyled or Tailwind classes have no effect:**
  - Confirm Tailwind is loaded in `templates/base.html`. This project includes a CDN-tailwind setup by default. If you prefer local build, follow `TAILWIND_SETUP.md`.
  - Check browser devtools console for errors or blocked resources (CSP, offline, adblockers).

- **If image uploads don't appear:**
  - Ensure `MEDIA_ROOT` exists and is writable.
  - Ensure `MEDIA_URL` serving is configured in `trekbook_manager/urls.py` (see step 7).

- **If named URL reversing fails (reverse or `{% url %}`):**
  - Ensure app `urls.py` defines `app_name = 'your_app'` when you intend to use namespaced URLs (e.g. `bookings:booking_list`).
  - Ensure `trekbook_manager/urls.py` includes the app with include(..., namespace='...') or without namespace if you use the non-namespaced names.

- **If migrations fail with model/form field errors:**
  - Make sure your `forms.py` lists only fields that exist on the model.
  - If you add fields to models (e.g. `bio`, `profile_image`), create migrations and migrate.

- **If you have a folder name with spaces (e.g. `Booking Project`) you may encounter tooling issues; consider renaming the folder to `booking_project`.**

### Windows-Specific Issues

- **If `mysqlclient` fails to install:**
  - This is expected on Windows. The project automatically uses PyMySQL when `USE_MYSQL=True` is set. No action needed.
  - If you see "Access denied" errors, verify your MySQL password in the `.env` file matches the one used in MySQL Workbench.

- **If virtual environment activation fails in PowerShell:**
  - You may need to set the execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
  - Alternatively, use `.\.venv\Scripts\activate.bat` instead of the PowerShell script.

- **If MySQL connection fails:**
  - Verify MySQL server is running: Check Windows Services or MySQL Workbench connection status.
  - Ensure `USE_MYSQL=True` is set in `.env` file.
  - Verify database credentials match those used in MySQL Workbench.
  - Try using `localhost` instead of `127.0.0.1` in `DB_HOST` (or vice versa).

### MySQL Connection Troubleshooting

- **"Access denied for user 'root'@'localhost'":**
  - Verify the password in `.env` matches your MySQL root password.
  - Check MySQL Workbench connection settings to confirm the correct password.
  - Ensure the MySQL user has proper permissions.

- **"Can't connect to MySQL server":**
  - Verify MySQL server is running.
  - Check that `DB_HOST` and `DB_PORT` in `.env` match your MySQL configuration.
  - On Windows, ensure MySQL service is started (check Services panel).

---

## 13. Tailwind / frontend workflow (optional)

This project includes `TAILWIND_SETUP.md`. If you want to compile Tailwind locally (recommended for production and better performance):

- Install Node.js and npm
- Follow `TAILWIND_SETUP.md` for registering Tailwind via npm and building a CSS file to include in `base.html` instead of CDN

---
