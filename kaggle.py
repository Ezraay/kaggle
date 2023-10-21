

def agent(observation, configuration):
    from source.core.board import Board
    from source.agents.smart_minimax_agent import SmartMinimaxAgent

    size = (configuration.columns, configuration.rows)
    board = Board()
    board.create_existing(size, observation.board)
    my_piece = observation.mark
    agent = SmartMinimaxAgent(4)
    return agent.get_move(board, my_piece, configuration.inarow)

    # board = observation.board
    # columns = configuration.columns
    # return [c for c in range(columns) if board[c] == 0][0]

# Run an episode using the agent above vs the default random agent.


if __name__ == "__main__":
    from kaggle_environments import make

    env = make("connectx", debug=True)
    try:
      env.run([agent, "random"])
    except:
      raise
    # Print schemas from the specification.
    print(env.specification.observation)
    print(env.specification.configuration)
    print(env.specification.action)

    with open('index.html', 'w+') as file:
      file.write(env.render(mode="html"))