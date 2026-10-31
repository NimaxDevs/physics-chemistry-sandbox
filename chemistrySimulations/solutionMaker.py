import pygame
import math
from random import randint, uniform
from sys import exit
import sys
import builtins
import json
import os

def ressource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    
    if "_MEI" in __file__:
        parts = os.path.abspath(__file__).split(os.sep)
        for part in parts:
            if part.startswith("_MEI"):
                base_dir = __file__.split(part)[0] + part
                return os.path.join(base_dir, relative_path)
                
    return os.path.join(os.path.abspath("."), relative_path)

_orig_exists = os.path.exists
def custom_exists(path):
    if isinstance(path, str) and not os.path.isabs(path):
        return _orig_exists(ressource_path(path)) or _orig_exists(path)
    return _orig_exists(path)
os.path.exists = custom_exists

_orig_getsize = os.path.getsize
def custom_getsize(path):
    if isinstance(path, str) and not os.path.isabs(path):
        try:
            return _orig_getsize(ressource_path(path))
        except FileNotFoundError:
            return _orig_getsize(path)
    return _orig_getsize(path)
os.path.getsize = custom_getsize

_original_open = builtins.open
def custom_open(file, *args, **kwargs):
    if isinstance(file, str) and not os.path.isabs(file):
        file = ressource_path(file)
    return _original_open(file, *args, **kwargs)
builtins.open = custom_open

_orig_img = pygame.image.load
pygame.image.load = lambda p: _orig_img(ressource_path(p))

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
pygame.display.set_caption("Solution Maker")
clock = pygame.time.Clock()
pygame.font.init()

#Sets the font of the simulation labels
titleFontPath = "fonts/segoeuib.ttf"
regularFontPath = "fonts/segoeui.ttf"

#Defines the "art" variables
titleFont = pygame.font.Font(ressource_path(titleFontPath), 25)
regularFont = pygame.font.Font(ressource_path(regularFontPath), 15)
backgroundColor = (43, 45, 47)
beakerLineColor = (255, 255, 255, 20)
whiteColor = (255, 255, 255)

#Defines some simulation variables
g = 9.8
vy = 0
solutes = [("Sodium Chloride", (255, 255, 255), 58.5),
             ("Glucose", (255, 255, 255), 180.0),
             ("Potassium Permanganate", (23, 0, 115), 158.0),
             ("Copper Sulfate", (0, 149, 255), 159.6),
             ("Sodium Hydroxide", (255, 255, 255), 40.0)]

soluteMass = 1000
soluteRadius = 2
simulatedSoluteIndex = 2 #
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
solventVolume = 1000
simulatedSolventIndex = 2 #
simulatedSolvent = solvents[simulatedSolventIndex][0]
simulatedSolventColor = None
simulatedSolventColorIntensity = 0.0
massConcentration = soluteMass / solventVolume
molarConcentration = (soluteMass / solutes[simulatedSoluteIndex][2]) / (solventVolume * 1e-3)
simulatedSolventColorFactor = massConcentration * 0.01

