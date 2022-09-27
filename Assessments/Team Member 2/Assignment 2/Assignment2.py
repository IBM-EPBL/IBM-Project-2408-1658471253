import time 
import random

def senseData():
    sensedData = random.randint(0,100)
    return sensedData


def main():
    for i in range(10):
        data = senseData()
        if data <= 20:
            print("low temperature ( {0} degree celcius )".format(data))
        elif data >= 40:
            print("high temperature ( {0} degree celcius )".format(data))
        else:
            print("Normal temperature ( {0} degree celcius )".format(data))
        time.sleep(2)

main()