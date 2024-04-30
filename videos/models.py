from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    link = models.CharField(max_length = 1000)
    image = models.FileField(upload_to="video_images/", blank=True)