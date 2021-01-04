#!/bin/python3

import os
import inc.configParse as parse

ports = parse.ports()

os.system("konsole -e ./superserver.py &\
konsole -e ./displayHandler.py &\
konsole -e ./magnetHandler.py &\
konsole -e ./speakerHandler.py &\
konsole -e ./timerHandler.py &\
konsole -e ./doorSensorHandler.py &\
konsole -e ./keypadHandler.py &")

os.chdir('/home/carson/.local/bin/')

choice = os.popen('choice=$(kdialog --menu "Choose your action:" door "Open door" code "Enter code" bad "Remove wrong wire" good "Remove all correct wires" close "Close the door"); echo $choice').read().rstrip()
print(choice)

while choice != 0:
  if choice == "door":
    os.system("./zerorpc tcp://127.0.0.1:" + ports['doorSensor'] + " open")
  elif choice == "code":
    code = "'" + os.popen('code=$(kdialog --title "Bomb Keypad" --inputbox "Code: \n(* to clear and # to submit)"); echo $code').read().rstrip() + "'"
    os.system("./zerorpc tcp://127.0.0.1:" + ports['keypad'] + " keys " + code)
  elif choice == "bad":
    os.system("./zerorpc tcp://127.0.0.1:" + ports['master'] + " wiresBad")
  elif choice == "good":
    os.system("./zerorpc tcp://127.0.0.1:" + ports['master'] + " wiresGood")
  elif choice == "close":
    os.system("./zerorpc tcp://127.0.0.1:" + ports['doorSensor'] + " closed")
  else:
    break
  choice = os.popen('choice=$(kdialog --menu "Choose your action:" door "Open door" code "Enter code" bad "Remove wrong wire" good "Remove all correct wires" close "Close the door"); echo $choice').read().rstrip()
  print(choice)
