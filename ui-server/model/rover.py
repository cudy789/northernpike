import csv
import threading
import time
import random
from writer import writerThread
class rover:

	def __init__(self, inputGyro, inputCompass, inputBarometer):
		self.inputGyro = inputGyro
		self.inputCompass = inputCompass
		self.inputBarometer = inputBarometer
		self.gyroDataTuple = self.inputGyro.getValue()
		self.compassDataTuple = self.inputCompass.getValue()
		self.barometerDataTuple = self.inputBarometer.getValue()

		threadGyro = writerThread(1, ["gyroX", "gyroY", "gyroZ", "compass", "barometer"], 'testfile1.csv', self.inputGyro, self.inputCompass, self.inputBarometer)
		threadGyro.start()

		updateData = threading.Thread(target=self.__run)
		updateData.start()

	def getRoverGyro(self):
		return "Gyro values x: %d y: %d z: %d" % (self.gyroDataTuple[0], self.gyroDataTuple[1], self.gyroDataTuple[2])

	def getRoverCompass(self):
		return "Direction: %d" % (self.compassDataTuple[0])
	def getRoverBarometer(self):
		return "Pressure: %d" % (self.barometerDataTuple[0])

	def __run(self):
		while True:
			self.gyroDataTuple = self.inputGyro.getValue()
			self.compassDataTuple = self.inputCompass.getValue()
			time.sleep(.2)







