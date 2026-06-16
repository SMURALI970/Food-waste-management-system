# Food-waste-management-system
A Django REST API application to track and reduce food wastage across donors, receivers, and inventory — built with Python, Django, and SQLite.

# Food Waste Management System

A Django REST API application to track and reduce food wastage across donors, receivers, and inventory.

## Tech Stack

- **Backend:** Python, Django
- **API:** Django REST Framework
- **Database:** SQLite

## Features

- Log food donations with donor name, food item, quantity, and location
- Track donation status — Available, Claimed, or Expired
- Full CRUD operations via REST API endpoints
- Browsable API interface for testing

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/donations/` | List all donations |
| POST | `/api/donations/` | Create a new donation |
| GET | `/api/donations/{id}/` | Retrieve a donation |
| PUT | `/api/donations/{id}/` | Update a donation |
| DELETE | `/api/donations/{id}/` | Delete a donation |

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/SMURALI970/Food-waste-management-system.git
cd Food-waste-management-system

# Install dependencies
pip install django djangorestframework

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/` to access the API.

## Author

S Murali — [GitHub](https://github.com/SMURALI970)
