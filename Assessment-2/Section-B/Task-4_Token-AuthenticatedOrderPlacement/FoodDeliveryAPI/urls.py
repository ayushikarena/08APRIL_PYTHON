"""
FoodDeliveryAPI/urls.py — Task 4: Token-Authenticated Order Placement
======================================================================
Root URL configuration.

Registered endpoints:
    /admin/          →  Django admin panel
    /api/token/      →  POST credentials → receive auth token (POST only)
    /api/my-orders/  →  PlaceOrderAPIView (GET + POST, requires token)
    /api/            →  DRF browsable API root (for browser testing)
    /api-auth/       →  DRF session login/logout (for browsable API in browser)
"""

from django.contrib  import admin
from django.urls     import path, include
from django.http     import JsonResponse

# DRF built-in view: POST credentials → receive an auth token
from rest_framework.authtoken.views import obtain_auth_token


def api_root(request):
    """
    Simple API root view — lists all available endpoints.
    Accessible via browser at http://127.0.0.1:8000/api/
    """
    return JsonResponse({
        "message"  : "Task 4 — Token-Authenticated Food Delivery API",
        "endpoints": {
            "generate_token" : {
                "url"    : "/api/token/",
                "method" : "POST",
                "auth"   : "No",
                "note"   : "Send username+password → receive token. Use Postman (POST only, not browser)."
            },
            "my_orders_list" : {
                "url"    : "/api/my-orders/",
                "method" : "GET",
                "auth"   : "Required — Authorization: Token <your_token>",
                "note"   : "Returns only the authenticated user's own orders."
            },
            "my_orders_create": {
                "url"    : "/api/my-orders/",
                "method" : "POST",
                "auth"   : "Required — Authorization: Token <your_token>",
                "note"   : "Places a new order. user is auto-assigned from token."
            },
            "admin_panel"    : {
                "url"    : "/admin/",
                "method" : "GET (browser)",
                "auth"   : "Superuser login",
                "note"   : "Django admin to manage orders and view tokens."
            },
        },
        "test_users": {
            "alice": {"password": "alice@1234"},
            "bob"  : {"password": "bob@1234"},
        }
    }, json_dumps_params={'indent': 2})


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # ✅ Token generation endpoint (POST only — use Postman, not browser GET)
    # Body: { "username": "alice", "password": "alice@1234" }
    # Returns: { "token": "9944b09..." }
    path('api/token/', obtain_auth_token, name='api-token-auth'),

    # DRF session login/logout for browsable API (allows testing GET in browser)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API root — shows all endpoints when you open /api/ in browser
    path('api/', api_root, name='api-root'),

    # API routes (my-orders/ is defined inside api/urls.py)
    path('api/', include('api.urls')),
]
