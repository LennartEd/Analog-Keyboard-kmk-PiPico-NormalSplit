![Image](https://github.com/LennartEd/Analog-Keyboard-kmk-PiPico-NormalSplit/blob/main/Images/DSC_0011.JPG)

# Analog-Keyboard-kmk-PiPico-NormalSplit
This is a fully analog keyboard using magnetic keys and hall sensors. I'm using a RP2040 but since it is KMK (circuitpython) based it should be compatible with other boards. I build a split keyboard, but any type form factor should work. 
This is my first experience with circuitpython so code might me wonky.

## PCB
**!DONT USE THE PCB PROVIDED!**
The PCB provided has some flaws that make it hard to work with.
**I would recomend making your own PCB and using mine as a template.**
In the future i might create v2 template that fixes the flaws

#### Parts
|Description | Part          | LCSC         |
|:-----------| ------------- |:-------------|
| Hall sensor| HX6659ISO-B   | C495742		|
| Multiplexer| CD74HC4067M96 | C496123		|
| TRRS jack  | PJ-3220-5A	 | C707251		|
| MCU		 | Waveshare RP2040-zero| --	|
| Capacitor 100uF| GRM21BR60J107ME15L| C141660|


#### Part notes
Hall sensor: 

Multiplexer: Curently any 16to1 Multiplexer should work (giving you 64 keys). If you are not hand soldering i recommend choosing a smaller sized one. Larger (32to1) should also work.

MCU: Any circuitpython compatible board should work. You just have to change the footprint on the PCB (which you should do anyway. See "Flaws with v1"

TRRS jack: 

Capacitor: Capacitors are not strictly nesesary but improve resulution. I tryed a few and found that 100uF worked the best.

#### How it works
The position of the magnet in the switch is red by the hall-effect sensor. Because the pi-pico only has 4 ADCs we need multiplexers to cycle between the sensors. 

#### Flaws with v1
- dont solder MCU doughterboard onto PCB directly
- bigger pads for handsoldering
- more mounting holes
- if posible 2 layer PCB for cost saving


## Code
To install the code connect your board and install circuitpython. Then copy the content of the "code" folder into the board. For editing the code you can use Thonny or any text editor.

#### pins
To make life easyer by not having to use "board.GP.." all the time, create (if not already present) a python file in lib/kmk/quickpin. Then add all the pins (see the other files for reference).
Now when imported with 
~~~
from kmk.quickpin.<boardTypeFolder>.<boardPins> import pinout as pins
~~~
into other files you can just use "pins[x]" to reference pins

#### kb.py:
Here you define most variables for you specific board.


#### Code.py


#### hallCali.py


#### analogio.py

## Case





