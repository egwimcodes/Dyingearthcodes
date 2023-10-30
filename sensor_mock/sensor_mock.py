import requests
from datetime import datetime
import random
import json
#############################
#
# You should change that to your demon
#
#############################
url = 'http://miau.de'



#######################################################
# After here no change should needed
#######################################################

datetimeobject = datetime.now()

# create the json object to send
myobj = {"time": datetimeobject.strftime("%Y-%m-%d %H:%M"), 'sensorData': [random.uniform(1,255), random.uniform(-12000,12000)], 'sensorId': 'sEnSoRiDRandom123'}

x = requests.post(url, json = myobj)
print(x.text)
