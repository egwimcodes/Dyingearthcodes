from django.contrib import admin
from .models import User, Sensor, Payloads,TodoApp, SoldSensorQr, UnSoldSensorQr

# Register your models here.
admin.site.register(User)
admin.site.register(Sensor)
admin.site.register(Payloads)
admin.site.register(TodoApp)
admin.site.register(SoldSensorQr)
admin.site.register(UnSoldSensorQr)


