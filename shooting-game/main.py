from src.game_ready import GameReady
from src.game_status import GameStatus


while True:
    if GameStatus.getGameReady():
        GameStatus.setGameReady(False)
        game_ready = GameReady()
        game_ready()