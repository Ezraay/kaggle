from source.core.board import *
from source.core.game import Game
from source.agents.random_agent import RandomAgent

def evaluate_window(window: list[int]):
    score = 0

    # check for 4 in a row
    if window.count(1) == 4:
        score += 1000000
        return score

    if window.count(2) == 4:
        score -= 1000000
        return score

    return score

def evaluate(board: Board):
    score = 0

    # horizontal
    for y in range(board.height):
        for x in range(board.width - 3):
            window = board.get_window(x, y, 1, 0, 4)
            score += evaluate_window(window)

    # vertical
    for y in range(board.height - 3):
        for x in range(board.width):
            window = board.get_window(x, y, 0, 1, 4)
            score += evaluate_window(window)

    # bottom-left to upper-right
    for y in range(board.height - 3):
        for x in range(board.width - 3):
            window = board.get_window(x, y, 1, 1, 4)
            score += evaluate_window(window)

    # upper-left to bottom-right
    for y in range(board.height - 3, board.height):
        for x in range(board.width - 3):
            window = board.get_window(x, y, -1, -1, 4)
            score += evaluate_window(window)

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