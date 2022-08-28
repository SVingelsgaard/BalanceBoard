#imports
import cv2

class Webcam:
    def __init__(self):
        print("1")
        self.cap = cv2.VideoCapture(1)
        self.record = True

    def cycle(self):
        self.ret, self.frame = self.cap.read()
        if not self.ret:
            print("camera not detected")
            self.end()

        self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Webcam", self.gray)
        cv2.waitKey(1)#for showing the image longer i think

    def end(self):
        self.cap.release()
        cv2.destroyAllWindows()
