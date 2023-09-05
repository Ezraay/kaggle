import random

from agent_importer import import_agent
from core.agent import Agent
from core.board import Board, beautify_board
from core.colours import GREEN, CLEAR, RED
from core.game import Game
from core.game_state import GameState


def simulate_game(agent1_class, agent2_class):
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
        return "Player 1 Won"
    elif game.game_state == GameState.PLAYER2_WON:
        return "Player 2 Won"
    elif game.game_state == GameState.TIE:
        return "Tie"
    else:
        return "Unknown State"


def simulate_multiple_agents(agents_classes):

    results = {}
    for agent1_class in agents_classes:
        for agent2_class in agents_classes:
            if agent1_class != agent2_class:  # Ensure the agent doesn't play against itself
                winner = simulate_game(agent1_class, agent2_class)

                print(f"Winner: {winner}")

                if winner not in results:
                    results[winner] = 1
                else:
                    results[winner] += 1
    return results

def main():
    """
    Main function to initiate and simulate a Connect 4 game between two agents.
    Configurations and seed for randomness are handled via command line arguments.

    Steps:
    1. Parse command line arguments.
    2. Set a random seed if provided.
    3. Load the agents using dynamic imports.
    4. Initialize the board and the game.
    5. Execute the game until completion.
    6. Display the final game state and results.
    """
    # Handle command line arguments to get game configuration
    config = create_config()

    # Set the seed for randomness if provided
    if config["seed"] != None:
        random.seed(config["seed"])
    # random.seed(8)
    # random.seed(40)

    # Dynamically load the agents' classes based on the file names provided in the config
    agent1_file = config["agent1"]
    agent2_file = config["agent2"]
    agent1_class = import_agent(agent1_file)
    agent2_class = import_agent(agent2_file)
    game_count = config["count"]

    all_results = {"Player 1 Won": 0, "Player 2 Won": 0, "Tie": 0, "Unknown State": 0}

    for i in range(game_count):
        results = simulate_multiple_agents([agent1_class, agent2_class])
        for key, value in results.items():
            all_results[key] += value

    for key, value in all_results.items():
        print(f"{key}: {value} wins out of {game_count} games")


def create_config():
    """
    Parses command line arguments to configure the Connect 4 game simulation.
    Returns:
        A dictionary containing parsed arguments including agent paths and optionally a seed.

    Parameters for Command Line:
    ---------------------------
    agent1 : str
        Path to the file containing the class definition of the first player's agent.
    agent2 : str
        Path to the file containing the class definition of the second player's agent.
    --seed : int (optional)
        Seed to initialize the random module. Helps in producing deterministic results.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Simulates a Connect 4 game between two automatic agents.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("agent1", help="Path to first player's agent")
    parser.add_argument("agent2", help="Path to second player's agent")
    parser.add_argument("--seed", help="Seed for random module", required=False, type=int)
    parser.add_argument("--write-database", help="Database to write results to", required=False, type=str)
    parser.add_argument("--count", help="number of games to play", type=int)
    args = parser.parse_args()
    config = vars(args)
    return config


if __name__ == '__main__':
    main()
