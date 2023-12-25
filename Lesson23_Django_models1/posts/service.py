from django.core.handlers.wsgi import WSGIRequest

from posts.models import Note, Tag


def create_note(request: WSGIRequest) -> Note:
    note = Note.objects.create(
        title=request.POST["title"],
        content=request.POST["content"],
        user=request.user,
        image=request.FILES.get("noteImage"),
    )

    # Если нет тегов, то будет пустой список
    tags_names: list[str] = request.POST.get("tags", "").split(",")
    tags_names = list(map(str.strip, tags_names))  # Убираем лишние пробелы

    tags_objects: list[Tag] = []
    for tag in tags_names:
        tag_obj, created = Tag.objects.get_or_create(name=tag)
        tags_objects.append(tag_obj)

    note.tags.set(tags_objects)  # `set` это переопределение всех тегов для заметки.

    return note
