import analogio
import digitalio
import time

import keypad

from kmk.scanners import Scanner
from kmk.modules import Module
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

class AnalogScanner(Scanner):
    def __init__(self,inPins, outPins,numOfKeys,analogAttrib):
        self.inPins = [analogio.AnalogIn(pin) for pin in inPins]
        self.outPins = [digitalio.DigitalInOut(pin) for pin in outPins]
        for pin in self.outPins:
            pin.direction = digitalio.Direction.OUTPUT
        
        self.aValold = [0]*16*len(inPins)
        self.aVal = [0]*16*len(inPins)
        self.que = []
        
        self.pressed = [False]*16*len(inPins)
        self.numOfKeys = numOfKeys
        
        self.analogAttrib = analogAttrib
        
        self.I = 0
        self.st = 0
        self.end = 0
            
    @property
    def key_count(self):
        return self.numOfKeys
    
    def scan_for_changes(self):
        '''
        Poll the analog pins for changes and return either None (if nothing updated)
        or a KeyEvent object if the pin value exceeds the threshold.
        '''
        
        if len(self.que) == 0:
            for i in range(16): #cycles through multiplexer
                self.outPins[0].value = (i & 0b0001) != 0
                self.outPins[1].value = (i & 0b0010) != 0
                self.outPins[2].value = (i & 0b0100) != 0
                self.outPins[3].value = (i & 0b1000) != 0
                for index, j in enumerate(self.inPins):    #reads multiplexers and stored thier values
                    self.aVal[i + 16 * index] = j.value
            
            for i in range(self.numOfKeys):
                
                if self.analogAttrib[keyboard.active_layers[0]][i + self.offset] > 0: #threshold mode
                    if self.aVal[i] > self.analogAttrib[keyboard.active_layers[0]][i + self.offset] and self.pressed[i] == False:
                        self.pressed[i] = True
                        self.que.append(i)
                    elif self.aVal[i] < self.analogAttrib[keyboard.active_layers[0]][i + self.offset] and self.pressed[i] == True:
                        self.pressed[i] = False
                        self.que.append(i)
                        
                elif self.analogAttrib[keyboard.active_layers[0]][i + self.offset] < 0: #rapid trigger mode
                    print("rapid trigger not implemented")
                     
        elif len(self.que) > 0:
            temp = self.que.pop(0)
            #print(temp + self.offset, self.pressed[temp])
            return keypad.Event(temp+self.offset, self.pressed[temp])
            
                
        
        """
        #for time messuring
        self.I += 1
        if self.I % 2 == 0:
            self.st = time.monotonic_ns()
        elif self.I % 2 == 1:
            self.end = time.monotonic_ns()
            print((self.end-self.st)/1000000)
        """
        #print("hi")
        #return keypad.Event(35,True)
        #print("js")
            
        
        
    
