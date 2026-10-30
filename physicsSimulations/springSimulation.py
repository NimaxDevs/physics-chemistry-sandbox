import pygame
import math
from sys import exit
import json
import os

#These lines define the window variables
frameRate = 60
vsyncActivated = 0
flags = pygame.SCALED
windowWidth = 1100
windowHeight = 580

launcherSettingsPath = os.path.join ("launcherSettings", "launcherSettings.json")
if os.path.exists(launcherSettingsPath) and os.path.getsize(launcherSettingsPath) > 0:
    with open("launcherSettings/launcherSettings.json", "r") as f:
        launcherSettings = json.load(f)
        frameRate = launcherSettings.get("fpsCap")
        vsyncActivated = launcherSettings.get("vsyncActivated")
else:
    frameRate = 60
    vsyncActivated = 0

#While these lines initialize the Pygame window (screen) and change some of its properties (title) as well as the clock
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight), flags, vsync = vsyncActivated)
pygame.display.set_caption("Spring Simulation")
clock = pygame.time.Clock()
pygame.font.init()

#These lines define the "art" variables
titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
springLineColor = (99, 113, 123)
springMassColor = (134, 141, 145)
whiteColor = (255, 255, 255)

#But these ones define the physical properties of the spring as well as a scale factor for its length
scaleFactor = 50 #1 centimeter corresponds to 60 pixels
springOrigin_x = windowWidth // 2
springOrigin_y = 100
springInitMass = 0.5 #The values from the launcher will be here
g = pygame.Vector2(0, 9.8) #The values from the launcher will be here
springLength = 1e-2 #The values from the launcher will be here
springInitStiffness = 5 #The values from the launcher will be here
springDampingCoef = 0.5 #The values from the launcher will be here
springMassMomentum = springInitMass * pygame.Vector2(0, 0)
springMassPosition_y = springLength 

simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath):
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "springSimulation":
            springInitMass = values.get("initMass", 0.5)
            g = pygame.Vector2(0, values.get("initGravAcc", 9.8))
            springLength = (values.get("initLength", 1)) * 10e-2
            springInitStiffness = values.get("initStiffness", 5) 
            springDampingCoef = values.get("dampingCoef", 0.5)
        else:
            springInitMass = 0.5
            g = pygame.Vector2(0, 9.8)
            springLength = 1e-2
            springInitStiffness = 5
            springDampingCoef = 0.5
else:
    springInitMass = 0.5
    g = pygame.Vector2(0, 9.8)
    springLength = 1e-2
    springInitStiffness = 5
    springDampingCoef = 0.5

#Defines some simulation control variables
t = 0
dt = 0.01

#The main loop runs here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #These lines calculate the main physics formulae for the spring (its force using Hooke's law, its damping force, net force, momentum and position)
    springCurrentLength = pygame.Vector2(0, springMassPosition_y - (springOrigin_y/ scaleFactor))
    springForce = - springInitStiffness * (pygame.Vector2.magnitude(springCurrentLength) - springLength) * pygame.Vector2.normalize(springCurrentLength)
    dampingForce = pygame.Vector2(0, - springDampingCoef * (springMassMomentum.y / springInitMass)) 
    netForce = springForce + (springInitMass * g) + dampingForce
    springMassMomentum += (netForce * dt) #Updates the momentum of the spring mass (the thing hanging) by using Euler's Method to integrate the values numerically
    springMassPosition_y += ((springMassMomentum.y * dt) / springInitMass) #Updates the positon of the spring mass by using the same method

    #These lines draw the elements of the screen
    pygame.draw.line(screen, springLineColor, (springOrigin_x, springOrigin_y), (springOrigin_x, springMassPosition_y * scaleFactor), 4) #This one draws the spring (line or helix)
    pygame.draw.circle(screen, springMassColor, (windowWidth // 2, springMassPosition_y * scaleFactor), 20) #This one draws the spring mass
    pygame.draw.circle(screen, springMassColor, (windowWidth / 2, springOrigin_y), 5) #And this one draws the origin point

    #These lines create the label surfaces describing the simulation's title as well as its physical properties with their respective values
    upperLabel = titleFont.render("Simulating Spring", True, whiteColor)
    springMassLabel = regularFont.render(f"Spring Mass: {springInitMass:.1f} kg", True, whiteColor)
    springLengthLabel = regularFont.render(f"Spring Length: {pygame.Vector2.magnitude(springCurrentLength):.1f} cm", True, whiteColor)
    springInitStiffnessLabel = regularFont.render(f"Spring Stiffness: {springInitStiffness:.1f} N/m", True, whiteColor)
    springDampingCoefLabel = regularFont.render(f"Spring Damping Coefficient: {springDampingCoef:.1f}", True, whiteColor)
    gLabel = regularFont.render(f"Gravitational Acceleration: {pygame.Vector2.magnitude(g):.1f} m/s²", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #And these lines add the labels to the screen (or window)
    screen.blit(upperLabel, (20, 20))
    screen.blit(springMassLabel, (20, 50))
    screen.blit(springLengthLabel, (20, 75))
    screen.blit(springInitStiffnessLabel, (20, 100))
    screen.blit(springDampingCoefLabel, (20, 125))
    screen.blit(gLabel, (20, 150))
    screen.blit(fpsLabel, (1040, 20))

    #Updates the time by a small step that is going to be used to integrate the values for the spring mass momentum and position by using Euler's Method
    t += dt

    #Finally, these lines update the screen
    pygame.display.update()
    clock.tick(frameRate)
