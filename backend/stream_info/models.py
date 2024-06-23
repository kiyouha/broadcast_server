from django.db import models

class StreamInfo(models.Model):
    name = models.CharField(max_length=100)
    hls_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    section_info = models.JSONField(null=True, blank=True)