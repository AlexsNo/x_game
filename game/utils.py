from django.utils.deprecation import MiddlewareMixin

from game.models import *

menu = [{"title": "Всё и Вся", "url_name": "all_news"},
        {"title": "Обзоры", "url_name": "review"},
        {"title": "Магазин", "url_name": "shop"},
        {"title": "Главная страница", "url_name": "index"},
        {"title": "Категории", "url_name": "#"},
        {"title": "Все Категории", "url_name": "genre_show"},
        {"title": "Контакты", "url_name": "contact"},
        {"title": "О Cайте", "url_name": "about"}, ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        context["category_menu"] = CategoryTitle.objects.all()

        return context

