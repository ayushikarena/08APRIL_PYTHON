from django.urls import path
from . import views

urlpatterns = [

    path('', views.profile_list, name='list'),
    path('create/', views.profile_create, name='create'),
    path('edit/<int:id>/', views.profile_edit, name='edit'),
    path('export/', views.export_csv, name='export'),

]