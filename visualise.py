# a module for writing video game
import pygame
from pygame import *

from source.agent_importer import import_agent
from source.core.agent import Agent
from source.core.board import Board, PLAYER_1_PIECE, PLAYER_2_PIECE
from source.core.game_state import GameState
from source.core.evaluation import evaluate


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

def visualise_history(history: list[int]):
    pass

def create_config():
    # create a dictionary contains changeable 
    import argparse
    parser = argparse.ArgumentParser(description="Visualises a Connect 4 game.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # parser.add_argument("board", help="Board state to display")
    # parser.add_argument('--versus', help='Agent to play againFst', required=False)
    # parser.add_argument('--show-hint', help='Whether to show evaluation of each move', required=False, type=bool)
    parser.add_argument("--agent1", help="Path to first player's agent", required=False)
    parser.add_argument("--agent2", help="Path to second player's agent", required=False)
    args = parser.parse_args()
    config = vars(args)
    return config


def main():
    config = create_config()

    # print(config)

    board = Board()
    board.create((7, 6))

    from visualiser.setup import Visualiser
    board_size = (7, 6)
    in_a_row = 4
    visualiser = Visualiser(board_size, in_a_row)
    if config['agent1'] is not None and config['agent2'] is not None:
        agent1_name = config['agent1']
        agent1_class = import_agent(agent1_name)
        agent1 = agent1_class()
        agent2_name = config['agent2']
        agent2_class = import_agent(agent2_name)
        agent2 = agent2_class()
        visualiser.agent_versus_agent(agent1, agent2)




    # if config['versus'] is None:
    #     # Player v Player game
    #     visualise(board)
    # else:
    #     agent_name = config['agent1']
    #     agent_class = import_agent(agent_name)
    #     agent = agent_class()
    #     visualise(board, agent)

if __name__ == "__main__":
    main()
