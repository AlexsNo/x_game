from django.conf.urls.static import static
from django.urls import path

from game.views import *
from x_game import settings

game_urls = [
    path('',redirect_index),
    path('anime-point/', AnimeHome.as_view(), name="index"),
    path('anime-point/about', AboutShow.as_view(), name="about"),
    path('anime-point/all_news', AllShow.as_view(), name="all_news"),
    path('anime-point/review', AboutShow.as_view(), name="review"),
    path('anime-point/shop', AboutShow.as_view(), name="shop"),
    path('anime-point/contact', ContactShow.as_view(), name="contact"),
    path('anime-point/category', GenreShow.as_view(), name="genre_show"),
    path('anime-point/category/<slug:cat_id>', CategoryShow.as_view(), name="category_show"),
    path('anime-point/<slug:title_id>', ShowPost.as_view(), name="show_post"),
    path('anime-point/account/register', SignUp.as_view(), name="register"),
    path('anime-point/account/login', Login.as_view(), name="login"),
    path('anime-point/account/logout', logout_user, name="logout"),

]
if settings.DEBUG:
    game_urls += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
