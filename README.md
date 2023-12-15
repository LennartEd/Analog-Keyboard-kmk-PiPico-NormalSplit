![Image](https://github.com/LennartEd/Analog-Keyboard-kmk-PiPico-NormalSplit/blob/main/Images/DSC_0011.JPG)

# Analog-Keyboard-kmk-PiPico-NormalSplit
This is a fully analog keyboard using magnetic keys and hall sensors. I'm using a RP2040 but since it is KMK (circuitpython) based it should be compatible with other boards. I build a split keyboard, but any type form factor should work. 
This is my first experience with circuitpython so code might me wonky.

## PCB
**DONT USE THE PCB PROVIDED**
The PCB provided has some flaws that make it hard to work with.
**I would recomend making your own PCB and using mine as a template**
In the future i might create v2 template that fixes the flaws

#### how it works

#### flaws with v1

## Code
To install the code connect your board and install circuitpython. Then copy the content of the "code" folder into the board. For editing the code you can use Thonny or any text editor.

#### pins
To make life easyer and not having to use "board.GP.." all the time, create (if not already present) a python file in lib/kmk/quickpin. Then add all the pins (see the other files for reference).
Now when imported with 
~~~
from kmk.quickpin.<boardTypeFolder>.<boardPins> import pinout as pins
~~~
into other files you can just use "pins[x]" to reference pins

#### kb.py:
here you define most variables for you specific board.

First

