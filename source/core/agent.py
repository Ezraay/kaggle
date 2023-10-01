from abc import ABC, abstractmethod

from source.core.board import Board

# abstract class for the agent to build on
class Agent(ABC):
    @abstractmethod
    def get_move(self, board: Board, my_piece: int, in_a_row: int) -> int:
        pass

    def get_name(self):
        return type(self).__name__