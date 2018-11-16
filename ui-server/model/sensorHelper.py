from writer import writer
from niceBattery import niceBattery
from niceBarometer import niceBarometer
from niceLeak import niceLeak
from niceHygrometer import niceHygrometer
from niceBoard import niceBoard

# -- I2C sensor addresses -- #
MY_ADDRESS = 1
BATTERY_ADDRESS = 2
BAROMETER_ADDRESS = 3
LEAK_ADDRESS = 4
HYGROMETER_ADDRESS = 5
BOARD_ADDRESSES = [6,7,8,9] # (magnometer, accelerometer, gyroscope, thermometer) addresses


class sensorHelper:

    def __init__(self):
        self.myBattery = niceBattery(BATTERY_ADDRESS)
        self.myBarometer = niceBarometer(BAROMETER_ADDRESS)
        self.myLeak = niceLeak(LEAK_ADDRESS)
        self.myHygrometer = niceHygrometer(HYGROMETER_ADDRESS)
        self.myBoard = niceBoard(BOARD_ADDRESSES)
        self.fileHeader = ["Voltage", "Current", "Pressure", "Water?", "Percent Humidity", "Temperature", "GravityX", "GravityY",
                           "GravityZ", "MagX", "MagY", "MagZ", "AccelX", "AccelY", "AccelX", "VelX", "VelY", "VelZ", "OrientX",
                           "OrientY", "OrientZ"]
        self.sensorList = [self.myBattery, self.myBarometer, self.myLeak, self.myHygrometer, self.myBoard]
        self.writer = writer(1, self.fileHeader, 'allSensors.csv', self.sensorList)
        self.writer.start()

    def getBattery(self):
        return self.myBattery
    def getBarometer(self):
        return self.myBarometer
    def getLeak(self):
        return self.myLeak
    def getHygrometer(self):
        return self.myHygrometer
    def getBoard(self):
        return self.myBoard
