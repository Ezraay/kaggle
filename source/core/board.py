from core.colours import GREEN, RED, CLEAR
from core.game_state import GameState


class Board:
    def create(self, size: tuple[int, int]):
        self.__heights = [0 for _ in range(size[0])]
        self.__board = [[0 for _ in range(size[1])] for _ in range(size[0])]
        self.size = size

    def can_make_move(self, x: int):
        return self.__heights[x] < self.size[1]

    def make_move(self, x: int, piece: int):
        self.__board[x][self.__heights[x]] = piece
        self.__heights[x] += 1

    def get_board_state(self, in_a_row: int) -> GameState:
        for x in range(self.size[0]):
            if self.can_make_move(x):
                break
        else:
            return GameState.TIE

        for x in range(self.size[0]):
            for y in range(self.__heights[x]):
                piece = self.__board[x][y]

                # Horizontal
                if x + in_a_row < self.size[0]:
                    for i in range(in_a_row):
                        if self.__board[x + i][y] != piece:
                            break
                    else:
                        return GameState.PLAYER1_WON if piece == 1 else GameState.PLAYER2_WON

                # Vertical
                if y + in_a_row <= self.__heights[x]:
                    for i in range(in_a_row):
                        if self.__board[x][y + i] != piece:
                            break
                    else:
                        return GameState.PLAYER1_WON if piece == 1 else GameState.PLAYER2_WON
        return GameState.IN_PROGRESS

    def __str__(self):
        result = ""
        for y in range(self.size[1] - 1, -1, -1):
            for x in range(self.size[0]):
                result += "[" + str(self.__board[x][y]) + "]"
            result += "\n"
        return result


def beautify_board(board: Board) -> str:
    board_values = str(board)
    board_values = board_values.replace("[2]", RED + "#")
    board_values = board_values.replace("[1]", GREEN + "#")
    board_values = board_values.replace("[0]", CLEAR + "O")
    board_values += CLEAR
    return board_values
