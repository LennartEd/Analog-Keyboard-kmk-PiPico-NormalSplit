
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

#LED order
led_positions = [
    19, 18, 13, 12,  6,  5,                  27, 28, 34, 35, 40, 41,
    20, 17, 14, 11,  7,  4,                  26, 29, 33, 36, 39, 42,
    21, 16, 15, 10,  8,  3,                  25, 30, 32, 37, 38, 43,
                     9,  2, 1, 0,    22, 23, 24, 31,
]

rgb_data = [
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],                                                              [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],                                                              [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],                                                              [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], 
                                                [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 25, 25],               [0, 25, 25],[0, 0, 0], [0, 0, 0], [0, 0, 0],
]

# Creates a tuple containing both LED position and RGB data
pos_rgb = [(x, y) for x, y in zip(led_positions, rgb_data)]


class KMKKeyboard(_KMKKeyboard):
    def __init__(
        self
    ):
        # create and register the scanner(s)
        self.matrix = [
            
            AnalogScanner(
                inPins = self.analogPins,
                outPins = self.outPins,
                multiNum = self.multiplexer,
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
            uart_flip = False,
            use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
        )
        self.modules.append(split)
        
        self.setup_rgb()
    
    analogPins = (      #analog pins from which values are read
    pins[27],pins[26],
    )
    outPins = (pins[15],pins[14],pins[13],pins[12]) #pins to control the multiplexers
    
    multiplexer = 16 #number of input pins of the multiplexer
    
    numberOfKeys = 22  #number of analog keys (per side if its split)
    

    
    analogKeyAttribut = [ #choose per key modes and values (positive means threshold negativ means rapid trigger 
        [
            2,2,2,2,2,2,
            2,2,2,2,2,2,
            2,2,2,2,2,2,
                  2,2,2,
                      2,
            
            0,0,0,0,0,0,
            
            2,2,2,2,2,2,
            2,2,2,2,2,2,
            2,2,2,2,2,2,
                  2,2,2,
                      2,
        ],
        [
            2,2,2,2,2,2,
            2,2,2,2,2,2,
            2,2,2,2,2,2,
                  2,2,2,
                      2,
            
            0,0,0,0,0,0,
            
            2,2,2,2,2,2,
            2,2,2,2,2,2,
            2,2,2,2,2,2,
                  2,2,2,
                      2,
        ],
        [
            2,2,2,-0.2,2,2,
            2,2,-0.2,-0.2,-0.2,2,
            2,2,2,2,2,2,
                  2,2,2,
                      2,
            
            0,0,0,0,0,0,
            
            2,2,2,2,2,2,
            2,2,2,2,2,2,
            2,2,2,2,2,2,
                  2,2,2,
                      2,
        ],
    ]
    
    encoderBtnPins = [pins[7]] #pins for the encoder buttons
    
    #encoder1 pins
    encoder1_a = pins[11] 
    encoder1_b = pins[10]
    #encoder2 pins
    encoder2_a = pins[9]
    encoder2_b = pins[8]
    
    rx = pins[1]
    tx = pins[0]
    rgb_pixel_pin = pins[16] #LED pin

    # Basic RGB code:
    def basic_rgb(self, pixels):
        from kmk.extensions.RGB import RGB

        rgb = RGB(
            pixel_pin=self.rgb_pixel_pin,
            num_pixels=pixels,
            val_limit=50,
            hue_default=0,
            sat_default=100,
            val_default=20,
        )
        
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

    # "Calculate" the position data
    def trim_pos(self, pos_rgb, cut):
        cut_pos = [p for (p, d) in pos_rgb if p not in cut]
        old_to_new = {old: new for new, old in enumerate(sorted(cut_pos))}
        return [old_to_new[p] for p in cut_pos]

    # Setup for peg_rgb or basic_rgb:
    def setup_rgb(self):
            self.brightness_limit = 0.1
            # Exctract and trim the position data from the pos_rgb tuple 
            self.led_key_pos = self.trim_pos(pos_rgb, [])
            # Return the number of items in the exctracted and trimmed data from above:
            self.num_pixels = len(led_positions)
            # Pass the specifig [R, G, B] data via 'led_display' into peg_rgb():
            #self.peg_rgb(self.trim_display(pos_rgb, []))
            self.peg_rgb(rgb_data)

    coord_mapping = [
        0,  1,  2,  3,  4,  5,         32, 31, 30, 29, 28, 27,
        6,  7,  8,  9, 10, 11,         38, 37, 36, 35, 34, 33,
       12, 13, 14, 15, 16, 17,         44, 43, 42, 41, 40, 39,
               18, 19, 20, 21,         48, 47, 46, 45,
                              22,   49,
                              
                       23, 24,         51, 50,
                       25, 26,         53, 52,
    ]
    
