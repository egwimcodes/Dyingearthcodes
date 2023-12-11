from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_Reminder_Email():
    User = get_user_model()
    # Get all users who meet the condition
    users = User.objects.all()

    for user in users:
        sensors = user.sensor_set.all()
        if user.sensor_set.exists():
            for s in sensors:
                if s.payload_set.soil_moisture < 30:
                    # Customize the email content based on user or any other logic
                    html_content = render_to_string('dashboard/email.html', {'user': user,'sensors': sensors, 'reminder': True})
                    text_content = strip_tags(html_content)

                    # Create EmailMultiAlternatives instance for each user
                    msg = EmailMultiAlternatives(
                        subject="Sensor Reminder from Dying Earth",
                        body=text_content,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[user.email],  # Send the email to the user's email address
                    )
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    break

def sensors_Reports_Email():
    User = get_user_model()

    # Get all users who meet the condition
    users = User.objects.all()

    for user in users:
        sensors = user.sensor_set.all()
        if user.sensor_set.exists():
            # Customize the email content based on user or any other logic
            html_content = render_to_string('dashboard/email.html', {'user': user,'sensors': sensors, 'report': True})
            text_content = strip_tags(html_content)

            # Create EmailMultiAlternatives instance for each user
            msg = EmailMultiAlternatives(
                subject="sensor Reports from Dying Earth",
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user.email],  # Send the email to the user's email address
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()