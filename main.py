import pygame,sys
from gamechess import Game
from settingchess import *
pygame.init()
screen = pygame.display.set_mode((Weight,Height))
pygame.display.set_caption('chess')
clock = pygame.time.Clock()
FBS = 60
game = Game()

font = pygame.font.SysFont('consolas', 60)
winnerwhite = font.render("white win", True, 'red')
winnerblack = font.render("black win", True, 'red')
textSurface = font.render("press 'r' to reset", True, 'red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game.reset == True:
                game.reset_game()
    try:
        mouse = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()
        game.draw(screen)
        if game.capture == False:
            if mouse[0] == True:
                game.get_click_chessman(mousepos)
            elif mouse[2] == True:
                game.get_click_new_pos(mousepos)
        elif game.capture == True:
            if mouse[0] == True:
                game.capture_click(mousepos)
        if game.end == True:
            if game.win == -2:
                screen.blit(winnerwhite, (200, 200))
            elif game.win == 2:
                screen.blit(winnerblack, (200, 200))
            screen.blit(textSurface, (50, 300))
            
    except:
        print('error')
    pygame.display.update()
    clock.tick(FBS)