import pygame
import math
from random import randint
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
pygame.display.set_caption("Bohr Atomic Representation")
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
electronColor = (0, 136, 209)
protonColor = (255, 0, 0)
neutronColor = (171, 171, 171)
protonOutlineColor = (150, 0, 0)
neutronOutlineColor = (120, 120, 120)
backgroundColor = (43, 45, 47)
whiteColor = (255, 255, 255)

#Defines some simulation variables
atomSelectionIndex = 0
atoms = [("Hydrogen", 1, 1), 
         ("Helium", 4, 2), 
         ("Lithium", 7, 3), 
         ("Beryllium", 9, 4), 
         ("Boron", 11, 5), 
         ("Carbon", 12, 6),
         ("Nitrogen", 14, 7),
         ("Oxygen", 16, 8),
         ("Fluorine", 19, 9),
         ("Neon", 20, 10),
         ("Sodium", 23, 11),
         ("Magnesium", 24, 12),
         ("Aluminium", 27, 13),
         ("Silicon", 28, 14),
         ("Phosphorus", 31, 15),
         ("Sulfur", 32, 16)]
unitRadius = 80
nucleonRadius = 8
electronRadius = 6
massNumber = atoms[atomSelectionIndex][1]
protonNumber = atoms[atomSelectionIndex][2]
neutronNumber = massNumber - protonNumber
angle = 0
electrons = []
electronShells = []
protons = []
neutrons = []

#Extracts the values selected from the launcher simulation configuration tab
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath):
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "bohrAtomSimulation":
            atomSelectionIndex = values.get("atomSelectionIndex")
            massNumber = atoms[atomSelectionIndex][1]
            protonNumber = atoms[atomSelectionIndex][2]
            neutronNumber = massNumber - protonNumber
        else:
            atomSelectionIndex = 0
            massNumber = atoms[atomSelectionIndex][1]
            protonNumber = atoms[atomSelectionIndex][2]
            neutronNumber = massNumber - protonNumber
else:
    atomSelectionIndex = 0
    massNumber = atoms[atomSelectionIndex][1]
    protonNumber = atoms[atomSelectionIndex][2]
    neutronNumber = massNumber - protonNumber

#Separates the values from the tuples of the "atoms" list (name, mass number, atomic or proton number)
for atomName, massN, protonsN in atoms:
    if protonNumber == protonsN and massNumber == massN:
        simulatedAtom = atomName
        break

#Function to create the protons with some definable parameters
def createProtons():
    center_x = windowWidth // 2
    center_y = windowHeight // 2
    proton = {
        "x": center_x + randint(-10, 15),
        "y": center_y + randint(-15, 10)
    }
    return proton

#Function to create the neutrons with some definable parameters
def createNeutrons():
    center_x = windowWidth // 2
    center_y = windowHeight // 2
    neutron = {
        "x": center_x + randint(-14, 14),
        "y": center_y + randint(-14, 14)
    }
    return neutron

#Function to create the electrons with some definable parameters
def createElectrons(shell, initialAngle):
    electron = {
        "x": windowWidth // 2,
        "y": windowHeight // 2,
        "angle": initialAngle,
        "rotationSpeed": 2,
        "shell": shell
    }
    return electron

#Function to check how many electron shells have to be drawn depending on the proton number
def checkAtomElectronShells(protonNumber):
    global electronShells
    if 1 <= protonNumber <= 2:
        electronShells.append(("1s", 2))

    if 3 <= protonNumber <= 4:
        electronShells.append(("1s", 2))
        electronShells.append(("2s", 2))

    if 5 <= protonNumber <= 10:
        electronShells.append(("1s", 2))
        electronShells.append(("2s", 2))
        electronShells.append(("2p", 6))

    if 11 <= protonNumber <= 12:
        electronShells.append(("1s", 2))
        electronShells.append(("2s", 2))
        electronShells.append(("2p", 6))
        electronShells.append(("3s", 2))

    if 13 <= protonNumber <= 18:
        electronShells.append(("1s", 2))
        electronShells.append(("2s", 2))
        electronShells.append(("2p", 6))
        electronShells.append(("3s", 2))
        electronShells.append(("3p", 6))

