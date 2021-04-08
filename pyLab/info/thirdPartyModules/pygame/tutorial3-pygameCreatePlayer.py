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
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 1
        self.speedX = 0
    
    def update(self):
        self.speedX = 0
        keyStroke = pygame.key.get_pressed()
        if keyStroke[pygame.K_LEFT]:
            self.speedX = -4
        elif keyStroke[pygame.K_RIGHT]:
            self.speedX = 4
        else:
            self.speedX = 0

        self.rect.x += self.speedX

        if self.rect.right > WIDTH : 
            self.rect.right = WIDTH
        
        if self.rect.left < 0:
            self.rect.left = 0
    
    def getCoordinates(self):
        return (self.rect.x, self.rext.y)

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