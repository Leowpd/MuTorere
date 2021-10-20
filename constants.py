# file with all the constants

# Constants for Main
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


ERROR_MESSAGE = "That is not a valid entry, please select 0-8"


LABEL_TO_POS = {
    0: (1, 1),
    1: (0, 1),
    2: (0, 2),
    3: (1, 2),
    4: (2, 2),
    5: (2, 1),
    6: (2, 0),
    7: (1, 0),
    8: (0, 0),
}


P1COLOR = "white"
P2COLOR = "black"


# Constants for GUI

LABELS = {
    "Putahi": (115.00, -230.00),
    "Tahi": (-25.00, 280.00),
    "Rua": (141.42, 221.42),
    "Toru": (235.00, 40.00),
    "Wha": (161.42, -141.42),
    "Rima": (-25.00, -210.00),
    "Ono": (-216.42, -141.42),
    "Whitu": (-315.00, 40.00),
    "Waru": (-211.42, 221.42),
    "Plyr Clrs": (-300.00, -245.0)
}


POSITIONS = {
    (1, 1): (-50.00, 50.00),  # PUTAHI
    (0, 1): (-50.00, 250.00),  # TAHI
    (0, 2): (91.42, 191.42),  # RUA
    (1, 2): (150.00, 50.00),  # TORU
    (2, 2): (91.42, -91.42),  # WHA
    (2, 1): (-50.00, -150.00),  # RIMA
    (2, 0): (-191.42, -91.42),  # ONO
    (1, 0): (-250.00, 50.00),  # WHITU
    (0, 0): (-191.42, 191.42),  # WARU
}


# Constants for logic:

BOARD_SETUP = [[1.0, 2.0, 2.0], [1.0, 0.0, 2.0], [1.0, 1.0, 2.0]]
