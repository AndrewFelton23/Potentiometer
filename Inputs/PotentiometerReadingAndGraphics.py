# STEP 1 add the libraries
# Library 1 = cvzone
# Library 2 = pyserial

# Import the functions from cv zone
from cvzone.SerialModule import SerialObject

import cv2
import numpy as np

# Assign the serial object to the arduino and specify the port
arduino = SerialObject("/dev/cu.usbmodem1411301")

# start the loop which will continuously run
while True:
    myData = arduino.getData()

    # Now we will show the amount of the potentiometer has been turned on an image
    # Load using the cv2 functions
    img = cv2.imread("../Resources/Potentiometer.jpg")
    # Convert the analog input to degrees from -90 to 270 using numpy
    try:
        print(myData[0])
        val = np.interp(int(myData[0]), [0, 1023], [-90, 270])
        # create a ellipse
        if val <= 0:
            cv2.ellipse(img, (320, 265), (131, 131), 0, -90, val, (255, 180, 0), 10)
    except:
        pass
    # show the image
    cv2.imshow("Potentiometer", img)
    cv2.waitKey(1)
