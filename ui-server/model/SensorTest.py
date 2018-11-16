
from niceBattery import niceBattery
from niceBarometer import niceBarometer
from niceLeak import niceLeak
from niceHygrometer import niceHygrometer

if __name__=='__main__':
    myBattery = niceBattery(1)
    myBarometer = niceBarometer(2)
    myLeak = niceLeak(3)
    myHygrometer = niceHygrometer(4)

    print(myBattery.isAlive())
    print(myBattery.getVoltage())
    print(myBattery.getCurrent())

    print(myBarometer.getPressure())

    print(myLeak.isWater())

    print(myHygrometer.getPercentHum())