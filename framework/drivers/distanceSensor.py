_autor_ = "Jorge R. Encinas"
import os
from time import sleep

from framework.drivers.simulator.dataVirtual import dataVirtual

from framework.drivers.driver import driver


class Ultrasonic(driver):
    def __init__(self):
        self.file = 'sensorUltrasonico.gpio.serial'
        self.file = os.path.join(os.getcwd(), 'DroneFramework', 'drivers', 'virtual', self.file)
        self.SensorVirtual = dataVirtual(dataVirtual.ULTRASONIC, self.file)
        # self.sensorVirtual = SensorVirtual('ultrasonico', file)
        try:
            self.SensorVirtual.start()
        except KeyboardInterrupt:
            if self.SensorVirtual.getRunStatus():
                self.SensorVirtual.stop()
        print 'mode virtual sensor: Ultrasonido is runing'

    def getData(self):
        return {'altura': self.SensorVirtual.getData()}

    def getStatus(self):
        # tiene los datos del sensor
        # ok, no_ok, excepcion,
        return 'ok'

    def forceRead(self):
        # fuerza a hacer una nueva lectura al sensor
        return self.getData()

    def reset(self):
        # inicializa datos sensor
        self.SensorVirtual.stop()
        sleep(.1)
        self.SensorVirtual = dataVirtual(dataVirtual.ULTRASONIC, self.file)
        self.SensorVirtual.start()

    def stop(self):
        self.SensorVirtual.stop()
