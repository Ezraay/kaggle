import random
from agents.random_agent import RandomAgent
from core.board import Board
import time as time

# This is to test if a move takes too long. Same as Random
# but take 5 more seconds.
class SlowAgent(RandomAgent):
    def get_move(self,board:Board,my_piece):
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        time.sleep(61)
        return random.choice(options)