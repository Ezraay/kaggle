import os
import random
from datetime import datetime

from source.agent_importer import import_agent
from source.core.agent import Agent
from source.core.board import Board, beautify_board
from source.core.colours import GREEN, RED, CLEAR, YELLOW
from source.core.game import Game
from source.core.game_state import GameState
from source.database.mongo_database import MongoDatabase
from visualiser.setup import Visualiser


def simulate(agent1_name, agent2_name, database: MongoDatabase, board_size, in_a_row: int):
    agent1_class = import_agent(agent1_name)
    agent2_class = import_agent(agent2_name)

    # Initialize agents and the board
    agent1: Agent = agent1_class()
    agent2: Agent = agent2_class()
    board = Board()
    board.create(board_size)

    # Start the game and run until completion
    game = Game(agent1, agent2, board, in_a_row)
    game.tick_to_completion()

    # Display the results, board state, and move history
    print(beautify_board(board))

    # Print the game outcome
    if game.game_state == GameState.PLAYER1_WON:
        print(f"{RED}Player 1 Won")
    if game.game_state == GameState.PLAYER2_WON:
        print(f"{YELLOW}Player 2 Won")
    if game.game_state == GameState.TIE:
        print(f"{CLEAR}Game ended in a tie")
    print(CLEAR + "History:")
    print(game.history)

    if database is not None:
        database.write_game(game.history, game.game_state, agent1, agent2, datetime.now())


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Tool for testing and visualising Connect 4 games.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("mode", help="Mode in which to run the program", choices=['simulate', 'visualise', 'versus'])
    parser.add_argument('agent1', nargs='?')
    parser.add_argument('agent2', nargs='?')
    parser.add_argument("--seed", help="Seed for random module", required=False, type=int)
    parser.add_argument("--write-database", help="Database to write results to", required=False, type=str)
    parser.add_argument("--inarow", help="How many in a row to win", required=False, type=int, const=1, nargs="?", default=4)
    parser.add_argument("--width", help="Width of the board", required=False, type=int, const=1, nargs="?", default=6)
    parser.add_argument("--height", help="Height of the board", required=False, type=int, const=1, nargs="?", default=7)

    args = parser.parse_args()
    config = vars(args)
    in_a_row = config['inarow']
    board_size = (config['width'], config['height'])
    # print(config)

    if config['seed'] is not None:
        random.seed(config['seed'])
    mode = config['mode']
    if mode == "simulate":
        if config['agent1'] is None:
            parser.error('First agent needs to be specified')
        if config['agent2'] is None:
            parser.error('Second agent needs to be specified')

        connection_string = config['write_database']
        if connection_string is None:
            database = None
        else:
            database = MongoDatabase()
            database.connect(connection_string)
        simulate(config['agent1'], config['agent2'], database, board_size, in_a_row)
    elif mode == "visualise":
        board = Board()
        board.create(board_size)
        visualiser = Visualiser(board_size, in_a_row)
        if config['agent1'] is not None and config['agent2'] is not None:
            agent1_name = config['agent1']
            agent1_class = import_agent(agent1_name)
            agent1 = agent1_class()
            agent2_name = config['agent2']
            agent2_class = import_agent(agent2_name)
            agent2 = agent2_class()
            visualiser.agent_versus_agent(agent1, agent2)
        elif config["agent1"] is not None and config['agent2'] is None:
            agent1_name = config['agent1']
            agent1_class = import_agent(agent1_name)
            agent1 = agent1_class()
            visualiser.player_versus_agent(agent1, random.random() < 0.5)
        elif config['agent2'] is None and config['agent2'] is None:
            visualiser.player_versus_player()
        else:
            parser.error('No valid configuration found to visualise')
    elif mode == "versus":
        pass


if __name__ == "__main__":
    main()
