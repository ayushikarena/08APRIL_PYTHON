# Food Delivery API - All Endpoints

Here is the complete list of all the URLs available in your `FoodDeliveryAPI` project running on `http://127.0.0.1:8001`.

### 🔐 Authentication & Users
*Use these to get your JWT access token.*
* **Register:** `POST http://127.0.0.1:8001/api/auth/register/` (Body: `username`, `email`, `password`)
* **Login (Get Token):** `POST http://127.0.0.1:8001/api/auth/login/` (Body: `username`, `password`)
* **Refresh Token:** `POST http://127.0.0.1:8001/api/auth/refresh/`
* **User Profile:** `GET http://127.0.0.1:8001/api/profile/` *(🔒 Requires JWT)*

### 🏙️ Cities
* **List / Create Cities:** `GET` | `POST http://127.0.0.1:8001/api/cities/`
* **View / Edit / Delete City:** `GET` | `PUT` | `DELETE http://127.0.0.1:8001/api/cities/<id>/`

### 🍔 Restaurants
* **List / Create Restaurants:** `GET` | `POST http://127.0.0.1:8001/api/restaurants/`
  * *Search Example:* `http://127.0.0.1:8001/api/restaurants/?city=1&cuisine=Italian`
* **View / Edit / Delete Restaurant:** `GET` | `PUT` | `DELETE http://127.0.0.1:8001/api/restaurants/<id>/`
* **View Restaurant Menu:** `GET http://127.0.0.1:8001/api/restaurants/<id>/menu/`

### 🍕 Menu Items
* **List / Create Menu Items:** `GET` | `POST http://127.0.0.1:8001/api/menu-items/`
* **View / Edit / Delete Menu Item:** `GET` | `PUT` | `DELETE http://127.0.0.1:8001/api/menu-items/<id>/`

### 🛒 Cart *(🔒 All Require JWT)*
* **View Cart:** `GET http://127.0.0.1:8001/api/cart/`
* **Add Item to Cart:** `POST http://127.0.0.1:8001/api/cart/items/`
  * *(Body: `{"menu_item": 1, "quantity": 2}`)*
* **Update / Remove Cart Item:** `PATCH` | `DELETE http://127.0.0.1:8001/api/cart/items/<item_id>/`

### 📦 Orders *(🔒 All Require JWT)*
* **View Order History / Place Order:** `GET` | `POST http://127.0.0.1:8001/api/orders/`
  * *(To place an order, send a `POST` request with an empty JSON body `{}`. It automatically converts your cart to an order.)*
* **View / Edit / Delete Order:** `GET` | `PUT` | `DELETE http://127.0.0.1:8001/api/orders/<id>/`

### ⚙️ Admin Interface
* **Django Admin:** `GET http://127.0.0.1:8001/admin/`

---
**How to use JWT Authentication in Postman:**
When testing routes marked with 🔒, go to the **Authorization** tab in Postman, choose **Bearer Token**, and paste the `access` token you received from the login endpoint.
