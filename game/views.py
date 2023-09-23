import time

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import *

from game.forms import *
from game.utils import *


class AnimeHome(DataMixin, ListView):
    model = BaseTitle
    template_name = "game/index.html"
    context_object_name = "title_object"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        srj = self.get_user_context(banner=Banner.objects.all(),
                                    title="Anime-Point",
                                    tags_post=TagsTitle.objects.all(),
                                    article="Коллекции")
        context = dict(list(context.items()) + list(srj.items()))
        return context


class ShowPost(DataMixin, ListView):
    model = BaseTitle
    template_name = "game/show_post.html"
    context_object_name = "title_object"
    slug_url_kwargs = "title_id"

    def post(self, request, *args, **kwargs):
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            data = request.POST
            user = request.user
            CommentTitle.objects.create(name=user.first_name, email=user.email,
                                        comment=data["comment"], idBase=self.get_queryset()[0])

            return JsonResponse({"status": "Success"})
        else:
            return JsonResponse({"status": "No success"})

    def get_queryset(self):
        return BaseTitle.objects.filter(slug=self.kwargs['title_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = TagsTitle.objects.get(idBase_id=self.get_queryset()[0].pk)
        srj = self.get_user_context(icon=Banner.objects.all(),
                                    article="Больше Постов",
                                    comment=CommentTitle.objects.filter(idBase_id=self.get_queryset()[0].pk),
                                    title=context["title_object"][0],
                                    genre=Genre.objects.all(),
                                    tags_id=tags.idTag.all(),
                                    tags_post=TagsTitle.objects.all(),
                                    form=CommentForm(),
                                    photoTitle=PhotoTitle.objects.filter(idBase_id=self.get_queryset()[0].pk),

                                    )
        context = dict(list(context.items()) + list(srj.items()))
        return context


class GenreShow(DataMixin, ListView):
    model = Genre
    template_name = "game/genre_show.html"
    context_object_name = "genre_object"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        BD_tags = TagsTitle.objects.all()
        Genre_count = {}
        for j in Genre.objects.all():
            count = 0
            for i in BD_tags:
                if i.idGenre.filter(slug=j.slug).count() == 1:
                    count += 1
            if count >= 1:
                Genre_count.update({j.slug: count})
        srj = self.get_user_context(title="Все Категории",
                                    Genre_count=Genre_count, )
        context = dict(list(context.items()) + list(srj.items()))
        return context


class AboutShow(DataMixin, ListView):
    model = BaseTitle
    template_name = "game/about.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        srj = self.get_user_context(title="О сайте", )
        context = dict(list(context.items()) + list(srj.items()))
        return context


class ContactShow(DataMixin, ListView):
    model = BaseTitle
    template_name = "game/contact.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        srj = self.get_user_context(title="Контакты")
        context = dict(list(context.items()) + list(srj.items()))
        return context


class CategoryShow(DataMixin, ListView):
    model = TagsTitle
    template_name = "game/category_show.html"
    context_object_name = "tags_post"
    slug_url_kwargs = "cat_id"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        BD_tags = TagsTitle.objects.all()
        srj = self.get_user_context()
        context = dict(list(context.items()) + list(srj.items()))
        arr_genre = []
        arr_tag = []

        for i in BD_tags:
            if i.idGenre.filter(slug=self.kwargs['cat_id']):
                arr_genre.append(i.idBase.slug)
            if i.idTag.filter(slug=self.kwargs['cat_id']):
                arr_tag.append(i.idBase.slug)

        if len(arr_genre) >= 1:
            context["title_object"] = BaseTitle.objects.filter(slug__in=arr_genre)
            context["article"] = Genre.objects.filter(slug=self.kwargs['cat_id'])[0]
        elif len(arr_tag):
            context["title_object"] = BaseTitle.objects.filter(slug__in=arr_tag)
            context["article"] = TagsT.objects.filter(slug=self.kwargs['cat_id'])[0]
        elif len(BaseTitle.objects.filter(catId__slug=self.kwargs["cat_id"])) >= 1:
            context["title_object"] = BaseTitle.objects.filter(catId__slug=self.kwargs["cat_id"])
            context["article"] = CategoryTitle.objects.filter(slug=self.kwargs["cat_id"])[0]
        elif len(BaseTitle.objects.filter(statId__slug=self.kwargs["cat_id"])) >= 1:
            context["title_object"] = BaseTitle.objects.filter(statId__slug=self.kwargs["cat_id"])
            context["article"] = StateTitle.objects.filter(slug=self.kwargs["cat_id"])[0]
        else:
            context["article"] = "Упс. Аниме тут нет("

        return context


class AllShow(DataMixin, ListView):
    model = BaseTitle
    template_name = "game/all_show.html"
    context_object_name = "title_object"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = Banner.objects.all()
        srj = self.get_user_context(title="Всё и Вся",
                                    tags_post=TagsTitle.objects.all(),
                                    article="Вся Коллекция")
        context = dict(list(context.items()) + list(srj.items()))
        return context


def redirect_index(request):
    return redirect('/anime-point/')


class SignUp(DataMixin, CreateView):
    model = User
    template_name = "game/register.html"
    context_object_name = "title_object"
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = self.get_user_context()
        context["form"] = form
        if request.method == "POST":
            if form.is_valid():
                data1 = form.cleaned_data
                user = User.objects.create_user(username=data1["username"],
                                         first_name=data1["first_name"],
                                         email=data1["email"],)
                user.set_password(data1["password"])
                user.save()
                return redirect("index")
            else:
                print(form.errors.as_data())
        return render(request, self.template_name, context)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        srj = self.get_user_context(title="Регистрация")
        context = dict(list(context.items()) + list(srj.items()))
        return context


class Login(DataMixin, LoginView):
    template_name = "game/login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        srj = self.get_user_context(title="Вход")
        context = dict(list(context.items()) + list(srj.items()))
        return context


def logout_user(request):
    logout(request)
    return redirect("index")
