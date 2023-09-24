import os
from datetime import datetime

from django.db import models

from django.urls import reverse

from x_game.settings import BASE_DIR


def content_file_name(instance, filename):
    ext = str(filename).split('.')[1]
    count = 0
    path_name = ''
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    filename = str(instance) + "_" + "0" + "." + ext
    if instance.__class__ == BaseTitle:
        path_name = 'imgTitle/%d/%d/%d/%s' % (year, month, day, filename)
    elif instance.__class__ == PhotoTitle:
        path_name = 'imgTitleAll/%d/%d/%d/%s' % (year, month, day, filename)
    elif instance.__class__ == Genre:
        path_name = 'category/%d/%s' % (year, filename)
    elif instance.__class__ == Banner:
        path_name = 'icon/%d/%s' % (year, filename)
    elif instance.__class__ == VideoTitle:
        path_name = 'video/%d/%s' % (year, filename)

    path_name_all = os.path.join(BASE_DIR, os.path.normpath("media\\" + path_name))
    if not os.path.exists(os.path.dirname(path_name_all)):
        os.mkdir(os.path.dirname(path_name_all))
    path_dir = os.listdir(os.path.dirname(path_name_all))
    for i in path_dir:
        if i == filename.replace(" ", "_"):
            filename = filename.replace("_" + str(count), "_" + str(count + 1))
            count += 1
    if instance.__class__ == BaseTitle:
        return 'imgTitle/%d/%d/%d/%s' % (year, month, day, filename)
    elif instance.__class__ == PhotoTitle:
        return 'imgTitleAll/%d/%d/%d/%s' % (year, month, day, filename)
    elif instance.__class__ == Genre:
        return 'category/%d/%s' % (year, filename)
    elif instance.__class__ == Banner:
        return 'icon/%d/%s' % (year, filename)
    elif instance.__class__ == VideoTitle:
        return 'video/%d/%s' % (year, filename)


