from django.urls import path
from .views import list_broadcast_standards, get_broadcast_standard

urlpatterns = [
    path('broadcast_standards/', list_broadcast_standards, name='list_broadcast_standards'),
    path('broadcast_standards/<str:country>/', get_broadcast_standard, name='get_broadcast_standard'),
]