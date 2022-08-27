#imports
import cv2

class Webcam:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def cycle(self):
        self.ret, self.frame = self.cap.read()
        self.grayFrame = 10
        print("sss")

    def end(self):
        self.cap.release()
        cv2.destroyAllWindows()
