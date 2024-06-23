from django.urls import path
from .views import list_streams, upload_stream

urlpatterns = [
    path('streams/', list_streams, name='list_streams'),
    path('upload/', upload_stream, name='upload_stream'),
]