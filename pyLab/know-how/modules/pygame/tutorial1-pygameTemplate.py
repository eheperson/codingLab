"""

Game Loop :
    - Process input (event:mouseClick)
    - Update Game (change)
    - Render (Draw everything on screen)
    - clock(fps)

Game Running Algorithm :
    1- Setup game
    2- while !exit :
        i-   Pool and handle events
        ii-  Update game elements
        iii- Draw surface
        iv-  Show surface
    3- Close down Game

pygame Template : 
    1- set window size and required parameters(color codes etc.)
    2- initialize pygame and create window
    3- code game loop algorithm
    4- close down the window and pygame
"""
import pygame
import random

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
    #   pass
    #draw surface
    screen.fill(GREEN)
    #show surface
    pygame.display.flip()


#close down pygame and windod
pygame.quit()