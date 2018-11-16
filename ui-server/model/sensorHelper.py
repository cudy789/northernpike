from writerThread import writerThread
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
        self.myBoard = niceBoard(BOARD_ADDRESSES) # Starts its own writerThreads

        self.batteryThread = writerThread(0, ["Voltage", "Current"], 'batteryData.csv', self.myBattery)
        self.barometerThread = writerThread(1, ["Pressure"], 'barometerData.csv', self.myBarometer)
        self.LeakThread = writerThread(2, ["isWater"], 'leakData.csv', self.myLeak)
        self.HygrometerThread = writerThread(3, ["Humidity Percent"], 'hygrometerData.csv', self.myHygrometer)
