import time

class GameStatus:
    __game_ready = True
    __game_play = False
    __game_txt = ''

    __player_win = False

    @classmethod
    def getGameReady(cls):
        return cls.__game_ready

    @classmethod
    def setGameReady(cls, ready):
        cls.__game_ready = ready

    @classmethod
    def getGamePlay(cls):
        return cls.__game_play

    @classmethod
    def setGamePlay(cls, play):
        cls.__game_play = play

    @classmethod
    def getGameTxt(cls):
        return cls.__game_txt

    @classmethod
    def setPlayerWin(cls, win):
        cls.__player_win = win

    @classmethod
    def start(cls):
        cls.__game_play = True
        cls.__game_txt = ''

    @classmethod
    def end(cls):
        cls.__game_play = False
        
        if cls.__player_win : 
            cls.__game_txt = ' You Win!'
        else : cls.__game_txt = 'GameOver!'


