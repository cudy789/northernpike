
from niceSensor import niceSensor
class niceLeak(niceSensor):

    def __inti__(self, address):
        self.address = address
        niceSensor. __init__(self, 1, address)

    def isWater(self):
        return "Is taking water: %s" % str((bool(niceSensor.getValue(self)[0])))
