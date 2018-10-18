import csv
import threading
import time
class roverState:

	def __init__(self):
		with open('testfile1.csv', mode='w', newline='\n') as csvfile:
			fieldnames = ['gyroX', 'gyroY', 'gyroZ']
			self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			self.writer.writeheader()
			self.writer.writerow({'gyroX': self.x, 'gyroY': self.y, 'gyroZ': self.z})

	def getRoverGyro(self):
		return "Gyro values x: %d y: %d z: %d" % (self.x, self.y, self.z)


	def getRoverCompass(self):
		return "Direction: %d" % (self.d)

	def readGyroData(self):
		return None

	# def writedata(self):


	x=10
	y=15
	z=20
	d=45



