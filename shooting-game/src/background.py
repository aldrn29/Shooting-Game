from src.object_controller import ObjectController
from src.game_status import GameStatus
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
from settings import *
import random, os

###
# Background information
###

BACKGROUND_INFO = {
    'background' : {
        'path' : os.path.join(IMAGE_PATH, 'background.png'),
        'width' : 240,
        'height' : 240,
        'name' : 'background'
    },
    'background2' : {
        'path' : os.path.join(IMAGE_PATH, 'background2.png'),
        'width' : 240,
        'height' : 240,
        'name' : 'background2'
    }
}

###
# Class
###

class Background:
    def __init__(self, name='background'):
        self.__name = name
        self.__width = SCREEN_WIDTH
        self.__height = SCREEN_HEIGHT
        self.__scroll_speed = 8
        self.__crop_point = SCREEN_HEIGHT
        self.__image = Image.open(BACKGROUND_INFO[self.name]['path']).resize((self.width, self.height))
        self.__fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

    @property
    def name(self):
        return self.__name

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
        
    def __get_image(self):
        ###
        # Scroll crop point calculation
        ###
        if self.__crop_point - self.__scroll_speed <= 0 :
            self.__crop_point = self.height
        else :
            self.__crop_point -= self.__scroll_speed
        ###
        # image move
        ###
        image = Image.open(BACKGROUND_INFO[self.name]['path']).resize((self.width, self.height))
        empty_image = Image.new('RGBA', (self.width, self.height))
        cropped_image1 = image.crop((0, self.__crop_point, self.width, self.height))
        cropped_image2 = image.crop((0, 0, self.width, self.__crop_point))
        empty_image.paste(cropped_image1, (0, 0))
        empty_image.paste(cropped_image2, (0, self.height-self.__crop_point))
        self.__image = empty_image
        return self.__image

    def __set_text(self, background, text):
        draw = ImageDraw.Draw(background)
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((38, 150), text, font=self.__fnt, fill=rcolor)

    def __call__(self):
        ObjectController.renew()
        background_image = self.__get_image()

        ###
        # Player's objects are sticked on the background image
        ###
        objects = ObjectController.getPlayerObjects()
        player, player_missiles = objects
        for info in player.items() :
            player_object = info[1]
            new_image = Image.alpha_composite(background_image.crop(player_object.image_coord), player_object.image)		
            background_image.paste(new_image, (player_object.image_coord[0], player_object.image_coord[1]))
        for info in player_missiles.items() :
            player_missile_object = info[1]
            new_image = Image.alpha_composite(background_image.crop(player_missile_object.image_coord), player_missile_object.image)		
            background_image.paste(new_image, (player_missile_object.image_coord[0], player_missile_object.image_coord[1]))

        ###
        # Enemy's objects are sticked on the background image
        ###
        objects = ObjectController.getEnemyObjects()
        enemy, enemy_missiles = objects
        for info in enemy.items() :
            enemy_object = info[1]
            new_image = Image.alpha_composite(background_image.crop(enemy_object.image_coord), enemy_object.image)		
            background_image.paste(new_image, (enemy_object.image_coord[0], enemy_object.image_coord[1]))        
        for info in enemy_missiles.items() :
            enemy_missile_object = info[1]
            new_image = Image.alpha_composite(background_image.crop(enemy_missile_object.image_coord), enemy_missile_object.image)		
            background_image.paste(new_image, (enemy_missile_object.image_coord[0], enemy_missile_object.image_coord[1]))

        ###
        # Effect objects are sticked on the background image
        ###    
        effect_objects = ObjectController.getEffectObjects()
        for info in effect_objects.items() :
            effect_object = info[1]
            new_image = Image.alpha_composite(background_image.crop(effect_object.image_coord), effect_object.image)		
            background_image.paste(new_image, (effect_object.image_coord[0], effect_object.image_coord[1]))        

        ###
        # Set Text
        ###
        game_text = GameStatus.getGameText()
        self.__set_text(background_image, game_text)

        return background_image
