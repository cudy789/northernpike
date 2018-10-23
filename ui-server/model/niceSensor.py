import random
class niceSensor:
    def __init__(self, numberOfOutputs, inputSensor=None):
        self.inputSensor = inputSensor
        self.numberOfOutputs = numberOfOutputs
    def getValue(self):
        self.thisList = []
        for x in range(self.numberOfOutputs):
            self.thisList.append(random.randint(1,100))
        return self.thisList