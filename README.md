# Overview
This is the backend for a Sessions Marketplace application built with:

Django 4.2 + Django REST Framework
PostgreSQL (SQLite used locally for simplicity so far)
JWT authentication via djangorestframework-simplejwt
Custom User model with roles (USER / CREATOR)
Events app (formerly sessions, because sessions was causing a name conflict)
Creator-only event creation and public event listing
Features Implemented So Far

1. User Management
Custom User model with:
username, email, role (USER or CREATOR)
avatar (optional URL)
Admin panel:
    Superuser creation
    Edit user roles
    /api/me/ endpoint to get logged-in user details
JWT authentication (access + refresh tokens)

2️. Events
Event model:
    title, description, creator, created_at
Admin panel:
    Create/edit events
Event APIs:
    GET /api/events/ — list all events (public)
    GET /api/events/<id>/ — view event details (public)
    POST /api/events/ — create new event (CREATOR only)

## Setup Instructions
1. Clone the Repository
    git clone <repo-url>
    cd backend
2. Create Virtual Environment
    python -m venv venv
    # Mac/Linux
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
3. Install Dependencies
    pip install -r requirements.txt


## Key packages:

Django==4.2
djangorestframework==3.16.1
djangorestframework-simplejwt==5.5.1
PyJWT==2.10.1

4. Run Migrations
    python manage.py makemigrations
    python manage.py migrate

5. Create Superuser
    python manage.py createsuperuser

    API Endpoints
    Health Check
    GET /health/


    Response:
    {"status": "ok"}

    Authentication (JWT)
    POST /api/token/
    POST /api/token/refresh/


### Get JWT Access + Refresh tokens:

    {
    "username": "creator_user",
    "password": "password"
    }

    User
    GET /api/me/


    Returns logged-in user info:
    {
    "id": 1,
    "username": "creator_user",
    "email": "",
    "role": "CREATOR",
    "avatar": null
    }

## Events

Public
    GET /api/events/
    GET /api/events/<id>/


Creator-only
    POST /api/events/


Body:
{
  "title": "Advanced Django",
  "description": "Deep dive into Django internals"
}


Requires JWT token for a user with role CREATOR

## Admin Panel

URL:
    http://127.0.0.1:8000/admin/

Manage Users and Roles
Manage Events
Tip: To edit user roles directly in the list view:

# users/admin.py
list_editable = ('role',)
Testing
Create test users:
    User with role CREATOR → can create events
    User with role USER → cannot create events

Get JWT token via /api/token/
    Call /api/events/ → public list
    Call /api/events/<id>/ → public detail
    Call /api/events/ (POST) → must be CREATOR

## Notes / Next Steps
Frontend integration is pending
Booking functionality not implemented yet
Payment and file upload not implemented
Role-based permissions can be refactored into DRF Permission classes fully
Database currently SQLite for local development; PostgreSQL to be configured later