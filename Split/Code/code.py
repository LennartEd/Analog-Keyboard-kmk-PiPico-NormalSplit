print("start")
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys



keyboard = KMKKeyboard()
holdtap = HoldTap()

keyboard.modules.append(holdtap)
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())


# Enable debugging: http://kmkfw.io/docs/debugging/ 
# keyboard.debug_enabled = True 
    

# Key aliases
xxxxx = KC.NO
_____ = KC.TRNS
TEM2 = KC.MO(2)
L0 = KC.TG(0)
L2 = KC.TG(2)
N2 = KC.HT(KC.TG(2), KC.MO(1), prefer_hold=True, tap_interrupted=False, tap_time=None)
N0 = KC.HT(KC.TG(0), KC.MO(1), prefer_hold=True, tap_interrupted=False, tap_time=None)

# Keymap 
# fmt: off bvb 
keyboard.keymap = [
    [
       #TrashBase !!change to real one 
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
        KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                                     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,   KC.LGUI, 
        KC.TAB,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                                    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.DEL,  
        KC.DEL,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                                    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,  
                                            KC.LALT,KC.SPC,N2,KC.LCTL,                KC.ENT,KC.RCTL,KC.BSPC,   KC.LSFT,
                                                            
                                                                #encoder btn
                                                            KC.N1,           KC.N1,
                                                            KC.MPLY,           KC.N2,
        #Encoder 1 (horizontal) 
        KC.A,    # left encoder Clock
        KC.B,    # left encoder counterClock
        KC.C,    # right encoder Clock
        KC.D,    # right encoder counterClock
        
        #Encoder 2 (vertical)
        KC.VOLU,    # left encoder Clock
        KC.VOLD,    # left encoder counterClock
        KC.MW_UP,    # right encoder Clock
        KC.MW_DN,    # right encoder counterClock
    ],
    [
       #Numbers
        _____,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,                                 xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,_____, 
        _____,KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,                                 KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,_____,  
        _____,xxxxx,xxxxx,xxxxx,xxxxx,xxxxx,                                 KC.LEFT,KC.UP,KC.RIGHT,xxxxx,xxxxx,xxxxx,  
                                _____,_____,_____,  _____,       _____,_____,_____,KC.DOWN,
                                                            
                                                                #encoder btn
                                                            KC.N1,           KC.N1,
                                                            KC.N2,           KC.N2,
        #Encoder 1 (horizontal)
        KC.A,    # left encoder Clock
        KC.B,    # left encoder counterClock
        KC.C,    # right encoder Clock
        KC.D,    # right encoder counterClock 
        
        #Encoder 2 (vertical)
        KC.VOLU,    # left encoder Clock 
        KC.VOLD,    # left encoder counterClock
        KC.MW_UP,    # right encoder Clock
        KC.MW_DN,    # right encoder counterClock
    ],
    [
       #Gaming 
        KC.ESC,KC.M,KC.Q, KC.W,KC.E,KC.R,                              xxxxx,xxxxx,  KC.UP,  xxxxx,   xxxxx,_____, 
        KC.TAB,KC.LSFT,KC.A, KC.S,KC.D,KC.F,                            xxxxx,KC.LEFT,KC.DOWN,KC.RIGHT,xxxxx,_____,  
        N0,KC.LCTL,xxxxx,KC.G,KC.N,KC.B,                                xxxxx,xxxxx,  xxxxx,  xxxxx,   xxxxx,xxxxx,  
                            KC.N2,KC.SPC,KC.N1,KC.N4,         _____,_____,_____,_____,
                                                            
                                                                #encoder btn
                                                            KC.N1,           KC.N1,
                                                            KC.MPLY,           KC.N2,
        #Encoder 1 (horizontal) 
        KC.A,    # left encoder Clock
        KC.B,    # left encoder counterClock
        KC.C,    # right encoder Clock
        KC.D,    # right encoder counterClock
        
        #Encoder 2 (vertical)
        KC.VOLU,    # left encoder Clock
        KC.VOLD,    # left encoder counterClock
        KC.MW_UP,    # right encoder Clock
        KC.MW_DN,    # right encoder counterClock
    ],
    
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()