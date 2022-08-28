#imports
from email.mime import image
import cv2

class Webcam:
    def __init__(self):
        print("camera starting...")
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        self.record = True


        print("camera ready")


    def cycle(self):
        self.ret, self.frame = self.cap.read()
        if not self.ret:
            print("camera not detected")
            self.end()

        self.grayFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        self.blurFrame = cv2.GaussianBlur(self.grayFrame, (7,7), 0)
        self.retVal, self.thresholdFrame = cv2.threshold(self.blurFrame, 220, 255, cv2.THRESH_BINARY)#donno what retVal is, but need it...
        
        cv2.imshow("Webcam", self.thresholdFrame)
        cv2.imshow("WebcamOriginal", self.frame)

        cv2.waitKey(1)#for showing the image longer i think. does not work without i

    def end(self):
        self.cap.release()
        cv2.destroyAllWindows()
