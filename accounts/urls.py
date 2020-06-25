from django.urls import path
from .views import register, login, panel

urlpatterns = [
    path('register', register , name='register'),
    path('login', login, name='login'),
    path('panel', panel, name='panel'),
]