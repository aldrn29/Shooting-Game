from settings import *

###
# Class
###

class Button:
    def __init__(self):
        self.__left = BUTTON_L
        self.__right = BUTTON_R
        self.__up = BUTTON_U
        self.__down = BUTTON_D
        self.__a = BUTTON_A
        self.__b = BUTTON_B
        self.__C = BUTTON_C

    @property
    def left(self):
        return False if self.__left.value else True
    @property
    def right(self):
        return False if self.__right.value else True
    @property
    def up(self):
        return False if self.__up.value else True
    @property
    def down(self):
        return False if self.__down.value else True
    @property
    def a(self):
        return False if self.__a.value else True
    @property
    def b(self):
        return False if self.__b.value else True
    @property
    def c(self):
        return False if self.__c.value else True