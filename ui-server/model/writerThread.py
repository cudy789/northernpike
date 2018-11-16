import threading
import time
import csv
class writerThread(threading.Thread):
    def __init__(self, threadID, fieldnames, filename, sensor):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.fieldnames = fieldnames
        self.filename = filename
        # self.counter = 0
        self.sensor = sensor
        self.dataList = []

        self.__updateList()

        with open(self.filename, mode='w', newline='\n') as self.csvfile:
            self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
    def run(self):
        while True:
            with open(self.filename, mode='a', newline='\n') as self.csvfile:
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
                self.__updateList()
                
                if len(self.fieldnames) == 1:
                    self.writer.writerow({self.fieldnames[0]: self.dataList[0]})
                elif len(self.fieldnames) == 2:
                    self.writer.writerow({self.fieldnames[0]: self.dataList[0], self.fieldnames[1]: self.dataList[1]})
                elif len(self.fieldnames) == 3:
                    self.writer.writerow({self.fieldnames[0]: self.dataList[0], self.fieldnames[1]: self.dataList[1],
                                          self.fieldnames[2]: self.dataList[2]})
                elif len(self.fieldnames) == 4:
                    self.writer.writerow({self.fieldnames[0]: self.dataList[0], self.fieldnames[1]: self.datalist[1],
                                          self.fieldnames[2]: self.dataList[2], self.fieldnames[3]: self.datalist[3]})
                    
                # print(self.threadID, self.counter)
                # self.counter+=1
                time.sleep(THREAD_SLEEP_TIME)
    def __updateList(self):
        self.dataList.clear()
        for i in range(len(self.fieldnames)):
            self.dataList.append(self.sensor.getValue().pop())

    THREAD_SLEEP_TIME = .1
