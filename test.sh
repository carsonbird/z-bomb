#!/bin/zsh

echo "OPENING STUFF"

cd /home/carson/proj/ek/z-bomb

konsole -e ./superserver.py &
konsole -e ./displayHandler.py &
konsole -e ./magnetHandler.py &
konsole -e ./speakerHandler.py &
konsole -e ./timerHandler.py &
konsole -e ./doorSensorHandler.py &
konsole -e ./keypadHandler.py &

cd /home/carson/.local/bin

echo "PRESS TO OPEN DOOR"

read -r -s

echo "OPENING DOOR"
./zerorpc tcp://127.0.0.1:65534 open

echo "PRESS TO INPUT INCORRECT CODE"

read -r -s

echo "INPUT INCORRECT CODE"
./zerorpc tcp://127.0.0.1:65531 keys 1
./zerorpc tcp://127.0.0.1:65531 keys 2
./zerorpc tcp://127.0.0.1:65531 keys 3
./zerorpc tcp://127.0.0.1:65531 keys 4
./zerorpc tcp://127.0.0.1:65531 keys '#'

echo "PRESS TO INPUT CORRECT CODE"

read -r -s

echo "INPUT CORRECT CODE"
./zerorpc tcp://127.0.0.1:65531 keys 0
./zerorpc tcp://127.0.0.1:65531 keys 0
./zerorpc tcp://127.0.0.1:65531 keys 0
./zerorpc tcp://127.0.0.1:65531 keys 0
./zerorpc tcp://127.0.0.1:65531 keys '#'

