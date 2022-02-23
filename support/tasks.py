from djangoProject.celery import app
from django.core.mail import send_mail
from time import sleep


@app.task
def send(email):
    # send_mail('change status', 'status your task has been changed', 'dimon@gmail.com', [email], fail_silently=False)
    sleep(20)
    return True
