# z-bomb

Welcome to the z-bomb project! The purpose of this project is to create a puzzle-bomb in the CSI Room of The Escape Key.

## Puzzle Flow
The flow of the puzzle is as follows:

1. The bomb in its housing is fixed to the wall next to the door of the escape room.
2. The players' attention is directed to the bomb at the beginning of the room.
3. Players are instructed that the bomb will arm itself and count down from 60 seconds once opened, so they shouldn't open it until they believe they can disarm it.
4. To disarm the bomb, they will need 3 2-digit codes, discovered by solving mysteries around the room.
5. Players eventually find the 6-digit combo for the bomb.
6. Players open the outer casing of the bomb.
7. The bomb plays a few starting up noises, and begins counting down from 60. The time is displayed on a screen.
8. Players input the 6 digit code, and hit the "`#`" button, believing this will shut down the bomb.
  1. If players input the wrong code, there is no penalty, only an incorrect feedback noise.
  2. If players press the "`*`" button, the disarm code buffer will be cleared.
9. If they input the right code, the bomb will NOT shut down, but will continue to count down. However, the box the keypad is connected to will suddenly pop open. It was secretly a door.
10. Behind this door is a jumble of colored wires. 3 of them are pink.
11. If groups pull out the 3 pink wires, the bomb will disarm itself, the countdown will cease, and a victory sound will be played.
  1. If any of the other wires are removed, the bomb explodes.
  2. If the timer hits zero, the bomb explodes.
12. If, at any time, a special reset code known only to gamemasters is input, the bomb will reset itself, give the gamemaster a few seconds to close the door, and the bomb will return to its original state, ready to arm itself if the door opens.

## What's been done so far?

In this repo, you will find a file titled "`CSI Exit Puzzle.drawio`". This is a flowchart file. You can view it using software provided by [Diagrams.net](https://www.diagrams.net/). It's basically a free open-source version of LucidChart. Pretty nifty. Anyway, inside this file, you'll find a sort-of state machine explaining the flow of the bomb from a programmer's perspective, as well as a diagram of layered pictures showing how the bomb should look physically and be constructed. The size of this diagram is accurate to scale.

I have begun writing the code for the bomb itself. I follow a sort-of "microservice architecture" in the designing of this bomb. If you don't know what that is, look it up. Basically, each python file is responsible for only 1 thing, and it listens to things around it and reacts based on the input it receives. For example:

1. The `doorSensorListener.py` listens for whether or not the door is closed.
2. If the door is opened, the door listener "`doorSensorListener.py`" tells the door logic handler "`doorSensorHandler.py`" that the door is open.
3. "`doorSensorHandler.py`" forwards this information to the master server "`superserver.py`", which handles the game logic of the whole bomb itself.
4. When the "`superserver.py`" hears that the door has been opened, it tells the speaker handler, "`speakerHandler.py`" to play the power-up sound through the speakers. It also creates the timer subprocess, "`timer.py`", which immediately begins counting, and tells the various handlers to play ticking sounds, and print the current time on the display.

Pretty simple, right? The reason I built it this way is because it makes coding it up very simple. Each piece is separate and independent of the others, and only has to worry about its little part of the overall machine.

It also makes completing the whole project much easier, as everything could be simulated virtually, before breaking out the soldering iron and wiring everything together on the Raspberry Pi. Troubleshooting will also be really easy, because the problems can be isolated down to their individual components.

You can find the relationship and communication routes between these microservices by looking at the drawio diagram, in the top right corner.

## What still needs to be done?

At this point, a few things:

1. We need to move the code to a Raspberry Pi and set up a physical development area.
2. Substitute the virtual testing parts out for actual pin-outs on the Raspberry Pi. 
3. We'll need to wire those parts in to the Raspberry Pi, and test it. 
4. We'll need to find audio files for the different sounds.
5. Begin and complete work on the pink wiring part.

## Other Notes

Startup:
The Operating System spawns the superserver.py.

superserver.py spawns:
- magnetHandler.py
- speakerHandler.py
- keypadHandler.py
- doorSensorHandler.py
- timerHandler.py
- displayHandler.py

superserver also spawns the timer when the players open the door.