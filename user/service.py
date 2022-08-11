from django.core.mail import send_mail

subject = 'Welcome to the Fruits Shop!'
message = """You was registrated in Fruits Shop!
 
Please login and enjoy!
You can find many interesting articles about fruits!
You can buy fruits!
 
Best regards,
Fruits Shop Team
"""


def send(user_email):
    send_mail(
        subject,
        message,
        'npythontest@mail.ru',
        [user_email],
        fail_silently=False,
    )
