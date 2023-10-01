from source.core.board import *
from source.core.game import Game
from source.agents.random_agent import RandomAgent

def evaluate_window(window: list[int], in_a_row: int):
    score = 0

    # check for n in a row
    if window.count(1) == in_a_row:
        score += 1000000

    if window.count(2) == in_a_row:
        score -= 1000000

    # add x^2 or exponential func for other vals (2+), also needs to account for opps, empty spots
    return score

def evaluate(board: Board, in_a_row: int):
    score = 0
    i = 0

    # horizontal
    for y in range(board.height):
        for x in range(board.width - in_a_row + 1):
            window = board.get_window(x, y, 1, 0, in_a_row)
            score += evaluate_window(window, in_a_row)
            i += 1

    # vertical
    for y in range(board.height - in_a_row + 1):
        for x in range(board.width):
            window = board.get_window(x, y, 0, 1, in_a_row)
            score += evaluate_window(window, in_a_row)
            i += 1

    # bottom-left to upper-right
    for y in range(board.height - in_a_row + 1):
        for x in range(board.width - in_a_row + 1):
            window = board.get_window(x, y, 1, 1, in_a_row)
            score += evaluate_window(window, in_a_row)
            i += 1

    # upper-left to bottom-right
    for y in range(in_a_row - 1, board.height):
        for x in range(board.width - in_a_row + 1):
            window = board.get_window(x, y, 1, -1, in_a_row)
            score += evaluate_window(window, in_a_row)
            i += 1

    return score


if __name__ == "__main__":

    for i in range(100):
        board = Board()
        board.create((7, 6))
        a1, a2 = RandomAgent(), RandomAgent()

        game = Game(a1, a2, board)
        game.tick_to_completion()

        if evaluate(board) == 0:
            print(beautify_board(board))