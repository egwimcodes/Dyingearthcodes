from django.core.mail import send_mail
from django.conf import settings


def mailTest(name):
    send_mail(
        subject="Testing for the subject ", 
        message=f"Here is what i want to tell you{name} ",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['officialsnowwisdom@gmail.com']
    )
    

