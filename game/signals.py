import os

from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver

from game.models import *
from x_game.settings import BASE_DIR


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@receiver(pre_delete, sender=Genre, )
@receiver(pre_delete, sender=Banner, )
@receiver(pre_delete, sender=PhotoTitle, )
@receiver(pre_delete, sender=BaseTitle, )
def post_save_image(sender, instance, **kwargs):
    if sender == PhotoTitle:
        pathPhoto = str(PhotoTitle.objects.get(pk=instance.pk).pathPhoto)
    elif sender == BaseTitle:
        pathPhoto = str(BaseTitle.objects.get(pk=instance.pk).photo)
    elif sender == Banner:
        pathPhoto = str(Banner.objects.get(pk=instance.pk).photo)
    elif sender == Genre:
        pathPhoto = str(Genre.objects.get(pk=instance.pk).pathPhoto)
    normPath = "media\\" + os.path.normpath(pathPhoto)
    path = os.path.join(BASE_DIR, normPath)
    _delete_file(path)
