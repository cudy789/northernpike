import threading
import time
import datetime
import csv
WRITE_MODE = 'w' # 'w' for overwrite, 'a' for append
#   -----Description-----
#   This is a threaded class that writes data
#   to a CSV file every self.writeInterval seconds.
#   ---------------------
class writer(threading.Thread):
    # Specify a time delay, a list of CSV column header names, the CSV filename, and the sensorHelper object
    def __init__(self, writeInterval, fieldnames, filename, sHelper):
        threading.Thread.__init__(self)

        self.writeInterval = writeInterval

        self.fieldnames = fieldnames
        self.fieldnames.append("Timestamp") # Add a field for timestamps so clients don't have to worry about it

        self.filename = filename
        self.sHelper = sHelper
        if WRITE_MODE == 'w': # If in overwrite mode, rewrite headers (which deletes all file data)
            with open(self.filename, mode='w', newline='\n') as self.csvfile:
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames) # Lets us write each column in a single row separately
                self.writer.writeheader()
    def run(self):
        while True:
            timestampValue = datetime.datetime.now() # Gets the current time
            # This isn't very efficient (opens & closes file every loop), but it works for our purposes
            with open(self.filename, mode='a', newline='\n') as self.csvfile:
                ss = self.sHelper.getSS()
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
                self.writer.writerow({
                        self.fieldnames[0]: ss[0], self.fieldnames[1]: ss[1], # Writes each ss list value in the appropriate self.fieldnames column
                        self.fieldnames[2]: ss[2], self.fieldnames[3]: ss[3],
                        self.fieldnames[4]: ss[4], self.fieldnames[5]: ss[5],
                        self.fieldnames[6]: ss[6], self.fieldnames[7]: ss[7],
                        self.fieldnames[8]: ss[8], self.fieldnames[9]: ss[9],
                        self.fieldnames[10]: ss[10], self.fieldnames[11]: ss[11],
                        self.fieldnames[12]: ss[12], self.fieldnames[13]: ss[13],
                        self.fieldnames[14]: ss[14], self.fieldnames[15]: ss[15],
                        self.fieldnames[16]: ss[16], self.fieldnames[17]: ss[17],
                        self.fieldnames[18]: ss[18], self.fieldnames[19]: ss[19],
                        self.fieldnames[20]: ss[20], self.fieldnames[21]: timestampValue})
                time.sleep(self.writeInterval)



