from Fruit_Shop.celery import app

from user.service import send


@app.task
def send_welcome_email(user_email):
    send(user_email)
