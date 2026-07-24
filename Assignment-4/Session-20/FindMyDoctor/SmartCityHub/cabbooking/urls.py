from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_cab, name='book_cab'),
]
