import math

from source.core.agent import Agent
from source.core.board import Board
from source.core.evaluation import evaluate

class MinimaxAgent(Agent):

    def get_move(self, board: Board, my_piece: int) -> int:
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        max_eval = -math.inf

        for move in options:
            min_eval = math.inf
            board.make_move(move, 1)
            eval_i = evaluate(board)

            opponent_options = [x for x in list(range(board.width)) if board.can_make_move(x)]
            for opp_move in opponent_options:
                board.make_move(opp_move, 2)

                eval_o = evaluate(board)
                eval_i = min(eval_i, eval_o)
                board.unmake_move()
            board.unmake_move()

            if eval_i > max_eval:
                max_eval = eval_i
                best_move = move

        return best_move