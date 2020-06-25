from django.urls import path
from .views import home, services

urlpatterns = [
    path('', home, name='home'),
    path('services', services, name='services')
]