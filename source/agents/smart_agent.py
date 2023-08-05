import random

from core.agent import Agent
from core.board import Board

# https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html

class SmartAgent(Agent):
    def get_move(self, board: Board, my_piece: int) -> int:
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        return random.choice(options)

    def evaluate_window(self, window, piece):
        score = 0
        my_piece = piece
        if my_piece == 1:
            opp_piece = 2
        else:
            opp_piece = 1

        # 4 - best case
        if window.count(piece) == 4:
            score += 100

        # 3 in a row
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5

        # 2 in a row
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        # blocking opponent's move (but still not as good as winning)
        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def score_pos(self, board, piece):
        score = 0
        c_arr = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if j == 3:
                    c_arr.append(board[i][j])

        c_count = c_arr.count(piece)
        score += c_count * 3

        # horizontal
        for r in range(len(board)):
            r_array = board[r]
            for c in range(4):
                window = r_array[c: c + 4]

                score += self.evaluate_window(window, piece)

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
                score += self.evaluate_window(window, piece)

        # pos diag (Up Right)
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        # neg diag (Down Left)
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                window = [board[r + 3 - i][c + 3 - i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score

    def player_ahead(self, board):
        res = self.score_pos(board, 1) - self.score_pos(board, 2)
        return res

B = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 2, 2, 0, 0],
     [0, 0, 0, 2, 1, 0, 0],
     [0, 0, 0, 1, 2, 1, 1]]


print(SmartAgent().player_ahead(B))






