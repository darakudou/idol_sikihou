from django.db import models


class Music(models.Model):
    artist = models.ForeignKey("Idol", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
