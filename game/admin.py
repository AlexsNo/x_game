from django.contrib import admin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

from game.models import *


class BaseTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'isPub', 'datePub', 'photo', 'contentSM', 'catId', 'statId']
    prepopulated_fields = {"slug": ("title",)}


class CategoryTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'slug', 'photo']
    prepopulated_fields = {"slug": ("category",)}


class CommentTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'idBase', 'comment']


class VideoTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'idBase', 'video']


class PropertyImageInline(admin.StackedInline):
    model = PhotoTitle
    extra = 3


class PhotoTitleAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = ['id', 'title', 'slug', 'isPub', 'datePub', 'photo', 'contentSM', 'catId', 'statId']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = BaseTitle


class PhotoTitlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'idBase', 'pathPhoto']


class ReviewsTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'idBase', 'reviews']


class TagsTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'idBase']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},

    }


class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'slug', 'pathPhoto']
    prepopulated_fields = {"slug": ("tag",)}


class TagsTAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'slug']
    prepopulated_fields = {"slug": ("tag",)}


class StateTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'slug']
    prepopulated_fields = {"slug": ("tag",)}


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'photo']
    prepopulated_fields = {"slug": ("name",)}


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'isPub', 'datePub', 'photo', 'tagId']
    prepopulated_fields = {"slug": ("name",)}


class CategoryShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'idCat', 'idShop']


class CategorySAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'slug']
    prepopulated_fields = {"slug": ("category",)}


class TagsShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'slug']
    prepopulated_fields = {"slug": ("tag",)}


class ReviewsShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'reviews', 'idShop']


class PhotoShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'pathPhoto', 'idShop']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email']


admin.site.register(BaseTitle, PhotoTitleAdmin)
admin.site.register(CategoryTitle, CategoryTitleAdmin)
admin.site.register(CommentTitle, CommentTitleAdmin)
admin.site.register(VideoTitle, VideoTitleAdmin)
admin.site.register(ReviewsTitle, ReviewsTitleAdmin)
admin.site.register(TagsTitle, TagsTitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(CategoryShop, CategoryShopAdmin)
admin.site.register(CategoryS, CategorySAdmin)
admin.site.register(TagsShop, TagsShopAdmin)
admin.site.register(ReviewsShop, ReviewsShopAdmin)
admin.site.register(PhotoShop, PhotoShopAdmin)
admin.site.register(TagsT, TagsTAdmin)
admin.site.register(StateTitle, StateTitleAdmin)
admin.site.register(PhotoTitle, PhotoTitlesAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
