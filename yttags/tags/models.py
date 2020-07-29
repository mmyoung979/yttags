# Django imports
from django.db import models


class Video(models.Model):
    youtube_id = models.CharField(max_length=50, blank=True)
