#!/bin/python3

import zerorpc, inc.configParse as parse

## INITIALIZE

ports = parse.ports()
# audio = parse.audio()

# def play(fileName, bigSpeaker=False):
#   '''Play sound on a specified speaker'''
#   if bigSpeaker:
#     print("Playing " + fileName + " on big speaker")
#   else:
#     print("Playing " + fileName + " on tiny speaker")


class SpeakerRPC(object):
  # def tick(self, fileName=audio['tick']):
  #   '''Plays a beep on the small speaker'''
  #   play(fileName)

  # def fail(self, fileName=audio['fail']):
  #   '''Plays the out-of-time sound'''
  #   play(fileName)

  # def blam(self, fileName=audio['blam']):
  #   '''Plays an explosion on the big speaker'''
  #   play(fileName, 1)
  
  # def arm(self, fileName=audio['arm']):
  #   '''Plays an arming / spin-up sound'''
  #   play(fileName)

  # def correct(self, fileName=audio['correct']):
  #   play(fileName)

  # def reset(self, fileName=audio['reset']):
  #   play(fileName)

  # def release(self, fileName=audio['release']):
  #   play(fileName)

  # def disarm(self, fileName=audio['disarm']):
  #   play(fileName)

  def play(self, fileName, bigSpeaker=False):
    '''Play sound on a specified speaker'''
    if bigSpeaker:
      print("Playing " + fileName + " on big speaker")
    else:
      print("Playing " + fileName + " on tiny speaker")

s = zerorpc.Server(SpeakerRPC())
print("Binding Speaker on port " + ports['speaker'])
s.bind("tcp://0.0.0.0:" + ports['speaker'])


## SETUP ##

# Create large and small speaker objects


## RUN ##

s.run()