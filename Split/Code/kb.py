
from kmk.quickpin.RP2040.YD_RP2040 import pinout as pins
#from kmk.quickpin.pro_micro.sparkfun_promicro_rp2040 import pinout as pins
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.analogio import AnalogScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.encoder2 import RotaryioEncoder2



# from kmk.extensions.peg_rgb_matrix import Color

# fmt: off
# DO NOT EDIT 'led_positions':
led_positions = [
    19, 18, 13, 12,  6,  5,                  27, 28, 34, 35, 40, 41,
    20, 17, 14, 11,  7,  4,                  26, 29, 33, 36, 39, 42,
    21, 16, 15, 10,  8,  3,                  25, 30, 32, 37, 38, 43,
                     9,  2, 1, 0,    22, 23, 24, 31,
]
# fmt: on

# fmt: off
# --8<-- [start:rgbdata]
# EDIT your [R, G, B] values below if you set the variable klor_rgb = 'peg_rgb':
rgb_data = [
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],                                                              [251, 64, 0], [254, 255, 0], [63, 255, 0], [0, 255, 128], [0, 191, 255], [0, 0, 255],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],                                                              [251, 64, 0], [254, 255, 0], [63, 255, 0], [0, 255, 128], [0, 191, 255], [0, 0, 255],
    [0, 0, 255], [0, 191, 255], [0, 255, 128], [63, 255, 0], [254, 255, 0], [251, 64, 0],                                                              [251, 64, 0], [254, 255, 0], [63, 255, 0], [0, 255, 128], [0, 191, 255], [0, 0, 255],
                                                             [254, 255, 0], [251, 64, 0], [247, 0, 122], [188, 255, 249],   [188, 0, 249], [247, 0, 122],[251, 64, 0], [254, 255, 0],
]
# --8<-- [end:rgbdata]
# fmt: on

# Creates a tuple containing both LED position and RGB data
pos_rgb = [(x, y) for x, y in zip(led_positions, rgb_data)]

# Cuts necessary for KLOR variants with less keys
cuts = {
    "polydactyl": [],
    "konrad": [0, 22],
    "yubitsume": [19, 20, 21, 41, 42, 43],
    "saegewerk": [0, 19, 20, 21, 22, 41, 42, 43],
}


