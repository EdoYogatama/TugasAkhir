from camera import Cam
import cv2 as cv
from datetime import datetime
import time

class Main:
    def __init__(self) -> None:
        self.camera = Cam()
        self.frame = None
        self.starttime = time.time()

    def run(self):
        while True:
            self.camera.start()
            self.frame = self.camera.frame

            self.captureFrame()

            k = cv.waitKey(5) & 0xFF
            if k == 27:
                break
        self.camera.stop()

    def captureFrame(self):
        print("Capture")
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if self.frame is not None:
            cv.imwrite("{}.jpg".format(now), self.frame)

if __name__=="__main__":
    main = Main()
    main.run()