from core.agent import Agent
from core.board import Board
from core.game_state import GameState
from core.move import Move


class Game:
    def __init__(self, agent1: Agent, agent2: Agent, board: Board, in_a_row=4):
        self.__agent1 = agent1
        self.__agent2 = agent2
        self.__board = board
        self.__turn = 0
        self.__in_a_row = in_a_row
        self.history: list[Move] = []

        self.game_state = GameState.IN_PROGRESS
        self.running = True

    def tick(self):
        current_agent = self.__agent1 if self.__turn == 0 else self.__agent2
        my_piece = self.__turn % 2 + 1
        move = current_agent.get_move(self.__board, my_piece)
        if not self.__board.can_make_move(move):
            raise ValueError("Can't place cell at x=" + str(move))

        move_data = Move(move, self.__board.get_height_at(move), my_piece)
        self.history.append(move_data)
        self.__board.make_move(move, my_piece)
        self.__turn += 1
        if self.__is_game_over():
            self.running = False

    def tick_to_completion(self):
        while self.running:
            self.tick()

    def __is_game_over(self):
        self.game_state = self.__board.get_board_state(self.__in_a_row)
        return self.game_state != GameState.IN_PROGRESS
