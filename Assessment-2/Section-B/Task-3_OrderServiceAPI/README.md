# FoodDeliveryAPI - Django REST Framework

This project implements a complete, paginated, and filterable Order API using Django REST Framework.

## Project Structure

```
Task-3_OrderServiceAPI/
│
├── venv/                     # Python virtual environment
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
├── api_urls.csv              # Spreadsheet containing all API endpoints
│
├── FoodDeliveryAPI/          # Main project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Project settings (DRF, pagination configured here)
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py
│
└── api/                      # Application directory
    ├── migrations/           # Database migrations
    ├── __init__.py
    ├── admin.py              # Admin configuration for Order model
    ├── apps.py
    ├── models.py             # Order model definition
    ├── serializers.py        # OrderSerializer definition
    ├── urls.py               # Application routing using DefaultRouter
    └── views.py              # OrderViewSet with filter and CRUD capabilities
```

## Setup & Run Instructions

The project is already initialized with all dependencies and migrations applied. To run it locally:

1. **Activate the virtual environment**:
   ```bash
   .\venv\Scripts\activate
   ```

2. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Postman Testing Steps

1. Open Postman.
2. Ensure the Django server is running (`http://127.0.0.1:8000/`).
3. Import the URLs from `api_urls.csv` or create new requests manually.
4. Test the following endpoints:

### 1. Create a New Order (POST)
- **Method:** `POST`
- **URL:** `http://127.0.0.1:8000/api/orders/`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "customer_name": "Alice Smith",
    "item": "Sushi Platter",
    "quantity": 2,
    "status": "pending"
}
```
**Sample Response (201 Created):**
```json
{
    "id": 1,
    "customer_name": "Alice Smith",
    "item": "Sushi Platter",
    "quantity": 2,
    "status": "pending"
}
```

### 2. List All Orders (GET - Paginated)
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/api/orders/`
**Sample Response (200 OK):**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "customer_name": "Alice Smith",
            "item": "Sushi Platter",
            "quantity": 2,
            "status": "pending"
        }
    ]
}
```

### 3. Filter Orders by Status (GET)
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/api/orders/?status=pending`
**Sample Response (200 OK):**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "customer_name": "Alice Smith",
            "item": "Sushi Platter",
            "quantity": 2,
            "status": "pending"
        }
    ]
}
```

### 4. Retrieve a Specific Order (GET)
- **Method:** `GET`
- **URL:** `http://127.0.0.1:8000/api/orders/1/`
**Sample Response (200 OK):**
```json
{
    "id": 1,
    "customer_name": "Alice Smith",
    "item": "Sushi Platter",
    "quantity": 2,
    "status": "pending"
}
```

### 5. Update an Order (PUT)
- **Method:** `PUT`
- **URL:** `http://127.0.0.1:8000/api/orders/1/`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "customer_name": "Alice Smith",
    "item": "Sushi Platter",
    "quantity": 3,
    "status": "confirmed"
}
```
**Sample Response (200 OK):**
```json
{
    "id": 1,
    "customer_name": "Alice Smith",
    "item": "Sushi Platter",
    "quantity": 3,
    "status": "confirmed"
}
```

### 6. Partially Update an Order (PATCH)
- **Method:** `PATCH`
- **URL:** `http://127.0.0.1:8000/api/orders/1/`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "status": "delivered"
}
```
**Sample Response (200 OK):**
```json
{
    "id": 1,
    "customer_name": "Alice Smith",
    "item": "Sushi Platter",
    "quantity": 3,
    "status": "delivered"
}
```

### 7. Delete an Order (DELETE)
- **Method:** `DELETE`
- **URL:** `http://127.0.0.1:8000/api/orders/1/`
**Sample Response (204 No Content):**
*(No body)*
