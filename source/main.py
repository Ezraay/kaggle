from agent_importer import import_agent
from core.agent import Agent


def main():
    # Handle command line args
    import argparse
    parser = argparse.ArgumentParser(description="Simulates a Connect 4 game between two automatic agents.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("agent1", help="Path to first player's agent")
    parser.add_argument("agent2", help="Path to second player's agent")
    args = parser.parse_args()
    config = vars(args)

    # Try load agents
    agent1_file = config["agent1"]
    agent2_file = config["agent2"]
    try:
        agent1_class = import_agent(agent1_file)
    except:
        print("Error importing agent1: " + agent1_file)
        return
    try:
        agent2_class = import_agent(agent2_file)
    except:
        print("Error importing agent2: " + agent2_file)
        return

    try:
        assert issubclass(agent1_class, Agent)
    except:
        print("Agent 1 doesn't inherit from Agent base class")
        return
    try:
        assert issubclass(agent2_class, Agent)
    except:
        print("Agent 2 doesn't inherit from Agent base class")
        return

    agent1: Agent = agent1_class()
    agent2: Agent = agent2_class()

    print(agent1.get_move())


if __name__ == '__main__':
    main()
