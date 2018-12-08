
from niceSensor import niceSensor
class niceBarometer(niceSensor):

    def __init__(self, address, inMessage):
        self.address = address
        niceSensor. __init__(self, 1, address, inMessage)

    def getPressure(self):
        return niceSensor.getValue(self)[0]