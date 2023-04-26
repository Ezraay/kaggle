import random

from core.agent import Agent
from core.board import Board


class RandomAgent(Agent):
    def get_move(self, board: Board, my_piece: int) -> int:
        options = [x for x in list(range(board.size[0])) if board.can_make_move(x)]
        return random.choice(options)
