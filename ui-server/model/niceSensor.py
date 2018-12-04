import random
import serial
import abc
class niceSensor(abc.ABC):
    def __init__(self, numberOfOutputs, sensorAddress, sObj):
        self.sensorAddress = sensorAddress
        self.sObj = sObj

        self.numberOfOutputs = numberOfOutputs
    def getValue(self):
        self.thisList = []
        cleanMessage = [x.strip() for x in self.sObj.readline().split(',')]
        for x in range(self.numberOfOutputs+self.sensorAddress-1):
            self.thisList.append(cleanMessage[x])
        return self.thisList
    def isAlive(self):
        return True