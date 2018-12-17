import random
import serial
import abc
class niceSensor(abc.ABC):
    def __init__(self, numberOfOutputs, sensorAddress, sObj):
        self.sensorAddress = sensorAddress
        self.sObj = sObj
        self.numberOfOutputs = numberOfOutputs
        self.errValues = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"

    def getValue(self):
        self.thisList = []
        try:
            cleanMessage = [y.strip() for y in self.sObj.readline().decode("utf-8").split(',')]
            if (len(cleanMessage) > 20):
                self.lastMessage = cleanMessage
            else:
                self.lastMessage = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
            # print("read serial")
        except UnicodeDecodeError:
            self.lastMessage = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
            print("error reading serial")
            self.sObj.flushInput()
        # print(self.lastMessage)
        # cleanMessage = [x.strip() for x in self.sObj.split(',')]
        for x in range(self.sensorAddress-1, (self.sensorAddress-1 + self.numberOfOutputs)):
            self.thisList.append(self.lastMessage[x])
            # print(self.lastMessage[x])
        # print(self.lastMessage)
        return self.thisList
    def isAlive(self):
        return True