import random
import serial
import abc
class niceSensor(abc.ABC):
    def __init__(self, numberOfOutputs, sensorAddress, sObj):
        self.sensorAddress = sensorAddress
        self.sObj = sObj
        self.numberOfOutputs = numberOfOutputs
        self.thisList = []
        self.lastMessage = "9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9"

    def getValue(self):
        print(self.sObj.readline())
        cleanMessage = [x.strip() for x in self.sObj.readline().decode("utf-8").split(',')]
        self.lastMessage = cleanMessage
        # self.sObj.flushInput()
        # print(self.lastMessage)
        # cleanMessage = [x.strip() for x in self.sObj.split(',')]
        for x in range(self.sensorAddress-1, self.sensorAddress-1+self.numberOfOutputs):
            self.thisList.append(self.lastMessage[x])
        print(self.lastMessage)
        return self.thisList
    def isAlive(self):
        return True