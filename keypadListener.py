#!/bin/python3

import zerorpc, inc.configParse as parse, time
import adafruit_matrixkeypad
from digitalio import DigitalInOut
import board

## INITIALIZE ##

ports = parse.ports()

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:" + ports['keypad'])

# Classic 3x4 matrix keypad
cols = [DigitalInOut(x) for x in (board.D2, board.D0, board.D4)]
rows = [DigitalInOut(x) for x in (board.D1, board.D6, board.D5, board.D3)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)


## SETUP ##


## LOOP ##

while True:
  keys = keypad.pressed_keys
  if keys:
    c.keys(keys)
  time.sleep(0.1)