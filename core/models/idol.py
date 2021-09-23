from django.db import models


class Idol(models.Model):
    name = models.CharField(unique=True, max_length=255)
    google_calender = models.CharField(max_length=255, null=True)
    is_group = models.BooleanField(default=False)
