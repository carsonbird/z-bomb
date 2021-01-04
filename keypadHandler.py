#!/bin/python3

import zerorpc, inc.configParse as parse

## INITIALIZE ##

ports = parse.ports()
settings = parse.settings()

master = zerorpc.Client()
master.connect("tcp://127.0.0.1:" + ports['master'])

keyBuffer = ""

def clearBuffer():
  '''Clears the code buffer'''
  print("KEYPAD: Clearing Key Buffer")
  global keyBuffer
  keyBuffer = ""
  # play clearing sound

def verifyBuffer():
  '''Checks the buffer against expected codes and sends results to controller'''
  if keyBuffer == disarmCode:
    print("KEYPAD: Unlock Code Accepted")
    master.codeCorrect()
  elif keyBuffer == resetCode:
    print("KEYPAD: Reset Code Accepted")
    master.reset()
  else:
    print("KEYPAD: Code Not Accepted")
    # Send state change to superserver
  clearBuffer()

class KeypadRPC(object):
  def keys(self, keys):
    '''Handles key inputs from keypadListener'''
    for key in keys:
      if key is '*':
        clearBuffer()
      elif key is '#':
        verifyBuffer()
      else:
        global keyBuffer
        keyBuffer += str(key)
        print("KEYPAD: Buffer = " + keyBuffer)
    return

s = zerorpc.Server(KeypadRPC())
print('KEYPAD: Binding Keypad on port ' + ports['keypad'])
s.bind("tcp://0.0.0.0:" + ports['keypad'])


## SETUP ##

disarmCode = settings['disarmCode']
resetCode =  settings['resetCode']


## RUN ##

s.run()