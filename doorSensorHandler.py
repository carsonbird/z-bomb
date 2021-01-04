#!/bin/python3

import zerorpc, inc.configParse as parse

## INITIALIZE ##

ports = parse.ports()

master = zerorpc.Client()
master.connect("tcp://127.0.0.1:" + ports['master'])

class DoorSensorRPC(object):
  def open(self):
    '''Sends open status on up to controller'''
    print("DOOR: Sensed Door Open")
    master.doorOpen()

  def closed(self):
    print("DOOR: Sensed Door Closed")
    master.doorClose()

s = zerorpc.Server(DoorSensorRPC())
print('DOOR: Binding Door Sensor on port ' + ports['doorSensor'])
s.bind("tcp://0.0.0.0:" + ports['doorSensor'])

## SETUP ##


## RUN ##

s.run()