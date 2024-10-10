import sys
import pygame
import numpy as np

pygame.init()

# Sizes
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
ROWS = 3
COLS = 3
SQUARE_SIZE = WIDTH // COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3  # O PLAYER
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)

# Initialize board
board = np.zeros((ROWS, COLS))

def draw_lines(color=WHITE):
    for i in range(1, ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

def draw_figures(color=WHITE):
    for row in range(ROWS):
        for col in range(COLS):
            # If 1: O , 2: X
            if board[row][col] == 1:
                # Square size //2 to center the circle
                pygame.draw.circle(screen, color, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                                   int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                   radius=CIRCLE_RADIUS, width=CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, 
                                 (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), 
                                 (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), 
                                 CROSS_WIDTH)
                pygame.draw.line(screen, color, 
                                 (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), 
                                 CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def check_board(check_board=board):
    for row in range(ROWS):
        for col in range(COLS):
            if check_board[row][col] == 0:
                return False
    return True

def check_winner(player, check_board=board):
    # Check rows
    for row in range(ROWS):
        if all([check_board[row][col] == player for col in range(COLS)]):
            return True
    # Check columns
    for col in range(COLS):
        if all([check_board[row][col] == player for row in range(ROWS)]):
            return True
    # Check diagonals
    if all([check_board[i][i] == player for i in range(ROWS)]):
        return True
    if all([check_board[i][ROWS - i - 1] == player for i in range(ROWS)]):
        return True
    return False

def minimax(minimax_board, depth, maximizing):
    if check_winner(2, minimax_board):
        return float('inf')
    elif check_winner(1, minimax_board):
        return float('-inf')
    elif check_board(minimax_board):
        return 0
    
    if maximizing:
        best_score = -1000
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = 1000
        for row in range(ROWS):
            for col in range(COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(best_score, score)  # Fix to minimize score for the minimizing player
        return best_score

def restart():
    screen.fill(BLACK)
    draw_lines()
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0

def best_move():
    best_score = -1000
    move = (-1, -1)
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    if move != (-1, -1):
        mark_square(move[0], move[1], 2)
        return True
    return False

draw_lines()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            # Convert mouse coordinates to row/col
            row = mouseY // SQUARE_SIZE
            col = mouseX // SQUARE_SIZE

            if available_square(row, col):
                mark_square(row, col, player)
                if check_winner(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if best_move():
                        if check_winner(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over:
                    if check_board():
                        game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Fix the restart key check
                restart()
                game_over = False
                player = 1
    if not game_over:
        draw_figures();
    else:
        if check_winner(1):
            draw_figures(GREEN);
            draw_lines(GREEN)
        elif check_winner(2):
            draw_figures(RED);
            draw_lines(RED);
        else:
            draw_figures(GRAY);
            draw_lines(GRAY);
    
    pygame.display.update()