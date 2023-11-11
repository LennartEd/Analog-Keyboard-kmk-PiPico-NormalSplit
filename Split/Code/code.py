print("start")
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap


keyboard = KMKKeyboard()
holdtap = HoldTap()

keyboard.modules.append(holdtap)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# Enable debugging: http://kmkfw.io/docs/debugging/
# keyboard.debug_enabled = True 


# Key aliases
xxxxx = KC.NO
_____ = KC.TRNS
RAISE = KC.MO(1)
LOWER = KC.MO(0)
N2 = KC.HT(KC.TG(2), KC.MO(1), prefer_hold=True, tap_interrupted=False, tap_time=None)
N0 = KC.HT(KC.TG(0), KC.MO(1), prefer_hold=True, tap_interrupted=False, tap_time=None)

# Keymap 
# fmt: off
keyboard.keymap = [
    [
       #TrashBase !!change to real one
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
        KC.ESC,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                                            KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.E, 
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                                          KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.ENT,  
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                                          KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,  
                                             KC.LALT,KC.SPC, N2,KC.LCTR,        KC.BSPC,   KC.TAB,   KC.DEL,   KC.N9,
                                                            
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
       #Numbers
        _____,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,                                 xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,_____, 
        _____,KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,                                 KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,_____,  
        _____,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,                                xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,  
                                _____,_____,_____,  _____,       _____,_____,_____,_____,
                                                            
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
       #Numbers
        _____,xxxxx,xxxxx,KC.W,xxxxx,xxxxx,                                 xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,_____, 
        _____,xxxxx,KC.A, KC.S,KC.D, xxxxx,                                 KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,_____,  
        _____,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,                                xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,  
                                _____,_____,N0   ,_____,       _____,_____,_____,_____,
                                                            
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
# fmt: on

if __name__ == "__main__":
    keyboard.go()