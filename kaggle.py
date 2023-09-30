from kaggle_environments import make

env = make("connectx", {"rows": 6, "columns": 7, "inarow": 4})


def agent(observation, configuration):
    print(observation)  # {board: [...], mark: 1}
    print(configuration)  # {rows: 10, columns: 8, inarow: 5}
    return [c for c in range(len(observation.board)) if observation.board[c] == 0][0]


# Run an episode using the agent above vs the default random agent.
env.run([agent, "random"])
env.render(mode="ansi")
