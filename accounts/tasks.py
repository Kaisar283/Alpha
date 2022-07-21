from celery import shared_task
from django.core.mail import send_mail
from Alpha.settings import EMAIL_HOST_USER


@shared_task()
def custom_send_mail(email: str, subject: str, message: str):
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