#Function to draw said electron shells
def drawElectronShells(electronShells):
    for electronShell in electronShells:
        if electronShell[0] == "1s":
            pygame.draw.circle(screen, whiteColor, (int(windowWidth / 2), int(windowHeight / 2)), unitRadius, 1)
        if electronShell[0] == "2s":
            pygame.draw.circle(screen, whiteColor, (int(windowWidth / 2), int(windowHeight / 2)), unitRadius + 30, 1)
        if electronShell[0] == "2p":
            pygame.draw.circle(screen, whiteColor, (int(windowWidth / 2), int(windowHeight / 2)), unitRadius + 60, 1)
        if electronShell[0] == "3s":
            pygame.draw.circle(screen, whiteColor, (int(windowWidth / 2), int(windowHeight / 2)), unitRadius + 90, 1)
        if electronShell[0] == "3p":
            pygame.draw.circle(screen, whiteColor, (int(windowWidth / 2), int(windowHeight / 2)), unitRadius + 120, 1)

#Function to add the created protons to their respective list
def addProtons(protonNumber):
    for i in range(protonNumber):
        protons.append(createProtons())

#Function to add the created neutrons to their respective list
def addNeutrons(neutronNumber):
    for i in range(neutronNumber):
        neutrons.append(createNeutrons())

#Function to add the created electrons to their respective list
def addElectrons(electronShells, protonNumber):
    remainingElectrons = protonNumber
    for electronShell in electronShells:
        shellName = electronShell[0]
        maxCapacity = electronShell[1]
        electronsToAdd = min(remainingElectrons, maxCapacity)

        for i in range(electronsToAdd):
            startAngle = (360 / electronsToAdd) * i
            electrons.append(createElectrons(shellName, startAngle))

        remainingElectrons -= electronsToAdd

#Function to make the electrons spin on the electron shells (update their position with trigonometry)
def updateElectronPos(electrons):
    center_x = windowWidth // 2
    center_y = windowHeight // 2

    electronShellRadii = {
        "1s": unitRadius,
        "2s": unitRadius + 30,
        "2p": unitRadius + 60,
        "3s": unitRadius + 90,
        "3p": unitRadius + 120
    }
    for electron in electrons:
        electron["angle"] += electron["rotationSpeed"]
        currentRadius = electronShellRadii[electron["shell"]]
        electronAngleRad = math.radians(electron["angle"])
        electron["x"] = center_x + currentRadius * math.cos(electronAngleRad)
        electron["y"] = center_y + currentRadius * math.sin(electronAngleRad)

#Function to draw the protons from their respective list
def drawProtons(protons):
    for proton in protons:
        pygame.draw.circle(screen, protonColor, (int(proton["x"]), int(proton["y"])), nucleonRadius)
        pygame.draw.circle(screen, protonOutlineColor, (int(proton["x"]), int(proton["y"])), nucleonRadius, 2)

#Function to draw the neutrons from their respective list
def drawNeutrons(neutrons):
    for neutron in neutrons:
        pygame.draw.circle(screen, neutronColor, (int(neutron["x"]), int(neutron["y"])), nucleonRadius)
        pygame.draw.circle(screen, neutronOutlineColor, (int(neutron["x"]), int(neutron["y"])), nucleonRadius, 2)

#Function to draw the electrons from their respective list
def drawElectrons(electrons):
    for electron in electrons:
        pygame.draw.circle(screen, electronColor, (int(electron["x"]), int(electron["y"])), electronRadius)

#Runs the functions to check the number of electron shells, add the protons, neutrons and electrons to their lists
checkAtomElectronShells(protonNumber)
addProtons(protonNumber)
addNeutrons(neutronNumber)
addElectrons(electronShells, protonNumber)

#Main loop here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Draws the protons and neutrons first
    drawProtons(protons)
    drawNeutrons(neutrons)

    #These lines draw the electron shells, update the position of the electrons and draw them on the screen
    drawElectronShells(electronShells)
    updateElectronPos(electrons)
    drawElectrons(electrons)

    #Creates labels describing some simulation informations (title, selected atom, etc...)
    upperLabel = titleFont.render("Simulating Bohr's Atomic Representation", True, whiteColor)
    atomLabel = regularFont.render(f"Atom: {simulatedAtom}", True, whiteColor)
    massNumberLabel = regularFont.render(f"Mass Number: {massNumber}", True, whiteColor)
    protonNumberLabel = regularFont.render(f"Proton Number: {protonNumber}", True, whiteColor)
    neutronNumberLabel = regularFont.render(f"Neutron Number: {neutronNumber}", True, whiteColor)
    electronNumberLabel = regularFont.render(f"Electron Number: {protonNumber}", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #Adds said labels to the screen
    screen.blit(upperLabel, (20, 20))
    screen.blit(atomLabel, (20, 50))
    screen.blit(massNumberLabel, (20, 75))
    screen.blit(protonNumberLabel, (20, 100))
    screen.blit(neutronNumberLabel, (20, 125))
    screen.blit(electronNumberLabel, (20, 150))
    screen.blit(fpsLabel, (1030, 20))

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)