import random
import time

while (1):
    temp = random.randint(0, 100)
    if temp>60:
        print("Detected temperature: "+str(temp)+"°C")
        time.sleep(1)