import random
import math

from core.agent import Agent
from core.game_state import GameState



# https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
# https://stackoverflow.com/questions/71187789/why-my-connect4-minimax-doesnt-work-properly

class SmartAgent(Agent):

    def __init__(self):
        self.depth = 5

    def evaluate_window(self, window):

        score = 0

        if window.count(1) == 4:
            return 10000, True

        elif window.count(1) == 3 and window.count(0) == 1:
            score += 5

        elif window.count(1) == 2 and window.count(0) == 2:
            score += 2

        if window.count(2) == 3 and window.count(0) == 1:
            score -= 4

        return score, False

    def evaluate(self, board_i):
        board = board_i.to_array()
        score = 0
        c_arr = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j == 3:
                    c_arr.append(board[i][j])

        c_count = c_arr.count(1)
        score += c_count * 3

        c_count = c_arr.count(2)
        score -= c_count * 3

        # horizontal
        for r in range(len(board)):
            r_array = board[r]
            for c in range(4):
                window = r_array[c: c + 4]
                score += self.evaluate_window(window)[0]


        # vertical
        transposed = []
        for c in range(len(board[0])):
            col_ar = []
            for r in range(len(board)):
                col_ar.append(board[r][c])
            transposed.append(col_ar)

        for r in range(len(transposed)):
            r_array = transposed[r]
            for c in range(4):
                window = r_array[c: c + 4]
                score += self.evaluate_window(window)[0]
                if self.evaluate_window(window)[1]:
                    return score

        # pos diag (Up Right)
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window)[0]

        # neg diag (Down Left)
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                window = [board[r + 3 - i][c + 3 - i] for i in range(4)]
                score += self.evaluate_window(window)[0]

        return score

    def minimax(self, board, depth, maximiser):

        if depth == 0 or board.get_board_state(4) != GameState.IN_PROGRESS:


        # player 1 (red) wants to max
        if maximiser:
            max_eval = -math.inf
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, 1)
                    evalu = self.minimax(board, depth - 1, False)
                    max_eval = max(max_eval, evalu)
                    board.revert(move)
            return max_eval

        # player 2 wants min
        else:
            min_eval = math.inf
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, 2)
                    evalu = self.minimax(board, depth - 1, True)
                    min_eval = min(min_eval, evalu)
                    board.revert(move)
            return min_eval

    def get_move(self, board, my_piece: int):
        if my_piece == 1:
            best_move = None
            max_eval = -100000000
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, my_piece)
                    evalu = self.minimax(board, self.depth - 1, False)
                    if evalu > max_eval:
                        max_eval = evalu
                        best_move = move
                    board.revert(move)
            return best_move

        else:
            best_move = None
            min_eval = 100000000
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, my_piece)
                    evalu = self.minimax(board, self.depth - 1, True)
                    if evalu < min_eval:
                        min_eval = evalu
                        best_move = move
                    board.revert(move)
            return best_move

