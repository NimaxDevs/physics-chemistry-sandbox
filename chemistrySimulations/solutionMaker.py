import pygame
import math
from random import randint, uniform
from sys import exit

windowWidth = 1100
windowHeight = 580
frameRate = 60

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Solution Maker")
clock = pygame.time.Clock()
pygame.font.init()

titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
beakerLineColor = (255, 255, 255, 20)
whiteColor = (255, 255, 255)

g = 9.8
vy = 0
solutes = [("Sodium Chloride", (255, 255, 255), 58.5),
             ("Glucose", (255, 255, 255), 180.0),
             ("Potassium Permanganate", (23, 0, 115), 158.0),
             ("Copper Sulfate", (0, 149, 255), 159.6),
             ("Sodium Hydroxide", (255, 255, 255), 40.0)]

soluteMass = 50
soluteRadius = 2
simulatedSoluteIndex = 3
simulatedSolute = solutes[simulatedSoluteIndex][0]
simulatedSoluteColor = None
simulatedSoluteParticles = soluteMass * 0.5
solutePosition_x = windowWidth // 2
solutePosition_y = 100
solvents = [("Water", (255, 255, 255, 10), 0.82, 1.8, 1.2),
            ("Ethanol", (255, 255, 255, 10), 0.88, 1.2, 0.8),
            ("Cyclohexane", (255, 255, 255, 10), 0.75, 2.5, 2.0),
            ("Hexane", (255, 255, 255, 10), 0.70, 3.0, 2.5),
            ("Acetone", (255, 255, 255, 10), 0.80, 2.2, 1.5)]
solventVolume = 100
simulatedSolventIndex = 0
simulatedSolvent = solvents[simulatedSolventIndex][0]
simulatedSolventColor = None
simulatedSolventColorIntensity = 0.0
massConcentration = soluteMass / solventVolume
molarConcentration = (soluteMass / solutes[simulatedSoluteIndex][2]) / (solventVolume * 10e-3)
simulatedSolventColorFactor = massConcentration * 0.01

