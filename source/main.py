import random

from agent_importer import import_agent
from core.agent import Agent
from core.board import Board, beautify_board
from core.colours import GREEN, CLEAR, RED
from core.game import Game
from core.game_state import GameState


def main():
    # Handle command line args
    config = create_config()

    if config["seed"] != None:
        random.seed(config["seed"])
    # random.seed(8)
    # random.seed(40)

    # Try load agents
    agent1_file = config["agent1"]
    agent2_file = config["agent2"]

    agent1_class = import_agent(agent1_file)
    agent2_class = import_agent(agent2_file)

    agent1: Agent = agent1_class()
    agent2: Agent = agent2_class()

    board = Board()
    board.create((7, 6))

    game = Game(agent1, agent2, board)
    game.tick_to_completion()
    print(beautify_board(board))
    print("\nBoard State:")
    print(board.to_array())
    print("\nHistory:")
    print(game.history)

    if game.game_state == GameState.PLAYER1_WON:
        print(f"{GREEN}Player 1 Won")
    if game.game_state == GameState.PLAYER2_WON:
        print(f"{RED}Player 2 Won")
    if game.game_state == GameState.TIE:
        print(f"{CLEAR}Game ended in a tie")
    print(CLEAR)


def create_config():
    import argparse
    parser = argparse.ArgumentParser(description="Simulates a Connect 4 game between two automatic agents.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("agent1", help="Path to first player's agent")
    parser.add_argument("agent2", help="Path to second player's agent")
    parser.add_argument("--seed", help="Seed for random module", required=False, type=int)
    args = parser.parse_args()
    config = vars(args)
    return config


if __name__ == '__main__':
    main()
