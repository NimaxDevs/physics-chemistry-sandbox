import pygame
import math
from sys import exit

windowWidth = 1100
windowHeight = 580
frameRate = 60

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pendulum Simulation")
clock = pygame.time.Clock()
pygame.font.init()

backgroundColor = (43, 45, 47)
pendulumLineColor = (99, 113, 123)
pendulumMassColor = (134, 141, 145)

pendulumOrigin = (windowWidth // 2, 100)
pendulumLength = 400 
pendulumInitAngle = 45
g = 9.8

pendulumAngularVelocity = 0
pendulumAngularAcceleration = 0
pendulumDamping = 0.995


while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pendulumAngularAcceleration = -(g / pendulumLength) * math.sin(pendulumInitAngle)
    pendulumAngularVelocity += pendulumAngularAcceleration
    pendulumAngularVelocity *= pendulumDamping
    pendulumInitAngle += pendulumAngularVelocity

    x = pendulumOrigin[0] + (pendulumLength * math.sin(pendulumInitAngle))
    y = pendulumOrigin[1] + (pendulumLength * math.cos(pendulumInitAngle))

    pygame.draw.line(screen, pendulumLineColor, pendulumOrigin, (int(x), int(y)), 2)
    pygame.draw.circle(screen, pendulumMassColor, (int(x), int(y)), 20)

    pygame.display.update()
    clock.tick(frameRate)