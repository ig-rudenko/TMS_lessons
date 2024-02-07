from celery import shared_task
from django.contrib.auth import get_user_model

from users.email import ConfirmUserRegisterEmailSender


User = get_user_model()


@shared_task
def test_a(a, b):
    print("TASK: test_a(a,b)=", a, b)
    return a + b


@shared_task(ignore_result=True)
def delete_user(user_id: int):
    print("TASK: delete_user(user_id)=", user_id)
    User.objects.filter(id=user_id, is_active=False).delete()


@shared_task(ignore_result=True, max_retries=3, autoretry_for=(Exception,))
def send_register_email_task(domain: str, user_id: int):
    print("TASK: send_register_email_task (", domain, user_id, ")")
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        pass
    else:
        ConfirmUserRegisterEmailSender(domain, user).send_mail()
