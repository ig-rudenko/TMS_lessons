from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives

import language_tool_python

from app.models import Recipe

User = get_user_model()


@shared_task
def home_page_task(string: str) -> str:
    print("Hello World!", string)
    return "OK"


@shared_task(ignore_result=True)
def send_periodical_email():
    for user in User.objects.all():
        if user.is_active:
            send_email_task.delay(email=user.email, subject="Рассылка", message="<h2>Новые рецепты!</h2>")


@shared_task(ignore_result=True, max_retries=3, autoretry_for=(Exception,))
def send_email_task(message: str, email: str, subject: str):
    print(f"sending email `{email}`, `{subject}`, `{message}`")

    if not email or not message:
        return

    mail = EmailMultiAlternatives(
        subject=subject,
        to=[email]
    )
    mail.attach_alternative(message, "text/html")
    mail.send()


@shared_task()
def check_recipe_content(recipe_id: int) -> str:
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return ""

    text = recipe.description

    tool = language_tool_python.LanguageToolPublicAPI("ru-RU")
    matches = tool.check(text)

    styles = '<style>.error{background-color: #ffcdcd;border-radius: 2px;cursor: help;}</style>'

    text_result = ""
    last_offset = 0
    for error in matches:
        text_result += text[last_offset: error.offset]

        title = error.message + " Варианты: " + ", ".join(error.replacements[:3])
        text_replacement = (
            f'<span class="error" title="{title}">'
            f'{text[error.offset:error.offset + error.errorLength]}</span>'
        )

        text_result += text_replacement
        last_offset = error.offset + error.errorLength

    text_result += text[last_offset:]
    text_result = styles + text_result
    text_result += f"<h2>У вас было найдено: {len(matches)} ошибок"

    return text_result
