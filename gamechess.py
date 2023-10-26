from grid import Grid
from chessmans import *
from settingchess import*
class Game:
    def __init__(self):
        self.grid = Grid()
        self.id = 0
        self.chessmans = {
                         1:Pawn_white(),-1:Pawn_black(),
                         2:King_white(),-2:King_black(),
                         3:Queen_white(),-3:Queen_black(),
                         4:Bishop_white(),-4:Bishop_black(),
                         5:Knight_white(),-5:Knight_black(),
                         6:Castle_white(),-6:Castle_black()
                        }
        self.chessman_now = Pawn_white()
        self.row = 0
        self.col = 0
        self.king_move = True
        self.castle_right = True
        self.castle_left = True
        self.capture = False
        self.capture_pos = 0
        self.draw_move = False
        self.take_turn = 1
        self.click = False
        self.end = False
        self.win = 0
        self.reset = False
    def get_click_chessman(self,mousepos):
        get_row = mousepos[1]//cell
        get_col = mousepos[0]//cell
        pygame.time.wait(100)
        if self.grid.grid[get_row][get_col]*self.take_turn > 0:
            self.chessman_now = self.chessmans[self.grid.grid[get_row][get_col]]
            self.row = get_row
            self.col = get_col
            self.draw_move == True
            self.click = True         
    def get_click_new_pos(self,mousepos):
        get_row = mousepos[1]//cell
        get_col = mousepos[0]//cell
        if self.click == True:
            for i in self.chessman_now.can_move:
                if self.check(self.row+i[0],self.col+i[1],self.row,self.col)== True and self.row+i[0] == get_row and self.col+i[1] == get_col:
                    if self.check_eat(get_row,get_col) == True:
                        self.delete_chessman(self.row,self.col)
                        self.move_new_pos(get_row,get_col)
                        self.click = False
                        self.take_turn*=-1
                        break
                elif self.row == 7 and self.col == 4 and get_row == 7  and  get_col == 7 and self.grid.grid[7][5] == 0 and self.grid.grid[7][6] == 0 and self.castle_right == True and self.king_move == True:
                    self.grid.grid[7][5] = 6
                    self.delete_chessman(7,7)
                    self.grid.grid[7][6] = 2
                    self.delete_chessman(7,4)
                    self.take_turn*=-1
                    self.click = False
                elif self.row == 7 and self.col == 4 and get_row == 7 and get_col == 0 and self.grid.grid[7][1] == 0 and self.grid.grid[7][2] == 0 and self.grid.grid[7][3] == 0 and self.castle_left == True and self.king_move == True:
                    self.grid.grid[7][2] = 2
                    self.delete_chessman(7,4)
                    self.grid.grid[7][3] = 6
                    self.delete_chessman(7,0)
                    self.take_turn*=-1
                    self.click = False
            if self.grid.grid[7][7] != 6:self.castle_right = False
            if self.grid.grid[7][0] != 6:self.castle_left = False
            if self.grid.grid[7][4] != 2:self.king_move = False
            self.check_to_capture()
    def check_eat(self,row,col):
        if self.chessman_now.id * self.grid.grid[row][col] <=0:
            return True
        return False
    def check(self,row,col,row_now,col_now):
        if row <= 7 and col <=7 and row>=0 and col>=0:
            if abs(self.chessman_now.id) == 6: #castle
                castle = self.check_move_castle(row_now,col_now)
                if castle[0]<=row <= castle[1] and castle[3]<=col <=castle[2]:
                    return True
            elif abs(self.chessman_now.id) == 4:#bishop
                change_col = col-col_now
                change_row = row-row_now
                bishop = self.check_move_bishop(row_now,col_now)
                if change_row*change_col <0:
                    if bishop[3][0] >= row >= bishop[1][0] and bishop[3][1]<= col <= bishop[1][1]:
                        return True
                elif change_row*change_col >0:
                    if bishop[2][0] >= row >= bishop[0][0] and bishop[2][1] >= col >= bishop[0][1]:
                        return True
            elif abs(self.chessman_now.id) == 3:#queen
                change_col = col-col_now
                change_row = row-row_now
                castle = self.check_move_castle(row_now,col_now)
                bishop = self.check_move_bishop(row_now,col_now)
                if change_col == 0 or change_row == 0:
                    if castle[0]<=row <= castle[1] and castle[3]<=col <=castle[2]:
                        return True
                else:
                    if change_row*change_col <0:
                        if bishop[3][0] >= row >= bishop[1][0] and bishop[3][1]<= col <= bishop[1][1]:
                            return True
                    elif change_row*change_col >0:
                        if bishop[2][0] >= row >= bishop[0][0] and bishop[2][1] >= col >= bishop[0][1]:
                            return True
            elif self.chessman_now.id == 1:#pawn
                return bool(self.check_eat_pawnwhite(row,col,row_now,col_now) or self.check_first_move_pawnwhite(row,col,row_now,col_now))
            elif self.chessman_now.id == -1:
                return bool(self.check_eat_pawnblack(row,col,row_now,col_now) or self.check_first_move_pawnblack(row,col,row_now,col_now))          
            else:
                return True
    def check_move_castle(self,row_now,col_now):
        x_left = col_now-1
        x_right = col_now+1
        y_up = row_now-1
        y_down = row_now+1
        if col_now == 7:
            x_right = 7
        else:
            while x_right <=6:
                if self.grid.grid[row_now][x_right] == 0:
                    x_right+=1
                else:
                    break
        if col_now == 0:
            x_left = 0
        else:
            while x_left > 0:
                if self.grid.grid[row_now][x_left] == 0:
                    x_left-=1
                else:
                    break
        if row_now == 7:
            y_down = 7
        else:
            while y_down < 7:
                if self.grid.grid[y_down][col_now] == 0:
                    y_down+=1
                else:
                    break
        if row_now == 0:
            y_up = 0
        else:
            while y_up > 0:
                if self.grid.grid[y_up][col_now] == 0:
                    y_up-=1
                else:
                    break
        return [y_up,y_down,x_right,x_left]    
    def check_move_bishop(self,row_now,col_now):
        botright_can = True
        topright_can = True
        botleft_can = True
        topleft_can = True
        botright = [row_now+1,col_now+1]
        topright = [row_now-1,col_now+1]
        botleft =  [row_now+1,col_now-1]
        topleft =  [row_now-1,col_now-1]
        if col_now == 7:
            if row_now != 0 and row_now != 7:
                botright = [row_now,7]
                topright = [row_now,7]
                botleft_can = True
                topleft_can = True
            elif row_now == 0:
                botright = [0,7]
                topright = [0,7]
                topleft =  [0,7]
                botleft_can = True
            elif row_now == 7:
                botright = [7,7]
                topright = [7,7]
                botleft =  [7,7]
                topleft_can = True
        if col_now == 0:
            if row_now != 0 and row_now != 7:
                botleft = [row_now,0]
                topleft = [row_now,0]            
            elif row_now == 0:
                topright = [0,0]
                botleft =  [0,0]
                topleft =  [0,0]
                botright_can = True
            elif row_now == 7:
                botleft =  [7,0]
                topleft =  [7,0]
                botright = [7,0]
                topright_can = True
        if botright_can == True:
            while botright[0]<7 and botright[1]<7:
                if self.grid.grid[botright[0]][botright[1]] == 0:
                    botright[0] += 1
                    botright[1] += 1
                else:break
        if botleft_can == True:
            while botleft[0]<7 and 0<botleft[1]:
                if self.grid.grid[botleft[0]][botleft[1]] == 0:
                    botleft[0] += 1
                    botleft[1] += -1
                else:break
        if topright_can == True:
            while 0<topright[0] and topright[1]<7:
                if self.grid.grid[topright[0]][topright[1]] == 0:
                    topright[0] += -1
                    topright[1] += 1
                else:break
        if topleft_can == True:
            while 0<topleft[0] and 0<topleft[1]:
                if self.grid.grid[topleft[0]][topleft[1]] == 0:
                    topleft[0] += -1
                    topleft[1] += -1
                else:break
        return [topleft,topright,botright,botleft]
    def check_first_move_pawnwhite(self,row,col,row_now,col_now):
        if row_now == 6 and row == 4:
            return True
    def check_first_move_pawnblack(self,row,col,row_now,col_now):
        if row_now == 1 and row == 3:
            return True
    def check_eat_pawnwhite(self,row,col,row_now,col_now):
        change_row = row-row_now
        change_col = col-col_now
        if self.grid.grid[row][col] != 0:
            if change_row == -1 and change_col == 0 :
                return False
            elif change_row == -1 and change_col == -1:
                return True
            elif change_row == -1 and change_col == 1:
                return True
        else:
            if change_row == -1 and change_col == 0 :
                return True
            elif change_row == -1 and change_col == -1:
                return False
            elif change_row == -1 and change_col == 1:
                return False
    def check_eat_pawnblack(self,row,col,row_now,col_now):
        change_row = row-row_now
        change_col = col-col_now
        if self.grid.grid[row][col] != 0:
            if change_row == 1 and change_col == 0 :
                return False
            elif change_row == 1 and change_col == -1:
                return True
            elif change_row == 1 and change_col == 1:
                return True
        else:
            if change_row == 1 and change_col == 0 :
                return True
            elif change_row == 1 and change_col == -1:
                return False
            elif change_row == 1 and change_col == 1:
                return False
    def to_capture(self,screen):
        if self.col >=5 :self.capture_pos = 5
        elif self.col <=1 :self.capture_pos = 1
        else :self.capture_pos = self.col
        self.surface_capture = pygame.Surface((cell*4,cell))
        for i in range(4):
            pygame.draw.rect(self.surface_capture,self.grid.coller(self.capture_pos+i-1,0),(i*cell,0,cell,cell))
        self.surface_capture.blit(self.chessmans[3].image,(cell*0,0))
        self.surface_capture.blit(self.chessmans[4].image,(cell*1,0))
        self.surface_capture.blit(self.chessmans[5].image,(cell*2,0))
        self.surface_capture.blit(self.chessmans[6].image,(cell*3,0))
        screen.blit(self.surface_capture,((self.capture_pos-1)*cell,0))
    def check_to_capture(self):
        if self.grid.grid[0][self.col] == 1:
            self.capture = True
    def capture_click(self,mousepos):
        get_row = mousepos[1]//cell
        get_col = mousepos[0]//cell
        if get_col == self.capture_pos-1 and get_row == 0:
            self.grid.grid[self.row][self.col] = 3
            self.capture = False
        elif get_col == self.capture_pos and get_row == 0:
            self.grid.grid[self.row][self.col] = 4
            self.capture = False
        elif get_col == self.capture_pos+1 and get_row == 0:
            self.grid.grid[self.row][self.col] = 5
            self.capture = False
        elif get_col == self.capture_pos+2 and get_row == 0:
            self.grid.grid[self.row][self.col] = 6
            self.capture = False
    def draw_can_move(self,screen,chessman,row,col):
        if abs(self.chessman_now.id) == 6:
            castle = self.check_move_castle(row,col)
            for i in range(castle[0],castle[1]):
                if self.grid.grid[i][self.col] * self.chessman_now.id <=0:
                    pygame.draw.rect(screen,self.collor_can_move(i,self.col),(col*cell,i*cell,cell,cell))
            for i in range(castle[3],castle[2]):
                if self.grid.grid[self.row][i] * self.chessman_now.id <=0:
                    pygame.draw.rect(screen,self.collor_can_move(self.row,i),(i*cell,row*cell,cell,cell))
        elif abs(self.chessman_now.id) == 5:
            for i in self.chessman_now.can_move:
                row_knight = row+i[0]
                col_knight = col+i[1]
                if 0<=row_knight <= 7 and 0<=col_knight <=7 :
                    if self.grid.grid[row_knight][col_knight] * self.chessman_now.id <=0:
                        pygame.draw.rect(screen,self.collor_can_move(row_knight,col_knight),(col_knight*cell,row_knight*cell,cell,cell))
        elif abs(self.chessman_now.id) == 4:
            bishop = self.check_move_bishop(row,col)
            i = 0
            while bishop[0][0]+i<bishop[2][0]:
                if self.grid.grid[bishop[0][0]+i][bishop[0][1]+i] * self.chessman_now.id <= 0:
                    pygame.draw.rect(screen,self.collor_can_move(bishop[0][0]+i,bishop[0][1]+i),((bishop[0][1]+i)*cell,(bishop[0][0]+i)*cell,cell,cell))    
                i+=1
            i = 0
            while bishop[1][0]+i<bishop[3][0]:
                if self.grid.grid[bishop[1][0]+i][bishop[1][1]-i] * self.chessman_now.id <= 0:
                    pygame.draw.rect(screen,self.collor_can_move(bishop[1][0]+i,bishop[1][1]-i),((bishop[1][1]-i)*cell,(bishop[1][0]+i)*cell,cell,cell))
                i+=1
        elif abs(self.chessman_now.id) == 3:
            castle = self.check_move_castle(row,col)
            bishop = self.check_move_bishop(row,col)
            for i in range(castle[0],castle[1]+1):
                if self.grid.grid[i][self.col] * self.chessman_now.id <=0:
                    pygame.draw.rect(screen,((self.collor_can_move(i,self.col))),(col*cell,i*cell,cell,cell))
            for i in range(castle[3],castle[2]+1):
                if self.grid.grid[self.row][i] * self.chessman_now.id <=0:
                    pygame.draw.rect(screen,self.collor_can_move(self.row,i),(i*cell,row*cell,cell,cell))
            i = 0
            while bishop[0][0]+i<bishop[2][0]:
                if self.grid.grid[bishop[0][0]+i][bishop[0][1]+i] * self.chessman_now.id <= 0:
                    pygame.draw.rect(screen,self.collor_can_move(bishop[0][0]+i,bishop[0][1]+i),((bishop[0][1]+i)*cell,(bishop[0][0]+i)*cell,cell,cell))    
                i+=1
            i = 0
            while bishop[1][0]+i<bishop[3][0]:
                if self.grid.grid[bishop[1][0]+i][bishop[1][1]-i] * self.chessman_now.id <= 0:
                    pygame.draw.rect(screen,self.collor_can_move(bishop[1][0]+i,bishop[1][1]-i),((bishop[1][1]-i)*cell,(bishop[1][0]+i)*cell,cell,cell))
                i+=1
        elif abs(self.chessman_now.id) == 2:
            for i in self.chessman_now.can_move:
                row_king = row+i[0]
                col_king = col+i[1]
                if 0<=row_king <= 7 and 0<=col_king <=7 :
                    if self.grid.grid[row_king][col_king] * self.chessman_now.id <= 0:
                        pygame.draw.rect(screen,self.collor_can_move(row_king,col_king),(col_king*cell,row_king*cell,cell,cell))
        elif abs(self.chessman_now.id) == 1:
            i = self.chessman_now.id
            if self.grid.grid[row-i][col] == 0:
                pygame.draw.rect(screen,(self.collor_can_move(row-i,col)),(col*cell,(row-i)*cell,cell,cell))
            if self.grid.grid[row-i][col-1]*i < 0:
                pygame.draw.rect(screen,self.collor_can_move(row-i,col-1),((col-1)*cell,(row-i)*cell,cell,cell))
            if self.grid.grid[row-i][col+1]*i < 0:
                pygame.draw.rect(screen,self.collor_can_move(row-i,col+1),((col+1)*cell,(row-i)*cell,cell,cell))
            if row == 6 and self.grid.grid[5][col] == 0 and self.grid.grid[4][col] == 0 and i == 1:
                pygame.draw.rect(screen,self.collor_can_move(4,col),(col*cell,4*cell,cell,cell))
            elif row == 1 and self.grid.grid[2][col] == 0 and self.grid.grid[3][col] == 0 and i == -1:
                pygame.draw.rect(screen,self.collor_can_move(3,col),(col*cell,3*cell,cell,cell))
    def collor_can_move(self,row,col):
        if col %2 ==0 and row %2 == 0:return  (233,237,204)#white
        elif col %2 != 0 and row %2 != 0:return (233,237,204)
        elif col %2 == 0 and row %2 != 0:return (119,153,84)  #light green
        elif col %2 != 0 and row %2 == 0:return (119,153,84) #light green
         #white
    def delete_chessman(self,row,col):
        self.grid.grid[row][col] = 0
    def move_new_pos(self,row,col):
        if abs(self.grid.grid[row][col]) == 2:
            self.end = True
            self.reset = True
            self.win = self.grid.grid[row][col]
        self.grid.grid[row][col] = self.chessman_now.id
        self.row = row
        self.col = col
    def reset_game(self):
        self.grid.grid =   [[-6,-5,-4,-3,-2,-4,-5,-6],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [1,1,1,1,1,1,1,1],
                            [6,5,4,3,2,4,5,6],]
        self.chessman_now = Pawn_white()
        self.row = 0
        self.col = 0
        self.king_move = True
        self.castle_right = True
        self.castle_left = True
        self.capture = False
        self.capture_pos = 0
        self.draw_move = False
        self.take_turn = 1
        self.click = False
        self.end = False
        self.win = 0
        self.reset = False
    def draw(self,screen):
        self.grid.draw(screen)
        self.draw_can_move(screen,self.chessman_now,self.row,self.col)
        for row in range(self.grid.num_rows):
            for col in range(self.grid.num_collumns):
                self.id = self.grid.grid[row][col]
                if self.id in self.chessmans:
                    screen.blit(self.chessmans[self.id].image,(col*cell,row*cell))
        
        if self.capture == True :self.to_capture(screen)