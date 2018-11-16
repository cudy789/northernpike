
from niceSensor import niceSensor
class niceBarometer(niceSensor):

    def __init__(self, address):
        self.address = address
        niceSensor. __init__(self, 1, address)

    def getPressure(self):
        return "Current pressure: %d" % (niceSensor.getValue(self)[0])