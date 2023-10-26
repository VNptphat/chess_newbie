import pygame,sys
pygame.init()
screen = pygame.display.set_mode((680,680))
pygame.display.set_caption('chess')
clock = pygame.time.Clock()
FBS = 60

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
            if event.key == pygame.K_r:
                print('sgs')
    screen.fill('white')
    screen.blit(winnerwhite, (200, 200))
    screen.blit(textSurface, (50, 300))
    pygame.display.update()