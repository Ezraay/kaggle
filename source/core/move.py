class Move:
    """
        A class to represent a move in the ConnectX game.

        Attributes:
        ----------
        x: int
            The x-coordinate (column) where the piece is placed.
        y: int
            The y-coordinate (row) where the piece lands after being dropped.
        piece: int
            The identifier for the piece being placed (typically representing a player or agent).
        """
    def __init__(self, x: int, y: int, piece: int):
        """
        Initializes a move with given x-coordinate, y-coordinate, and piece identifier.
        """
        self.x = x
        self.y = y
        self.piece = piece

    def __repr__(self):
        """
        Returns a string representation of the move in the format (x, y, piece).
        """
        return f"({self.x}, {self.y}, {self.piece})"
