import time

class Controller:
    def __init__(self):
        self.PV = [0, 0]
        self.SP = [0, 0]
        self.error = [0, 0]
        self.output = [0, 0]

        self.Kp = .1
        self.Ki = 0
        self.Kd = 1

        self.integralError = [0, 0]
        self.errorLast = [0, 0]
        self.derivativeError = [0, 0]


        #clock
        self.cycletime = 0.05 #the cycletime of when the cyclefunction will actually run is set here
        self.timeLast = time.time()

        print("controller loaded.")
        
    #scuffed way to determen a cycletime of the cyclefunction without using delay
    def clock(self):
        self.timeNow = time.time()
        self.runCycle = False
        if (self.timeNow - self.timeLast) > self.cycletime:
            self.readCycletime = time.time() - self.timeLast
            self.timeLast = time.time()
            self.runCycle = True

    def PID(self):
        pass

    def cycle(self, SP, PV):
        self.clock()
        if (self.runCycle):
            self.error = [-(SP[0] - PV[0]), -(SP[1] - PV[1])]#calculating "avvik". both negativ cus it do be like that(reveresed controll smthing maby idk.)
            
            self.integralError[0] += self.error[0] * self.readCycletime#integrating error for both x and y
            self.integralError[1] += self.error[1] * self.readCycletime

            if self.readCycletime == 0:#donno why i do this. think it is for not braking first cycle.
                self.readCycletime = self.cycletime
            else:
                self.derivativeError[0] = (self.error[0] - self.errorLast[0]) / self.readCycletime
                self.derivativeError[1] = (self.error[1] - self.errorLast[1]) / self.readCycletime #calculating derivative error.

            self.errorLast = self.error

            self.output[0] = int((self.Kp * self.error[0]) + (self.Ki * self.integralError[0]) + (self.Kd * self.derivativeError[0]))
            self.output[1] = int((self.Kp * self.error[1]) + (self.Ki * self.integralError[1]) + (self.Kd * self.derivativeError[1]))

    def end(self):
        self.output = [0, 0]
