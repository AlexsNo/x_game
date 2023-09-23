from django import template

from game.models import *

register = template.Library()


@register.simple_tag()
def get_base():
    return BaseTitle.objects.all()


@register.simple_tag()
def get_base1():
    return BaseTitle.objects.filter(title="Вторжение Кальмарки")[0]


@register.simple_tag()
def get_video():
    title = VideoTitle.objects.all()
    return {"title": title}
