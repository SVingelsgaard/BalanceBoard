#imports
import numpy as np
import cv2
import matplotlib.pyplot as plt
dist = lambda x1, y1, x2, y2: ((np.abs(np.float16(x1) - np.float16(x2))**2)+(np.abs(np.float16(y1) - np.float16(y2))**2))#pythagorian theorem

class Webcam:
    def __init__(self):
        print("camera starting...")
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.lastCircle = None
        self.circlePositionsX = []
        self.circlePositionsY = []
        print("camera ready")


    def cycle(self):
        self.ret, self.frame = self.cap.read()
        if not self.ret:
            print("camera not detected")
            self.end()

        self.grayFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

        self.blurFrame = cv2.GaussianBlur(self.grayFrame, (7,7), 0)

        self.retVal, self.thresholdFrame = cv2.threshold(self.blurFrame, 220, 255, cv2.THRESH_BINARY)#donno what retVal is, but need it...
        

        self.circles = cv2.HoughCircles(self.blurFrame, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=20 , maxRadius=40)#detect circles.

        if self.circles is not None:
            self.circles = np.uint16(np.around(self.circles))
            self.circle = None
            for i in self.circles[0, :]:
                if self.circle is None: 
                    self.circle = i
                if self.lastCircle is not None:
                    if dist(i[0], i[1], self.lastCircle[0], self.lastCircle[1]) < dist(self.circle[0], self.circle[1], self.lastCircle[0], self.lastCircle[1]):#check for the circle closest to last circle
                        self.circle = i
            self.lastCircle = self.circle

            cv2.circle(self.frame, (self.circle[0], self.circle[1]), self.circle[2], (0,0,0), 3)#draw circle
            self.circlePositionsX.append(self.circle[0])#graph x pos
            self.circlePositionsY.append(self.circle[1])#graph y pos
            print(self.circle[2])
        
        cv2.imshow("Webcam", self.frame)

        cv2.waitKey(1)#for showing the image longer i think. does not work without i

    def end(self):
        #graph
        plt.style.use('seaborn-whitegrid')
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.ax.plot(self.circlePositionsX, self.circlePositionsY)
        self.ax.axis("equal")
        self.ax.set(xlim = (0, 800), ylim = (600, 0))
        
        plt.show()
        
        self.cap.release()
        cv2.destroyAllWindows()
        
