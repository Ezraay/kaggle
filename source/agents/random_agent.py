import random

from core.agent import Agent
from core.board import Board
import time as time

class RandomAgent(Agent):
    def get_move(self, board: Board, my_piece: int) -> int:
        # connect 4 can only place piece in the topmost position
        # generate a list possible from the class Board and return a random move
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        return random.choice(options)
    
    def time_move(self, board: Board, my_piece: int):
        start = time.time()
        self.get_move(board,my_piece)
        res = time.time() - start
        print("This takes {res} seconds to respond.") 
