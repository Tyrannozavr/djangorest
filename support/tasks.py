from time import sleep

from django.core.mail import send_mail

from djangoProject.celery import app


@app.task
def send(email):
    # send_mail('change status', 'status your task has been changed', 'dimon@gmail.com', [email], fail_silently=False)
    sleep(20)
    return True
