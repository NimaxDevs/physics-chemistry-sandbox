import pygame
import math
import numpy as np
from sys import exit
import json
import os

#Window settings
windowWidth = 1100
windowHeight = 580
frameRate = 60
if os.path.exists("images/icons/png/launcherIcon.png"):
    iconSurface = pygame.image.load("images/icons/png/launcherIcon.png")
    pygame.display.set_icon(iconSurface)

#Initializes the Pygame window, clock and font system
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Fluid Simulation")
clock = pygame.time.Clock()
pygame.font.init()

#Main loop here
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)
