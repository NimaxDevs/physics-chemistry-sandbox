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
redColor = (255, 0, 0)
rayColorsList = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
refractiveIndexesList = [1.0, 1.33, 1.52, 1.36, 2.417, 1.59] #Air, Water, Glass, Ethanol, Diamond and Plastic (PS)
refractiveIndexesColorList = [(0, 0, 0, 100), (41, 94, 207, 100), (200, 200, 200, 30), (200, 200, 200, 10), (171, 215, 245, 70), (200, 200, 200, 150)] #Air, Water, Glass, Ethanol, Diamond and Plastic (PS)
rayColor = rayColorsList[6]
rayThickness = 2
initIncidenceAngle = 45
refractiveIndex1 = refractiveIndexesList[0]
refractiveIndex2 = refractiveIndexesList[0]
pointALightRayCoords = [45, 50]
pointBLightRayCoords = [windowWidth / 2, 400]
pointCRefractedLightRayCoords = [windowWidth - 50, windowHeight - 50]
lightRayLength = 200

if refractiveIndex1 == refractiveIndexesList[0]:
    mediumColor1 = refractiveIndexesColorList[0]
elif refractiveIndex1 == refractiveIndexesList[1]:
    mediumColor1 = refractiveIndexesColorList[1]
elif refractiveIndex1 == refractiveIndexesList[2]:
    mediumColor1 = refractiveIndexesColorList[2]
elif refractiveIndex1 == refractiveIndexesList[3]:
    mediumColor1 = refractiveIndexesColorList[3]
elif refractiveIndex1 == refractiveIndexesList[4]:
    mediumColor1 = refractiveIndexesColorList[4]
elif refractiveIndex1 == refractiveIndexesList[5]:
    mediumColor1 = refractiveIndexesColorList[5]
else:
    mediumColor1 = refractiveIndexesColorList[6]

if refractiveIndex2 == refractiveIndexesList[0]:
    mediumColor2 = refractiveIndexesColorList[0]
elif refractiveIndex2 == refractiveIndexesList[1]:
    mediumColor2 = refractiveIndexesColorList[1]
elif refractiveIndex2 == refractiveIndexesList[2]:
    mediumColor2 = refractiveIndexesColorList[2]
elif refractiveIndex2 == refractiveIndexesList[3]:
    mediumColor2 = refractiveIndexesColorList[3]
elif refractiveIndex2 == refractiveIndexesList[4]:
    mediumColor2 = refractiveIndexesColorList[4]
elif refractiveIndex2 == refractiveIndexesList[5]:
    mediumColor2 = refractiveIndexesColorList[5]
else:
    mediumColor2 = refractiveIndexesColorList[6]

mediumRect1 = pygame.Surface((windowWidth, 400), pygame.SRCALPHA)
mediumRect1.fill(mediumColor1)
mediumRect2 = pygame.Surface((windowWidth, 400), pygame.SRCALPHA)
mediumRect2.fill(mediumColor2)

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

    pointCRefractedLightRayCoords[0] = pointBLightRayCoords[0] + math.sin(math.radians(betaAngle)) * lightRayLength
    pointCRefractedLightRayCoords[1] = pointBLightRayCoords[1] + math.cos(math.radians(betaAngle)) * lightRayLength
    initIncidenceAngleLabel = regularFont.render(f"Incidence Angle: {alphaAngle:.1f}°", True, whiteColor)
    refractedAngleLabel = regularFont.render(f"Refracted Angle: {betaAngle:.1f}°", True, whiteColor)
    screen.blit(initIncidenceAngleLabel, (20, 70))
    screen.blit(refractedAngleLabel, (20, 95))

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

    screen.blit(mediumRect1, (0, 0))
    screen.blit(mediumRect2, (0, 400))
    RefractingLight()
    pygame.draw.line(screen, rayColor, pointALightRayCoords, pointBLightRayCoords, rayThickness)
    pygame.draw.line(screen, rayColor, pointBLightRayCoords, pointCRefractedLightRayCoords, rayThickness)
    #pygame.draw.rect(screen, mediumColor1, (0, 400, windowWidth, 400), 0)
    pygame.draw.line(screen, axisLineColor, (0, 400), (windowWidth, 400), 2)

    upperLabel = titleFont.render("Simulating Refraction", True, whiteColor)
    instructionsLabel = regularFont.render("Click on [UP ARROW] to increase the incidence angle or [DOWN ARROW] to decrease it", True, whiteColor)
    refractiveIndex1Label = regularFont.render(f"Refractive Index 1: {refractiveIndex1}", True, whiteColor)
    refractiveIndex2Label = regularFont.render(f"Refractive Index 2: {refractiveIndex2}", True, whiteColor)
    screen.blit(upperLabel, (20, 20))
    screen.blit(instructionsLabel, (20, 45))
    screen.blit(refractiveIndex1Label, (20, 120))
    screen.blit(refractiveIndex2Label, (20, 145))

    pygame.display.update()
    clock.tick(frameRate)