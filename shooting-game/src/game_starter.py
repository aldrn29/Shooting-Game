from settings import *
from src.object_controller import ObjectController
from src.game_status import GameStatus
from src.button import Button
from src.game_objects import Player, Enemy, Missile, BoomEffect
import random, time

class GameStarter:
    def __init__(self, level, background):
        self.__level = level
        self.__background = background
        self.__step = 0
        self.__boss = False
        GameStatus.setGamePlay(True)
 
    def __next_step(self):
        self.__step = self.__step + 1
        self.__set_enemy()

    ###
    # name, spawnTime, spawnNumber, postiion(direction)
    ###
    def __set_enemy(self):
        
        if self.__step == 0:
            self.__name = 'enemy1'
            self.__spawn_time = 3
            self.__spawn_number = 5
            self.__direction = 'random'
        if self.__step == 1:
            self.__name = 'enemy2'
            self.__spawn_time = 0.7
            self.__spawn_number = 3
            self.__direction = 'left'
        if self.__step == 2:
            self.__name = 'enemy2-2'
            self.__spawn_time = 0.7
            self.__spawn_number = 3
            self.__direction = 'right'
        if self.__step == 3:
            self.__name = 'enemy2'
            self.__spawn_time = 0.6
            self.__spawn_number = 5
            self.__direction = 'left'
        if self.__step == 4:
            self.__name = 'enemy2-2'
            self.__spawn_time = 0.6
            self.__spawn_number = 5
            self.__direction = 'right'
        if self.__step == 5:
            self.__name = 'enemy3'
            self.__spawn_time = 10
            self.__spawn_number = 1
            self.__direction = 'middle'
        if self.__step == 6:
            self.__name = 'boss'
            self.__spawn_time = 20
            self.__spawn_number = 1
            self.__direction = 'middle'

        self.__position = (random.randint(1, SCREEN_WIDTH-1), 0)
        if self.__direction == 'left': self.__position = (1, 0)
        elif self.__direction == 'right': self.__position = (SCREEN_WIDTH-1, 0)
        elif self.__direction == 'middle': self.__position = (SCREEN_WIDTH//2, 0)

    def __call__(self):
        GameStatus.start()
        ObjectController.reset()
        player = Player(START_POINT)
        button = Button()
        self.__set_enemy()

        prev_time = time.time()
        number = 0

        while True :
            # player control
            kill = player.kill_point

            if button.left : 
                player.move('L')
            elif button.right :
                player.move('R')
            elif button.up : 
                player.move('U')
            elif button.down :
                player.move('D')
        
            if button.a :
                player.shoot()

            # display image
            DISPLAY.image(self.__background())

            if GameStatus.getGamePlay():
                # game play
                if time.time() - prev_time > self.__spawn_time :
                    if self.__spawn_number > number :
                        if self.__direction == 'random' : self.__position = (random.randint(2, SCREEN_WIDTH-2), 0)
                        if self.__name == 'boss' : self.__boss = True
                        Enemy(self.__position, self.__name)
                        number += 1
                        prev_time = time.time()
                    else :
                        number = 0
                        self.__next_step()

                # game end
                enemy = ObjectController.getEnemyObjects() 
                if player.hp <= 0 or (self.__boss and len(list(enemy[0])) <= 0) : 
                    GameStatus.setPlayerWin(False) if player.hp <= 0 else GameStatus.setPlayerWin(True)
                    GameStatus.end()
                    prev_time = time.time()
            
            if not GameStatus.getGamePlay() and time.time() - prev_time > 5:
                GameStatus.setGameReady(True)
                GameStatus.setGamePlay(False)
                break

