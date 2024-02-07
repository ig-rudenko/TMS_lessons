from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives

User = get_user_model()


@shared_task
def home_page_task(string: str) -> str:
    print("Hello World!", string)
    return "OK"


@shared_task(ignore_result=True)
def send_periodical_email():
    for user in User.objects.all():
        if user.is_active:
            send_email_task.delay(user.email, "Рассылка", "<h2>Новые рецепты!</h2>")


@shared_task(ignore_result=True, max_retries=3, autoretry_for=(Exception,))
def send_email_task(email: str, subject: str, message: str):
    mail = EmailMultiAlternatives(
        subject=subject,
        to=[email]
    )
    mail.attach_alternative(message, "text/html")
    mail.send()
