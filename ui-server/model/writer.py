import threading
import time
import csv

class writerThread(threading.Thread):
    def __init__(self, threadID, fieldnames, filename, Gyro, Compass, Barometer):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.fieldnames = fieldnames
        self.filename = filename
        self.counter = 0

        self.Compass = Compass
        self.Gyro = Gyro
        self.Barometer = Barometer

        self.__updateTuples()

        with open(self.filename, mode='w', newline='\n') as self.csvfile:
            self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
    def run(self):
        while True:
            with open(self.filename, mode='a', newline='\n') as self.csvfile:
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)

                self.__updateTuples()

                self.writer.writerow({self.fieldnames[0]: self.latestGyro[0], self.fieldnames[1]: self.latestGyro[1],
                                      self.fieldnames[2]: self.latestGyro[2], self.fieldnames[3]: self.latestCompass[0],
                                      self.fieldnames[4]: self.latestBarometer[0]})

                print(self.threadID, self.counter)
                self.counter+=1
                time.sleep(.1)
        print ("Finished!")
    def __updateTuples(self):
        self.latestGyro = self.Gyro.getValue()
        self.latestCompass = self.Compass.getValue()
        self.latestBarometer = self.Barometer.getValue()