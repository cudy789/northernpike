import csv
class roverState:

	def __init__(self):
		with open('testfile1.csv', 'w', newline='\n') as csvfile:
			self.writer = csv.writer(csvfile, delimiter = ',')
			self.writer.writerows(['newbar'])

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



