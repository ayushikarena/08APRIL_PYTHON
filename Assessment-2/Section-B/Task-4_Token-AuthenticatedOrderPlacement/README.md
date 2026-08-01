# Task 4 — Token-Authenticated Order Placement
### Food Delivery API · Django REST Framework

---

## Project Structure

```
Task-4_Token-AuthenticatedOrderPlacement/
├── FoodDeliveryAPI/
│   ├── __init__.py
│   ├── settings.py          ← TokenAuthentication configured here
│   ├── urls.py              ← /api/token/ + /api/my-orders/
│   └── wsgi.py
├── api/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py             ← OrderAdmin with user column
│   ├── apps.py
│   ├── models.py            ← Order model with User ForeignKey
│   ├── serializers.py       ← OrderSerializer (user read-only)
│   ├── urls.py              ← my-orders/ route
│   └── views.py             ← PlaceOrderAPIView (GET + POST)
├── seed.py                  ← Creates alice & bob + tokens
├── manage.py
└── README.md
```

---

## Setup Commands (Run Once)

```bash
# 1. Install dependencies
pip install django djangorestframework

# 2. Run migrations (creates authtoken_token table)
python manage.py makemigrations api
python manage.py migrate

# 3. Create a superuser for Django Admin (optional)
python manage.py createsuperuser

# 4. Seed test users (alice & bob) and generate their tokens
python seed.py

# 5. Start the development server
python manage.py runserver
```

---

## API Endpoints

| Method | URL | Auth Required | Description |
|--------|-----|:---:|-------------|
| `POST` | `/api/token/` | No | Get auth token via username + password |
| `GET` | `/api/my-orders/` | **Yes** | List only the current user's orders |
| `POST` | `/api/my-orders/` | **Yes** | Place a new order as current user |

---

## Postman Testing Guide

### Step 1 — Generate Token (`POST /api/token/`)

Get the auth token by sending your credentials.

**Request:**
```
Method : POST
URL    : http://127.0.0.1:8000/api/token/
Headers: Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "username": "alice",
    "password": "alice@1234"
}
```

**Response 200 OK:**
```json
{
    "token": "c3f7482940e3d35d17eb7db3be0c8989e5710657"
}
```

> Copy this token — you'll use it in every subsequent request.

---

### Step 2 — Create Order (`POST /api/my-orders/`)

Place a new order as the authenticated user.

**Request:**
```
Method : POST
URL    : http://127.0.0.1:8000/api/my-orders/
Headers:
    Content-Type  : application/json
    Authorization : Token c3f7482940e3d35d17eb7db3be0c8989e5710657
```

**Body (raw JSON):**
```json
{
    "item": "Chicken Biryani",
    "quantity": 2,
    "status": "pending"
}
```

**Response 201 Created:**
```json
{
    "status": "success",
    "message": "Order placed successfully!",
    "order": {
        "id": 1,
        "user": "alice",
        "item": "Chicken Biryani",
        "quantity": 2,
        "status": "pending",
        "created_at": "2024-07-25T01:43:00.000000Z"
    }
}
```

---

### Step 3 — Get My Orders (`GET /api/my-orders/`)

Retrieve only the orders belonging to the authenticated user.

**Request:**
```
Method : GET
URL    : http://127.0.0.1:8000/api/my-orders/
Headers:
    Authorization : Token c3f7482940e3d35d17eb7db3be0c8989e5710657
```

**Response 200 OK:**
```json
{
    "status": "success",
    "user": "alice",
    "count": 2,
    "orders": [
        {
            "id": 2,
            "user": "alice",
            "item": "Paneer Tikka",
            "quantity": 1,
            "status": "confirmed",
            "created_at": "2024-07-25T01:44:00.000000Z"
        },
        {
            "id": 1,
            "user": "alice",
            "item": "Chicken Biryani",
            "quantity": 2,
            "status": "pending",
            "created_at": "2024-07-25T01:43:00.000000Z"
        }
    ]
}
```

---

### Step 4 — Unauthorized Request (no token)

Send a request **without** the Authorization header.

**Request:**
```
Method : GET
URL    : http://127.0.0.1:8000/api/my-orders/
Headers: (none — no Authorization)
```

**Response 401 Unauthorized:**
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

### Step 5 — Invalid Token

Send a request with a **wrong or expired** token.

**Request:**
```
Method : GET
URL    : http://127.0.0.1:8000/api/my-orders/
Headers:
    Authorization : Token invalidtoken123abc
```

**Response 401 Unauthorized:**
```json
{
    "detail": "Invalid token."
}
```

---

## Data Isolation Proof

Alice and Bob each have their own tokens. Orders placed by Alice **never** appear in Bob's responses:

| User | Token (first 10 chars) | Can see Alice's orders? |
|------|------------------------|:-----------------------:|
| Alice | `c3f7482940...` | Yes (her own only) |
| Bob | `b6d83cacc8...` | No — returns only Bob's |

The view enforces this with:
```python
orders = Order.objects.filter(user=request.user)
```

---

## Test Users (created by seed.py)

| Username | Password | Token |
|----------|----------|-------|
| `alice` | `alice@1234` | `c3f7482940e3d35d17eb7db3be0c8989e5710657` |
| `bob` | `bob@1234` | `b6d83cacc86405b2758ba902d9cd796aa1f7c580` |

---

## Django Admin

```
URL      : http://127.0.0.1:8000/admin/
Username : (the superuser you created)
```

- **Orders** → view/search all orders, filtered by user or status  
- **Tokens** → `http://127.0.0.1:8000/admin/authtoken/token/` to see all generated tokens

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| `TokenAuthentication` only | Stateless — no session cookies needed |
| `user` is read-only in serializer | Prevents client from spoofing order ownership |
| `serializer.save(user=request.user)` | Owner injected server-side at save time |
| `Order.objects.filter(user=request.user)` | Enforces per-user data isolation |
| `obtain_auth_token` at `/api/token/` | DRF built-in — no custom token logic needed |
