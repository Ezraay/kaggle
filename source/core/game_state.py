from enum import IntEnum


class GameState(IntEnum):
    IN_PROGRESS = 0
    PLAYER1_WON = 1
    PLAYER2_WON = 2
    TIE = 3
