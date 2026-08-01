"""
Main URL Configuration

This file routes all incoming web requests to our app's URL configuration.
"""

from django.urls import path, include

urlpatterns = [
    # Forward all URLs to our app's url configuration
    path('', include('app.urls')),
]
