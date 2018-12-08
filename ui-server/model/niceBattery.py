
from niceSensor import niceSensor
class niceBattery(niceSensor):

    def __init__(self, address, inMessage):
        self.address = address
        niceSensor. __init__(self, 2, address, inMessage)

    def getVoltage(self):
        return niceSensor.getValue(self)[0]

    def getCurrent(self):
        return niceSensor.getValue(self)[1]