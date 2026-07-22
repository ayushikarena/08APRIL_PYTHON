from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class RestaurantDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)