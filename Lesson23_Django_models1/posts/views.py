from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q, F
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpRequest
from django.core.handlers.wsgi import WSGIRequest

from .models import Note, User
from .service import create_note


def home_page_view(request: HttpRequest):
    """
    Обязательно! Каждая функция view должна принимать первым параметром request.
    """

    queryset = (
        Note.objects.all()  # Получение всех объектов из таблицы Note
        .select_related("user")  # Вытягивание связанных данных из таблицы User в один запрос
        .prefetch_related("tags")  # Вытягивание связанных данных из таблицы Tag в отдельные запросы
        .annotate(
            # Создание нового вычисляемого поля username из связанной таблицы User
            username=F('user__username'),

            # Создание массива уникальных имен тегов для каждой заметки
            tag_names=ArrayAgg('tags__name', distinct=True)
        )
        .values("uuid", "title", "created_at", "username", "tag_names")  # Выбор только указанных полей для результата
        .distinct()  # Убирание дубликатов, если они есть
        .order_by("-created_at")  # Сортировка результатов по убыванию по полю created_at
    )

    print(queryset.query)

    return render(request, "home.html", {"notes": queryset[:100]})


def filter_notes_view(request: WSGIRequest):
    """
    Фильтруем записи по запросу пользователя.
    HTTP метод - GET.
    Обрабатывает URL вида: /filter/?search=<text>
    """

    search: str = request.GET.get("search", "")  # `get` - получение по ключу. Если такого нет, то - "",

    # Если строка поиска не пустая, то фильтруем записи по ней.
    if search:
        # ❗️Нет обращения к базе❗️
        # Через запятую запросы формируются c ❗️AND❗️
        # notes_queryset = Note.objects.filter(title__icontains=search, content__icontains=search)
        # SELECT "posts_note"."uuid", "posts_note"."title", "posts_note"."content", "posts_note"."created_at"
        # FROM "posts_note" WHERE (
        # "posts_note"."title" LIKE %search% ESCAPE '\' AND "posts_note"."content" LIKE %search% ESCAPE '\')

        # ❗️Все импорты сверху файла❗️
        # from django.db.models import Q

        notes_queryset = Note.objects.filter(title__icontains=search, content__icontains=search)
        # Аналогия
        notes_queryset = Note.objects.filter(Q(title__icontains=search), Q(content__icontains=search))

        # Оператор - `|` Означает `ИЛИ`.
        # Оператор - `&` Означает `И`.
        # notes_queryset = Note.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        notes_queryset = Note.objects.filter(title=search)

    else:
        # Если нет строки поиска.
        notes_queryset = Note.objects.all()  # Получение всех записей из модели.

    notes_queryset = notes_queryset.order_by("-created_at")  # ❗️Нет обращения к базе❗️

    # SELECT "posts_note"."uuid", "posts_note"."title", "posts_note"."content", "posts_note"."created_at"
    # FROM "posts_note" WHERE
    # ("posts_note"."title" LIKE %python% ESCAPE '\' OR "posts_note"."content" LIKE %python% ESCAPE '\')
    # ORDER BY "posts_note"."created_at" DESC

    print(notes_queryset.query)

    context: dict = {
        "notes": notes_queryset[:100],
        "search_value_form": search,
    }
    return render(request, "home.html", context)


@login_required
def create_note_view(request: WSGIRequest):
    if request.method == "POST":
        note = create_note(request)
        return HttpResponseRedirect(reverse('show-note', args=[note.uuid]))

    # Вернется только, если метод не POST.
    return render(request, "create_form.html")


def show_note_view(request: WSGIRequest, note_uuid):
    try:
        note = Note.objects.get(uuid=note_uuid)  # Получение сразу только ОДНОЙ записи.

    except Note.DoesNotExist:
        # Если не найдено такой записи.
        raise Http404

    return render(request, "note.html", {"note": note})


def delete_note_view(request: WSGIRequest, note_uuid: str):
    if request.method == "POST":
        Note.objects.filter(uuid=note_uuid).delete()
    return HttpResponseRedirect(reverse("home"))


def register(request: WSGIRequest):
    if request.method != "POST":
        return render(request, "registration/register.html")
    print(request.POST)
    if not request.POST.get("username") or not request.POST.get("email") or not request.POST.get("password1"):
        return render(
            request,
            "registration/register.html",
            {"errors": "Укажите все поля!"}
        )
    print(User.objects.filter(
            Q(username=request.POST["username"]) | Q(email=request.POST["email"])
    ))
    # Если уже есть такой пользователь с username или email.
    if User.objects.filter(
            Q(username=request.POST["username"]) | Q(email=request.POST["email"])
    ).count() > 0:
        return render(
            request,
            "registration/register.html",
            {"errors": "Если уже есть такой пользователь с username или email"}
        )

    # Сравниваем два пароля!
    if request.POST.get("password1") != request.POST.get("password2"):
        return render(
            request,
            "registration/register.html",
            {"errors": "Пароли не совпадают"}
        )

    # Создадим учетную запись пользователя.
    # Пароль надо хранить в БД в шифрованном виде.
    User.objects.create_user(
        username=request.POST["username"],
        email=request.POST["email"],
        password=request.POST["password1"]
    )
    return HttpResponseRedirect(reverse('home'))