soluteParticles = []
solubilityMatrix = {
    "Sodium Chloride":        {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False},
    "Glucose":                {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False},
    "Potassium Permanganate": {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": True},
    "Copper Sulfate":         {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False},
    "Sodium Hydroxide":       {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False}
}

t = 0
dt = 0.1

isSoluble = solubilityMatrix[simulatedSolute][simulatedSolvent]

for soluteName, soluteColor, soluteMolarMass in solutes:
    if simulatedSolute == soluteName:
        simulatedSoluteColor = soluteColor
        break

for solventName, solventColor, viscosity, diffusionSpeed, dissolutionSpeed in solvents:
    if simulatedSolvent == solventName:
        simulatedSolventColor = solventColor
        break

def createSoluteParticles():
    soluteParticle = {
        "x": solutePosition_x + randint(0, 20),
        "y": solutePosition_y + randint(-15, 45),
        "color": simulatedSoluteColor,
        "soluteParticleRadius": soluteRadius,
        "vx": uniform(-0.2, 0.2),
        "vy": 0,
        "alpha": 255.0
    }
    return soluteParticle

def addSoluteParticles(simulatedSoluteParticles):
    for i in range(int(simulatedSoluteParticles)):
        soluteParticles.append(createSoluteParticles())

def drawSoluteParticles(soluteParticles):
    for soluteParticle in soluteParticles:
        rChannel, gChannel, bChannel = soluteParticle["color"]
        soluteParticleSurface = pygame.Surface((soluteParticle["soluteParticleRadius"] * 2, soluteParticle["soluteParticleRadius"] * 2), pygame.SRCALPHA)
        pygame.draw.circle(soluteParticleSurface, (rChannel, gChannel, bChannel, soluteParticle["alpha"]), (soluteParticle["soluteParticleRadius"], soluteParticle["soluteParticleRadius"]), soluteParticle["soluteParticleRadius"])
        screen.blit(soluteParticleSurface, (int(soluteParticle["x"] - soluteParticle["soluteParticleRadius"]), int(soluteParticle["y"] - soluteParticle["soluteParticleRadius"])))

def updateSoluteParticlesPos(soluteParticles):
    accel_y = g 
    currentSolvent = solvents[simulatedSolventIndex]
    viscosity = currentSolvent[2]
    diffusionSpeed = currentSolvent[3]
    dissolutionSpeed = currentSolvent[4]
    for soluteParticle in soluteParticles[:]:
        if soluteParticle["y"] < 190:
            soluteParticle["vy"] += (accel_y * dt)
            soluteParticle["y"] += (soluteParticle["vy"] * dt)
            soluteParticle["x"] += soluteParticle["vx"]
        else:
            soluteParticle["vy"] += (accel_y * dt)
            soluteParticle["vy"] = soluteParticle["vy"] * viscosity
            soluteParticle["y"] += (soluteParticle["vy"] * dt)

            if isSoluble:
                if soluteParticle["vx"] == 0 or abs(soluteParticle["vx"]) < 0.5:
                    soluteParticle["vx"] = uniform(-0.1, 0.1)
                    soluteParticle["x"] += soluteParticle["vx"]
                alphaLoss = dissolutionSpeed * uniform(0.8, 1.5)
                soluteParticle["alpha"] -= alphaLoss

                global simulatedSolventColorIntensity
                if simulatedSolventColorIntensity < 180:
                    simulatedSolventColorIntensity += alphaLoss * simulatedSolventColorFactor
                
                if soluteParticle["alpha"] > 50:
                    soluteParticle["soluteParticleRadius"] = soluteRadius + (1.0 - (soluteParticle["alpha"] / 255.0)) * 4

                if soluteParticle["alpha"] <= 0 or soluteParticle["y"] >= 500:
                    soluteParticles.remove(soluteParticle)

            else:
                soluteParticle["vx"] = 0
                if soluteParticle["y"] >= 500:
                    soluteParticle["y"] = 500
                    soluteParticle["vy"] = 0

addSoluteParticles(simulatedSoluteParticles)

while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if simulatedSolventColor:
        rSimulatedSolventColorChannel, gSimulatedSolventColorChannel, bSimulatedSolventColorChannel, aSimulatedSolventColorChannel = simulatedSolventColor
    else:
        rSimulatedSolventColorChannel, gSimulatedSolventColorChannel, bSimulatedSolventColorChannel, aSimulatedSolventColorChannel = (255, 255, 255, 10)
    
    solventSurface = pygame.Surface((250, 300), pygame.SRCALPHA)
    solventSurface.fill((rSimulatedSolventColorChannel, gSimulatedSolventColorChannel, bSimulatedSolventColorChannel, aSimulatedSolventColorChannel))
    screen.blit(solventSurface, ((windowWidth // 2) - 120, 201))
    
    if isSoluble and simulatedSoluteColor is not None and simulatedSolventColorIntensity > 0:
        rSoluteChannel, gSoluteChannel, bSoluteChannel = simulatedSoluteColor
        solventTintSurface = pygame.Surface((250, 300), pygame.SRCALPHA)
        solventTintSurface.fill((rSoluteChannel, gSoluteChannel, bSoluteChannel, int(simulatedSolventColorIntensity)))
        screen.blit(solventTintSurface, ((windowWidth // 2) - 120, 201))

    drawSoluteParticles(soluteParticles)
    updateSoluteParticlesPos(soluteParticles)

    pygame.draw.line(screen, beakerLineColor, ((windowWidth // 2) - 120, 180), ((windowWidth // 2) - 120, 501), 2)
    pygame.draw.line(screen, beakerLineColor, ((windowWidth // 2) + 130, 180), ((windowWidth // 2) + 130, 501), 2)
    pygame.draw.line(screen, beakerLineColor, ((windowWidth // 2) - 120, 501), ((windowWidth // 2) + 130, 501), 2)

    upperLabel = titleFont.render("Solution Maker", True, whiteColor)
    soluteLabel = regularFont.render(f"Solute: {simulatedSolute}", True, whiteColor)
    solventLabel = regularFont.render(f"Solvent: {simulatedSolvent}", True, whiteColor)
    soluteMassLabel = regularFont.render(f"Solute Mass: {soluteMass:.1f} g", True, whiteColor)
    solventVolumeLabel = regularFont.render(f"Solvent Volume: {solventVolume:.1f} mL", True, whiteColor)
    solutionMassConcentrationLabel = regularFont.render(f"Solution Mass Concentration: {massConcentration:.1f} g/mL", True, whiteColor)
    solutionMolarConcentrationLabel = regularFont.render(f"Solution Molar Concentration: {molarConcentration:.1f} mol/L", True, whiteColor)
    solubilityLabel = regularFont.render(f"Soluble: {isSoluble}", True, whiteColor)

    screen.blit(upperLabel, (20, 20))
    screen.blit(soluteLabel, (20, 50))
    screen.blit(solventLabel, (20, 75))
    screen.blit(soluteMassLabel, (20, 100))
    screen.blit(solventVolumeLabel, (20, 125))
    screen.blit(solutionMassConcentrationLabel, (20, 150))
    screen.blit(solutionMolarConcentrationLabel, (20, 175))
    screen.blit(solubilityLabel, (20, 200))
    
    pygame.display.update()
    clock.tick(frameRate)