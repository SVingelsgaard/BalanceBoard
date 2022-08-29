#folow this for setup with aduino: https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#imports
import serial
import time



class Servos:
    def __init__(self):
        self.arduino = serial.Serial(port="COM4", baudrate=9600, timeout=.1)

        #clock
        self.cycletime = 1 #the cycletime of when the cyclefunction will actually run is set here
        self.timeLast = time.time()

        #servos
        self.servoX = 0
        self.servoY = 0
        
    #scuffed way to determen a cycletime of the cyclefunction without using delay
    def clock(self):
        self.timeNow = time.time()
        self.runCycle = False
        if (self.timeNow - self.timeLast) > self.cycletime:
            self.timeLast = time.time()
            self.runCycle = True

    def cycle(self):
        self.clock()
        if (self.runCycle):
            self.servoX += 1
            self.data = str(self.servoX)
            self.arduino.write(self.data.encode("utf-8"))


    def end(self):
        self.arduino.close()