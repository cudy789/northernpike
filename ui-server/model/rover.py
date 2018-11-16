import threading
import time
from writer import writer
from sensorHelper import sensorHelper

class rover:

    def __init__(self, inputGyro, inputCompass, inputBarometer):
        self.mySensorHelper = sensorHelper()


        updateData = threading.Thread(target=self.__run)
        updateData.start()

    def getRoverGyro(self):
        return "Gyro values x: %d y: %d z: %d" % (self.gyroDataList[0], self.gyroDataList[1], self.gyroDataList[2])

    def getRoverCompass(self):
        return "Direction: %d" % (self.compassDataList[0])

    def getRoverBarometer(self):
        return "Pressure: %d" % (self.barometerDataList[0])

    def __run(self):
        while True:
            self.gyroDataList = self.mySensorHelper.getBoard().getAbsoluteOrientation()
            self.compassDataList = self.mySensorHelper.getBoard().getMagneticVector()
            self.barometerDataList = self.mySensorHelper.getBarometer().getPressure()
            time.sleep(.2)
