# a module for writing vidoe game
import pygame

# test_board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 2, 0, 0, 0], [1, 2, 1, 1, 2, 0, 2]]


def visualise(board: list[list[int]]):
    """
    :param board: a 2d array with None, 1 or 2 in each subarray
    :return: a pygame instance displaying the board. It does not indicate a winning move.
    """
    width = len(board[0])
    height = len(board)

    piece_size = 90
    spacing = 5
    padding = 20
    #setting screen size
    cell_size = piece_size + 2 * spacing
    screen_width = width * cell_size + 2 * padding
    screen_height = height * cell_size + 2 * padding
    # loading chip image
    red_chip = pygame.image.load("assets/images/redchip.png")
    yellow_chip = pygame.image.load("assets/images/yellowchip.png")
    empty = pygame.image.load("assets/images/empty.png")
    #alter it to ideal size
    updated_size = (90, 90)
    red_scaled = pygame.transform.scale(red_chip, updated_size)
    yellow_scaled = pygame.transform.scale(yellow_chip, updated_size)
    empty_scaled = pygame.transform.scale(empty, updated_size)

    # Alter title of pygame running window
    pygame.display.set_caption("Connect-X Visualisation Demo")
    background_colour = (42, 42, 199)

    def draw_board(board):
        # visually construct the progress of the games
        pygame.draw.rect(screen, background_colour, (0, 0, screen_height, screen_width))
        
        for col in range(height):
            for row in range(width):
                piece = board[col][height - row - 2]
                position = (col * cell_size + padding + spacing, row * cell_size + padding + spacing)
                if piece == 1:
                    screen.blit(red_scaled, position)
                elif piece == 2:
                    screen.blit(yellow_scaled, position)
                elif piece == 0:
                    screen.blit(empty_scaled, position)
    #initalise the display
    pygame.init()
    screen = pygame.display.set_mode((screen_height, screen_width))

    while True:
        # Handle events
        for event in pygame.event.get():
            # terminates when ther is not more event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # redraw the next move from the previous one
            draw_board(board)
            pygame.display.flip()


def create_config():
    # create a dictionary contains changeable 
    import argparse
    parser = argparse.ArgumentParser(description="Visualises a Connect 4 game.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("board", help="Board state to display")
    args = parser.parse_args()
    config = vars(args)
    return config


def main():
    config = create_config()

    board_value = config["board"].strip()
    board = []
    try:
        for row_value in board_value[1: -1].split("],"):
            row = []
            for piece in row_value.strip()[1:]:
                if piece.isdigit():
                    row.append(int(piece))
            board.append(row)
    except:
        print("Error parsing board state")
        raise

    print(board)
    visualise(board)


if __name__ == "__main__":
    main()
