from agent_importer import import_agent
from core.agent import Agent
from core.board import Board, beautify_board


def main():
    # Handle command line args
    config = create_config()

    # Try load agents
    agent1_file = config["agent1"]
    agent2_file = config["agent2"]

    agent1_class = import_agent(agent1_file)
    agent2_class = import_agent(agent2_file)

    agent1: Agent = agent1_class()
    agent2: Agent = agent2_class()

    board = Board()
    board.create((7, 6))


def create_config():
    import argparse
    parser = argparse.ArgumentParser(description="Simulates a Connect 4 game between two automatic agents.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("agent1", help="Path to first player's agent")
    parser.add_argument("agent2", help="Path to second player's agent")
    args = parser.parse_args()
    config = vars(args)
    return config


if __name__ == '__main__':
    main()
