#!/bin/python3

from gpiozero.pins.mock import MockFactory
from gpiozero import Device, Button
import zerorpc, inc.configParse as parse, time

## INITIALIZE ##

Device.pin_factory = MockFactory()

ports = parse.ports()
pins = parse.pins()

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:" + ports['doorSensor'])


## SETUP ##

doorSensor = Button(pins['doorSensor'])


## LOOP ##

while True:
  # Read door sensor pin
  # if Circuit OPEN:
  if not doorSensor.is_pressed():
    c.open()
  time.sleep(0.1)