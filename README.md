# TrekMate

A Django-based booking application for treks.

## Prerequisites
- Python 3.11+
- Git (optional)

## Setup for Windows

### 1. Clone & Setup Directory
```powershell
git clone https://github.com/arthurr455565/TrekMate.git
cd TrekMate
```
*Or download/extract ZIP if you don't use Git.*

### 2. Create Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Create .env File
Copy the sample below into a new file named `.env`:
```ini
SECRET_KEY=django-insecure-YOUR_DEV_KEY_HERE
DEBUG=True
# Database settings (using SQLite by default)
```
*Note: To use MySQL, set `USE_MYSQL=True` and add your database credentials.*

### 5. Setup Database
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py populate_treks
```
*`populate_treks` adds sample treks (Annapurna, Everest, Manaslu) to the database.*

### 6. Run Server
```powershell
python manage.py runserver
```
Go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Administration

A superuser account is pre-configured:
*   **Login URL:** `/admin/` or via Login page
*   **Username:** `admin`
*   **Password:** `admin@123`

## Features
*   **Treks:** Browse and book treks.
*   **User Roles:** Trekkers (booking) & Guides (admin managed).
*   **Registration:** Public signup creates "Trekker" accounts only.
*   **Dashboard:** View your bookings and status.
