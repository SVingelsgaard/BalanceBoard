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
        self.servoXZero = 84#ball lies still with these
        self.servoYZero = 98
        self.servoXlim = [-24, 27]
        self.servoYlim = [-24, 24]
        print("servo's ready")
        
    #scuffed way to determen a cycletime of the cyclefunction without using delay
    def clock(self):
        self.timeNow = time.time()
        self.runCycle = False
        if (self.timeNow - self.timeLast) > self.cycletime:
            self.timeLast = time.time()
            self.runCycle = True

    def cycle(self, output):
        self.clock()
        if (self.runCycle):

            #set and cap servo x
            if output[0] < self.servoXlim[0]:
                self.servoX = self.servoXlim[0]
            elif output[0] > self.servoXlim[1]:
                self.servoX = self.servoXlim[1]
            else:
                self.servoX = output[0]

            #set and cap servo 2
            if output[1] < self.servoYlim[0]:
                self.servoY = self.servoYlim[0]
            elif output[1] > self.servoYlim[1]:
                self.servoY = self.servoYlim[1]
            else:    
                self.servoY = output[1]

            self.servoX += self.servoXZero#+zero so 0 pos is flat on the board.
            self.servoY += self.servoYZero#+zero so 0 pos is flat on the board.

            self.data = str(self.servoX+100)+str(self.servoY+100)#+100 to make sure data uses 3 digits.
            self.arduino.write(bytes(self.data, 'utf-8'))

    def end(self):
        #write zero position
        self.servoX, self.servoY = self.servoXZero, self.servoYZero
        self.data = str(self.servoX+100)+str(self.servoY+100)#+100 to make sure data uses 3 digits.
        self.arduino.write(bytes(self.data, 'utf-8'))
        self.arduino.close()