class KMKKeyboard(_KMKKeyboard):
    def __init__(
        self,
        klor_variant="saegewerk",
        klor_rgb="none",
        klor_oled=False,
        klor_speaker=False,
    ):
        # create and register the scanner(s)
        self.matrix = [
            AnalogScanner(
                inPins = self.analogPins,
                outPins = self.outPins,
                numOfKeys = self.numberOfKeys,
                analogAttrib = self.analogKeyAttribut
            ),
            
            KeysScanner(
            # require argument:
            pins=self.encoderBtnPins,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
            ),
            RotaryioEncoder(
                pin_a=self.encoder1_a,
                pin_b=self.encoder1_b,
                divisor=2,
            ),
            RotaryioEncoder2(
                pin_a=self.encoder2_a,
                pin_b=self.encoder2_b,
                divisor=2,
            ),
            
             
        ]

        # Split code:
        split = Split(
            split_flip=True,  # If both halves are the same, but flipped, set this True
            split_side=None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
            split_type=SplitType.UART,  # Defaults to UART
            uart_interval=1,  # Sets the uarts delay. Lower numbers draw more power
            data_pin=self.rx,  # The primary data pin to talk to the secondary device with
            data_pin2=self.tx,  # Second uart pin to allow 2 way communication
            use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
        )
        self.modules.append(split)
        
        self.setup_oled(klor_oled)
        self.setup_speaker(klor_speaker)
        self.setup_rgb(klor_variant, klor_rgb)
    
    #VARIABLES----------------------------------------------------------------------------------------------------------------------
    analogPins = (      #analog pins from which values are read
    pins[29],pins[28],
    )
    outPins = (        #digital pins to controll multiplexers
    pins[2],pins[3],pins[4],pins[5]
    )
    numberOfKeys = 22  #number of analog keys
    
    analogKeyAttribut = [ #choose per key modes and values (positive means threshold negativ means rapid trigger
        [
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
                        50000,50000,50000,50000,
            0,0,0,0,0,0,#dont change zeros
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
                        50000,50000,50000,50000,
        ],
        [
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
                        50000,50000,50000,50000,
            0,0,0,0,0,0,#dont change zeros
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
            50000,50000,50000,50000,50000,50000,
                        50000,50000,50000,50000,
        ],
    
    ]
    
    encoderBtnPins = [pins[6],pins[7]] #pins for the encoder buttons
    
    #encoder1 pins
    encoder1_a = pins[12] 
    encoder1_b = pins[13]
    #encoder2 pins
    encoder2_a = pins[14]
    encoder2_b = pins[15]
    
    SCL = None 
    SDA = None
    rx = pins[1]
    tx = pins[0]
    buzzer_pin = None
    rgb_pixel_pin = pins[23] #LED pin

    # OLED Code:
    def setup_oled(self, klor_oled):
        if klor_oled == True:
            from kmk.extensions.peg_oled_Display import (
                Oled,
                OledDisplayMode,
                OledReactionType,
                OledData,
            )

            # --8<-- [start:oled]
            oled_ext = Oled(
                OledData(
                    corner_one={
                        0: OledReactionType.STATIC,
                        1: ["Layer"],
                    },
                    corner_two={
                        0: OledReactionType.LAYER,
                        1: ["0", "1", "2"],
                    },
                    corner_three={
                        0: OledReactionType.LAYER,
                        1: ["BASE", "RAISE", "LOWER"],
                    },
                    corner_four={
                        0: OledReactionType.LAYER,
                        1: ["qwerty", "nums", "sym"],
                    },
                ),
                toDisplay=OledDisplayMode.TXT,
                flip=True,
                # oHeight=64,
            )
            # --8<-- [end:oled]
            self.extensions.append(oled_ext)

    # Speaker Code:
    def setup_speaker(self, klor_speaker):
        if klor_speaker == True:
            import digitalio
            import pwmio
            import time

            buzzer = pwmio.PWMOut(self.buzzer_pin, variable_frequency=True)
            OFF = 0
            ON = 2**15
            buzzer.duty_cycle = ON
            buzzer.frequency = 2000
            time.sleep(0.2)
            buzzer.frequency = 1000
            time.sleep(0.2)
            buzzer.duty_cycle = OFF

    # Basic RGB code:
    def basic_rgb(self, pixels):
        from kmk.extensions.RGB import RGB

        # --8<-- [start:rgb]
        rgb = RGB(
            pixel_pin=self.rgb_pixel_pin,
            num_pixels=pixels,
            val_limit=50,
            hue_default=0,
            sat_default=100,
            val_default=20,
        )
        # --8<-- [end:rgb]
        self.extensions.append(rgb)

    # PEG_RGB code (per key RGB):
    def peg_rgb(self, led_display):
        from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Rgb_matrix_data

        rgb_ext = Rgb_matrix(
            ledDisplay=led_display,
            split=True,
            rightSide=False,
            disable_auto_write=True,
        )
        self.extensions.append(rgb_ext)

    # "Calculate" the RGB data for a specifig KLOR variant:
    def trim_display(self, pos_rgb, cut):
        return [d for (p, d) in pos_rgb if p not in cut]

    # "Calculate" the position data for a specifig KLOR variant:
    def trim_pos(self, pos_rgb, cut):
        cut_pos = [p for (p, d) in pos_rgb if p not in cut]
        old_to_new = {old: new for new, old in enumerate(sorted(cut_pos))}
        return [old_to_new[p] for p in cut_pos]

    # Setup for peg_rgb or basic_rgb:
    def setup_rgb(self, klor_variant, klor_rgb):
        if klor_rgb == "peg_rgb":

            self.brightness_limit = 0.3
            # Exctract and trim the position data from the pos_rgb tuple according to a KLOR variant:
            self.led_key_pos = self.trim_pos(pos_rgb, cuts[klor_variant])
            # Return the number of items in the exctracted and trimmed data from above:
            self.num_pixels = len(self.led_key_pos)
            # Pass the specifig [R, G, B] data for a KLOR variant via 'led_display' into peg_rgb():
            self.peg_rgb(self.trim_display(pos_rgb, cuts[klor_variant]))

        if klor_rgb == "basic_rgb":
            # In basic RGB implementation you only pass the LED count per side not the total of both sides:
            half_pos = len(self.trim_pos(pos_rgb, cuts[klor_variant])) // 2
            # Pass the number of LEDs of one keyboard half via 'half_pos' into basic_rgb():
            self.basic_rgb(pixels=(half_pos))

    # NOQA
    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,         33, 32, 31, 30, 29, 28,
        6,  7,  8,  9, 10, 11,         39, 38, 37, 36, 35, 34,
       12, 13, 14, 15, 16, 17,         45, 44, 43, 42, 41, 40,
               18, 19, 20, 21,         49, 48, 47, 46,
                              22,   50,
                              23,   51,
                       24, 25,         53, 52,
                       26, 27,         55, 54,
    ]
    # fmt: on
