from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path("delete/<int:id>/", views.delete_product, name="delete_product"),

]