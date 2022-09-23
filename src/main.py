#importing functionality
from msilib.schema import Control
from servos import Servos
from webcam import Webcam
from controller import Controller
import keyboard
import time

cam = Webcam()
controller = Controller()
servos = Servos()

SP = [244,277]

while True:
    if keyboard.is_pressed('q'): #if key 'q' is pressed 
        print('exiting')
        controller.end()
        servos.end()
        cam.end()
        break

    cam.cycle(SP)#gather input. passing SP so we can get graphics
    controller.cycle(SP, cam.PV)#determen output. passing SP and PV
    servos.cycle(controller.output)#write output. pasing motor posiqq