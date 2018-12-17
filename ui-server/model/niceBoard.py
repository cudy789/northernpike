from niceSensor import niceSensor
class niceBoard(niceSensor):
    def __init__(self, address, sObj):
        self.address = address
        self.sObj = sObj
        niceSensor.__init__(self, 16, self.address, self.sObj)

    def getTemp(self):
        return [niceSensor.getValue(self)[0]]
    def getGravityVector(self):
        return [niceSensor.getValue(self)[1], niceSensor.getValue(self)[2], niceSensor.getValue(self)[3]]
    def getMagneticVector(self):
        return [niceSensor.getValue(self)[4], niceSensor.getValue(self)[5], niceSensor.getValue(self)[6]]
    def getAccelerationVector(self):
        return [niceSensor.getValue(self)[7], niceSensor.getValue(self)[8], niceSensor.getValue(self)[9]]
    def getAngularVelocity(self):
        return [niceSensor.getValue(self)[10], niceSensor.getValue(self)[11], niceSensor.getValue(self)[12]]
    def getAbsoluteOrientation(self):
        print([niceSensor.getValue(self)[13], niceSensor.getValue(self)[14], niceSensor.getValue(self)[15]])
        return [niceSensor.getValue(self)[13], niceSensor.getValue(self)[14], niceSensor.getValue(self)[15]]

    def isAlive(self):
        return True