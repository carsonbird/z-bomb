#!/bin/python3

import zerorpc, inc.configParse as parse, time

## INITIALIZE ##

ports = parse.ports()
settings = parse.settings()

# Connect to keypadHandler
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:" + ports['timer'])


## SETUP ##

seconds = int(settings['initialSeconds'])


## LOOP ##

while seconds > 0:
  c.clock(seconds)
  seconds -= 1
  time.sleep(1)

c.zero()