# ---------------------------------------Base model our Title---------------------------------------
class BaseTitle(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")  # Name Title
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    isPub = models.BooleanField(default=True, verbose_name="Публикация")
    datePub = models.DateField(auto_now_add=True, verbose_name="Дата публикации")  # Date create title in DB
    dateChange = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")  # Date change title in DB
    photo = models.ImageField(upload_to=content_file_name, verbose_name="Распол. основного фото")
    contentSM = models.CharField(max_length=500, verbose_name="Краткое описание")  # Small description
    contentMain = models.TextField()  # All description
    catId = models.ForeignKey('CategoryTitle', on_delete=models.PROTECT, verbose_name="Категория")  # Category title
    statId = models.ForeignKey('StateTitle', on_delete=models.PROTECT, verbose_name="Состояние")
    url_an = models.CharField(max_length=255, verbose_name="Ссылка на аниме", null=True)
    url_num = models.IntegerField(verbose_name="Количество серий", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тайтл-Аниме"
        verbose_name_plural = "Тайтл-Аниме"
        ordering = ['datePub', 'title']

    def get_absolute_url(self):
        return reverse('show_post', kwargs={"title_id": self.slug, })




# Category for Title
class CategoryTitle(models.Model):
    category = models.CharField(max_length=255, unique=True, verbose_name="Категория")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to=content_file_name, verbose_name="Фото", blank=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Тайтл-Категория"
        verbose_name_plural = "Тайтл-Категория"

    def get_absolute_url(self):
        return reverse('category_show', kwargs={"cat_id": self.slug, })


# Comment for Title
class CommentTitle(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.CharField(max_length=50, verbose_name="Email")
    comment = models.TextField(max_length=600, verbose_name="Комментарий")
    idBase = models.ForeignKey('BaseTitle', on_delete=models.CASCADE, verbose_name="Заголовок Тайтла")
    datePub = models.DateField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Тайтл-Комментарий"
        verbose_name_plural = "Тайтл-Комментарий"
        ordering = ['pk']


# Video for Title
class VideoTitle(models.Model):
    video = models.CharField(max_length=600, verbose_name="URL")
    idBase = models.ForeignKey('BaseTitle', on_delete=models.CASCADE, verbose_name="Заголовок Тайтла")

    def __str__(self):
        return self.idBase.slug

    class Meta:
        verbose_name = "Тайтл-Видео"
        verbose_name_plural = "Тайтл-Видео"


# Photos for Title
class PhotoTitle(models.Model):
    pathPhoto = models.ImageField(upload_to=content_file_name, verbose_name="Распол. фото")  # Path all photo title
    idBase = models.ForeignKey('BaseTitle', on_delete=models.CASCADE, verbose_name="Заголовок Тайтла")

    class Meta:
        verbose_name = "Тайтл-Изображение"
        verbose_name_plural = "Тайтл-Изображение"

    def __str__(self):
        return self.idBase.slug


# Reviews for Title


class ReviewsTitle(models.Model):
    reviews = models.TextField(verbose_name="Обзор")
    idBase = models.ForeignKey('BaseTitle', on_delete=models.CASCADE, verbose_name="Заголовок Тайтла")

    def __str__(self):
        return self.reviews

    class Meta:
        verbose_name = "Тайтл-Обзоры"
        verbose_name_plural = "Тайтл-Обзоры"


# Tags Title for Title
class TagsTitle(models.Model):
    idBase = models.ForeignKey('BaseTitle', on_delete=models.CASCADE, verbose_name="Заголовок Тайтла")
    idGenre = models.ManyToManyField('Genre', verbose_name="Жанр", related_name="genreSet")  # Id tags from BD TagsT
    idTag = models.ManyToManyField('TagsT', verbose_name="Тэг", blank=True, related_name="tagSet")

    class Meta:
        verbose_name = "Тайтл-Тэги"
        verbose_name_plural = "Тайтл-Тэги"

    def __str__(self):
        return self.idBase.title


# State Title
class StateTitle(models.Model):
    tag = models.CharField(max_length=255, unique=True, verbose_name="Состояние тайтла")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Тайтл-Состояние"
        verbose_name_plural = "Тайтл-Состояние"

    def get_absolute_url(self):
        return reverse('category_show', kwargs={"cat_id": self.slug, })


# Genre
class Genre(models.Model):
    tag = models.CharField(max_length=255, unique=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    pathPhoto = models.ImageField(upload_to=content_file_name, verbose_name="Распол. фото", blank=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Тайтл-Жанр"
        verbose_name_plural = "Тайтл-Жанр"

    def get_absolute_url(self):
        return reverse('category_show', kwargs={"cat_id": self.slug, })


# Tag
class TagsT(models.Model):
    tag = models.CharField(max_length=255, unique=True, verbose_name="Тэг")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Тайтл-Тэг"
        verbose_name_plural = "Тайтл-Тэг"

    def get_absolute_url(self):
        return reverse('category_show', kwargs={"cat_id": self.slug, })


# Banners
class Banner(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to=content_file_name, verbose_name="Распол. банера")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Банеры"
        verbose_name_plural = "Банеры"


# ---------------------------------------Base model Shop---------------------------------------
class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Наименование продукта")  # Name Product
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")
    price = models.FloatField(verbose_name="Цена")
    isPub = models.BooleanField(default=True, verbose_name="Публикация")
    datePub = models.DateField(auto_now_add=True, verbose_name="Дата публикации")  # Date create product in DB
    dateChange = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")  # Date change product in DB
    photo = models.ImageField(upload_to="imgShop/%Y/%m/%d", verbose_name="Распол. основного фото")
    contentAdd = models.TextField(verbose_name="Доп.описание")  # Additional description Product
    content = models.TextField(verbose_name="Описание продукта")  # All description Product
    tagId = models.ForeignKey('TagsShop', on_delete=models.PROTECT, verbose_name="Категория")  # Category product

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазин"
        ordering = ['datePub', 'name']


# Category Shop for Product
class CategoryShop(models.Model):
    idCat = models.ForeignKey('CategoryS', on_delete=models.CASCADE, verbose_name="Категория")
    idShop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name="Заголовок")

    class Meta:
        verbose_name = "Магазин-категории"
        verbose_name_plural = "Магазин-категории"


# Category
class CategoryS(models.Model):
    category = models.CharField(max_length=255, unique=True, verbose_name="Категория")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Магазин-К"
        verbose_name_plural = "Магазин-К"


# Tags
class TagsShop(models.Model):
    tag = models.CharField(max_length=255, unique=True, verbose_name="Тэг")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = "Магазин-Теги"
        verbose_name_plural = "Магазин-Теги"

    def __str__(self):
        return self.tag


# Reviews for Product
class ReviewsShop(models.Model):
    reviews = models.TextField(verbose_name="Обзор")
    idShop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name="Заголовок")

    def __str__(self):
        return self.reviews

    class Meta:
        verbose_name = "Магазин-Обзоры"
        verbose_name_plural = "Магазин-Обзоры"


# Photos for Product
class PhotoShop(models.Model):
    pathPhoto = models.ImageField(upload_to="imgShopAll/%Y/%m/%d", verbose_name="Путь фото")  # Path all photo title
    idShop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name="Заголовок")

    def __str__(self):
        return self.pathPhoto

    class Meta:
        verbose_name = "Магазин-Фото"
        verbose_name_plural = "Магазин-Фото"
