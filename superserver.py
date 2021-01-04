#!/bin/python3

import zerorpc, inc.configParse as parse, time
import subprocess as sub
import os
import signal

## INITIALIZE ##

ports = parse.ports()
audio = parse.audio()

# magnetHandler = sub.Popen(['python3', 'magnetHandler.py'])
# speakerHandler = sub.Popen(['python3', 'speakerHandler.py'])
# keypadHandler = sub.Popen(['python3', 'keypadHandler.py'])
# # keypadListener = sub.Popen(['python3', 'keypadListener.py'])
# doorSensorHandler = sub.Popen(['python3', 'doorSensorHandler.py'])
# # doorSensorListener = sub.Popen(['python3', 'doorSensorListener.py'])
# timerHandler = sub.Popen(['python3', 'keypadHandler.py'])
# displayHandler = sub.Popen(['python3', 'displayHandler.py'])

speaker = zerorpc.Client()
speaker.connect("tcp://127.0.0.1:" + ports['speaker'])

magnet = zerorpc.Client()
magnet.connect("tcp://127.0.0.1:" + ports['magnet'])

# Will point to the timer subprocess, once it is created.
timer = ""

def killTimer():
  global timer
  print("MASTER: Killing Timer")
  timer.terminate()

def victory():
  print("MASTER: Victory!")
  speaker.play(audio['victory'])

def startCountdown():
  print("MASTER: Countdown Starting...")
  global timer
  timer = sub.Popen(['python3', 'timer.py'])
  speaker.play(audio['arm'])

def spinUp():
  print("MASTER: Powering up...")
  speaker.play(audio['power'])
  time.sleep(2)

def disarm():
  # Disarm and stuff
  print("MASTER: BOMB DISARMED")
  speaker.play(audio['disarm'])
  killTimer()
  time.sleep(2)
  victory()

def fail():
  print("MASTER: Failed")
  speaker.play(audio['fail'])
  time.sleep(1)
  explode()
  
def explode():
  speaker.play(audio['blam'], True)
  print("MASTER: KABLAM")
  killTimer()

class MasterRPC(object):
  def doorOpen(self):
    print("MASTER: Door Handler says Door Opened")
    spinUp()
    startCountdown()

  def doorClose(self):
    print("MASTER: Door Handler says Door Closed")

  def codeCorrect(self):
    print("MASTER: Code Correct")
    speaker.play(audio['correct'])
    time.sleep(3)
    magnet.release()
    speaker.play(audio['release'])

  def wiresGood(self):
    print("MASTER: Wires Good")
    disarm()

  def wiresBad(self):
    print("MASTER: Wires Bad")
    fail()

  def timeZero(self):
    print("MASTER: Time's up!")
    fail()

  def reset(self):
    print("MASTER: Resetting...")
    global timer
    if timer.poll() is None:
      killTimer()
    print("MASTER: Engaging Magnet")
    magnet.engage()
    speaker.play(audio['reset'])
    
    

s = zerorpc.Server(MasterRPC())
print('Binding Master on port ' + ports['master'])
s.bind("tcp://0.0.0.0:" + ports['master'])


## SETUP ##


## RUN ##

s.run()