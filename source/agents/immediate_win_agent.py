import copy
import random
from core.board import Board, PLAYER_1_PIECE,PLAYER_2_PIECE
from core.game_state import GameState
from random_agent import RandomAgent

def check_winning_move(self, board: Board, piece):
    # https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html
    can_win = True
    # 1. check for horizontal location for winning move
    for col in range(board.width - 3):
        for row in range(board.height):
            if (board.to_array()[row][col] == piece and board.to_array()[row][col + 1] == piece
                    and board.to_array()[row][col + 2] == piece
                    and board.to_array()[row][col + 3] == piece):
                return can_win

    # 2. check for vertical location for winning move
    for col in range(board.width):
        for row in range(board.height - 3):
            if (board.to_array()[row][col] == piece and board.to_array()[row + 1][col] == piece
                    and board.to_array()[row + 2][col] == piece
                    and board.to_array()[row + 3][col] == piece):
                return can_win

    # 3. check positive slope diagonal
    for col in range(board.width - 3):
        for row in range(board.height - 3):
            if (board.to_array()[row][col] == piece and board.to_array()[row + 1][col + 1] == piece
                    and board.to_array()[row + 2][col + 2] == piece
                    and board.to_array()[row + 3][col + 3] == piece):
                return can_win

    # 4. check negative slope diagonal
    for col in range(board.width - 3):
        for row in range(3, board.height):
            if (board.to_array()[row][col] == piece
                    and board.to_array()[row - 1][col + 1] == piece
                    and board.to_array()[row - 2][col + 2] == piece
                    and board.to_array()[row - 3][col + 3] == piece):
                return can_win


class ImmediateWinAgent(RandomAgent):

    def get_move(self, board: Board, my_piece: int) -> int:
        oppo_piece = PLAYER_1_PIECE if my_piece == PLAYER_2_PIECE else PLAYER_2_PIECE
        valid_moves = [i for i in range(board.width) if board.can_make_move(i)]
        # check for immediate win move
        for move in valid_moves:
            temp_board = copy.deepcopy(board)
            temp_board.make_move(move, my_piece)
            if temp_board.get_board_state(4) in [GameState.PLAYER1_WON, GameState.PLAYER2_WON]:
                return move
        # If no immediate winning move, select a random move
        return super().get_move(board,my_piece)






