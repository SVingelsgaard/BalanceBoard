#folow this for setup with aduino: https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#imports
import serial
import time



class Servos:
    def __init__(self):
        print("servo's starting...")
        self.arduino = serial.Serial(port="COM4", baudrate=9600, timeout=.1)
        time.sleep(3)#literry dying without this idk.

        #clock
        self.cycletime = 0.05 #the cycletime of when the cyclefunction will actually run is set here
        self.timeLast = time.time()

        #servos
        self.servoX = 0
        self.servoY = 0
        print("servo's ready")
        
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

            #test
            self.servoX += 1
            if self.servoX > 180:
                self.servoX = 0
            
            print(self.servoX)


            self.data = str(self.servoX+100)+str(self.servoY+100)#+100 to make sure data uses 3 digits.
            self.arduino.write(bytes(self.data, 'utf-8'))


    def end(self):
        self.arduino.close()