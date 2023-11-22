
def sensor_code_generator(unregistered_sensors):
    for i in range(unregistered_sensors):
        uuid_code = uuid.uuid4()
        main_uuid = str(uuid_code).upper().replace('-', '')[:20]
        formatted = "DE-" + \
            '-'.join([main_uuid[i:i + 5]
                     for i in range(0, len(main_uuid), 5)])
        try:
            # Try creating the new sensor entry
            SensorQr.objects.create(sensor_qr=formatted)
        except IntegrityError:
            # If there's a duplicate (IntegrityError), delete one of them and then create the new entry
            duplicate_sensor = SensorQr.objects.filter(
                sensor_qr=formatted).first()
            if duplicate_sensor:
                duplicate_sensor.delete()
            SensorQr.objects.create(sensor_qr=formatted)
