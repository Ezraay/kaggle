import math
import random

from source.core.agent import Agent
from source.core.board import Board
from source.core.evaluation import evaluate
from source.core.game_state import GameState

class MinimaxAgent(Agent):

    def get_move(self, board: Board, my_piece: int, in_a_row: int) -> int:

        if my_piece == 1:
            opp_piece = 2
            maximise = True
        else:
            opp_piece = 1
            maximise = False

        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        random.shuffle(options)

        if maximise:
            best_eval = -999999999
        else:
            best_eval = 999999999

        for move in options:
            board.make_move(move, my_piece)
            eval_i = evaluate(board, in_a_row)
            if board.get_board_state(4) != GameState.IN_PROGRESS:
                board.unmake_move()
                return move

            opponent_options = [x for x in list(range(board.width)) if board.can_make_move(x)]

            for opp_move in opponent_options:
                board.make_move(opp_move, opp_piece)
                eval_o = evaluate(board, in_a_row)
                board.unmake_move()
                if maximise:
                    eval_i = min(eval_i, eval_o)
                else:
                    eval_i = max(eval_i, eval_o)

            board.unmake_move()

            if maximise and eval_i > best_eval:
                best_eval = eval_i
                best_move = move

            elif not maximise and eval_i < best_eval:
                best_eval = eval_i
                best_move = move

        return best_move