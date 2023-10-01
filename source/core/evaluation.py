from source.core.board import Board

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
    #













