from chessman import Chessman
from settingchess import *
import pygame
class Pawn_white(Chessman):
    def __init__(self):
        super().__init__(id = 1)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\whitepawn.png'),(cell,cell))
        self.can_move = [[-1,0],[-1,-1],[-1,1],[-2,0]]
class King_white(Chessman):
    def __init__(self):
        super().__init__(id = 2)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\whiteking.png'),(cell,cell))
        self.can_move = [[-1,-1],[-1,0],[-1,1],
                         [0, -1],       [0, 1],
                         [1, -1],[1, 0],[1, 1]]
class Queen_white(Chessman):
    def __init__(self):
        super().__init__(id = 3)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\whitequeen.png'),(cell,cell))
        self.can_move = [[i,0] for i in range(-8,8)]+[[0,i] for i in range(-8,8)]+[[i,i] for i in range(-8,8)]+[[-i,i] for i in range(-8,8)]
class Bishop_white(Chessman):
    def __init__(self):
        super().__init__(id = 4)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\whitebishop.png'),(cell,cell))
        self.can_move = [[i,i] for i in range(-8,8)]+[[-i,i] for i in range(-8,8)]
class Knight_white(Chessman):
    def __init__(self):
        super().__init__(id = 5)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\whiteknight.png'),(cell,cell))
        self.can_move = [       [-2,-1],         [-2, 1],
                         [-1,-2],                       [-1, 2],
                         
                         
                         [1, -2],                       [ 1, 2],
                                [2,-1],          [ 2, 1]]
class Castle_white(Chessman):
    def __init__(self):
        super().__init__(id = 6)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\whitecastle.png'),(cell,cell))
        self.can_move = [[i,0] for i in range(-8,8)]+[[0,i] for i in range(-8,8)]
class Pawn_black(Chessman):
    def __init__(self):
        super().__init__(id = -1)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\Blackpawn.png'),(cell,cell))
        self.can_move = [[1,0],[1,-1],[1,1],[2,0]]
class King_black(Chessman):
    def __init__(self):
        super().__init__(id = -2)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\Blackking.png'),(cell,cell))
        self.can_move = [[-1,-1],[-1,0],[-1,1],
                         [0, -1],       [0, 1],
                         [1, -1],[1, 0],[1, 1]]
class Queen_black(Chessman):
    def __init__(self):
        super().__init__(id = -3)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\Blackqueen.png'),(cell,cell))
        self.can_move = [[i,0] for i in range(-8,8)]+[[0,i] for i in range(-8,8)]+[[i,i] for i in range(-8,8)]+[[-i,i] for i in range(-8,8)]
class Bishop_black(Chessman):
    def __init__(self):
        super().__init__(id = -4)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\Blackbishop.png'),(cell,cell))
        self.can_move = [[i,i] for i in range(-8,8)]+[[-i,i] for i in range(-8,8)]
class Knight_black(Chessman):
    def __init__(self):
        super().__init__(id = -5)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\Blackknight.png'),(cell,cell))
        self.can_move = [       [-2,-1],         [-2, 1],
                         [-1,-2],                       [-1, 2],
                         
                         
                         [1, -2],                       [ 1, 2],
                                [2,-1],          [ 2, 1]]
class Castle_black(Chessman):
    def __init__(self):
        super().__init__(id = -6)
        self.image = pygame.transform.scale(pygame.image.load('D:\chessgame\imagechess\Blackcastle.png'),(cell,cell))
        self.can_move = [[i,0] for i in range(-8,8)]+[[0,i] for i in range(-8,8)]