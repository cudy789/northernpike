import threading
import time
import csv

class writer(threading.Thread):
    def __init__(self, threadID, fieldnames, filename, sensors):
        threading.Thread.__init__(self)

        self.THREAD_SLEEP_TIME = .1

        self.threadID = threadID
        self.fieldnames = fieldnames
        self.filename = filename
        # self.counter = 0
        self.sensors = sensors
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

                # for i in range(len(self.fieldnames)):
                #     self.writer.writerow({self.fieldnames[i]: self.dataList[i]})

                self.writer.writerow({self.fieldnames[0]: self.dataList[0], self.fieldnames[1]: self.dataList[1],
                                      self.fieldnames[2]: self.dataList[2], self.fieldnames[3]: self.dataList[3],
                                      self.fieldnames[4]: self.dataList[4], self.fieldnames[5]: self.dataList[5],
                                      self.fieldnames[6]: self.dataList[6], self.fieldnames[7]: self.dataList[7],
                                      self.fieldnames[8]: self.dataList[8], self.fieldnames[9]: self.dataList[9],
                                      self.fieldnames[10]: self.dataList[10], self.fieldnames[11]: self.dataList[11],
                                      self.fieldnames[12]: self.dataList[12], self.fieldnames[13]: self.dataList[13],
                                      self.fieldnames[14]: self.dataList[14], self.fieldnames[15]: self.dataList[15],
                                      self.fieldnames[16]: self.dataList[16], self.fieldnames[17]: self.dataList[17],
                                      self.fieldnames[18]: self.dataList[18], self.fieldnames[19]: self.dataList[19],
                                      self.fieldnames[20]: self.dataList[20]

                                      })

                # print(self.threadID, self.counter)
                # self.counter+=1
                time.sleep(self.THREAD_SLEEP_TIME)

    def __updateList(self):
        self.dataList.clear()

        self.dataList.append(self.sensors[0].getValue().pop())
        self.dataList.append(self.sensors[0].getValue().pop())

        self.dataList.append(self.sensors[1].getValue().pop())
        self.dataList.append(self.sensors[2].getValue().pop())
        self.dataList.append(self.sensors[3].getValue().pop())

        for i in range(16):
            self.dataList.append(self.sensors[4].getValue().pop())






