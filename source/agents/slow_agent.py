import random
from source.agents.random_agent import RandomAgent
from source.core.board import Board
import time as time

# This is to test if a move takes too long. Same as Random
# but take 3 more seconds. It will pass the first
class SlowAgent(RandomAgent):
    def get_move(self,board:Board,my_piece):
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        time.sleep(3)
        return random.choice(options)