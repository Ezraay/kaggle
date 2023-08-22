import random
from source.core.agent import Agent
from source.core.board import Board

class RandomAgent(Agent):
    def get_move(self, board: Board, my_piece: int) -> int:
        # connect 4 can only place piece in the topmost position
        # generate a list possible from the class Board and return a random move
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        return random.choice(options)












