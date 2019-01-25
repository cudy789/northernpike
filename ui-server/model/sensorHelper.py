import serial
import time
from writer import writer # Might give a linter error, but runs fine
from threading import Thread


SERIAL_PORT = '/dev/ttyUSB0' # Won't change if the Arduino is always plugged into the same USB port
SERIAL_RATE = 9600 # Baud rate for the Arduino
CSV_WRITE_INTERVAL = .2 # Log data to Pi every 200 ms
SER_UPDATE_INTERVAL = .01 # Update our state every 10 ms

#   -----Description-----
#   This class manages the serial connection to the Arduino,
#   starts data logging with the Writer class, and has
#   accessors for status of sensors and sensor values
#   ---------------------
class sensorHelper:

    def __init__(self):
        # Setup & start Arduino serial connection
        self.s = serial.Serial(SERIAL_PORT)
        self.recieveValues = [] # List of sensor values 21 digits long
                # Order is joyX, joyY, joyZ, slider, buttons 1 - 9
        # self.sendValues = ["0","0","0","0","0","0","0","0","0","0","0","0","0"] # List of values to send
        self.sendValues = ["0","0","0"] # Testing with only joystick xyz
        # Setup & start a thread to read & write to the serial bus
        readProcess = Thread(target=self.__doSerial)
        readProcess.start()

        time.sleep(3) # Wait for serial connection to initialize
        # Setup % start a thread to log sensor data to the RPi
        # File header for local .csv file
                        #     [0]       [1]         [2]     [3]         [4]             [5]           [6]        [7]       [8]       [9]   [10]   [11]    [12]     [13]     [14]    [15]    [16]  [17]     [18]     [19]      [20]
        self.fileHeader = ["Voltage","Current","Pressure","Leak","Percent Humidity","Temperature","GravityX","GravityY","GravityZ","MagX","MagY","MagZ","AccelX","AccelY","AccelZ","VelX","VelY","VelZ","OrientX","OrientY","OrientZ"]
        self.writer = writer(CSV_WRITE_INTERVAL, self.fileHeader, 'allSensors.csv', self)
        self.writer.start()

    # Returns the 21 digit long sensor value list
    def getSS(self): # getSerialString
        return self.recieveValues

    def setNav(self, sendValues, startPos):
        j = 0
        for i in range(startPos, startPos+len(sendValues)):
            self.sendValues[i] = sendValues[j]
            j+=1

    # If a sensor returns a value of 'x', it isn't functioning properly.
    # This returns "All sensors are functional" when there are no errors,
    # otherwise it returns a message containing which sensors aren't functional.
    def sensorsOnline(self):
        errorSensors = []
        for x in range(0,21):
            if self.recieveValues[x] == "x": errorSensors.append(self.fileHeader[x])
        if len(errorSensors)==0: return "All sensors functional"
        else: return "Error: %s are not functional." % errorSensors
    # This function polls the serial bus every SER_UPDATE_INTERVAL seconds
    # for new data. The values are stored locally to self.recieveValues.
    # If the string isn't of proper length (i.e. we have malformed data),
    # the entire string is replaced with "x,x,x,......". 'x' signifies
    # invalid data.
    def __doSerial(self):
        while True:
            #Reads data from the Arduino
            try:
                cleanMessage = [y.strip() for y in self.s.readline().decode("utf-8").split(',')] # Decodes and formats data into a list of strings
                if (len(cleanMessage) == 21):
                    self.recieveValues = cleanMessage
                else:
                    self.recieveValues = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
            except UnicodeDecodeError: # Catches errors when decoding data at an invalid start position
                self.recieveValues = "x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x\n"
                print("error reading serial")
                self.s.flushInput() # Flushes serial bus (might not be necessary)
            # Sends data back to the Arduino
            sendData = ""
            for i in range(0, len(self.sendValues)):
                sendData += str(self.sendValues[i])
                if not (i == len(self.sendValues)):
                    sendData += ","
                else:
                    sendData += "\n"
            self.s.write(sendData.encode("utf-8"))
            time.sleep(SER_UPDATE_INTERVAL)
