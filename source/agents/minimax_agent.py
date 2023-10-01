import math

from source.core.agent import Agent
from source.core.board import Board
from source.core.evaluation import evaluate

class MinimaxAgent(Agent):

    def get_move(self, board: Board, my_piece: int) -> int:
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        max_eval = -math.inf

        for move in options:
            copy_b = board.copy()
            copy_b.make_move(move, 1)
            eval = evaluate(copy_b)

            if eval > max_eval:
                max_eval = eval
                best_move = move


        return best_move