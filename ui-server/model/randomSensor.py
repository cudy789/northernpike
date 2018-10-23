import random
class randomSensor:
    def __init__(self, numberOfOutputs):
        self.numberOfOutputs = numberOfOutputs
    def getValue(self):
        self.thisList = []
        for x in range(3):
            self.thisList.append(random.randint(1,100))
        return self.thisList