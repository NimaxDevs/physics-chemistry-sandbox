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
pygame.display.set_caption("Refraction Simulation (Snell-Descartes Law)")
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
axisLineColor = (99, 113, 123)
whiteColor = (255, 255, 255)
redColor = (255, 0, 0)

#Defines some simulation variables (physical properties)
refractiveIndexesColorList = [(0, 0, 0, 100), (41, 94, 207, 100), (200, 200, 200, 30), (200, 200, 200, 10), (171, 215, 245, 70), (200, 200, 200, 150)] #Air, Water, Glass, Ethanol, Diamond and Plastic (PS)
rayColor = "White"
rayThickness = 2
initIncidenceAngle = 45
refractiveIndex1 = 1.0
refractiveIndex2 = 1.0
pointALightRayCoords = [45, 50]
pointBLightRayCoords = [windowWidth / 2, 400]
pointCRefractedLightRayCoords = [windowWidth - 50, windowHeight - 50]
lightRayLength = 200

#Extracts the values selected from the launcher simulation configuration tab and applies some data conversion and formatting methods
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(simulationConfigValuesPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "refractionSimulation":
            rawinitRefractiveIndex1Str = values.get("initRefractiveIndex1")
            rawinitRefractiveIndex2Str = values.get("initRefractiveIndex2")
            if rawinitRefractiveIndex1Str.replace(".", "", 1).isdigit() == True:
                if float(rawinitRefractiveIndex1Str) < 1.0:
                    refractiveIndex1 = 1.0
                elif float(rawinitRefractiveIndex1Str) > 2.0:
                    refractiveIndex1 = 2.0
                else:
                    refractiveIndex1 = float(rawinitRefractiveIndex1Str)
            else:
                if rawinitRefractiveIndex1Str == "Air (1.0)":
                    refractiveIndex1 = 1.0
                elif rawinitRefractiveIndex1Str == "Water (1.33)":
                    refractiveIndex1 = 1.33
                elif rawinitRefractiveIndex1Str == "Glass (1.52)":
                    refractiveIndex1 = 1.52
                elif rawinitRefractiveIndex1Str == "Ethanol (1.36)":
                    refractiveIndex1 = 1.36
                elif rawinitRefractiveIndex1Str == "Diamond (2.417)":
                    refractiveIndex1 = 2.417
                elif rawinitRefractiveIndex1Str == "Plastic (1.59)":
                    refractiveIndex1 = 1.59
                else:
                    refractiveIndex1 = 1.0

            if rawinitRefractiveIndex2Str.replace(".", "", 1).isdigit() == True:
                if float(rawinitRefractiveIndex2Str) < 1.0:
                    refractiveIndex2 = 1.0
                elif float(rawinitRefractiveIndex2Str) > 2.0:
                    refractiveIndex2 = 2.0
                else:
                    refractiveIndex2 = float(rawinitRefractiveIndex2Str)
            else:
                if rawinitRefractiveIndex2Str == "Air (1.0)":
                    refractiveIndex2 = 1.0
                elif rawinitRefractiveIndex2Str == "Water (1.33)":
                    refractiveIndex2 = 1.33
                elif rawinitRefractiveIndex2Str == "Glass (1.52)":
                    refractiveIndex2 = 1.52
                elif rawinitRefractiveIndex2Str == "Ethanol (1.36)":
                    refractiveIndex2 = 1.36
                elif rawinitRefractiveIndex2Str == "Diamond (2.417)":
                    refractiveIndex2 = 2.417
                elif rawinitRefractiveIndex2Str == "Plastic (1.59)":
                    refractiveIndex2 = 1.59
                else:
                    refractiveIndex2 = 1.0

            initIncidenceAngle = values.get("initIncidenceAngle", 45)    
            rayColor = values.get("rayColor", "White")
        else:
            refractiveIndex1 = 1.0
            refractiveIndex2 = 1.0
            initIncidenceAngle = 45
            rayColor = "White"
else:
    refractiveIndex1 = 1.0
    refractiveIndex2 = 1.0
    initIncidenceAngle = 45
    rayColor = "White"

#These lines define the color of the medium shown on the screen based on the refractive indexes
if refractiveIndex1 == 1.0:
    mediumColor1 = (0, 0, 0, 100)
elif refractiveIndex1 == 1.33:
    mediumColor1 = (41, 94, 207, 100)
elif refractiveIndex1 == 1.52:
    mediumColor1 = (200, 200, 200, 30)
elif refractiveIndex1 == 1.36:
    mediumColor1 = (200, 200, 200, 10)
elif refractiveIndex1 == 2.417:
    mediumColor1 = (171, 215, 245, 70)
elif refractiveIndex1 == 1.59:
    mediumColor1 = (200, 200, 200, 150)
else:
    mediumColor1 = (0, 0, 0, 100)

if refractiveIndex2 == 1.0:
    mediumColor2 = (0, 0, 0, 100)
elif refractiveIndex2 == 1.33:
    mediumColor2 = (41, 94, 207, 100)
elif refractiveIndex2 == 1.52:
    mediumColor2 = (200, 200, 200, 30)
elif refractiveIndex2 == 1.36:
    mediumColor2 = (200, 200, 200, 10)
elif refractiveIndex2 == 2.417:
    mediumColor2 = (171, 215, 245, 70)
elif refractiveIndex2 == 1.59:
    mediumColor2 = (200, 200, 200, 150)
else:
    mediumColor2 = (0, 0, 0, 100)

#While these lines create said mediums
mediumRect1 = pygame.Surface((windowWidth, 400), pygame.SRCALPHA)
mediumRect1.fill(mediumColor1)
mediumRect2 = pygame.Surface((windowWidth, 400), pygame.SRCALPHA)
mediumRect2.fill(mediumColor2)

#Function to calculate the angle of the refracted light ray by using Snell-Descartes Law taking into account the refractive indexes of the two mediums and the initial incidence angle by using some trigonometry
def RefractingLight():
    pointALightRayCoords[0] = pointBLightRayCoords[0] - math.sin(math.radians(initIncidenceAngle)) * lightRayLength
    pointALightRayCoords[1] = pointBLightRayCoords[1] - math.cos(math.radians(initIncidenceAngle)) * lightRayLength
    alphaAngle = initIncidenceAngle
    sinBetaAngle = refractiveIndex1 * math.sin(math.radians(alphaAngle)) / refractiveIndex2
    if sinBetaAngle <= 1:
        betaAngle = math.degrees(math.asin(sinBetaAngle))
    else:
        betaAngle = 180 - alphaAngle
        totalInternalRefractionLabel = regularFont.render("Total Internal Refraction", True, redColor)
        screen.blit(totalInternalRefractionLabel, (20, 170))

    #These lines update the position of the simulated light ray (line) by projecting the incidence and refracted angles on the unit circle
    pointCRefractedLightRayCoords[0] = pointBLightRayCoords[0] + math.sin(math.radians(betaAngle)) * lightRayLength
    pointCRefractedLightRayCoords[1] = pointBLightRayCoords[1] + math.cos(math.radians(betaAngle)) * lightRayLength
    initIncidenceAngleLabel = regularFont.render(f"Incidence Angle: {alphaAngle:.1f}°", True, whiteColor)
    refractedAngleLabel = regularFont.render(f"Refracted Angle: {betaAngle:.1f}°", True, whiteColor)
    screen.blit(initIncidenceAngleLabel, (20, 75))
    screen.blit(refractedAngleLabel, (20, 100))

#Main loop here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and initIncidenceAngle < 90:
                initIncidenceAngle += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and initIncidenceAngle > 0:
                initIncidenceAngle -= 1

    #Draws the mediums on the screen
    screen.blit(mediumRect1, (0, 0))
    screen.blit(mediumRect2, (0, 400))

    #Runs the function to calculate the refracted & incidence angle as said previously
    RefractingLight()

    #Draws the light rays (initial and refracted)
    pygame.draw.line(screen, rayColor, pointALightRayCoords, pointBLightRayCoords, rayThickness)
    pygame.draw.line(screen, rayColor, pointBLightRayCoords, pointCRefractedLightRayCoords, rayThickness)
    pygame.draw.line(screen, axisLineColor, (0, 400), (windowWidth, 400), 2)

    #Creates labels describing some simulation informations (title, instructions, etc...)
    upperLabel = titleFont.render("Simulating Refraction", True, whiteColor)
    instructionsLabel = regularFont.render("Click on [UP ARROW] to increase the incidence angle or [DOWN ARROW] to decrease it", True, whiteColor)
    refractiveIndex1Label = regularFont.render(f"Refractive Index 1: {refractiveIndex1}", True, whiteColor)
    refractiveIndex2Label = regularFont.render(f"Refractive Index 2: {refractiveIndex2}", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #Adds said labels to the screen
    screen.blit(upperLabel, (20, 15))
    screen.blit(instructionsLabel, (20, 45))
    screen.blit(refractiveIndex1Label, (20, 125))
    screen.blit(refractiveIndex2Label, (20, 150))
    screen.blit(fpsLabel, (1030, 20))

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)