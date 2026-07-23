from django.urls import path

from .views import MusicWeather
from .views import FoodLocation
from .views import CountryInfo
from .views import GithubRepos

urlpatterns = [

    path(
        "music-weather/<str:city>/",
        MusicWeather.as_view(),
    ),

    path(
        "food-location/",
        FoodLocation.as_view(),
    ),

    path(
        "country-info/<str:country_name>/",
        CountryInfo.as_view(),
    ),

    path(
        "github-repos/<str:username>/",
        GithubRepos.as_view(),
    ),

]