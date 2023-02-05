from django.urls import path, include
from . import views

path('', include('authentication.urls')),
