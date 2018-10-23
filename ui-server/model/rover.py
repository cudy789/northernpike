import csv
import threading
import time
import random
from writer import writerThread
class roverState:

	def __init__(self, inputGyro):
		self.inputGyro = inputGyro
		self.gyroDataTuple = self.inputGyro.getValue(self)
		threadGyro = writerThread(1, ["gyroX", "gyroY", "gyroZ"], 'testfile1.csv', self.inputGyro)
		threadGyro.start()
		self.d = 10

	def getRoverGyro(self):
		return "Gyro values x: %d y: %d z: %d" % (self.gyroDataTuple[0], self.gyroDataTuple[1], self.gyroDataTuple[2])
	def run(self):
		self.gyroDataTuple = self.inputGyro.getValue(self)

	def getRoverCompass(self):
		return "Direction: %d" % (self.d)

	def readGyroData(self, inputGyro):
		self.inputGyro = inputGyro
		return None






