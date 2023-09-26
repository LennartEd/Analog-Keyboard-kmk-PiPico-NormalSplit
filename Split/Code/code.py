print("start")
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
#from test import test
#from analog import Analog

# fmt: off
# ↓ EDIT CONFIG HERE ↓
klor_variant = "polydactyl"  # Options: "polydactyl", "konrad", "yubitsume", "saegewerk"
klor_rgb = "peg_rgb"        # Options: "basic_rgb", "peg_rgb", "none"
klor_oled = False           # Options: True, False
klor_speaker = False        # Options: True, False
# ↑ EDIT CONFIG HERE ↑
# fmt: on

keyboard = KMKKeyboard(klor_variant, klor_rgb, klor_oled, klor_speaker)

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

# Keymap dd
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
    [
       #LOWER
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
               KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                     KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,           \
      _______,  KC.ESC, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx, KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, _______,  \
      _______, KC.CAPS, KC.TILD, xxxxxxx, xxxxxxx, xxxxxxx, KC.MUTE,   KC.MPLY, xxxxxxx, xxxxxxx, xxxxxxx, KC.PIPE,  KC.DQT, _______,  \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx,  KC.ENT, xxxxxxx,  KC.DEL,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
]
# fmt: onl

if __name__ == "__main__":
    keyboard.go()