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

titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
pendulumLineColor = (99, 113, 123)
pendulumMassColor = (134, 141, 145)
whiteColor = (255, 255, 255)

scaleFactor = 400 #1 meter corresponds to 400 px
pendulumOrigin = (windowWidth // 2, 100)
pendulumLength = 1 * scaleFactor 
pendulumInitAngle = math.radians(90)
pendulumMass = 1
g = 9.8

pendulumAngularVelocity = 0.1
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

    x = pendulumOrigin[0] + (pendulumLength * -math.cos(pendulumInitAngle))
    y = pendulumOrigin[1] + -(pendulumLength * -math.sin(pendulumInitAngle))

    pygame.draw.line(screen, pendulumLineColor, pendulumOrigin, (int(x), int(y)), 2)
    pygame.draw.circle(screen, pendulumMassColor, (windowWidth / 2, 100), 5)
    pygame.draw.circle(screen, pendulumMassColor, (int(x), int(y)), 20)

    upperLabel = titleFont.render("Simulating Pendulum", True, whiteColor)
    pendulumLengthLabel = regularFont.render(f"Pendulum Length: {pendulumLength / scaleFactor:.1f} m", True, whiteColor)
    pendulumAngleLabel = regularFont.render(f"Pendulum Angle: {math.degrees(pendulumInitAngle):.1f}°", True, whiteColor)
    pendulumAngularVelocityLabel = regularFont.render(f"Pendulum Angular Velocity: {pendulumAngularVelocity:.1f} rad/s", True, whiteColor)
    pendulumMassLabel = regularFont.render(f"Pendulum Mass: {pendulumMass:.1f} kg", True, whiteColor)
    gLabel = regularFont.render(f"Gravitational Acceleration: {g:.1f} m/s²", True, whiteColor)

    screen.blit(upperLabel, (20, 20))
    screen.blit(pendulumLengthLabel, (20, 45))
    screen.blit(pendulumAngleLabel, (20, 70))
    screen.blit(pendulumAngularVelocityLabel, (20, 95))
    screen.blit(pendulumMassLabel, (20, 120))
    screen.blit(gLabel, (20, 145))

    pygame.display.update()
    clock.tick(frameRate)