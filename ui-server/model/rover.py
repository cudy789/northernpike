import threading
import time
from writerThread import writerThread


class rover:

    def __init__(self, inputGyro, inputCompass, inputBarometer):
        self.inputGyro = inputGyro
        self.inputCompass = inputCompass
        self.inputBarometer = inputBarometer

        self.gyroDataList = self.inputGyro.getValue()
        self.compassDataList = self.inputCompass.getValue()
        self.barometerDataList = self.inputBarometer.getValue()

        threadGyro = writerThread(1, ["gyroX", "gyroY", "gyroZ"], 'gyroData.csv', self.inputGyro) # Create & start data logging threads
        threadCompass = writerThread(2, ["heading"], 'compassData.csv', self.inputCompass)
        threadBarometer = writerThread(3, ["pressure"], 'barometerData.csv', self.inputBarometer)
        threadGyro.start()
        threadCompass.start()
        threadBarometer.start()

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
            self.gyroDataList = self.inputGyro.getValue()
            self.compassDataList = self.inputCompass.getValue()
            self.barometerDataList = self.inputBarometer.getValue()
            time.sleep(.2)
