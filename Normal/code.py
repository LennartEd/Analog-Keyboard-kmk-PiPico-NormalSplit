print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB

# KEYTBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
keyboard.modules = [layers, encoders]

# SWITCH MATRIX
keyboard.col_pins = (board.GP9, board.GP10, board.GP11, board.GP12)
keyboard.row_pins = (board.GP13, board.GP14, board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoders.pins = ((board.GP3, board.GP4, board.GP5, False), (board.GP6, board.GP7, board.GP8, False),)

# EXTENSIONS
rgb_ext = RGB(pixel_pin = board.GP23, num_pixels=1, hue_default=100)
keyboard.extensions.append(rgb_ext)
keyboard.debug_enabled = False

___ = KC.TRNS
xxx = KC.NO

# KEYMAPS 
keyboard.keymap = [
    # MACROS 
    [
        KC.A,   KC.B,     KC.C,    KC.D,
        KC.E,   KC.F,     KC.G,    KC.H,
        KC.I,   KC.J,     KC.K,    KC.MO(1),
    ],
    [
        KC.N1, KC.N2, KC.N3, KC.N4,
        KC.N5, KC.N6, KC.N7, KC.N8,
        KC.N9, KC.X,  KC.Y,  ___,
    ]
]

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.MUTE)),   # MACROS
]

if __name__ == '__main__':
    keyboard.go()