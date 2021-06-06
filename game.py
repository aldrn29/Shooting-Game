import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
disp.image(image)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

udlr_fill = "#00FF00"
udlr_outline = "#00FFFF"
button_fill = "#FF00FF"
button_outline = "#FFFFFF"

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

x = width / 2 - 15
y = height - 30
w = 30
h = 10

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        draw.ellipse((x, y, x+10, y+10), outline=udlr_outline, fill=udlr_fill)
    def move(self):
        self.y += 5
        draw.ellipse((self.x, self.y, self.x+10, self.y+10), outline=udlr_outline, fill=udlr_fill)

class SpawnEnemy():
    def __init__(self, num):
        self.num = num
        self.arr = []
        for i in range(num):
            self.arr.append(Enemy(random.randint(0, width - 15), random.randint(0, 30) - 30))
    def move(self):
        for i in range(self.num):
            self.arr[i].move()

draw.rectangle((x, y, x+w, y+h), outline=udlr_outline, fill=udlr_fill)
enemy = SpawnEnemy(10)
start = time.time()

while True:
    spawnTime = time.time() - start
    if spawnTime > 10:
        enemy = SpawnEnemy(10)
        start = time.time()
        
    if not button_U.value:  # up pressed 
        y -= 5
    if not button_D.value:  # down pressed
        y += 5
    if not button_L.value:  # left pressed
        x -= 5
    if not button_R.value:  # right pressed
        x += 5

    #if not button_C.value:  # center pressed
    #if not button_A.value:  # A button pressed
    #if not button_B.value:  # B button pressed
    
    #Clear display
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

    enemy.move()
    draw.rectangle((x, y, x+w, y+h), outline=button_outline, fill=button_fill)     
    
    # Display the Image
    disp.image(image)

    time.sleep(0.01)


