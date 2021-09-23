from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Music(models.Model):
    artist = models.ForeignKey("Idol", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    seconds = models.IntegerField(help_text="秒数")
    lower_title = models.CharField(max_length=255)

    @classmethod
    def get_titles(cls, artist):
        return cls.objects.filter(artist=artist).values_list("title", flat=True)\

    @classmethod
    def get_lower_title(cls, artist):
        return cls.objects.filter(artist=artist).values_list("identifications_title", flat=True)


@receiver(pre_save, sender=Music)
def create_lower_title(sender, instance, *args, **kwargs):
    """
    save時に動く処理、タイトルからスペースを取ってlowercaseで保存する
    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
    instance.identifications_title = instance.title.replace(" ", "").lower()
