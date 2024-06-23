from django.urls import path
from .views import create_tuner_config, list_tuner_configs

urlpatterns = [
    path('configs/', list_tuner_configs, name='list_tuner_configs'),
    path('configs/create/', create_tuner_config, name='create_tuner_config'),
]