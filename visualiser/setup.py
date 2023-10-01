import pygame
from pygame import *

from source.core.agent import Agent
from source.core.board import Board
from source.core.game import Game
from visualiser.display import Display


class Visualiser:
    def __init__(self, board_size: tuple[int, int], in_a_row: int):
        self.__board = Board()
        self.__board.create(board_size)
        self.__in_a_row = in_a_row

        self.__display = Display()
        self.__display.start((self.__board.width, self.__board.height))

    def agent_versus_agent(self, agent1: Agent, agent2: Agent):
        game = Game(agent1, agent2, self.__board, self.__in_a_row)
        game.tick_to_completion()
        history = game.history
        shown_turn = len(history) - 1

        running = True
        while running:
            for event in pygame.event.get():
                # terminates when there is no more event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT and shown_turn >= 0:
                        self.__board.unmake_move()
                        shown_turn -= 1
                    if event.key == K_RIGHT and shown_turn < len(history) - 1:
                        shown_turn += 1
                        move = history[shown_turn]
                        self.__board.make_move(move.x, move.piece)
                    print(shown_turn)
            self.__display.draw(self.__board)

    def player_versus_player(self):
        pass

    def player_versus_agent(self, agent: Agent):
        pass
