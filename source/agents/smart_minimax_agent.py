import math

from source.agents.minimax_agent import MinimaxAgent

class SmartMinimaxAgent(MinimaxAgent):
    def __init__(self):
        super().__init__(4)

    def evaluate_window(self, window: list[int], in_a_row: int, my_piece: int):
        score = 0
        opp_piece = 3 - my_piece

        if window.count(my_piece) == 2:
            score += 10
        if window.count(opp_piece) == 2:
            score -= 10
        if window.count(my_piece) == 3:
            score += 20
        if window.count(opp_piece) == 3:
            score -= 20

        # check for n in a row
        # if window.count(1) == in_a_row:
        #     score += 1000
        #
        # if window.count(2) == in_a_row:
        #     score -= 1000

        # if window.count(1) == in_a_row - 1:
        #     score += 5
        #
        # if window.count(2) == in_a_row - 1:
        #     score -= 5
        #
        # if window.count(2) == in_a_row - 1 and window.count(1) == 1:
        #     score += 1
        #
        # if window.count(1) == in_a_row - 1 and window.count(2) == 1:
        #     score += 1

        # add x^2 or exponential func for other vals (2+), also needs to account for opps, empty spots
        return score
