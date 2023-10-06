print("start")
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
#from test import test
#from analog import Analog

# fmt: off

# fmt: on

keyboard = KMKKeyboard()

#keyboard.modules.append(Analog())
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
#keyboard.extensions.append(test())

# Enable debugging: http://kmkfw.io/docs/debugging/
# keyboard.debug_enabled = True 


# Key aliases
xxxxx = KC.NO
_____ = KC.TRNS
RAISE = KC.MO(1)
LOWER = KC.MO(0)

# Keymap 
# fmt: off
keyboard.keymap = [
    [
       #BASE
        
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
        KC.Q,     KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.EQL, 
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.ENT,  
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,  
                           KC.LCTR, KC.LALT, KC.SPC,  RAISE,                       KC.N7,   KC.N6,   KC.N7,   KC.N9,
                                                            
                                                                #encoder btn
                                                            KC.N1,           KC.N1,
                                                            KC.N2,           KC.N2,
        # Encoders
        KC.A,    # encoder 1 left side
        KC.B,    # encoder 1 left side
        KC.C,    # encoder 1 Right side
        KC.D,    # encoder 1 Right side
        
        KC.E,    # encoder 2 left side
        KC.F,    # encoder 2 left side
        KC.G,    # encoder 2 right side
        KC.H,    # encoder 2 right side
    ],
    [
       #RAISE
        KC.Q,     KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.EQL, 
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.ENT,  
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,  
                           KC.LCTR, KC.LALT, KC.SPC,  RAISE,                       KC.N7,   KC.N6,   KC.N7,   KC.N9,
                                                            
                                                                #encoder btn
                                                            KC.N1,           KC.N1,
                                                            KC.N2,           KC.N2,
        # Encoders 
        KC.A,    # encoder 1 left side
        KC.B,    # encoder 1 left side
        KC.C,    # encoder 1 Right side
        KC.D,    # encoder 1 Right side
        
        KC.E,    # encoder 2 left side
        KC.F,    # encoder 2 left side
        KC.G,    # encoder 2 right side
        KC.H,    # encoder 2 right side
    ],
    
]
# fmt: onl

if __name__ == "__main__":
    keyboard.go()