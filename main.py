import tinytuya
import psutil
import json
import time

f = open('devices.json')
deviceData = json.load(f)
DEVICE_ID = deviceData[0].get('id')
DEVICE_KEY = deviceData[0].get('key')
f.close()
f = open('snapshot.json')
deviceData = json.load(f)
DEVICE_IP = deviceData.get('devices')[0].get('ip')
f.close()

#Outlet stuff
d = tinytuya.OutletDevice(DEVICE_ID, DEVICE_IP, DEVICE_KEY)
d.set_version(3.3)
#Bettery stuff
battery = psutil.sensors_battery()
while battery.power_plugged == True:
    batteryPerc = psutil.sensors_battery().percent
    if(batteryPerc >= 80):
        d.turn_off()
    print("Battery: " + str(batteryPerc) + "%")
    print("Outlet status: " + str(d.status()))
    time.sleep(60)