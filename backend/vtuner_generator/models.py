from django.db import models

class TunerConfig(models.Model):
    name = models.CharField(max_length=100)
    frequency = models.IntegerField()
    bandwidth = models.IntegerField()
    modulation = models.CharField(max_length=50)