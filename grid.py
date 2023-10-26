import pygame
from settingchess import*
class Grid:
    def __init__(self):
        self.num_collumns = 8
        self.num_rows = 8
        self.cell_size = cell
        self.grid = [[-6,-5,-4,-3,-2,-4,-5,-6],
                     [-1,-1,-1,-1,-1,-1,-1,-1],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [1,1,1,1,1,1,1,1],
                     [6,5,4,3,2,4,5,6],]
    def coller(self,check_x,check_y):
        if check_x %2 ==0 and check_y %2 == 0:return (248, 251, 237) #white
        elif check_x %2 != 0 and check_y %2 == 0:return (137, 212, 43) #light green
        elif check_x %2 == 0 and check_y %2 != 0:return (137, 212, 43)  #light green
        elif check_x %2 != 0 and check_y %2 != 0:return (248, 251, 237) #white
    def draw(self,screen):
        for row in range(self.num_rows):
            for col in range(self.num_collumns):
                cell_rect = pygame.Rect(col*self.cell_size, row*self.cell_size,self.cell_size,self.cell_size)
                pygame.draw.rect(screen,self.coller(row,col), cell_rect)