import serial
from writer import writer
from niceBattery import niceBattery
from niceBarometer import niceBarometer
from niceLeak import niceLeak
from niceHygrometer import niceHygrometer
from niceBoard import niceBoard

# -- Instruction Addresses -- #
BATTERY_ADDRESS = 1
BAROMETER_ADDRESS = 3 # batteryAddress needs 2 addresses
LEAK_ADDRESS = 4
HYGROMETER_ADDRESS = 5
BOARD_ADDRESS = 6 # magnometer, accelerometer, gyroscope, thermometer
SERIAL_PORT = '/dev/ttyACM0'
SERIAL_RATE = 9600

class sensorHelper:

    def __init__(self):
        self.s = serial.Serial(SERIAL_PORT)
        # self.s.baudrate = SERIAL_RATE

        self.myBattery = niceBattery(BATTERY_ADDRESS, self.s)
        self.myBarometer = niceBarometer(BAROMETER_ADDRESS, self.s)
        self.myLeak = niceLeak(LEAK_ADDRESS, self.s)
        self.myHygrometer = niceHygrometer(HYGROMETER_ADDRESS, self.s)
        self.myBoard = niceBoard(BOARD_ADDRESS, self.s)

        # self.fileHeader = ["Voltage", "Current", "Pressure", "Water?", "Percent Humidity", "Temperature", "GravityX", "GravityY",
        #                    "GravityZ", "MagX", "MagY", "MagZ", "AccelX", "AccelY", "AccelX", "VelX", "VelY", "VelZ", "OrientX",
        #                    "OrientY", "OrientZ"]
        # self.sensorList = [self.myBattery, self.myBarometer, self.myLeak, self.myHygrometer, self.myBoard]
        # self.writer = writer(1, self.fileHeader, 'allSensors.csv', self.sensorList)
        # self.writer.start()
    def readSerial(self):
        self.sString = self.s.readline()
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
    def sensorsOnline(self):
        bool = True
        if (not self.myBattery.isAlive()): bool = False
        if (not self.myBarometer.isAlive()): bool = False
        if (not self.myLeak.isAlive()): bool = False
        if (not self.myHygrometer.isAlive()): bool = False
        if (not self.myBoard.isAlive()): bool = False
        return bool

