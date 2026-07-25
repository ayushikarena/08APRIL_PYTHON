# FoodDeliveryAPI

A complete Django REST Framework project implementing a fully functional Food Delivery REST API backend following professional coding standards.

## Project Overview

FoodDeliveryAPI provides a robust backend solution for a food delivery platform. It includes core entities like `Category`, `MenuItem`, and `Order`, and implements CRUD operations using Django REST Framework's `ModelViewSet`. The API is secured using Token Authentication, supports pagination, and allows filtering on orders.

## Features

- **Categories**: CRUD operations to manage menu categories (Publicly accessible).
- **Menu Items**: CRUD operations to manage food items tied to categories (Publicly accessible).
- **Orders**: Secure CRUD operations for ordering menu items. Automatically assigns the ordering user as the customer.
- **Authentication**: Token-based authentication using `rest_framework.authtoken`.
- **Validation**: Robust data validation on serializers to ensure data integrity (e.g., price > 0, quantity >= 1).
- **Pagination**: Implemented `PageNumberPagination` with 5 items per page.
- **Filtering**: Easily filter orders based on their status using `django-filter`.

## Expected Folder Structure

```
FoodDeliveryRESTAPIBackend/
├── FoodDeliveryAPI/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── foodapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Installation Steps

### 1. Create the project from scratch
(If you are starting completely fresh without the existing files)
```bash
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

django-admin startproject FoodDeliveryAPI .
python manage.py startapp foodapp
```

### 2. Install all required packages
```bash
pip install django djangorestframework django-filter
```

## Database Migration Steps

### 3. Commands to make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Authentication Steps

### 4. Command to create a superuser
```bash
python manage.py createsuperuser
```
(Follow the prompts to enter a username, email, and password).

### 5. Commands to generate authentication tokens
Tokens are automatically generated when creating a user if you use signals, or they can be generated from the admin panel. Alternatively, request a token via the API:
```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ -d "username=yourusername&password=yourpassword"
```

### 6. Commands to run the server
```bash
python manage.py runserver
```

## API Endpoint List

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| POST | `/api-token-auth/` | Obtain Auth Token | No |
| GET | `/categories/` | List all categories | No |
| POST | `/categories/` | Create a new category | No |
| GET | `/categories/<id>/` | Retrieve a category | No |
| PUT | `/categories/<id>/` | Update a category | No |
| DELETE | `/categories/<id>/` | Delete a category | No |
| GET | `/menu-items/` | List all menu items | No |
| POST | `/menu-items/` | Create a new menu item | No |
| GET | `/menu-items/<id>/` | Retrieve a menu item | No |
| PUT | `/menu-items/<id>/` | Update a menu item | No |
| DELETE | `/menu-items/<id>/` | Delete a menu item | No |
| GET | `/orders/` | List all orders | Yes |
| POST | `/orders/` | Create a new order | Yes |
| GET | `/orders/<id>/` | Retrieve an order | Yes |
| PUT | `/orders/<id>/` | Update an order | Yes |
| DELETE | `/orders/<id>/` | Delete an order | Yes |

## Postman Testing Instructions

1. **Get Token**: Send a POST request to `/api-token-auth/` with your credentials in the form-data or JSON body.
2. **Authorize**: Copy the `token` from the response. Go to the "Authorization" tab in Postman for your subsequent requests (like creating an Order), select "API Key" or "Bearer Token" (Use Token as prefix manually).
3. **Sample Authorization Header**:
   ```
   Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
   ```

## Sample Requests and Responses

### 1. Categories
**Create Category (POST `/categories/`)**
Request:
```json
{
    "name": "Beverages",
    "description": "Cold and hot drinks."
}
```
Response (201 Created):
```json
{
    "id": 1,
    "name": "Beverages",
    "description": "Cold and hot drinks."
}
```

### 2. Menu Items
**Create Menu Item (POST `/menu-items/`)**
Request:
```json
{
    "name": "Coca Cola",
    "price": "2.50",
    "category": 1,
    "is_available": true
}
```
Response (201 Created):
```json
{
    "id": 1,
    "name": "Coca Cola",
    "price": "2.50",
    "is_available": true,
    "category": 1
}
```

### 3. Orders
**Create Order (POST `/orders/`)**
*Requires Authorization Header*
Request:
```json
{
    "item": 1,
    "quantity": 2
}
```
Response (201 Created):
```json
{
    "id": 1,
    "customer": "admin",
    "item": 1,
    "quantity": 2,
    "status": "pending",
    "created_at": "2026-07-25T14:45:00Z"
}
```

## Pagination Example
The Order endpoint uses `PageNumberPagination` with a size of 5.

**Request:** `GET /orders/?page=2`
**Response:**
```json
{
    "count": 12,
    "next": "http://127.0.0.1:8000/orders/?page=3",
    "previous": "http://127.0.0.1:8000/orders/?page=1",
    "results": [
        {
            "id": 6,
            "customer": "admin",
            "item": 1,
            "quantity": 1,
            "status": "pending",
            "created_at": "2026-07-25T14:45:00Z"
        },
        ... (4 more items)
    ]
}
```

## Order Filtering Example
The Order endpoint allows filtering by status.

**Request:** `GET /orders/?status=delivered`
**Response:**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "customer": "admin",
            "item": 1,
            "quantity": 1,
            "status": "delivered",
            "created_at": "2026-07-25T14:45:00Z"
        }
    ]
}
```
