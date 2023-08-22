import random
import math

from source.core.agent import Agent
from source.core.game_state import GameState
from source.core.game import Game

from source.core.board import Board


# https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
# https://stackoverflow.com/questions/71187789/why-my-connect4-minimax-doesnt-work-properly

class SmartAgent(Agent):

    def __init__(self):
        self.depth = 1

    def evaluate_window(self, window):

        score = 0
        if window.count(1) == 4 and window.count(0) == 0:
            score += 100000
        # elif window.count(1) == 3 and window.count(0) == 1:
        #     score += 10
        # elif window.count(1) == 2 and window.count(0) == 2:
        #     score += 3
        #
        if window.count(2) == 4 and window.count(1) == 0:
            score -= 1000000
        # elif window.count(2) == 3 and window.count(0) == 1:
        #     score -= 6
        # elif window.count(2) == 2 and window.count(0) == 2:
        #     score -= 2

        return score

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
                score += self.evaluate_window(window)

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
                score += self.evaluate_window(window)

        # pos diag (Up Right)
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window)

        # neg diag (Down Left)
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                window = [board[r + 3 - i][c + 3 - i] for i in range(4)]
                score += self.evaluate_window(window)
        # print(score)
        return score

    def minimax(self, board, depth, maximiser):
        if depth == 0 or  board.get_board_state(4) != GameState.IN_PROGRESS:
            # print(self.evaluate(board))
            return self.evaluate(board)

        # player 1 (red) wants to max
        if maximiser:
            max_eval = -100000000
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, 1)
                    evalu = self.minimax(board, depth - 1, False)
                    max_eval = max(max_eval, evalu)
                    board.revert(move)
            return max_eval

        else:
            min_eval = 100000000
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
                    eval = self.minimax(board, self.depth - 1, False)
                    if eval > max_eval:
                        max_eval = eval
                        best_move = move
                    board.revert(move)
            return best_move

        else:
            best_move = None
            min_eval = 100000000
            for move in range(board.width):
                if board.can_make_move(move):
                    board.make_move(move, my_piece)
                    eval = self.minimax(board, self.depth - 1, True)
                    if eval < min_eval:
                        min_eval = eval
                        best_move = move
                    board.revert(move)
            return best_move


A = [[0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0],
     [1, 1, 2, 1, 0, 0],
     [1, 2, 0, 0, 0, 0],
     [2, 2, 2, 2, 0, 0]]

if __name__ == '__main__':
    # Test evaluation
    agent = SmartAgent()
    # board = Board()
    # board.create((7, 6))
    # board.make_move(0, 1)
    # board.make_move(0, 1)
    # board.make_move(0, 1)
    # board.make_move(0, 1)
    # board.make_move(1, 2)
    # print(agent.evaluate(board))
