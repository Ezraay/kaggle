import random

import pygame
from pygame import *

from source.core.agent import Agent
from source.core.board import Board, PLAYER_1_PIECE, PLAYER_2_PIECE
from source.core.game import Game
from source.core.game_state import GameState
from visualiser.display import Display


class Visualiser:
    def __init__(self, board_size: tuple[int, int], in_a_row: int):
        self.__board = Board()
        self.__board.create(board_size)
        self.__in_a_row = in_a_row

        self.__display = Display()
        self.__display.start((self.__board.width, self.__board.height))

    def agent_versus_agent(self, agent1: Agent, agent2: Agent, seed = None):
        if seed is None:
            seed = random.randint(0, 1000000)
        print("Seed: " + str(seed))
        random.seed(seed)
        
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
            self.__display.draw(self.__board)

    def player_versus_player(self):
        running = True
        current_turn = PLAYER_1_PIECE
        while True:
            for event in pygame.event.get():
                # terminates when there is no more event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP and running:
                    pos = pygame.mouse.get_pos()
                    column = self.__display.to_board_column(pos)
                    if self.__board.can_make_move(column):
                        self.__board.make_move(column, current_turn)
                        current_turn = 3 - current_turn
                        running = self.__board.get_board_state(self.__in_a_row) == GameState.IN_PROGRESS
                        print(self.__board)
            self.__display.draw(self.__board)

    def player_versus_agent(self, agent: Agent, player_starts: bool):
        running = True
        my_piece = PLAYER_1_PIECE if player_starts else PLAYER_2_PIECE
        if not player_starts:
            self.__board.make_move(agent.get_move(self.__board, 3 - my_piece, self.__in_a_row), 3 - my_piece)

        while True:
            for event in pygame.event.get():
                # terminates when there is no more event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP and running:
                    pos = pygame.mouse.get_pos()
                    column = self.__display.to_board_column(pos)
                    if self.__board.can_make_move(column):
                        self.__board.make_move(column, my_piece)
                        running = self.__board.get_board_state(self.__in_a_row) == GameState.IN_PROGRESS
                        if running:
                            self.__board.make_move(agent.get_move(self.__board, 3 - my_piece, self.__in_a_row), 3 - my_piece)
                        # current_turn = 3 - current_turn
                        running = self.__board.get_board_state(self.__in_a_row) == GameState.IN_PROGRESS
            self.__display.draw(self.__board)
