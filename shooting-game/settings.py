import adafruit_rgb_display.st7789 as st7789
from digitalio import DigitalInOut, Direction
import board
import datetime


# Create the display
PIN_CS = DigitalInOut(board.CE0)
PIN_DC = DigitalInOut(board.D25)
PIN_RESET = DigitalInOut(board.D24)
BAUDRATE = 24000000

SPI = board.SPI()
DISPLAY = st7789.ST7789(
    SPI,
    height=240,
    y_offset=80,
    rotation=180,
    cs=PIN_CS,
    dc=PIN_DC,
    rst=PIN_RESET,
    baudrate=BAUDRATE,
)

# Input pins:
BUTTON_A = DigitalInOut(board.D5)
BUTTON_A.direction = Direction.INPUT

BUTTON_B = DigitalInOut(board.D6)
BUTTON_B.direction = Direction.INPUT

BUTTON_L = DigitalInOut(board.D27)
BUTTON_L.direction = Direction.INPUT

BUTTON_R = DigitalInOut(board.D23)
BUTTON_R.direction = Direction.INPUT

BUTTON_U = DigitalInOut(board.D17)
BUTTON_U.direction = Direction.INPUT

BUTTON_D = DigitalInOut(board.D22)
BUTTON_D.direction = Direction.INPUT

BUTTON_C = DigitalInOut(board.D4)
BUTTON_C.direction = Direction.INPUT

# Turn on the Backlight
BACKLIGHT = DigitalInOut(board.D26)
BACKLIGHT.switch_to_output()
BACKLIGHT.value = True

SCREEN_WIDTH = DISPLAY.width
SCREEN_HEIGHT = DISPLAY.height
START_POINT = (SCREEN_WIDTH//2, 4*(SCREEN_HEIGHT//5))

IMAGE_PATH = 'images'
