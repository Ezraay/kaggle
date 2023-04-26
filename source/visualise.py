import random
import pygame



BOARD_WIDTH = 800
BOARD_HEIGHT = 700
SLOT_SIZE = 100
SLOT_SPACING = 10

RED = (255,0,0)
YELLOW = (255,255,0)

pygame.display.set_caption("Connect-X Visulisation Demo")

def draw_board(board):
    pygame.draw.rect(screen, (0, 0, 255), (0, 0, BOARD_WIDTH, BOARD_HEIGHT))

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                color = RED
            elif board[row][col] == 2:
                color = YELLOW
            else:
                color = (255, 255, 255)
            pygame.draw.circle(screen, color, (col * (SLOT_SIZE + SLOT_SPACING) + SLOT_SIZE // 2,
                                               row * (SLOT_SIZE + SLOT_SPACING) + SLOT_SIZE // 2), SLOT_SIZE // 2)

pygame.init()
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, 2, None, None, None],
    [1, None, 1, 1, 2, None, 2]
]


print(board)

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        draw_board(board)
        pygame.display.flip()

