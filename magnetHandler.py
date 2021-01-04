#!/bin/python3

import zerorpc, inc.configParse as parse

## INITIALIZE ##

ports = parse.ports()

class MagnetRPC(object):
  def release(self):
    '''Tells the magnets to release'''
    # Set magnet pin to low
    print("MAGNET: Releasing Magnets")

  def engage(self):
    '''Tells the magnets to release'''
    # Set magnet pin to low
    print("MAGNET: Engaging Magnets")

s = zerorpc.Server(MagnetRPC())
print('MAGNET: Binding Magnet on port ' + ports['magnet'])
s.bind("tcp://0.0.0.0:" + ports['magnet'])


## SETUP ##

# Set magnet pin to high


## RUN ##

s.run()