import csv
class roverState:

	def __init__(self):
		self.writer = csv.writer(testfile1.csv, dialect='excel')

	def getRoverGyro(self):
		return "Gyro values x: %d y: %d z: %d" % (self.x, self.y, self.z)


	def getRoverCompass(self):
		return "Direction: %d" % (self.d)

	def readGyroData(self):
		return None


	def writedata(self):
		self.writer.writerows(x,y,z,d)

	x=10
	y=15
	z=20
	d=45



