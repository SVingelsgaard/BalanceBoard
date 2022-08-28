#importing functionality
from servos import Servos
from webcam import Webcam
import keyboard
import time

cam = Webcam()

while True:
    if keyboard.is_pressed('q'): #if key 'q' is pressed 
        print('exiting')
        cam.end()
        break

    cam.cycle()

    #time.sleep(0.2)
    


