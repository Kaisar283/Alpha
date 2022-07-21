from celery import shared_task
from django.core.mail import EmailMessage
from product.models import Orders
from Alpha import settings


@shared_task()
def order_pdf_creater(owner_id: int, email: str):
    """
    Here will be generater PDF file. I will use fpdf2.
    We can generate data via owner_id
    """
    email_from = settings.EMAIL_HOST
    message = EmailMessage('This is list of orders', 'Hello your list is done!', email_from, to=[email, ])
    message.attach_file('here file path')  # for example: 'my_files/list_orders.pdf'
    message.send()
