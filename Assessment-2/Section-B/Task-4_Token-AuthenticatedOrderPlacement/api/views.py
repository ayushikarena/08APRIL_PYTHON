"""
views.py — Task 4: Token-Authenticated Order Placement
=======================================================
PlaceOrderAPIView:
  • A single APIView that handles both GET and POST on /api/my-orders/.
  • Authentication : TokenAuthentication
  • Permission     : IsAuthenticated  (401 if no valid token is present)
  • GET  → returns ONLY the authenticated user's own orders.
  • POST → creates a new order automatically owned by request.user.
  • Unauthenticated requests get a 401 with a descriptive JSON message.
"""

from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions    import IsAuthenticated

from .models      import Order
from .serializers import OrderSerializer


class PlaceOrderAPIView(APIView):
    """
    Endpoint : /api/my-orders/

    Methods:
        GET  — List all orders belonging to the currently authenticated user.
        POST — Place a new order; owner is automatically set to request.user.

    Authentication:
        Token-based via the 'Authorization: Token <token>' HTTP header.

    Permissions:
        IsAuthenticated — any request without a valid token returns 401.
    """

    # ✅ Apply TokenAuthentication for this view
    authentication_classes = [TokenAuthentication]

    # ✅ Require authentication — unauthenticated → 401 Unauthorized
    permission_classes = [IsAuthenticated]

    # ------------------------------------------------------------------
    # GET /api/my-orders/
    # ------------------------------------------------------------------
    def get(self, request):
        """
        Return a list of orders that belong ONLY to the authenticated user.
        Users cannot see orders placed by other users.
        """
        # Filter by the logged-in user — enforces per-user data isolation
        orders = Order.objects.filter(user=request.user)

        serializer = OrderSerializer(orders, many=True)

        return Response(
            {
                "status"  : "success",
                "user"    : request.user.username,
                "count"   : orders.count(),
                "orders"  : serializer.data,
            },
            status=status.HTTP_200_OK
        )

    # ------------------------------------------------------------------
    # POST /api/my-orders/
    # ------------------------------------------------------------------
    def post(self, request):
        """
        Create a new order for the authenticated user.

        The 'user' field is NOT taken from the request body — it is always
        injected from request.user to prevent users from spoofing ownership.

        Expected request body:
            {
                "item"     : "Chicken Biryani",
                "quantity" : 2,
                "status"   : "pending"   ← optional, defaults to 'pending'
            }
        """
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            # ✅ Automatically assign the logged-in user as the owner
            # serializer.save() calls Order.objects.create(user=request.user, ...)
            order = serializer.save(user=request.user)

            return Response(
                {
                    "status"  : "success",
                    "message" : "Order placed successfully!",
                    "order"   : OrderSerializer(order).data,
                },
                status=status.HTTP_201_CREATED
            )

        # Validation failed — return field-level error details
        return Response(
            {
                "status" : "error",
                "message": "Order could not be placed. Please fix the errors below.",
                "errors" : serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
