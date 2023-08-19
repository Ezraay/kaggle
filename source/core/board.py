from core.colours import GREEN, RED, CLEAR
from core.game_state import GameState

PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2
EMPTY_PIECE = 0


class Board:
    def create(self, size: tuple[int, int]):
        self.__heights = [0 for _ in range(size[0])]
        self.__board = [[EMPTY_PIECE for _ in range(size[1])] for _ in range(size[0])]
        #size[width,height] for constructing the connect 4 board
        self.__size = size

    @property
    def width(self):
        return self.__size[0]

    @property
    def height(self):
        return self.__size[1]

    def can_make_move(self, x: int):
        # check if you can make a move in that column
        return self.get_height_at(x) < self.height

    def get_height_at(self, x: int):
        return self.__heights[x]

    def make_move(self, x: int, piece: int):
        self.__board[x][self.get_height_at(x)] = piece
        self.__heights[x] += 1

    def get_board_state(self, in_a_row: int) -> GameState:
        
        # return an Tie if there is no one can make a move
        for x in range(self.__size[0]):
            if self.can_make_move(x):
                break
        else:
            return GameState.TIE
        # Determine who is the winner base on the last piece of the winning move
        def piece_to_winner(piece: int):
            if piece == PLAYER_1_PIECE:
                return GameState.PLAYER1_WON
            if piece == PLAYER_2_PIECE:
                return GameState.PLAYER2_WON
                
        # examine vertical win condition base on in_a_row
        for x in range(self.width):
            current_in_a_row = 0  # Reset on new
            current_piece = 0
            for y in range(self.height):
                piece = self.__board[x][y]
                if piece != current_piece:  # Streak broken
                    #register new type of piece to see if there is vertical win
                    current_in_a_row = 1
                    current_piece = piece
                else:
                    # add vertical streak and if it equal to require number to win
                    # and it is not an empty_piece, then return winner
                    current_in_a_row += 1
                    if current_in_a_row == in_a_row and piece != EMPTY_PIECE:
                        return piece_to_winner(piece)  # There is a winner
                
        # examine horizontal win condition base on in_a_row same vertically examination
        for y in range(self.height):
            current_in_a_row = 0
            current_piece = 0
            for x in range(self.width):
                piece = self.__board[x][y]
                if piece != current_piece:
                    current_in_a_row = 1
                    current_piece = piece
                else:
                    current_in_a_row += 1
                    if current_in_a_row == in_a_row and piece != EMPTY_PIECE:
                        return piece_to_winner(piece)

        diagonals = self.width + self.height - 1  # Number of diagonals like in diagram above
        for i in range(diagonals):
            x = max(0, i - self.height + 1)  # The starting position of the diagonal
            y = min(i, self.height - 1)
            current_in_a_row = 0  # Reset on new diagonal
            current_piece = 0
            for j in range(min(self.width, self.height, i + 1, diagonals - i)):  # Length of the diagonal
                piece = self.__board[x + j][y - j]
                if piece != current_piece:  # Streak broken
                    current_in_a_row = 1
                    current_piece = piece
                else:
                    current_in_a_row += 1
                    if current_in_a_row == in_a_row and piece != EMPTY_PIECE:
                        return piece_to_winner(piece)  # Someone won

        for i in range(diagonals):
            x = max(0, i - self.height + 1)
            y = max(0, self.height - i - 1)
            current_in_a_row = 0
            current_piece = 0
            for j in range(min(self.width, self.height, i + 1, diagonals - i)):
                piece = self.__board[x + j][y + j]
                if piece != current_piece:
                    current_in_a_row = 1
                    current_piece = piece
                else:
                    current_in_a_row += 1
                    if current_in_a_row == in_a_row and piece != EMPTY_PIECE:
                        return piece_to_winner(piece)

        # for x in range(self.size[0]):
        #     for y in range(self.__heights[x]):
        #         piece = self.__board[x][y]
        #
        #         # Horizontal
        #         if x + in_a_row < self.size[0]:
        #             for i in range(in_a_row):
        #                 if self.__board[x + i][y] != piece:
        #                     break
        #             else:
        #                 return GameState.PLAYER1_WON if piece == PLAYER_1_PIECE else GameState.PLAYER2_WON
        #
        #         # Vertical
        #         if y + in_a_row <= self.__heights[x]:
        #             for i in range(in_a_row):
        #                 if self.__board[x][y + i] != piece:
        #                     break
        #             else:
        #                 return GameState.PLAYER1_WON if piece == PLAYER_2_PIECE else GameState.PLAYER2_WON
        return GameState.IN_PROGRESS

    def to_array(self):
        # return the whole borad
        return self.__board

    def __str__(self):
        # return result in an array form
        result = ""
        for y in range(self.__size[1] - 1, -1, -1):
            for x in range(self.__size[0]):
                result += "[" + str(self.__board[x][y]) + "]"
            result += "\n"
        return result


def beautify_board(board: Board) -> str:
    board_values = str(board)
    board_values = board_values.replace(f"[{PLAYER_2_PIECE}]", RED + "[@]")
    board_values = board_values.replace(f"[{PLAYER_1_PIECE}]", GREEN + "[#]")
    board_values = board_values.replace(f"[{EMPTY_PIECE}]", CLEAR + " ' ")
    board_values += CLEAR
    return board_values
