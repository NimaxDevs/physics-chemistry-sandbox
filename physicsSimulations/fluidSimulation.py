import pygame
import math
import numpy as np
from sys import exit
import sys
import builtins
import json
import os

def ressource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

_orig_exists = os.path.exists
def custom_exists(path):
    if isinstance(path, str) and not os.path.isabs(path):
        return _orig_exists(ressource_path(path)) or _orig_exists(path)
    return _orig_exists(path)
os.path.exists = custom_exists

_orig_getsize = os.path.getsize
def custom_getsize(path):
    if isinstance(path, str) and not os.path.isabs(path):
        try:
            return _orig_getsize(ressource_path(path))
        except FileNotFoundError:
            return _orig_getsize(path)
    return _orig_getsize(path)
os.path.getsize = custom_getsize

_original_open = builtins.open
def custom_open(file, *args, **kwargs):
    if isinstance(file, str) and not os.path.isabs(file):
        file = ressource_path(file)
    return _original_open(file, *args, **kwargs)
builtins.open = custom_open

_orig_fnt = pygame.font.Font
def custom_font(path, size):
    if isinstance(path, str):
        return _orig_fnt(ressource_path(path), size)
    return _orig_fnt(path, size)
pygame.font.Font = custom_font

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
