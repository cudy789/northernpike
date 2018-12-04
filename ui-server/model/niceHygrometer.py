
from niceSensor import niceSensor
class niceHygrometer(niceSensor):

    def __init__(self, address, inMessage):
        self.address = address
        niceSensor. __init__(self, 1, address, inMessage)

    def getPercentHum(self):
        return "Hygrometer: %i" % (niceSensor.getValue(self)[0])