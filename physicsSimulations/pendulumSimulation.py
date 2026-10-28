import pygame
import math
from sys import exit
import json
import os

#These lines define the window variables
windowWidth = 1100
windowHeight = 580
frameRate = 60

#While these lines initialize the Pygame window (screen) and change some of its properties (title) as well as the clock
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Pendulum Simulation")
clock = pygame.time.Clock()
pygame.font.init()

#Defines the "art" variables
titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
pendulumLineColor = (99, 113, 123)
pendulumMassColor = (134, 141, 145)
whiteColor = (255, 255, 255)

#Defines the physical properties of the pendulum as well as a scale factor for its length
scaleFactor = 400 #1 meter corresponds to 400 px
pendulumOrigin = (windowWidth // 2, 100)
pendulumLength = 1 * scaleFactor 
pendulumInitAngle = math.radians(45)
pendulumMass = 10
g = 9.8
pendulumAngularVelocity = 0
pendulumDamping = 0.5

simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath):
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        pendulumInitAngle = math.radians(values.get("initAngle", 45))
        pendulumAngularVelocity = values.get("initAngularVel", 0)
        pendulumLength = (values.get("initLength", 1)) * scaleFactor
        pendulumMass = values.get("initMass", 10)
        g = values.get("initGravAcc", 9.8)
        pendulumDamping = values.get("dampingCoef", 0.1)      
else:
    pendulumInitAngle = math.radians(45)
    pendulumAngularVelocity = 0
    init_g = 9.8
    initMass = 10
    initDiameter = 1
    dragCoef = 0.1    

#Defines some simulation control variables
t = 0
dt = 0.1 #Time step for the Euler Method

#Here is the main loop
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    t += dt

    #Updates the angular velocity of the pendulum in radians per second using a formula which takes the pendulum's length, inital launch angle, damping coefficient, mass and previous angular velocity
    pendulumAngularVelocity += (g / pendulumLength) * math.cos(pendulumInitAngle) * dt + pendulumDamping / (pendulumMass * pendulumLength**2) * (-pendulumAngularVelocity) * dt
    pendulumInitAngle += pendulumAngularVelocity * dt #Updates the pendulum's angle based on the previous angular velocity using the Euler Method to integrate it numerically

    #Updates the x and y positions of the pendulum mass (or bob) by using its length as well as the cosine and sine of the pendulum angle
    x = pendulumOrigin[0] + (pendulumLength * -math.cos(pendulumInitAngle))
    y = pendulumOrigin[1] + -(pendulumLength * -math.sin(pendulumInitAngle))

    #Draws the whole pendulum
    pygame.draw.line(screen, pendulumLineColor, pendulumOrigin, (int(x), int(y)), 2) #This line draws the pendulum line
    pygame.draw.circle(screen, pendulumMassColor, (windowWidth / 2, 100), 5) #This one draws the pendulum mass (or bob)
    pygame.draw.circle(screen, pendulumMassColor, (int(x), int(y)), 20) #And this one draws the origin point of the pendulul

    #These lines create the surfaces (labels) of the simulation title as well as the physical properties of the pendulum
    upperLabel = titleFont.render("Simulating Pendulum", True, whiteColor)
    pendulumLengthLabel = regularFont.render(f"Pendulum Length: {pendulumLength / scaleFactor:.1f} m", True, whiteColor)
    pendulumAngleLabel = regularFont.render(f"Pendulum Angle: {math.degrees(pendulumInitAngle):.1f}°", True, whiteColor)
    pendulumAngularVelocityLabel = regularFont.render(f"Pendulum Angular Velocity: {pendulumAngularVelocity:.1f} rad/s", True, whiteColor)
    pendulumMassLabel = regularFont.render(f"Pendulum Mass: {pendulumMass:.1f} kg", True, whiteColor)
    gLabel = regularFont.render(f"Gravitational Acceleration: {g:.1f} m/s²", True, whiteColor)

    #And these lines add the labels mentioned above to the screen (window)
    screen.blit(upperLabel, (20, 20))
    screen.blit(pendulumLengthLabel, (20, 50))
    screen.blit(pendulumAngleLabel, (20, 75))
    screen.blit(pendulumAngularVelocityLabel, (20, 100))
    screen.blit(pendulumMassLabel, (20, 125))
    screen.blit(gLabel, (20, 150))

    #Lastly, these lines update the whole screen (or window)
    pygame.display.update()
    clock.tick(frameRate)