# a module for writing video game
import pygame
from pygame import *

from source.agent_importer import import_agent
from source.core.agent import Agent
from source.core.board import Board, PLAYER_1_PIECE, PLAYER_2_PIECE
from source.core.game_state import GameState


# test_board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 2, 0, 0, 0], [1, 2, 1, 1, 2, 0, 2]]


def evaluate_window(window):
    score = 0

    if window.count(1) == 4:
        return 10000, True

    if window.count(2) == 4:
        return -10000, True

    elif window.count(1) == 3 and window.count(0) == 1:
        score += 5

    elif window.count(2) == 3 and window.count(0) == 1:
        score -= 5

    elif window.count(1) == 2 and window.count(0) == 2:
        score += 2

    elif window.count(2) == 2 and window.count(0) == 2:
        score -= 2

    return score, False

def evaluate(board_i):
    board = board_i.to_array()
    # board = board_i
    score = 0
    c_arr = []

    # for i in range(len(board)):
    #     for j in range(len(board[i])):
    #         if j == 3:
    #             c_arr.append(board[i][j])
    #
    # c_count = c_arr.count(1)
    # score += c_count * 3
    #
    # c_count = c_arr.count(2)
    # score -= c_count * 3

    rows = 6
    cols = 7

    # horizontal
    for i in range(rows):
        for j in range(cols - 3):
            window = [board[j][i], board[j + 1][i], board[j + 2][i], board[j + 3][i]]
            res = evaluate_window(window)
            score += res[0]
            if res[1]:
                return score

    # vertical
    for k in range(cols):
        for l in range(rows - 3):
            window = [board[k][l], board[k][l + 1], board[k][l + 2], board[k][l + 3]]
            res = evaluate_window(window)
            score += res[0]
            if res[1]:
                return score

    # diagonal up
    for m in range(cols - 3):
        for n in range(rows - 3):
            window = [board[m][n], board[m + 1][n + 1], board[m + 2][n + 2], board[m + 3][n + 3]]
            res = evaluate_window(window)
            score += res[0]
            if res[1]:
                return score

    # diagonal down
    for o in range(cols - 4):
        for p in range(rows - 3, rows + 1):
            window = [board[p][o], board[p - 1][o + 1], board[p - 2][o + 2], board[p - 3][o + 3]]
            res = evaluate_window(window)
            score += res[0]
            if res[1]:
                return score

    return score

def minimax(board, depth, maximiser):

    outcome = board.get_board_state(4)

    if depth == 0 or outcome != GameState.IN_PROGRESS:
        if outcome == GameState.PLAYER1_WON:
            return 10000000
        elif outcome == GameState.PLAYER2_WON:
            return -10000000
        else:
            return evaluate(board)

    if maximiser:
        max_eval = -math.inf
        for move in range(board.width):
            if board.can_make_move(move):
                board.make_move(move, 1)
                evalu = minimax(board, depth - 1, False)
                max_eval = max(max_eval, evalu)
                board.revert(move)
        return max_eval

    else:
        min_eval = math.inf
        for move in range(board.width):
            if board.can_make_move(move):
                board.make_move(move, 2)
                evalu = minimax(board, depth - 1, True)
                min_eval = min(min_eval, evalu)
                board.revert(move)
        return min_eval

