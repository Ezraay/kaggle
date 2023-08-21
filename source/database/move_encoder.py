from source.core.move import Move


def encode_move(move: Move):
    return {
        'x': move.x,
        'y': move.y,
        'piece': move.piece,
    }

def decode_move(data: dict):
    return Move(data['x'], data['y'], data['piece'])

def encode_moves(moves: list[Move]):
    result = []
    for move in moves:
        result.append(encode_move(move))
    return result

def decode_moves(data: list[dict]):
    result: list[Move] = []
    for move in data:
        result.append(decode_move(move))
    return result