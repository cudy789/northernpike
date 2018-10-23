#1/usr/bin/env python
import itertools
import time
import random
import importlib
# import rover
from rover import roverState
from randomSensor import randomSensor
from flask import Flask, Response, redirect, request, url_for

app = Flask(__name__)

myGyro = randomSensor(3)
myCompass = randomSensor(1)
rover1 = roverState(myGyro, myCompass)

def Gyroscope():
	returnString = "Data 1: %d %d %d" % (random.randint(1,21)*5, random.randint(1,21)*5, random.randint(1,21)*5)
	return returnString

def roverLocation():
	returnString = "%s, %s" % (rover1.getRoverGyro(), rover1.getRoverCompass())
	return returnString

@app.route('/')
def index():
	if request.headers.get('accept') == 'text/event-stream':
		def events():
			for i, c in enumerate(itertools.cycle('\|/-')):
				rover1.run()
				yield "data: %s %s\n\n" % (c, roverLocation())
				time.sleep(.1)  # an artificial delay
		return Response(events(), content_type='text/event-stream')
	return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
