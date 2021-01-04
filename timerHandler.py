#!/bin/python3

import zerorpc, inc.configParse as parse

## INITIALIZE ##

ports = parse.ports()
audio = parse.audio()

master = zerorpc.Client()
master.connect("tcp://127.0.0.1:" + ports['master'])

display = zerorpc.Client()
display.connect("tcp://127.0.0.1:" + ports['display'])

speaker = zerorpc.Client()
speaker.connect("tcp://127.0.0.1:" + ports['speaker'])

class TimerRPC(object):
  def clock(self, seconds):
    '''Receives seconds remaining and sends them where appropriate'''
    print("TIMER: " + str(seconds) + " seconds")
    display.displaySeconds(seconds)
    speaker.play(audio['tick'])
    # Do stuff with the seconds, like send it to the display

  def zero(self):
    '''Tells superserver that time is up'''
    # Tell superserver that time's up
    print("TIMER: Timer hit zero")
    master.timeZero()

s = zerorpc.Server(TimerRPC())
print('TIMER: Binding Timer on port ' + ports['timer'])
s.bind("tcp://0.0.0.0:" + ports['timer'])


## SETUP ##


## RUN ##

s.run()