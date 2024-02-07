print("start")
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.handlers.sequences import send_string, simple_key_sequence


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
T2 = KC.HT(KC.CAPS, KC.MO(1))
L0 = KC.TG(0)
L2 = KC.TG(2)
N2 = KC.HT(KC.TG(2), KC.MO(1))
N0 = KC.HT(KC.TG(0), KC.MO(1), prefer_hold=True, tap_interrupted=False, tap_time=None)
nW = simple_key_sequence((KC.LALT(KC.TAB),KC.MPLY)) #KC.MACRO_SLEEP_MS(1000)
pas = send_string("hi")

# Keymap 
# fmt: off 
keyboard.keymap = [
    [
       #Default qwerty
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
        KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                                     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,   KC.LGUI, 
        KC.TAB,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                                    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.DEL,  
        KC.BSPC,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                                    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.PSCR,  
                                            N2,KC.SPC,KC.LALT,KC.LCTL,                KC.ENT,KC.RCTL,KC.BSPC,   KC.LSFT,
                                                            
                                                                #encoder btn
                                                                nW,                   KC.MPLY,
                                                            
                                                            
        #Encoder 1 (horizontal) 
        KC.LEFT,    # left encoder Clock
        KC.RIGHT,    # left encoder counterClock
        KC.DOWN,    # right encoder Clock
        KC.UP,    # right encoder counterClock
        
        #Encoder 2 (vertical) 
        KC.VOLD,    # left encoder Clock
        KC.VOLU,    # left encoder counterClock
        KC.MPRV,    # right encoder Clock
        KC.MNXT,    # right encoder counterClock
    ],
    [
       #Numbers 
        _____,pas,KC.F1,KC.F2,KC.F3,KC.F4,                                 KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10, 
        _____,KC.N0,KC.N1,KC.N2,KC.N3,KC.N4,                                 KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.F11,  
        _____,xxxxx,xxxxx,xxxxx,xxxxx,KC.RALT,                                 KC.LEFT,KC.UP,KC.DOWN,KC.RIGHT,xxxxx,KC.F12,  
                                _____,_____,_____,  _____,       _____,_____,_____,_____,
                                                            
                                                #encoder btn
                                                    _____,                   _____,
        #Encoder 1 (horizontal) 
        _____,    # left encoder Clock
        _____,    # left encoder counterClock
        _____,    # right encoder Clock
        _____,    # right encoder counterClock
        
        #Encoder 2 (vertical)
        _____,    # left encoder Clock
        _____,    # left encoder counterClock
        _____,    # right encoder Clock
        _____,    # right encoder counterClock
    ],
    [
       #Gaming 
        KC.ESC,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                                     KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,   KC.LGUI, 
        KC.TAB,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                                    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.DEL,  
        KC.DEL,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                                    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,  
                                            N2,KC.SPC,KC.LALT,KC.LCTL,                KC.ENT,KC.RCTL,KC.BSPC,   KC.LSFT,
                                                            
                                                                #encoder btn
                                                                _____,                   _____,
                                                            
                                                            
        #Encoder 1 (horizontal) 
        _____,    # left encoder Clock
        _____,    # left encoder counterClock
        _____,    # right encoder Clock
        _____,    # right encoder counterClock
        
        #Encoder 2 (vertical)
        _____,    # left encoder Clock
        _____,    # left encoder counterClock
        _____,    # right encoder Clock
        _____,    # right encoder counterClock
    ],
    
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
    