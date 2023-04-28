import pygame

test_board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, 1, None, 2, None, None, None],
    [1, 2, 1, 1, 2, None, 2]
]

def visualise(board):
    """
    :param board: a 2d array with None, 1 or 2 in each subarray
    :return: a pygame instance displaying the board. It does not indicate a winning move.
    """

    SLOT_SIZE = 105
    BOARD_WIDTH = len(board[0]) * SLOT_SIZE
    BOARD_HEIGHT = len(board) * SLOT_SIZE


    red_chip = pygame.image.load("assets/images/redchip.png")
    yellow_chip = pygame.image.load("assets/images/yellowchip.png")
    empty = pygame.image.load("assets/images/empty.png")

    updated_size = (90, 90)

    red_scaled = pygame.transform.scale(red_chip, updated_size)
    yellow_scaled = pygame.transform.scale(yellow_chip, updated_size)
    empty_scaled = pygame.transform.scale(empty, updated_size)

    pygame.display.set_caption("Connect-X Visualisation Demo")

    def draw_board(board):
        pygame.draw.rect(screen, (42, 42, 199), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 1:
                    screen.blit(red_scaled, (col * SLOT_SIZE, row * SLOT_SIZE))

                elif board[row][col] == 2:
                    screen.blit(yellow_scaled, (col * SLOT_SIZE, row * SLOT_SIZE))
                else:
                    color = (255, 255, 255)
                    screen.blit(empty_scaled, (col * SLOT_SIZE, row * SLOT_SIZE))

    pygame.init()
    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            draw_board(board)
            pygame.display.flip()

def test():
    return visualise(test_board)