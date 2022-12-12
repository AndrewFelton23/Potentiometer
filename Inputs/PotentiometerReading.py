#STEP 1 add the libraries
#Library 1 = cvzone
#Library 2 = pyserial

#Import the functions from cv zone
from cvzone.SerialModule import SerialObject

#Assign the serial object to the arduino and specify the port
arduino = SerialObject("/dev/cu.usbmodem1431301")

#start the loop which will continuously run
while True:
    myData = arduino.getData()
    print(myData[0])

