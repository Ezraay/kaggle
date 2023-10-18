from source.core.agent import Agent
from source.core.board import Board
from source.core.game_state import GameState
from source.core.move import Move
import time as time


class Game:
    '''
        A class to represent the ConnectX game.

        Attributes:
        ----------
        __agent1: Agent
            The first agent/player.
        __agent2: Agent
            The second agent/player.
        __board: Board
            The game board instance.
        __turn: int
            Current turn number. (0 for agent1 and 1 for agent2)
        __in_a_row: int
            The number of pieces in a row required for a win. Default is 4.
        history: list[Move]
            List of moves made in the game.
        game_state: GameState
            The current state of the game.
        running: bool
            Boolean indicating if the game is still in progress.
    '''
    def __init__(self, agent1: Agent, agent2: Agent, board: Board, in_a_row=4):
        # Initializes a new game of ConnectX with given agents and board.
        self.__agent1 = agent1
        self.__agent2 = agent2
        self.__board = board
        self.__board_copy = board.copy()
        self.__turn = 0
        self.__in_a_row = in_a_row
        self.history: list[Move] = []

        self.game_state = GameState.IN_PROGRESS
        self.running = True

    @property
    def board(self):
        return self.__board_copy


    def tick(self):
        # Performs a single game move for the current agent. Updates game state.
        '''
        Executes a move for the current agent. If the move is invalid, raises an exception.
        Checks for game over after the move.
        '''

        current_agent = self.__agent1 if self.__turn % 2 == 0 else self.__agent2
        my_piece = self.__turn % 2 + 1
        start = time.time()
        move = current_agent.get_move(self.__board_copy, my_piece, self.__in_a_row)
        if not self.__board_copy.equals(self.__board):
            raise Exception("Board copy not returned to original state, check do/undo's")
        t = time.time() - start
        if t > 2 and self.__turn -1 > 0:
            raise TimeoutError("Player " + str(my_piece) + " at Turn " + str(self.__turn) 
                               + ": This take too long.\n" + str(t) + " seconds. Expect within 2 seconds.")
        elif self.__turn -1 <= 0 and t > 60 :
            raise TimeoutError(("Player " + str(my_piece) + " fails inital turn limits.\n " + 
                                str(t) + " seconds. Expect within 60 seconds."))
        if not isinstance(move, int):
            raise ValueError("Result needs to be an int, got: " + str(type(move)))
        if not self.__board.can_make_move(move):
            raise ValueError("Can't place cell at x=" + str(move))

        move_data = Move(move, self.__board.get_height_at(move), my_piece)
        self.history.append(move_data)
        self.__board.make_move(move, my_piece)
        self.__board_copy.make_move(move, my_piece)
        self.__turn += 1
        if self.__is_game_over():
            self.running = False

    def tick_to_completion(self):
        # Continues the game until completion.
        """
        keeps excuting moves until game ended
        """
        while self.running:
            self.tick()

    def __is_game_over(self):
        # Checks if the game has ended and updates the game_state attribute.
        """
        Checks the current board state and returns a boolean indicating if the game has ended.
        """
        self.game_state = self.__board.get_board_state(self.__in_a_row)
        return self.game_state != GameState.IN_PROGRESS
