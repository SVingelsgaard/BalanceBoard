#importing functionality
from operator import truediv
from servos import Servos
from webcam import Webcam
import keyboard
import time



cam = Webcam()

while True:
    if keyboard.is_pressed('q'): #if key 'q' is pressed 
        cam.end()
        print('exiting loop')
        break

    cam.cycle()

    time.sleep(0.01)
    


