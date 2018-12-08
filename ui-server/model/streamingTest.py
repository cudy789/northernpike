# 1/usr/bin/env python
import itertools
import time
import random
import importlib
from rover import rover
from niceSensor import niceSensor
from flask import Flask, Response, redirect, request, url_for

app = Flask(__name__)

# myGyro = niceSensor(3)
# myCompass = niceSensor(1)
# myBarometer = niceSensor(1)
nPike = rover()


def nPikeStringData():
    returnString = "%s, %s, %s" % (nPike.getRoverGyro(), nPike.getRoverMagnometer(), nPike.getRoverBarometer())
    return returnString


@app.route('/')
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():
            for i, c in enumerate(itertools.cycle('\|/-')):
                yield "data: %s %s\n\n" % (c, nPikeStringData())
                time.sleep(.1)  # an artificial delay

        return Response(events(), content_type='text/event-stream')
    return redirect(url_for('static', filename='index.html'))


if __name__ == "__main__":
    while True:
        print(nPike.getRoverBarometer())

    app.run(host='0.0.0.0', port=80)

