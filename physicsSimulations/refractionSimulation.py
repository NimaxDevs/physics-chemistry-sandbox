import pygame
import math
from sys import exit

windowWidth = 1100
windowHeight = 580
frameRate = 60

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Refraction Simulation (Snell-Descartes Law)")
clock = pygame.time.Clock()
pygame.font.init()

titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
axisLineColor = (99, 113, 123)
whiteColor = (255, 255, 255)
rayColor = "Blue"
initIncidenceAngle = 45
refractiveIndex1 = 1.2
refractiveIndex2 = 1.5
lightRayCoords = [[45, 50], [windowWidth / 2, 400]]
lightRayLength = 200

def RefractingLight():
    pass

while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.line(screen, axisLineColor, (0, 400), (windowWidth, 400), 2)

    pygame.display.update()
    clock.tick(frameRate)