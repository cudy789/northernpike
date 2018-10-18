import threading
import time

class writerThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading