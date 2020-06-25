from django.urls import path
from .views import toefl, order_details

urlpatterns = [
    path('details/<int:order_id>', order_details, name='order_details'),
    path('toefl', toefl, name='toefl'),
]