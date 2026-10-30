import pygame
import math
from sys import exit
import random
import json
import os

#The window variables go here
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

#These lines initialize the Pygame window as well as the clock and the font
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight), flags, vsync = vsyncActivated)
pygame.display.set_caption("Projectile Simualtion")
clock = pygame.time.Clock()
pygame.font.init()

#The "art" variables go here
titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
projectileColor = (74, 93, 107)
groundLineColor = (99, 113, 123)
projectileTrailColor = (134, 141, 145)
grayColor = (128, 128, 128)
whiteColor = (255, 255, 255)
redColor = (255, 0, 0)

#The physical variables go here
scaleFactor = 4 #1 meter corresponds to 4 pixels
init_g = 9.8 
initVelocity = 60 
initAngle = 65 
initMass = 10 
initDiameter = 1 
dragCoef = 0.1 
initialSurfaceArea = math.pi * (initDiameter/2)**2
airRho = 1.225 #Air density in kg/m³
start_x = 100
start_y = (windowHeight - 50) - initDiameter * 4

#These lines extract the values from the launcher
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(simulationConfigValuesPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "projectileSimulation":
            initVelocity = values.get("initVelocity", 60)
            initAngle = values.get("initAngle", 45)
            init_g = values.get("initGravAcc", 9.8)
            initMass = values.get("initMass", 10)
            initDiameter = values.get("initDiameter", 1)
            dragCoef = values.get("dragCoef", 0.1)
        else:
            initVelocity = 60
            initAngle = 65
            init_g = 9.8
            initMass = 10
            initDiameter = 1
            dragCoef = 0.1  
else:
    initVelocity = 60
    initAngle = 65
    init_g = 9.8
    initMass = 10
    initDiameter = 1
    dragCoef = 0.1    

#This variable stores the points plotted by the projectile trajectory
trajectoryPoints = []

#The simulation control variables go here
time = 0
dt = 0.1

#These lines of code initialize the variables needed to make the physics calculations
initAngleRad = math.radians(initAngle) #converting degrees to radians
vx = initVelocity * math.cos(initAngleRad) #creates the x-component of the velocity
vy = -initVelocity * math.sin(initAngleRad) #creates the y-component of the velocity
x = start_x
y = start_y

#The main loop is here
while True:
    screen.fill(backgroundColor) #Fills the screen with a white background
    
    #Checks if the "X" button of the window is pressed and if so: the window closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Calculates the total velocity of the projectile (I know that I should have used vectors instead of this, I might change the logic later)
    totalVelocity = math.sqrt(vx**2 + vy**2)

    #Calculates the total drag force using the air density, drag coefficient, surface area of the projectile and the total velocity squared   
    if totalVelocity > 0:
        totalDragForce = 0.5 * airRho * dragCoef * initialSurfaceArea * (totalVelocity**2)
        dragForce_x = totalDragForce * (vx / totalVelocity) #creates the x-component of the drag force
        dragForce_y = totalDragForce * (vy / totalVelocity) #creates the y-component of the drag force
    else:
        dragForce_x = 0
        dragForce_y = 0

    #These lines protect the simulation from breaking (launching a hot air balloon at Mach 1 for example) by checking the value of the x-component of the velocity
    if abs((dragForce_x / initMass) * dt) > abs(vx):
        vx = 0
        warningLabel = titleFont.render("bro, the values are so unrealistic that the simulation would actually break", True, redColor)
        warningLabelRect = warningLabel.get_rect(center = (windowWidth // 2, windowHeight // 2))
        screen.blit(warningLabel, warningLabelRect)
    else:
        vx -= (dragForce_x / initMass) * dt

    #These lines also protect the simulation from breaking by checking the value of the y-component of the velocity
    if abs((dragForce_y / initMass) * dt) > abs (vy):
        vy = 0
        warningLabel = titleFont.render("bro, the values are so unrealistic that the simulation would actually break", True, redColor)
        warningLabelRect = warningLabel.get_rect(center = (windowWidth // 2, windowHeight // 2))
        screen.blit(warningLabel, warningLabelRect)
    else:
        vy -= (dragForce_y / initMass) * dt

    #Applies the gravitational acceleration to the y-component of the velocity (the x-component isn't affected by gravity; therefore, this isn't done for the x-component)
    vy += init_g * dt

    #Updates the position of the projectile by using the Euler's method (by integrating them numerically)
    x += vx * scaleFactor * dt #Updates the x position
    y += vy * scaleFactor * dt #Updates the y position

    #Adds the predefined time step to the simulation time variable
    time += dt

    #Sticks the projectile to the ground by checking if it reaches the y position of the ground line (sort of collision checking)    
    if y > (windowHeight - 50) - initDiameter * 4 and vy > 0:
        y = (windowHeight - 50) - initDiameter * 4

    #Draws the points plotted by the projectile trajectory if the simulation time variable is greater than 0
    if time > 0:
        trajectoryPoints.append((int(x), int(y)))
    for point in trajectoryPoints:
        pygame.draw.circle(screen, projectileTrailColor, point, 2)

    #And this one draws the floor (a line)
    pygame.draw.line(screen, groundLineColor, (0, windowHeight - 50), (windowWidth, windowHeight - 50), 2)

    #Well, this line draws the projectile
    pygame.draw.circle(screen, projectileColor, (int(x), int(y)), initDiameter * 4)

    #These lines create the labels representing the values of the physical properties of the simulation
    upperLabel = titleFont.render("Simulating Projectile", True, whiteColor)
    gLabel = regularFont.render(f"Gravitational Acceleration: {init_g:.1f} m/s²", True, whiteColor)
    velocityLabel = regularFont.render(f"Velocity: {initVelocity:.1f} m/s", True, whiteColor)
    angleLabel = regularFont.render(f"Angle: {initAngle:.1f}°", True, whiteColor)
    massLabel = regularFont.render(f"Mass: {initMass} kg", True, whiteColor)
    diameterLabel = regularFont.render(f"Diameter: {initDiameter} m", True, whiteColor)
    distanceTraveledLabel = regularFont.render(f"Distance Traveled (m): {(x - start_x) / scaleFactor:.1f} m", True, whiteColor)
    currentHeightLabel = regularFont.render(f"Current Height (m): {(start_y - y) / scaleFactor:.1f} m", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #And these lines add them to the main window (screen)
    screen.blit(upperLabel, (20, 20))
    screen.blit(gLabel, (20, 50))
    screen.blit(velocityLabel, (20, 75))
    screen.blit(angleLabel, (20, 100))
    screen.blit(massLabel, (20, 125))
    screen.blit(diameterLabel, (20, 150))
    screen.blit(distanceTraveledLabel, (20, 175))
    screen.blit(currentHeightLabel, (20, 200))
    screen.blit(fpsLabel, (1040, 20))

    #These lines update the whole window
    pygame.display.update()
    clock.tick(frameRate)