#!/bin/python3

import zerorpc, inc.configParse as parse
from Adafruit_LED_Backpack import AlphaNum4



## INITIALIZE ##

ports = parse.ports()

class DisplayRPC(object):
  def displaySeconds(self, seconds):
    '''Writes <seconds> to the display'''
    print("DISPLAY: " + str(seconds))
    # Write seconds to display

  def displayMessage(self, message):
    '''Writes scrolling message to display'''
    # Handle this
    print("DISPLAY: " + message)

s = zerorpc.Server(DisplayRPC())
print('DISPLAY: Binding Display on port ' + ports['display'])
s.bind("tcp://0.0.0.0:" + ports['display'])


## SETUP ##


## RUN ##

s.run()