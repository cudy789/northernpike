import threading
import time
from sensorHelper import sensorHelper # Might give linter error, but runs fine
#   -----Description-----
# This class contains all the getter
# methods to observe the current state
# of the rover. It also contains the setter
# methods to pass navigation information to
# the Arduino.
#   ---------------------
BATTERY_ADDRESS = 1
BAROMETER_ADDRESS = 3 # batteryAddress needs 2 addresses
LEAK_ADDRESS = 4
HYGROMETER_ADDRESS = 5
BOARD_ADDRESS = 6 # magnometer, accelerometer, gyroscope, thermometer

class rover:

    def __init__(self):
        self.mySensorHelper = sensorHelper()

    ##### GETTERS #####

    def sensorsOnline(self):
        return self.mySensorHelper.sensorsOnline()

    def getRoverVoltage(self):
        return self.mySensorHelper.getSS()[BATTERY_ADDRESS-1]

    def getRoverCurrent(self):
        return self.mySensorHelper.getSS()[BATTERY_ADDRESS-1+1]

    def getRoverBarometer(self): # barometer
        return self.mySensorHelper.getSS()[BAROMETER_ADDRESS-1]

    def getRoverLeak(self):
        return bool(self.mySensorHelper.getSS()[LEAK_ADDRESS-1])

    def getRoverHygrometer(self): # humidity
        return self.mySensorHelper.getSS()[HYGROMETER_ADDRESS-1]


    def getRoverThermometer(self): # temp
        return self.mySensorHelper.getSS()[BOARD_ADDRESS-1]

    def getRoverGravity(self): # 3 values, x y z
        return [self.mySensorHelper.getSS()[BOARD_ADDRESS-1+1],
                self.mySensorHelper.getSS()[BOARD_ADDRESS-1+2],
                self.mySensorHelper.getSS()[BOARD_ADDRESS-1+3]]

    def getRoverMagnometer(self): #compass, 3 values, x y z
        return [self.mySensorHelper.getSS()[BOARD_ADDRESS-1+4],
                self.mySensorHelper.getSS()[BOARD_ADDRESS-1+5],
                self.mySensorHelper.getSS()[BOARD_ADDRESS-1+6]]

    def getRoverAccelerometer(self): # acceleration x y z
        return [self.mySensorHelper.getSS()[BOARD_ADDRESS - 1 + 7],
                self.mySensorHelper.getSS()[BOARD_ADDRESS - 1 + 8],
                self.mySensorHelper.getSS()[BOARD_ADDRESS - 1 + 9]]

    def getRoverVelocity(self): # velocity x y z
        return [self.mySensorHelper.getSS()[BOARD_ADDRESS - 1 + 10],
                self.mySensorHelper.getSS()[BOARD_ADDRESS - 1 + 11],
                self.mySensorHelper.getSS()[BOARD_ADDRESS - 1 + 12]]

    def getRoverGyro(self): # 3 values, x y z
        return [self.mySensorHelper.getSS()[BOARD_ADDRESS-1+13],
                self.mySensorHelper.getSS()[BOARD_ADDRESS-1+14],
                self.mySensorHelper.getSS()[BOARD_ADDRESS-1+15]]
    ###################

    ##### SETTERS #####
    ###################

