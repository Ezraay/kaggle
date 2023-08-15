import random
from source.core.agent import Agent
from source.core.board import Board

class RandomAgent(Agent):
    def get_move(self, board: Board, my_piece: int) -> int:
        # connect 4 can only place piece in the topmost position
        # generate a list possible from the class Board and return a random move
        options = [x for x in list(range(board.width)) if board.can_make_move(x)]
        return random.choice(options)


    def check_winning_move(self, board, piece):
        # https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
        can_win = True
        # 1. check for horizontal location for winning move
        for col in range(len(board) - 3):
            for row in range(len(board[col])):
                if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                    return can_win

        # 2. check for vertical location for winning move
        for col in range(len(board)):
            for row in range(len(board[col])-3):
                if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                    return can_win

        # 3. check positive slope diagonal
        for col in range(len(board)-3):
            for row in range(len(board[col])-3):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                    return can_win

        # 4. check negative slope diagonal
        for col in range(len(board)-3):
            for row in range(3, len(board[col])):
                if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                    return can_win









