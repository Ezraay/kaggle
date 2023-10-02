import math
import random
from abc import abstractmethod

from source.core.agent import Agent
from source.core.board import Board
from source.core.game_state import GameState

class MinimaxAgent(Agent):
    def __init__(self, depth=2):
        self.depth = depth

    @abstractmethod
    def evaluate_window(self, window: list[int], in_a_row: int):
        pass

    def evaluate(self, board: Board, in_a_row: int):
        score = 0
        i = 0

        # horizontal
        for y in range(board.height):
            for x in range(board.width - in_a_row + 1):
                window = board.get_window(x, y, 1, 0, in_a_row)
                score += self.evaluate_window(window, in_a_row)
                i += 1

        # vertical
        for y in range(board.height - in_a_row + 1):
            for x in range(board.width):
                window = board.get_window(x, y, 0, 1, in_a_row)
                score += self.evaluate_window(window, in_a_row)
                i += 1

        # bottom-left to upper-right
        for y in range(board.height - in_a_row + 1):
            for x in range(board.width - in_a_row + 1):
                window = board.get_window(x, y, 1, 1, in_a_row)
                score += self.evaluate_window(window, in_a_row)
                i += 1

        # upper-left to bottom-right
        for y in range(in_a_row - 1, board.height):
            for x in range(board.width - in_a_row + 1):
                window = board.get_window(x, y, 1, -1, in_a_row)
                score += self.evaluate_window(window, in_a_row)
                i += 1

        return score

    def minimax(self, board: Board, depth: int, max_player: bool, player: int, opponent: int, in_a_row: int):
        current_eval = self.evaluate(board, in_a_row)

        if depth == 0 or board.get_board_state(in_a_row) != GameState.IN_PROGRESS:
            return current_eval

        if max_player:
            max_eval = -99999999
            options = [x for x in list(range(board.width)) if board.can_make_move(x)]

            for move in options:
                new_b = board.copy()
                new_b.make_move(move, player)
                eval = self.minimax(new_b, depth - 1, False, player, opponent, in_a_row)
                max_eval = max(max_eval, eval)
            return max_eval

        else:
            min_eval = 99999999
            options = [x for x in list(range(board.width)) if board.can_make_move(x)]

            for move in options:
                new_b = board.copy()
                new_b.make_move(move, opponent)
                eval = self.minimax(new_b, depth - 1, True, player, opponent, in_a_row)
                min_eval = min(min_eval, eval)
            return min_eval

    def get_move(self, board: Board, my_piece: int, in_a_row: int) -> int:

        opponent = 3 - my_piece

        best_move = None

        if my_piece == 1:
            max_eval = -9999999
            max = True
        else:
            min_eval = 9999999
            max = False

        options = [x for x in list(range(board.width)) if board.can_make_move(x)]

        for move in options:
            new_b = board.copy()
            new_b.make_move(move, my_piece)
            eval = self.minimax(new_b, self.depth, max, my_piece, opponent, in_a_row)

            if max:
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            else:
                if eval < min_eval:
                    min_eval = eval
                    best_move = move

        return best_move

    def get_move_old(self, board: Board, my_piece: int, in_a_row: int) -> int:

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
            eval_i = self.evaluate(board, in_a_row)
            if board.get_board_state(in_a_row) != GameState.IN_PROGRESS:
                board.unmake_move()
                return move

            opponent_options = [x for x in list(range(board.width)) if board.can_make_move(x)]

            for opp_move in opponent_options:
                board.make_move(opp_move, opp_piece)
                eval_o = self.evaluate(board, in_a_row)
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