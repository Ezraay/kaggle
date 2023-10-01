import random
import math

from source.core.agent import Agent
from source.core.game_state import GameState
from source.core.board import Board



# https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
# https://stackoverflow.com/questions/71187789/why-my-connect4-minimax-doesnt-work-properly

class SmartAgent(Agent):

    def __init__(self):
        self.depth = 3

    def evaluate_window(self, window):
        score = 0

        if window.count(1) == 4:
            return 10000, True

        elif window.count(1) == 3 and window.count(0) == 1:
            score += 5

        elif window.count(1) == 2 and window.count(0) == 2:
            score += 2

        return score, False

    def evaluate(self, board_i):
        board = board_i.to_array()
        #board = board_i
        score = 0
        c_arr = []

        #
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         if j == 3:
        #             c_arr.append(board[i][j])
        #
        # c_count = c_arr.count(1)
        # score += c_count * 3
        #
        # c_count = c_arr.count(2)
        # score -= c_count * 3

        rows = 6
        cols = 7

        # horizontal
        for i in range(rows):
            for j in range(cols-3):
                window = [board[j][i], board[j+1][i], board[j+2][i], board[j+3][i]]
                res = self.evaluate_window(window)
                score += res[0]
                if res[1]:
                    return score

        # vertical
        for k in range(cols):
            for l in range(rows-3):
                window = [board[k][l], board[k][l+1], board[k][l+2], board[k][l+3]]
                res = self.evaluate_window(window)
                score += res[0]
                if res[1]:
                    return score

        # diagonal up
        for m in range(cols - 3):
            for n in range(rows - 3):
                window = [board[m][n], board[m+1][n+1], board[m+2][n+2], board[m+3][n+3]]
                res = self.evaluate_window(window)
                score += res[0]
                if res[1]:
                    return score

        # diagonal down
        for o in range(cols - 4):
            for p in range(rows-3, rows+1):
                window = [board[p][o], board[p-1][o+1], board[p-2][o+2], board[p-3][o+3]]
                res = self.evaluate_window(window)
                score += res[0]
                if res[1]:
                    return score

        return score

    def minimax(self, board, depth, maximiser):

        outcome = board.get_board_state(4)

        if depth == 0 or outcome != GameState.IN_PROGRESS:
            if outcome == GameState.PLAYER1_WON:
                return 10000000
            elif outcome == GameState.PLAYER2_WON:
                return -10000000
            else:
                return self.evaluate(board)

        if maximiser:
            max_eval = -math.inf
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, 1)
                    evalu = self.minimax(board, depth - 1, False)
                    max_eval = max(max_eval, evalu)
                    board.unmake_move()
            return max_eval

        else:
            min_eval = math.inf
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, 2)
                    evalu = self.minimax(board, depth - 1, True)
                    min_eval = min(min_eval, evalu)
                    board.unmake_move()
            return min_eval

    def get_move(self, board, my_piece: int, in_a_row: int):
        if my_piece == 1:
            best_move = None
            max_eval = -math.inf
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, my_piece)
                    evalu = self.minimax(board, self.depth - 1, False)
                    if evalu > max_eval:
                        max_eval = evalu
                        best_move = move
                    board.unmake_move()
            return best_move


