import pygame;
from ...definitions import BLACK,RED,ROWS,SQUARE_SIZE,COLS,WHITE;
from .piece import Piece
class Board:

    def __init__(self):
        self.board = [];
        self.red_left = self.white_left = 12;
        self.red_kings = self.white_kings = 0
        self.createBoard();
    
    def draw_squares(self,win):
        win.fill(BLACK);
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win,RED,(row + SQUARE_SIZE,col + SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
                    # •	row + SQUARE_SIZE: This is the x-coordinate of the top-left corner of the rectangle. It starts from the value of row, offset by SQUARE_SIZE pixels.
                    # •	col + SQUARE_SIZE: This is the y-coordinate of the top-left corner of the rectangle. It starts from the value of col, offset by SQUARE_SIZE pixels.
	                # •	SQUARE_SIZE: The width of the rectangle in pixels.
	                # 	SQUARE_SIZE: The height of the rectangle in pixels.

                
    def evulate(self):
        return (self.white_left-self.red_left) + (self.white_kings*0.5 - self.red_kings*0.5);

    def get_all_pieces(self,color):
        pieces = [];
        for row in self.board:
            for piece in row:
                if (piece != 0 and piece.color == color): 
                    pieces.append(piece);
        return pieces;

    def move(self,piece , col,row ) :
        # understand more
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

        if row == ROWS-1 or row==0:
            piece.beking();
            if(piece.color == WHITE):
                self.white_kings+=1;
            else:
                self.red_kings+=1;

    def get_piece(self,row,col):
        return self.board[row][col];

    def createBoard(self):
        for row in range(ROWS):
            self.board.append([]);
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self,win):
        self.draw_squares(win);
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col];
                if piece!=0:
                    piece.draw(win);

    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None
    
