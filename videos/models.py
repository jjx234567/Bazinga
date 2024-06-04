from django.db import models
from django.conf import settings

class Video(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    link = models.CharField(max_length = 1000)
    image = models.FileField(upload_to="video_images/", blank=True)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)