#Extracts the values selected from the launcher simulation configuration tab
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(launcherSettingsPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "solutionMaker":
            simulatedSolvent = values.get("initSolvent", "Water (H₂O)")
            if simulatedSolvent == "Water (H₂0)":
                simulatedSolvent = solvents[0][0]
            elif simulatedSolvent == "Ethanol (C₂H₅OH)":
                simulatedSolvent = solvents[1][0]
            elif simulatedSolvent == "Cyclohexane (C₆H₁₂)":
                simulatedSolvent = solvents[2][0]
            elif simulatedSolvent == "Hexane (C₆H₁₄)":
                simulatedSolvent = solvents[3][0]
            elif simulatedSolvent == "Acetone (C₃H₆O)":
                simulatedSolvent = solvents[4][0]
            else:
                simulatedSolvent = solvents[0][0]
            solventVolume = values.get("initSolventVolume", 550)
            simulatedSolute = values.get("initSolute", "Sodium Chloride (NaCl)")
            if simulatedSolute == "Sodium Chloride (NaCl)":
                simulatedSolute = solutes[0][0]
                molarMass = solutes[0][2]
            elif simulatedSolute == "Glucose (C₆H₁₂O₆)":
                simulatedSolute = solutes[1][0]
                molarMass = solutes[1][2]
            elif simulatedSolute == "Potassium Permanganate (KMnO₄)":
                simulatedSolute = solutes[2][0]
                molarMass = solutes[2][2]
            elif simulatedSolute == "Copper Sulfate (CuSO₄)":
                simulatedSolute = solutes[3][0]
                molarMass = solutes[3][2]
            elif simulatedSolute == "Sodium Hydroxide (NaOH)":
                simulatedSolute = solutes[4][0]
                molarMass = solutes[4][2]
            else:
                simulatedSolute = solutes[0][0]
                molarMass = solutes[0][2]
            
            soluteMass = values.get("initSoluteMass", 550)
        else:
            simulatedSolvent = solvents[0][0]
            solventVolume = 1000
            simulatedSolute = solutes[0][0]
            soluteMass = 1000
            molarMass = solutes[0][2]
else:
    simulatedSolvent = solvents[0][0]
    solventVolume = 1000
    simulatedSolute = solutes[0][0]
    soluteMass = 1000
    molarMass = solutes[0][2]

massConcentration = soluteMass / solventVolume
molarConcentration = (soluteMass / molarMass) / (solventVolume * 1e-3)
simulatedSolventColorFactor = massConcentration * 0.01
simulatedSoluteParticles = soluteMass * 0.5
    
soluteParticles = []
solubilityMatrix = {
    "Sodium Chloride":        {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False},
    "Glucose":                {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False},
    "Potassium Permanganate": {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": True},
    "Copper Sulfate":         {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False},
    "Sodium Hydroxide":       {"Water": True, "Ethanol": False, "Cyclohexane": False, "Hexane": False, "Acetone": False}
}

#Defines some simulation control variables
t = 0
dt = 0.1

#Checks if the selected solute and solvent are soluble
isSoluble = solubilityMatrix[simulatedSolute][simulatedSolvent]

#Separates the values from the tuples of the "solutes" list
for soluteName, soluteColor, soluteMolarMass in solutes:
    if simulatedSolute == soluteName:
        simulatedSoluteColor = soluteColor
        break

#Separates the values from the tuples of the "solvents" list
for solventName, solventColor, viscosity, diffusionSpeed, dissolutionSpeed in solvents:
    if simulatedSolvent == solventName:
        simulatedSolventColor = solventColor
        break

#Creates the solute particles with some parameters
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

#Function to aadd said particles to their respective list
def addSoluteParticles(simulatedSoluteParticles):
    for i in range(int(simulatedSoluteParticles)):
        soluteParticles.append(createSoluteParticles())

#Function to draw the solute particles on the screen by creating a surface to control its alpha channel value (dissolution effect)
def drawSoluteParticles(soluteParticles):
    for soluteParticle in soluteParticles:
        rChannel, gChannel, bChannel = soluteParticle["color"]
        soluteParticleSurface = pygame.Surface((soluteParticle["soluteParticleRadius"] * 2, soluteParticle["soluteParticleRadius"] * 2), pygame.SRCALPHA)
        pygame.draw.circle(soluteParticleSurface, (rChannel, gChannel, bChannel, soluteParticle["alpha"]), (soluteParticle["soluteParticleRadius"], soluteParticle["soluteParticleRadius"]), soluteParticle["soluteParticleRadius"])
        screen.blit(soluteParticleSurface, (int(soluteParticle["x"] - soluteParticle["soluteParticleRadius"]), int(soluteParticle["y"] - soluteParticle["soluteParticleRadius"])))

#Updates the position of the solute particles (with respect to gravity)
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

#Adds the solute particles to the list
addSoluteParticles(simulatedSoluteParticles)

#Main loop here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Separates the color channels of the color of the selected solvent
    if simulatedSolventColor:
        rSimulatedSolventColorChannel, gSimulatedSolventColorChannel, bSimulatedSolventColorChannel, aSimulatedSolventColorChannel = simulatedSolventColor
    else:
        rSimulatedSolventColorChannel, gSimulatedSolventColorChannel, bSimulatedSolventColorChannel, aSimulatedSolventColorChannel = (255, 255, 255, 10)

    #Adds a first layer to the screen representing the base solvent color
    solventSurface = pygame.Surface((250, 300), pygame.SRCALPHA)
    solventSurface.fill((rSimulatedSolventColorChannel, gSimulatedSolventColorChannel, bSimulatedSolventColorChannel, aSimulatedSolventColorChannel))
    screen.blit(solventSurface, ((windowWidth // 2) - 120, 201))

    #Adds a second layer to the screen representing the solvent gaining the solute's color if they are soluble
    if isSoluble and simulatedSoluteColor is not None and simulatedSolventColorIntensity > 0:
        rSoluteChannel, gSoluteChannel, bSoluteChannel = simulatedSoluteColor
        solventTintSurface = pygame.Surface((250, 300), pygame.SRCALPHA)
        solventTintSurface.fill((rSoluteChannel, gSoluteChannel, bSoluteChannel, int(simulatedSolventColorIntensity)))
        screen.blit(solventTintSurface, ((windowWidth // 2) - 120, 201))

    #These lines draw and update the solute particles
    drawSoluteParticles(soluteParticles)
    updateSoluteParticlesPos(soluteParticles)

    #While these lines draw the beaker containing the solution (solute + solvent)
    pygame.draw.line(screen, beakerLineColor, ((windowWidth // 2) - 120, 180), ((windowWidth // 2) - 120, 501), 2)
    pygame.draw.line(screen, beakerLineColor, ((windowWidth // 2) + 130, 180), ((windowWidth // 2) + 130, 501), 2)
    pygame.draw.line(screen, beakerLineColor, ((windowWidth // 2) - 120, 501), ((windowWidth // 2) + 130, 501), 2)

    #Creates labels describing some simulation informations (title, selected solute and solvent, etc...)
    upperLabel = titleFont.render("Solution Maker", True, whiteColor)
    soluteLabel = regularFont.render(f"Solute: {simulatedSolute}", True, whiteColor)
    solventLabel = regularFont.render(f"Solvent: {simulatedSolvent}", True, whiteColor)
    soluteMassLabel = regularFont.render(f"Solute Mass: {soluteMass:.1f} g", True, whiteColor)
    solventVolumeLabel = regularFont.render(f"Solvent Volume: {solventVolume:.1f} mL", True, whiteColor)
    solutionMassConcentrationLabel = regularFont.render(f"Solution Mass Concentration: {massConcentration:.1f} g/mL", True, whiteColor)
    solutionMolarConcentrationLabel = regularFont.render(f"Solution Molar Concentration: {molarConcentration:.1f} mol/L", True, whiteColor)
    solubilityLabel = regularFont.render(f"Soluble: {isSoluble}", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #Adds said labels to the screen
    screen.blit(upperLabel, (20, 20))
    screen.blit(soluteLabel, (20, 50))
    screen.blit(solventLabel, (20, 75))
    screen.blit(soluteMassLabel, (20, 100))
    screen.blit(solventVolumeLabel, (20, 125))
    screen.blit(solutionMassConcentrationLabel, (20, 150))
    screen.blit(solutionMolarConcentrationLabel, (20, 175))
    screen.blit(solubilityLabel, (20, 200))
    screen.blit(fpsLabel, (1030, 20))

    #Updates the time variable with a time step for Euler's Method (calculations of the particle positions)
    t += dt

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)