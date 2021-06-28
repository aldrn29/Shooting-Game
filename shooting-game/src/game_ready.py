from settings import *
from src.background import *
from PIL import Image, ImageDraw, ImageFont
from colorsys import hsv_to_rgb
from src.game_starter import GameStarter
from src.button import Button

class GameReady:
    def __init__(self):
        self.__width = SCREEN_WIDTH
        self.__height = SCREEN_HEIGHT
        self.__image = Image.new("RGB", (self.__width, self.__height))
        self.__draw = ImageDraw.Draw(self.__image)
        self.__fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        self.__background = list(BACKGROUND_INFO)
        self.__background_index = 0
        self.__choice_up = True
        self.__level = 1

    def __set_text(self, position, txt):
        self.__draw.text(position, txt, font=self.__fnt, fill=(255, 255, 255))

    def __set_menu(self, up):
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        if up : 
            self.__draw.rectangle((0, 0, self.__width, self.__height//2), outline=0, fill=rcolor)  
            self.__draw.rectangle((0, self.__height//2+1, self.__width, self.__height), outline=0, fill=(51, 51, 51))  
        else :
            self.__draw.rectangle((0, 0, self.__width, self.__height//2), outline=0, fill=(51, 51, 51))  
            self.__draw.rectangle((0, self.__height//2+1, self.__width, self.__height), outline=0, fill=rcolor)  
        self.__draw.rectangle((10, 10, self.__width-10, self.__height//2-10), outline=0, fill=(102, 102, 153))  
        self.__draw.rectangle((10, self.__height//2+11, self.__width-10, self.__height-10), outline=0, fill=(102, 204, 204))  
        self.__set_text((20, 20), '1. sky')
        self.__set_text((20, self.__height//2+21), '2. space')

    def __call__(self):
        button = Button()

        while True :
            self.__set_menu(self.__choice_up)

            # display image
            DISPLAY.image(self.__image)

            if button.up : 
                self.__background_index = 0
                self.__choice_up = True
            if button.down : 
                self.__background_index = 1
                self.__choice_up = False
            if button.b : 
                self.gameStart(self.__level, self.__background[self.__background_index])
                break

    def gameStart(self, level, background):
        game_starter= GameStarter(level, Background(background))
        game_starter()
