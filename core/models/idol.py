from django.db import models


class Idol(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Music(models.Model):
    artist = models.ForeignKey("Idol", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    seconds = models.IntegerField()
