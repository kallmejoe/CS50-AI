import pygame;
from .definitions import RED,WHITE,SQUARE_SIZE,GRAY , CROWN;
from checkers.board import Board;

class game:
    
    def __init__(self,win):
        self._init();
        self.win =win;
    

    def update(self):
        # draw a window
        self.board.draw(self.win);
