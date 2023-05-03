class Move:
    def __init__(self, x: int, y: int, piece: int):
        self.x = x
        self.y = y
        self.piece = piece

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.piece})"