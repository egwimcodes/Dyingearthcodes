from celery import shared_task 
from django.contrib.auth import get_user
from .email import send_Reminder_Email, sensors_Reports_Email
  
@shared_task
def sensorsReminder():
    send_Reminder_Email()


@shared_task
def sensorsReports():
    sensors_Reports_Email()
