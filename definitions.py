import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128,128,128)

WIDTH , HEIGHT = 800, 800;
ROWS,COLS = 8,8;

# '//' makes an integer division (it divides and round down) , '/' makes floating point division
SQUARE_SIZE = WIDTH//COLS;

# loading crown image and resizing it
CROWN = pygame.transform.scale(pygame.image.load('../crown.png'),(44,25))