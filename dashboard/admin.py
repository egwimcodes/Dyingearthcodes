from django.contrib import admin
from .models import User, Sensor, Payloads,TodoApp, SensorQr

# Register your models here.
admin.site.register(User)
admin.site.register(Sensor)
admin.site.register(Payloads)
admin.site.register(TodoApp)
admin.site.register(SensorQr)
