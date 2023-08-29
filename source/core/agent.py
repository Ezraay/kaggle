from abc import ABC, abstractmethod

from core.board import Board

# abstract class for the agent to build on
class Agent(ABC):
    @abstractmethod
    def get_move(self, board: Board, my_piece: int) -> int:
        pass
