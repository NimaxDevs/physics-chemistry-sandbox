import pygame
import math
from sys import exit
import json
import os

#Window settings
frameRate = 60
vsyncActivated = 0
flags = pygame.SCALED
windowWidth = 1100
windowHeight = 580
if os.path.exists("images/icons/png/launcherIcon.png"):
    iconSurface = pygame.image.load("images/icons/png/launcherIcon.png")
    pygame.display.set_icon(iconSurface)

#Extracts settings from the launcher
launcherSettingsPath = os.path.join ("launcherSettings", "launcherSettings.json")
if os.path.exists(launcherSettingsPath) and os.path.getsize(launcherSettingsPath) > 0:
    with open("launcherSettings/launcherSettings.json", "r") as f:
        launcherSettings = json.load(f)
        frameRate = launcherSettings.get("fpsCap")
        vsyncActivated = launcherSettings.get("vsyncActivated")
else:
    frameRate = 60
    vsyncActivated = 0

#Initializes the Pygame window, clock and font system
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight), flags, vsync = vsyncActivated)
pygame.display.set_caption("Gravity Simulation")
clock = pygame.time.Clock()
pygame.font.init()

#Sets the font of the simulation labels
if os.path.exists("fonts/segoeuib.ttf"):
    titleFontPath = "fonts/segoeuib.ttf"
else:
    titleFontPath = None
if os.path.exists("fonts/segoeui.ttf"):
    regularFontPath = "fonts/segoeui.ttf"
else:
    regularFontPath = None   

#Defines the "art" variables
titleFont = pygame.font.Font(titleFontPath, 25)
regularFont = pygame.font.Font(regularFontPath, 15)
backgroundColor = (43, 45, 47)
groundLineColor = (99, 113, 123)
massColor = (134, 141, 145)
whiteColor = (255, 255, 255)

#Defines some simulation variables (physical properties)
scaleFactor = 200
g = 9.8
initMass = 100
initHeight = 10
initRadius = 1
initVelocity = 0
initSurfaceArea = math.pi * initRadius**2
airRho = 1.225 #in kg/m³
dragCoef = 0.5
position_y = 1
restitutionCoef = 0.75 #A basket ball for reference

#Extracts the values selected from the launcher simulation configuration tab
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(simulationConfigValuesPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "gravitySimulation":
            initMass = values.get("initMass", 0.5)
            g = values.get("initGravAcc", 9.8)
            initHeight = (values.get("initHeight", 1))
        else:
            initMass = 100
            g = 9.8
            initHeight = 1 
else:
    initMass = 100
    g = 9.8
    initHeight = 1

#Defines some simulation control variables
t = 0
dt = 0.01

#Main loop here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Calculates the value of the acceleration in the y axis by applying a predefined air resistance using the drag force formula
    accel_y = g - ((0.5 * airRho * dragCoef * initSurfaceArea) / initMass) * initVelocity**2
    initVelocity += (accel_y * dt)
    position_y += (initVelocity * dt)

    #Updates the position of the simulated object and applies a scale factor to represent it on the screen accurately
    screenPosition_y = position_y * scaleFactor

    #Draws the ground line on the screen
    pygame.draw.line(screen, groundLineColor, (0, windowHeight - 50), (windowWidth, windowHeight - 50), 2)

    #Makes the object bounce if it hits the ground
    if screenPosition_y >= windowHeight - 70:
        screenPosition_y = windowHeight - 70
        position_y = (screenPosition_y / scaleFactor) - 0.001
        initVelocity = -initVelocity * restitutionCoef

    #Draws the simulated object
    pygame.draw.circle(screen, massColor, (windowWidth / 2, screenPosition_y), 20)

    #Creates labels describing some simulation informations (title, mass, etc...)
    upperLabel = titleFont.render("Simulating Gravity", True, whiteColor)
    objectMassLabel = regularFont.render(f"Object Mass: {initMass:.1f} kg", True, whiteColor)
    objectHeightLabel = regularFont.render(f"Object Height: {abs(initHeight - position_y - 7.5):.1f} m", True, whiteColor)
    objectRadiusLabel = regularFont.render(f"Object Radius: {initRadius:.1f} m", True, whiteColor)
    objectVelocityLabel = regularFont.render(f"Object Velocity: {initVelocity:.1f} m/s", True, whiteColor)
    objectSurfaceAreaLabel = regularFont.render(f"Object Surface Area: {initSurfaceArea:.1f} m²", True, whiteColor)
    objectAirDensityLabel = regularFont.render(f"Air Density: {airRho} kg/m³", True, whiteColor)
    dragCoefLabel = regularFont.render(f"Drag Coefficient: {dragCoef}", True, whiteColor)
    restitutionCoefLabel = regularFont.render(f"Restitution Coefficient: {restitutionCoef}", True, whiteColor)
    gLabel = regularFont.render(f"Gravitational Acceleration: {g} m/s²", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #Adds said labels to the screen
    screen.blit(upperLabel, (20, 20))
    screen.blit(objectMassLabel, (20, 50))
    screen.blit(objectHeightLabel, (20, 75))
    screen.blit(objectRadiusLabel, (20, 100))
    screen.blit(objectVelocityLabel, (20, 125))
    screen.blit(objectSurfaceAreaLabel, (20, 150))
    screen.blit(objectAirDensityLabel, (20, 175))
    screen.blit(dragCoefLabel, (20, 200))
    screen.blit(restitutionCoefLabel, (20, 225))
    screen.blit(gLabel, (20, 250))
    screen.blit(fpsLabel, (1030, 20))

    #Updates the time variable with a time step for Euler's Method
    t += dt

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)