import threading
import time
import csv

class writerThread(threading.Thread):
    def __init__(self, threadID, fieldnames, filename, objName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.fieldnames = fieldnames
        self.filename = filename
        self.counter = 0
        self.objName = objName
        self.latestTuple = self.objName.getValue(self)
        with open(self.filename, mode='w', newline='\n') as self.csvfile:
            self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
    def run(self):
        while self.counter < 10000:
            with open(self.filename, mode='a', newline='\n') as self.csvfile:
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
                self.latestTuple = self.objName.getValue(self)
                self.writer.writerow({self.fieldnames[0]: self.latestTuple[0], self.fieldnames[1]: self.latestTuple[1], self.fieldnames[2]: self.latestTuple[2]})
                print(self.threadID, self.counter)
                self.counter+=1
                time.sleep(.2)
        print ("Finished!")


# thread1 = writerThread(1, "Thread1")
#
# thread1.start()