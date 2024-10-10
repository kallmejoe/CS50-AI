from .definitions import RED,WHITE,SQUARE_SIZE,GRAY , CROWN;
import pygame;
class piece:
    PADDING = 14;
    OUTLINE = 1.4;
    def __init__(self,row,col,color):
 

        self.row = row;
        self.col = col;
        self.color = color;
        self.king = False;
        self.x = 0;
        self.y = 0;
        self.calc_pos();

    def calc_pos(self):
        self.x = (SQUARE_SIZE*self.col)+self.col;
        self.y = (SQUARE_SIZE*self.row)+self.row;
    
    def beking(self):
        self.king = True;

    # i don't know what win is 
    def draw(self, win):
        radius = (SQUARE_SIZE//2)-self.PADDING;
        pygame.draw.circle(win,GRAY,(self.x,self.y),radius+self.OUTLINE);
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - radius, self.y - radius))

    def move(self,row,col):
        self.row = row;
        self.col = col;
        self.calc_pos();
    
    # The method __repr__ is a special method in Python that defines how an object is represented when it is printed or displayed in the console,
    def __repr__(self):
        return str(self.color)