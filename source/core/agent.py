from abc import ABC, abstractmethod

from core.board import Board


class Agent(ABC):
    @abstractmethod
    def get_move(self, board: Board, my_piece: int) -> int:
        pass
