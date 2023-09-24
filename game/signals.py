
from django.db.models.signals import *
import requests, re
from django.dispatch import receiver

from game.models import *
from x_game.settings import BASE_DIR


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


def parser(param):
    col_eps = int(param.url_num)
    url = param.url_an
    resul = []
    for i in range(1, col_eps + 1):
        url_mod = ''
        ser = "/" + str(i) + "/"
        for j in range(1, col_eps + 1):
            temp = "/" + str(j) + "/"
            if temp in url:
                url_mod = url.replace(temp, ser)
        index = requests.get(url_mod).text

        index = re.findall('src="(.*)"', index)
        for k in range(0, len(index)):
            if "mangavost" in index[k]:
                resul.append(str(index[k]).split(' ')[0].replace('"', ''))
    return resul


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


@receiver(pre_save, sender=BaseTitle, )
def post_save_url(sender, instance, **kwargs):
    if sender == BaseTitle:
        resul = parser(instance)
        obj = VideoTitle.objects
        for i in range(0, len(resul)):
            obj.create(video=resul[i], idBase=instance)
