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
pendulumInitAngle = math.radians(45)
pendulumMass = 1
g = 9.8

pendulumAngularVelocity = 0.1
pendulumAngularAcceleration = 0
pendulumDamping = 0.995

t = 0
dt = 0.1


while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    t += dt
    
    pendulumAngularVelocity += (g / pendulumLength) * math.cos(pendulumInitAngle) * dt + pendulumDamping / (pendulumMass * pendulumLength**2) * (-pendulumAngularVelocity) * dt
    pendulumInitAngle += pendulumAngularVelocity * dt

    x = pendulumOrigin[0] + (pendulumLength * math.cos(pendulumInitAngle))
    y = pendulumOrigin[1] + -(pendulumLength * -math.sin(pendulumInitAngle))

    pygame.draw.line(screen, pendulumLineColor, pendulumOrigin, (int(x), int(y)), 2)
    pygame.draw.circle(screen, pendulumMassColor, (windowWidth / 2, 100), 5)
    pygame.draw.circle(screen, pendulumMassColor, (int(x), int(y)), 20)

    pygame.display.update()
    clock.tick(frameRate)