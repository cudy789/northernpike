import threading
import time
import csv

class writer(threading.Thread):
    def __init__(self, threadID, fieldnames, filename, sHelper):
        threading.Thread.__init__(self)

        self.THREAD_SLEEP_TIME = .01

        self.threadID = threadID
        self.fieldnames = fieldnames
        self.filename = filename
        # self.counter = 0
        self.lastMessage = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
        self.sHelper = sHelper

        # self.__updateList()

        with open(self.filename, mode='w', newline='\n') as self.csvfile:
            self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
            self.writer.writeheader()
    def run(self):
        while True:
            ss = self.sHelper.getSerialString()
            with open(self.filename, mode='a', newline='\n') as self.csvfile:
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
                # self.__updateList()


                self.writer.writerow({
                    self.fieldnames[0]: ss[0], self.fieldnames[1]: ss[1],
                    self.fieldnames[2]: ss[2], self.fieldnames[3]: ss[3],
                    self.fieldnames[4]: ss[4], self.fieldnames[5]: ss[5],
                    self.fieldnames[6]: ss[6], self.fieldnames[7]: ss[7],
                    self.fieldnames[8]: ss[8], self.fieldnames[9]: ss[9],
                    self.fieldnames[10]: ss[10], self.fieldnames[11]: ss[11],
                    self.fieldnames[12]: ss[12], self.fieldnames[13]: ss[13],
                    self.fieldnames[14]: ss[14], self.fieldnames[15]: ss[15],
                    self.fieldnames[16]: ss[16], self.fieldnames[17]: ss[17],
                    self.fieldnames[18]: ss[18], self.fieldnames[19]: ss[19],
                    self.fieldnames[20]: ss[20]

                })

                # print(self.threadID, self.counter)
                # self.counter+=1
                time.sleep(self.THREAD_SLEEP_TIME)

    # def __updateList(self):
    #     try:
    #         cleanMessage = [y.strip() for y in self.sObj.readline().decode("utf-8").split(',')]
    #         self.lastMessage = cleanMessage
    #         # print("read serial")
    #     except UnicodeDecodeError:
    #         print("error reading serial")
    #         self.sObj.flushInput()






