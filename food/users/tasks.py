from celery import shared_task


@shared_task
def test_a(a, b):
    print("TASK: test_a(a,b)=", a, b)
    return a + b
