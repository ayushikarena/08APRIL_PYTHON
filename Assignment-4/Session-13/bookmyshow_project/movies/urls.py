from django.urls import path

from . import views

urlpatterns=[

    path("",views.watchlater,name="watchlater"),
    path("delete/<int:id>/",views.delete_movie,name="delete_movie"),

]