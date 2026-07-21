from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home,name='home'),
    path('my_orders/', views.my_orders, name='orders'),
    path('post-product/',views.post_product,name='post_product'),
    #=====================Task-3========================
    path("add-review/", views.add_review, name="add_review"),
    path("view-review/", views.view_review, name="view_review"),
    #====================Task-4=========================
    path('',views.dashboard,name='dashboard'),
]