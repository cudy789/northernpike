import csv
import threading
import time
import random
from writer import writerThread
class roverState:

	def __init__(self, inputGyro, inputCompass):
		self.inputGyro = inputGyro
		self.inputCompass = inputCompass
		self.gyroDataTuple = self.inputGyro.getValue()
		self.compassDataTuple = self.inputCompass.getValue()
		threadGyro = writerThread(1, ["gyroX", "gyroY", "gyroZ", "compass"], 'testfile1.csv', self.inputGyro, self.inputCompass)
		threadGyro.start()
	def getRoverGyro(self):
		return "Gyro values x: %d y: %d z: %d" % (self.gyroDataTuple[0], self.gyroDataTuple[1], self.gyroDataTuple[2])
	def run(self):
		self.gyroDataTuple = self.inputGyro.getValue()
		self.compassDataTuple = self.inputCompass.getValue()

	def getRoverCompass(self):
		return "Direction: %d" % (self.compassDataTuple[0])

	def readGyroData(self, inputGyro):
		self.inputGyro = inputGyro
		return None






