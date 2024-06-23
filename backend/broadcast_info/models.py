from django.db import models

class BroadcastStandard(models.Model):
    country = models.CharField(max_length=100)
    json_data = models.JSONField()