import random

from agents.random_agent import RandomAgent
from agents.smart_agent import SmartAgent
from core.agent import Agent
from core.board import Board, beautify_board
from core.colours import GREEN, CLEAR, RED
from core.game import Game
from core.game_state import GameState

def test(agent1, agent2, g_num, verbose=False):
    g_res = []

    for i in range(g_num):
        board = Board()
        board.create((7, 6))

        # Start the game and run until completion
        game = Game(agent1, agent2, board)
        game.tick_to_completion()

        # Display the results, board state, and move history

        if verbose:
            print(beautify_board(board))
            print("\nBoard State:")
            print(board.to_array())
            print("\nHistory:")
            print(game.history)

        if game.game_state == GameState.PLAYER1_WON:
            g_res.append(1)
        if game.game_state == GameState.PLAYER2_WON:
            g_res.append(2)
        if game.game_state == GameState.TIE:
            g_res.append(0)

        print(i)

    p1_win, p2_win, tie = g_res.count(1), g_res.count(2), g_res.count(0)
    print(g_res)
    return p1_win, p2_win

s = SmartAgent()
r = RandomAgent()

print(test(s, r, 1, True))
