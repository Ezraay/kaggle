import math

from source.core.agent import Agent
from source.core.board import Board
from source.core.evaluation import evaluate
from source.core.game_state import GameState

class MinimaxAgent(Agent):

    def get_move(self, board: Board, my_piece: int) -> int:
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        max_eval = -999999999
        best_move = options[0]

        for move in options:
            min_eval = math.inf

            board.make_move(move, 1)
            eval_i = evaluate(board)
            board.unmake_move()
            if eval_i > 10000:
                return move

            # opponent_options = [x for x in list(range(board.width)) if board.can_make_move(x)]
            # for opp_move in opponent_options:
            #     their_copy = my_copy.copy()
            #     their_copy.make_move(opp_move, 2)
            #
            #     eval_o = evaluate(their_copy)
            #     eval_i = min(eval_i, eval_o)



            if eval_i > max_eval:
                max_eval = eval_i
                best_move = move

        return best_move