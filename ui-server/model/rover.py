import threading
import time
from writer import writer
from sensorHelper import sensorHelper

class rover:

    def __init__(self):
        self.mySensorHelper = sensorHelper()

    def sensorsOnline(self):
        return self.mySensorHelper.sensorsOnline()

    def getRoverBarometer(self): # barometer
        self.barometerData = self.mySensorHelper.getBarometer().getPressure()
        return self.barometerData

    def getRoverHygrometer(self): # humidity
        self.hygrometerData = self.mySensorHelper.getHygrometer().getPercentHum()
        return self.hygrometerData

    def getRoverThermometer(self): # temp
        self.thermometerData = self.mySensorHelper.getBoard().getTemp()
        return self.thermometerData

    def getRoverGravity(self):
        self.gravityDataList = self.mySensorHelper.getBoard().getGravityVector()
        return self.gravityDataList

    def getRoverMagnometer(self): #compass, 3 values, x y z
        self.compassDataList = self.mySensorHelper.getBoard().getMagneticVector()
        return self.compassDataList

    def getRoverAccelerometer(self): # acceleration x y z
        self.accelerometerDataList = self.mySensorHelper.getBoard().getAccelerationVector()
        return self.accelerometerDataList

    def getRoverVelocity(self): # velocity x y z
        self.velocityDataList = self.mySensorHelper.getBoard().getAngularVelocity()
        return self.velocityDataList

    def getRoverGyro(self): # 3 values, x y z
        self.gyroDataList = self.mySensorHelper.getBoard().getAbsoluteOrientation()
        return self.gyroDataList


