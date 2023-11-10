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
    def __init__(self,inPins,outPins,multiNum,numOfKeys,analogAttrib):
         
        self.inPins = [analogio.AnalogIn(pin) for pin in inPins] #setup pins where analog signals are read
        
        self.outPins = [digitalio.DigitalInOut(pin) for pin in outPins] #setup pins to controll multiplexers
        for pin in self.outPins:
            pin.direction = digitalio.Direction.OUTPUT
        
        self.multiNum = multiNum
        
        self.aVal = [self.inPins[0].value]*self.multiNum*len(inPins) #array to store current value
        self.aValold = [self.inPins[0].value]*self.multiNum*len(inPins) #array to store last value
        self.que = [] #que to store keys which have to be pressed
        
        self.pressed = [False]*self.multiNum*len(inPins) #array to store state of keys 
        self.numOfKeys = numOfKeys #number of keys
        
        
        
        self.analogAttrib = analogAttrib #per key info about threshold/press type
               
    @property
    def key_count(self):
        return self.numOfKeys
    
    def scan_for_changes(self):
        '''
        Poll the analog pins for changes and return either None (if nothing updated)
        or a KeyEvent object if the pin value exceeds the threshold.
        '''
        #print(self.offset)
        if len(self.que) == 0: #if no key is in que
            for i in range(self.multiNum): #cycles through multiplexer
                self.outPins[0].value = (i & 0b0001) != 0
                self.outPins[1].value = (i & 0b0010) != 0
                self.outPins[2].value = (i & 0b0100) != 0
                self.outPins[3].value = (i & 0b1000) != 0
                for index, j in enumerate(self.inPins):    #read and stored analog values
                    self.aVal[i + self.multiNum * index] = j.value
            #print(self.aVal)
            
            for i in range(self.numOfKeys): #checks if values have changed
                #threshold mode
                #print(i,i+self.offset)
                if self.analogAttrib[keyboard.active_layers[0]][i + self.offset] > 0:
                    if self.aVal[i] < self.analogAttrib[keyboard.active_layers[0]][i + self.offset] and self.pressed[i] == False:
                        self.pressed[i] = True
                        self.que.append(i)
                    elif self.aVal[i] > self.analogAttrib[keyboard.active_layers[0]][i + self.offset] and self.pressed[i] == True:
                        self.pressed[i] = False
                        self.que.append(i)
                #rapid trigger mode      
                elif self.analogAttrib[keyboard.active_layers[0]][i + self.offset] < 0: 
                    if self.aVal[i] < self.aValold[i] - abs(self.analogAttrib[keyboard.active_layers[0]][i + self.offset]):
                        self.aValold[i] = self.aVal[i]
                        if not self.pressed[i]:
                            self.pressed[i] = True
                            self.que.append(i)
                    elif self.aVal[i] > self.aValold[i] + abs(self.analogAttrib[keyboard.active_layers[0]][i + self.offset]):
                        self.aValold[i] = self.aVal[i]
                        if self.pressed[i]:
                            self.pressed[i] = False
                            self.que.append(i)
                     
        elif len(self.que) > 0: #if keys in que: remove one from que and send return 
            temp = self.que.pop(0)
            #print(temp, self.pressed[temp])
            return keypad.Event(temp+self.offset, self.pressed[temp])

            
        
        
    
