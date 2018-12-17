import threading
import time

class readSerial(threading.Thread):
    def __init__(self, sObj, string):
        threading.Thread.__init__(self)
        self.stringValues = string
        self.THREAD_SLEEP_TIME = .01

        self.sObj = sObj

    def run(self):
        while True:
            try:
                cleanMessage = [y.strip() for y in self.sObj.readline().decode("utf-8").split(',')]
                if (len(cleanMessage) > 20):
                    self.stringValues = cleanMessage
                else:
                    self.stringValues = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
                # print("read serial")
            except UnicodeDecodeError:
                self.stringValues = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
                print("error reading serial")
                self.sObj.flushInput()

    def getString(self):
        return self.stringValues