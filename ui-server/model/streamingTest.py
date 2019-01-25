# !/usr/bin/env python3
import itertools
import time
import random
import importlib
from rover import rover
from flask import Flask, Response, redirect, request, url_for

app = Flask(__name__)

nPike = rover()


def nPikeStringData():
    returnString = "%s, %s, %s" % (nPike.getRoverVoltage(), nPike.getRoverCurrent(), nPike.getRoverMagnometer())
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
    x=0
    while True:
        nPike.sendJoystick([x,2,1])
        print(x)
        time.sleep(1)
        if x == 9: x = 0
        else: x+=1
    app.run(host='0.0.0.0', port=80)


