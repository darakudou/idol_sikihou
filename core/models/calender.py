import re

from django.db import models


class Calender(models.Model):
    idol = models.ForeignKey("core.Idol", on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)
    start = models.DateField()  # start["date"] あまり意味の無い項目かも..
    end = models.DateField()  # end["date"] あまり意味の無い項目かも..
    location = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    class Meta:
        unique_together = ("summary", "start")

    @property
    def start_time(self):
        try:
            return re.search("START.*[0-9]:[0-9][0-9]", self.description)[0].replace("START ", "")
        except TypeError:
            pass
        try:
            return re.search("ST.*[0-9]:[0-9][0-9]", self.description)[0].replace("ST", "")
        except TypeError:
            pass

    @property
    def is_online(self):
        if "配信" in self.summary:
            return True
        return False
