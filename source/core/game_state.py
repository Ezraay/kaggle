from enum import IntEnum


class GameState(IntEnum):
    """
    An enumeration representing the possible states of a ConnectX game.

    Attributes:
    ----------
    IN_PROGRESS: int
        The game is still ongoing, and no player has won yet.
    PLAYER1_WON: int
        Agent1 has achieved the required condition and won the game.
    PLAYER2_WON: int
        Agent2 has achieved the required condition and won the game.
    TIE: int
        The game has concluded without either player winning, typically when the board is full.
    """
    IN_PROGRESS = 0
    PLAYER1_WON = 1
    PLAYER2_WON = 2
    TIE = 3
