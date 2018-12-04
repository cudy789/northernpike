
from niceSensor import niceSensor
class niceLeak(niceSensor):

    def __init__(self, address, inMessage):
        self.address = address
        niceSensor.__init__(self, 1, address, inMessage)

    def isWater(self):
        return str((bool(niceSensor.getValue(self)[0])))
