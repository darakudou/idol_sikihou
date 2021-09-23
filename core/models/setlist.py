from django.db import models


class SetList(models.Model):
    live = models.ForeignKey("core.Live", on_delete=models.CASCADE)
    music = models.ForeignKey("core.music", on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
