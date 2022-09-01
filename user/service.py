from django.core.mail import send_mail

subject = 'Welcome to the Fruit Shop!'
message = """You was registrated in Fruit Shop!
 
Best regards,
Fruit Shop Team
"""


def send(user_email):
    send_mail(
        subject,
        message,
        'npythontest@mail.ru',
        [user_email],
        fail_silently=False,
    )
