## Creating a new Agent
In order to create a new agent, first create a new file in the agents folder with the name of your agent in snake_case_naming.
`some_agent.py`

Next add a class to this file that inherits from either the base `Agent` class or another existing agent.
```python
class SomeAgent(RandomAgent):
    pass
```
Note how the name of the class is the same as the filename but in PascalCaseNaming. This is necessary for the simulation to find the class to import, so make sure the filename and classname match.

You can now use your new agent by specifying the name in the terminal:
```
python ./main.py SomeAgent RandomAgent
```

This command will create a game between your new agent and the existing RandomAgent

## Adding functionality
To add functionality, simply override the `get_move` function:
```python
class SomeAgent(RandomAgent):
    def get_move(self, board: Board, my_piece: int) -> int:
        # Custom logic here

        # Fallback on base class implementation
        return super().get_move(board, my_piece)
```

The function has to return an index referring to the column it has decided is the best move.
The board has useful functions and properties that gives all the necessary info to pick the right move.

## Advanced functionality
Sometimes there may be a need to create functions that is used in multiple agents. If this code cannot exist as part of 
the class and be used by subclasses, consider creating it as an importable function.
```python
# some_agent.py

def get_winning_move(board: Board, my_piece: int) -> int:
    # Logic goes here

class SomeAgent(RandomAgent):
    def get_move(self, board: Board, my_piece: int) -> int:
        winning_move = get_winning_move(board, my_piece)
        if winning_move is not None:
            return winning_move

        # Fallback on base class implementation
        return super().get_move(board, my_piece)
```

```python
# some_other_agent.py
from agents.some_agent import get_winning_move


class SomeOtherAgent(RandomAgent):
    def get_move(self, board: Board, my_piece: int) -> int:
        winning_move = get_winning_move(board, my_piece)
        # Other logic goes here

        # Fallback on base class implementation
        return super().get_move(board, my_piece)
```
The above `get_winning_move` function can be imported and used in other agents as necessary