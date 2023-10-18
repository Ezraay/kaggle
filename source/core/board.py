from source.core.colours import GREEN, RED, CLEAR, YELLOW
from source.core.game_state import GameState

PLAYER_1_PIECE = 1
PLAYER_2_PIECE = 2
EMPTY_PIECE = 0


class Board:
    def create(self, size: tuple[int, int]):
        self.__heights = [0 for _ in range(size[0])]
        self.__board = [[EMPTY_PIECE for _ in range(size[1])] for _ in range(size[0])]
        #size[width,height] for constructing the connect 4 board
        self.__size = size
        self.history = []

    @property
    def width(self):
        return self.__size[0]

    @property
    def height(self):
        return self.__size[1]

    def get_piece_at(self, x: int, y: int):
        return self.__board[x][y]
    
    def can_make_move(self, x: int):
        # check if you can make a move in that column
        return self.get_height_at(x) < self.height

    def get_height_at(self, x: int):
        return self.__heights[x]
    
    def unmake_move(self):
        y = self.history.pop()
        self.__board[y][self.get_height_at(y)-1] = 0
        self.__heights[y] -= 1

    def make_move(self, x: int, piece: int):
        self.__board[x][self.get_height_at(x)] = piece
        self.history.append(x)
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
            if y != 0:
                result += "\n"
        return result

    def copy(self):
        """Create a deep copy of the current board."""
        new_board = Board()
        new_board.__heights = self.__heights.copy()
        new_board.__board = [row.copy() for row in self.__board]
        new_board.__size = self.__size
        new_board.history = self.history.copy()
        return new_board

    def equals(self, other):
        if other.__heights != self.__heights:
            return False
        for i in range(self.width):
            if other.__board[i] != self.__board[i]:
                return False
        return True

    def get_window(self, x: int, y: int, dx: int, dy: int, length: int):
        result = []
        for i in range(length):
            pos_x = i * dx + x
            pos_y = i * dy + y
            if pos_x >= self.width or pos_x < 0:
                raise Exception(f"x-value out of bounds\nGot: {pos_x}\nExpected: [0-{self.width - 1}]")
            if pos_y >= self.height or pos_y < 0:
                raise Exception(f"y-value out of bounds\nGot: {pos_y}\nExpected: [0-{self.height - 1}]")
            result.append(self.get_piece_at(pos_x, pos_y))
        return result



def beautify_board(board: Board) -> str:
    board_values = str(board)
    board_values = board_values.replace(f"[{PLAYER_1_PIECE}]", RED + "[#]")
    board_values = board_values.replace(f"[{PLAYER_2_PIECE}]", YELLOW + "[@]")
    board_values = board_values.replace(f"[{EMPTY_PIECE}]", CLEAR + " ' ")
    board_values += CLEAR
    return board_values


if __name__ == "__main__":
    b = Board()
    b.create((7,6))
    m = [3,2,3,3,4,5,2,4,2]
    p = 2
    for i in m:
        if p == 1:
            p = 2
        else:
            p = 1
        b.make_move(i,p)
    print(b.history)
    b.unmake_move()
    print(b.history)

    b2 = b.copy()
    b2.make_move(0, 1)
    print(b2.equals(b))
