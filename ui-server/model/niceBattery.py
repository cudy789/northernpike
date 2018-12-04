
from niceSensor import niceSensor
class niceBattery(niceSensor):

    def __init__(self, address, inMessage):
        self.address = address
        niceSensor. __init__(self, 2, address, inMessage)

    def getVoltage(self):
        return "Voltage is: %d" % (niceSensor.getValue(self)[0])

    def getCurrent(self):
        return "Current is: %d" % (niceSensor.getValue(self)[1])