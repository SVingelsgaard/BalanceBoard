#importing functionality
from servos import Servos
from webcam import Webcam
import keyboard
import time

cam = Webcam()
servos = Servos()

while True:
    if keyboard.is_pressed('q'): #if key 'q' is pressed 
        print('exiting')
        cam.end()
        servos.end()
        break

    cam.cycle()
    servos.cycle()

    
    


