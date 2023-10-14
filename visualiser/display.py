import math

import pygame

from source.core.board import Board

class Display:
    BACKGROUND_COLOUR = (40, 40, 40)
    CELL_SIZE = 100
    CELL_PADDING = 5
    WINDOW_PADDING = 20

    def __init__(self):

        cell_size_tuple = (self.CELL_SIZE, self.CELL_SIZE)
        red_chip = pygame.image.load("visualiser/assets/images/redchip.png")
        yellow_chip = pygame.image.load("visualiser/assets/images/yellowchip.png")
        empty = pygame.image.load("visualiser/assets/images/empty.png")
        self.__red_scaled = pygame.transform.scale(red_chip, cell_size_tuple)
        self.__yellow_scaled = pygame.transform.scale(yellow_chip, cell_size_tuple)
        self.__empty_scaled = pygame.transform.scale(empty, cell_size_tuple)

    def start(self, board_size):
        self.__num_columns = board_size[0]
        pygame.display.set_caption("Connect-X Visualisation Demo")
        pygame.init()
        pygame.font.init()
        self.__font = pygame.font.SysFont('Comic Sans MS', 30)

        self.__screen_width = board_size[0] * (self.CELL_SIZE + 2 * self.CELL_PADDING) + 2 * self.WINDOW_PADDING
        self.__screen_height = board_size[1] * (self.CELL_SIZE + 2 * self.CELL_PADDING) + 2 * self.WINDOW_PADDING
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))

    def draw(self, board: Board):
        self.__screen.fill(self.BACKGROUND_COLOUR)
        for col in range(board.width):
            for row in range(board.height):
                piece = board.get_piece_at(col, row)
                position = (col * (self.CELL_SIZE + 2 * self.CELL_PADDING) + self.WINDOW_PADDING + self.CELL_PADDING,
                            self.__screen_height -
                            ((row + 1) * (self.CELL_SIZE + 2 * self.CELL_PADDING) + self.WINDOW_PADDING - self.CELL_PADDING))
                if piece == 1:
                    self.__screen.blit(self.__red_scaled, position)
                elif piece == 2:
                    self.__screen.blit(self.__yellow_scaled, position)
                elif piece == 0:
                    self.__screen.blit(self.__empty_scaled, position)
        pygame.display.flip()

    def to_board_column(self, screen_position):
        x = screen_position[0]
        column =(x - self.WINDOW_PADDING) / (self.CELL_SIZE + 2 * self.CELL_PADDING)
        return math.floor(min(self.__num_columns - 1, max(0, column)))