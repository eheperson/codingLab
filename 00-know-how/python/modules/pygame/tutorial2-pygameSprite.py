"""
Sprite :  ekranda hareket eden objeler
"""
import pygame
import random
#
#
#
# define player class (inheriting from pygame.sprite )
class player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.ySpeed = 5
    
    def update(self):
        self.rect.y += self.ySpeed
        if self.rect.bottom > HEIGHT - 200 :
            self.ySpeed = -5
        if self.rect.top < 0 :
            self.ySpeed = 5
#
#
# set window size
WIDTH = 360
HEIGHT = 360
FPS = 30
# set color codes 
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
# initialize pygame
pygame.init()
#
# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game Screen")
clock = pygame.time.Clock() 
#
#sprite 
allSprite = pygame.sprite.Group()
player = player()
allSprite.add(player)

# game loop
running = True
while running:
    #keep loop running at right speed
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update game elements
    allSprite.update()
    #draw surface
    screen.fill(GREEN)
    allSprite.draw(screen)
    #show surface
    pygame.display.flip()


#close down pygame and windod
pygame.quit()