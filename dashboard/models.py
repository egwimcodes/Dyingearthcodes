from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# ####### Sensor User model start ########labdooadmin
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=100, null=True , blank=True)
    city = models.CharField(max_length=100, null=True , blank=True) 
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.png')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
# ####### Sensor User model end ########


# ####### Sensor model start ########
class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sensor_set')
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    counter = models.FloatField(default=20.0)
    token = models.CharField(max_length=100, null=True, blank=True, default='No Location Added')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sensors'
# ####### Sensor model end ########


# ####### Sensor Qr Code start ########
class SensorQr(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE, null=True, blank=True)
    sensor_qr = models.CharField(max_length=27, null=True, blank=True, unique=True)
    qr_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.sensor_qr

    class Meta:
        verbose_name_plural = "Sensor Qr Code"
# ####### Sensor Qr Code end #######


# ####### Payloads model start ########
class Payloads(models.Model):
    sensor = models.OneToOneField(Sensor, on_delete=models.CASCADE, related_name='payload_set')
    time = models.DateTimeField(null=True, blank=True, default=timezone.now)
    sensor_identifier = models.CharField(max_length=100, null=True, blank=True)  # Change 'sensor_id' to 'sensor_identifier' or another unique name
    soil_moisture = models.FloatField(default=1.0)
    temperature = models.FloatField(default=1.0)
    humidity = models.FloatField(default=1.0)
    payload_name = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return str(self.sensor)

    class Meta:
        verbose_name_plural = 'Payloads'
# ####### Payloads model end ########



# ################# Todo model start ##################
class TodoApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_set')
    text = models.CharField(max_length=500, null=True, blank=True)
    done = models.BooleanField(default=False)
    time = models.DateTimeField(null=True, blank=True, default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name_plural = 'Todo App'
# ################# Todo model end  ##################
#
#
#
#
# # ######### Soil Moisture model start ##########
# class SoilMoisture(models.Model):
#     payload = models.OneToOneField(Payloads, on_delete=models.CASCADE)
#     value = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.payload)
#
#     class Meta:
#         verbose_name_plural = 'Soil Moisture'
# # ######### Soil Moisture model end ##########
#
#
# # ################# Soil Moisture model Content start ##################
# class SoilMoistureMineralContent(models.Model):
#     nitrogen = models.FloatField(default=0.0)
#     phosphorus = models.FloatField(default=0.0)
#     potassium = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.nitrogen) + " " + str(self.phosphorus) + " " + str(self.potassium)
#
#     class Meta:
#         verbose_name_plural = 'Soil Moisture Mineral Content'
# # ################# Soil Moisture model content end ##################
#
#
# # ################# Ph Level model start ##################
# class PhLevel(models.Model):
#     payload = models.OneToOneField(Payloads, on_delete=models.CASCADE)
#     value = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.payload)
#
#     class Meta:
#         verbose_name_plural = 'Ph Level'
# # ################# ph level model end##################
#
#
# # ################# ph level model content start ##################
# class PhLevelMineralContent(models.Model):
#     nitrogen = models.FloatField(default=0.0)
#     phosphorus = models.FloatField(default=0.0)
#     potassium = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.nitrogen) + " " + str(self.phosphorus) + " " + str(self.potassium)
#
#     class Meta:
#         verbose_name_plural = 'Ph Level Mineral Content'
# # #################  ph level model content end ##################
#
#
# # ################# Salinity model start ##################
# class Salinity(models.Model):
#     payload = models.OneToOneField(Payloads, on_delete=models.CASCADE)
#     value = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.payload)
#
#     class Meta:
#         verbose_name_plural = 'Salinity'
# # ################# Salinity model end ###################
#
#
# # ################# Salinity model content start ##################
# class SalinityMineralContent(models.Model):
#     nitrogen = models.FloatField(default=0.0)
#     phosphorus = models.FloatField(default=0.0)
#     potassium = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.nitrogen) + " " + str(self.phosphorus) + " " + str(self.potassium)
#
#     class Meta:
#         verbose_name_plural = 'Salinity Mineral Content'
# # ################# Salinity model start ##################
#
#
# # ################# Air-humidity model start ##################
# class AirHumidity(models.Model):
#     payload = models.OneToOneField(Payloads, on_delete=models.CASCADE)
#     value = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.payload)
#
#     class Meta:
#         verbose_name_plural = 'Air Humidity'
# # ################# Air-humidity model end ##################
#
#
# # ################# Air-humidity model content start ##################
# class AirHumidityMineralContent(models.Model):
#     nitrogen = models.FloatField(default=0.0)
#     phosphorus = models.FloatField(default=0.0)
#     potassium = models.FloatField(default=0.0)
#
#     def __str__(self):
#         return str(self.nitrogen) + " " + str(self.phosphorus) + " " + str(self.potassium)
#
#     class Meta:
#         verbose_name_plural = 'Air Humidity Mineral Content'
# # ################# Air-humidity model content end ##################
