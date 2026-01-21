# TrekMate Project Documentation

## 1. Objective
TrekMate is a web-based trekking booking platform designed to connect trek enthusiasts with Himalayan adventures. The primary objective is to provide a seamless, user-friendly interface for browsing treks, booking trips, and managing trekking profiles, while offering administrators and guides powerful tools to manage bookings and treks.

## 2. Purpose
- **For Trekkers**: To easily discover trekking destinations, view detailed itineraries, and book trips online securely.
- **For Guides**: To showcase their expertise and manage assigned treks.
- **For Administrators**: To oversee the entire operation, manage users, bookings, and content (treks/guides).

## 3. Technology Stack
- **Backend**: Django 5.2.5 (Python 3.11+)
- **Frontend**: Django Templates, Tailwind CSS (via CDN)
- **Database**: SQLite (Development) / MySQL (Production-ready)
- **Styling**: Custom CSS and Tailwind utility classes for modern, responsive design.

## 4. System Architecture
The project follows the standard Django **Model-View-Template (MVT)** architecture:
- **Models**: Define the database structure (Treks, Bookings, Users).
- **Views**: Handle the business logic and modify data (Booking creation, Dashboard display).
- **Templates**: Render the user interface (HTML files).

## 5. Code Structure & Application Breakdown

The project is organized into modular Django apps:

### `core` App
*   **Purpose**: Handles main pages and dashboard logic.
*   **Key Files**:
    *   `views.py`: Renders Home, About, Contact, and Dashboard pages.
    *   `urls.py`: Defines routing for core pages.

### `accounts` App
*   **Purpose**: Manages User Authentication and Registration.
*   **Key Features**:
    *   **Custom User Model**: Extends `AbstractUser` to add `role` (Trekker/Guide).
    *   **Restricted Registration**: Public signup is limited to "Trekker" role only.
    *   `forms.py`: Handles login and registration validation.

### `treks` App
*   **Purpose**: Manages Trek information and catalog.
*   **Key Features**:
    *   `models.py`: Defines the `Trek` model (Name, Description, Difficulty, Price, etc.).
    *   `views.py`: Lists all treks and shows trek details.
    *   `management/commands/populate_treks.py`: Custom command to seed the database with initial trek data.

### `bookings` App
*   **Purpose**: Handles the core booking functionality.
*   **Key Features**:
    *   `models.py`: Defines `Booking` model connecting a `User` to `Trek`(s).
    *   `forms.py`: `TrekBookingForm` for capturing user input.
    *   `views.py`: Processes AJAX booking requests and saves data.
    *   `trek_booking_modal.html`: The popup form interface for making bookings.

### `guides` App
*   **Purpose**: Manages Guide profiles (if implemented separately from accounts).
*   **Key Features**: Listing available guides and their details.

## 6. Key Features & Workflows

### A. User Registration & Auth
- Users sign up as **Trekkers**.
- Login/Logout functionality with redirection.
- **Profile Dropdown**: Access Dashboard or Logout easily from the navbar.

### B. Trek Booking System
1.  User browses treks and clicks **"Book This Trek"**.
2.  If logged in: A modal opens with pre-filled details.
3.  If not logged in: Redirects to Login page.
4.  User fills preferences (Dates, Experience).
5.  **AJAX Submission**: Form submits without page reload.
6.  **Success**: Confirmation message appears, and booking is saved.

### C. Booking Management (Dashboard)
- Users can view their booking history in the **Dashboard**.
- Displays status (Pending/Confirmed), dates, and selected treks.

## 7. Deployment & Setup
(See `README.md` for detailed commands)
1.  Clone Repository
2.  Install Requirements (`pip install -r requirements.txt`)
3.  Setup Database (`migrate`)
4.  Populate Data (`populate_treks`)
5.  Run Server (`runserver`)

## 8. Role-Based Access Control
- **Trekker**: Can book treks, view their own dashboard.
- **Guide**: Has a specific dashboard (future expansion).
- **Admin**: Full access via Django Admin Panel (`/admin/`).
