from source.agents.minimax_agent import MinimaxAgent

class SmartMinimaxAgent(MinimaxAgent):
    def evaluate_window(self, window: list[int], in_a_row: int):
        score = 0

        # check for n in a row
        if window.count(1) == in_a_row:
            score += 1000000

        if window.count(2) == in_a_row:
            score -= 1000000

        if window.count(1) == in_a_row - 1:
            score += 5

        if window.count(2) == in_a_row - 1:
            score -= 5

        if window.count(2) == in_a_row - 1 and window.count(1) == 1:
            score += 1

        if window.count(1) == in_a_row - 1 and window.count(2) == 1:
            score += 1

        # add x^2 or exponential func for other vals (2+), also needs to account for opps, empty spots
        return score
