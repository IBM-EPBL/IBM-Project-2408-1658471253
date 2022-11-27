
import time
import sys
import ibmiotf.application
import ibmiotf.device
import random


#Provide your IBM Watson Device Credentials
organization = "wu5b55" 
deviceType = "crop1"
deviceId = "1234"
authMethod = "token"
authToken = "1234567890"

# Initialize GPIO 
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        
        temp=random.randint(0,100)
        Hum=random.randint(0,100)
        moisture=random.randint(0,100)
        
        data = { 'temperature' : temp, 'Humidity': Hum, 'Moisture':moisture }

        #print data
        def myOnPublishCallback():
            print ("Temperature = " + str(temp)+" C Humidity = " + str(hum)+ " moisture = " + str(moisture) + "to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(10)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
