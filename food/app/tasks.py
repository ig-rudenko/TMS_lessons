from celery import shared_task


@shared_task
def home_page_task(string: str) -> str:
    print("Hello World!", string)
    return "OK"