def visualise(board: Board, agent: Agent = None):
    """
    :param board: a 2d array with None, 1 or 2 in each subarray
    :return: a pygame instance displaying the board. It does not indicate a winning move.
    """
    width = board.width
    height = board.height

    piece_size = 90
    spacing = 0
    padding = 0
    # setting screen size
    cell_size = piece_size + 2 * spacing
    screen_width = width * cell_size + 2 * padding
    screen_height = height * cell_size + 2 * padding
    # loading chip image
    red_chip = pygame.image.load("source/assets/images/redchip.png")
    yellow_chip = pygame.image.load("source/assets/images/yellowchip.png")
    empty = pygame.image.load("source/assets/images/empty.png")
    # alter it to ideal size
    updated_size = (90, 90)
    red_scaled = pygame.transform.scale(red_chip, updated_size)
    yellow_scaled = pygame.transform.scale(yellow_chip, updated_size)
    empty_scaled = pygame.transform.scale(empty, updated_size)

    # Alter title of pygame running window
    pygame.display.set_caption("Connect-X Visualisation Demo")
    background_colour = (42, 42, 199)

    # initalise the display
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    screen = pygame.display.set_mode((screen_width, screen_height))

    def get_board_column(mouse_position: tuple[int, int]):
        result = mouse_position[0] / piece_size
        return int(result)

    current_turn = PLAYER_1_PIECE

    def calculate_evaluations(board: Board, current_turn: int):
        result = []
        for i in range(board.width):
            if not board.can_make_move(i):
                result.append(None)
                continue
            board.make_move(i, current_turn)
            result.append(evaluate(board))
            board.unmake_move()
        return result

    evaluations = [0 for i in range(board.width)]

    def make_move(move: int):
        nonlocal evaluations
        nonlocal current_turn
        if board.can_make_move(move):
            board.make_move(move, current_turn)
            print(evaluate(board))
            current_turn = PLAYER_1_PIECE if current_turn == PLAYER_2_PIECE else PLAYER_2_PIECE
            evaluations = calculate_evaluations(board, current_turn)

    while True:
        # Handle events
        game_running = board.get_board_state(4) == GameState.IN_PROGRESS

        if game_running and current_turn == PLAYER_1_PIECE and agent is not None:
            move = agent.get_move(board, PLAYER_1_PIECE)
            make_move(move)

        for event in pygame.event.get():
            # terminates when there is no more event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP and game_running:
                pos = pygame.mouse.get_pos()
                column = get_board_column(pos)
                make_move(column)
                # current_turn = PLAYER_1_PIECE if current_turn == PLAYER_2_PIECE else PLAYER_2_PIECE
            if event.type == pygame.KEYDOWN:
                if event.key == K_z:
                    if not len(board.history) == 0:
                        board.unmake_move()
                        current_turn = PLAYER_1_PIECE if current_turn == PLAYER_2_PIECE else PLAYER_2_PIECE
                        evaluations = calculate_evaluations(board, current_turn)

        screen.fill((0, 0, 255))
        for col in range(width):
            for row in range(height):
                piece = board.get_piece_at(col, row)
                # piece = board[col][height - row - 2]
                position = (col * cell_size + padding + spacing,
                            screen_height - ((row + 1) * cell_size + padding + spacing))
                if piece == 1:
                    screen.blit(red_scaled, position)
                elif piece == 2:
                    screen.blit(yellow_scaled, position)
                elif piece == 0:
                    screen.blit(empty_scaled, position)
        if game_running:
            for i in range(board.width):
                if not board.can_make_move(i):
                    continue
                value = evaluations[i]
                text_surface = my_font.render(str(value), False, (0, 0, 0))
                position = (i * piece_size + piece_size / 2 - text_surface.get_width() / 2,
                            screen_height - (board.get_height_at(
                                i) * piece_size + piece_size / 2) - text_surface.get_height() / 2)
                screen.blit(text_surface, position)

        pygame.display.flip()

def create_config():
    # create a dictionary contains changeable 
    import argparse
    parser = argparse.ArgumentParser(description="Visualises a Connect 4 game.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument("board", help="Board state to display")
    parser.add_argument('--versus', help='Agent to play againFst', required=False)
    args = parser.parse_args()
    config = vars(args)
    return config


def main():
    config = create_config()

    # print(config)

    board = Board()
    board.create((7, 6))

    if config['versus'] is None:
        # Player v Player game
        visualise(board)
    else:
        agent_name = config['versus']
        agent_class = import_agent(agent_name)
        agent = agent_class()
        visualise(board, agent)

if __name__ == "__main__":
    main()
