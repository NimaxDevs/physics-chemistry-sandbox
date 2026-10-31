import pygame
import math
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

#Extracts launcher settings (FPS, V-Sync)
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
pygame.display.set_caption("Molecular Lab")
clock = pygame.time.Clock()
pygame.font.init()

#Sets the font of the simulation labels
titleFontPath = "fonts/segoeuib.ttf"
regularFontPath = "fonts/segoeui.ttf"

#Defines the "art" variables
titleFont = pygame.font.Font(ressource_path(titleFontPath), 25)
regularFont = pygame.font.Font(ressource_path(regularFontPath), 15)
backgroundColor = (43, 45, 47)
lewisLineColor = (99, 113, 123)
lightBlueColor = (3, 165, 252)
lightGrayColor = (148, 148, 148)
greenColor = (0, 204, 24)
blackColor = (0, 0, 0)
darkBlueColor = (0, 27, 204)
darkGrayColor = (77, 77, 77)
darkGreenColor = (0, 94, 19)
redColor = (255, 0, 0)
darkRedColor = (150, 0, 0)
pinkColor = (255, 194, 194)
whiteColor = (255, 255, 255)

#Defines some simulation variables
carbonAtomRadius = 40
hydrogenAtomRadius = 30
oxygenAtomRadius = 35
hydrogenAtomColor = greenColor
carbonAtomColor = darkGreenColor
oxygenAtomColor = darkRedColor
carbonAtomPos_x = 200
lewisSingleConnexionLineThickness = 5
lewisDoubleConnexionLineThickness = 15
selectedMolecule = "Glucose (C₆H₁₂O₆)"

#Extracts the values selected from the launcher simulation configuration tab
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(simulationConfigValuesPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "molecularLab":
            selectedMolecule = values.get("initMolecule", "Glucose (C₆H₁₂O₆)")
            hydrogenAtomColor = values.get("initHydrogenColor", "Light Blue")
            if hydrogenAtomColor == "Light Blue Color":
                hydrogenAtomColor = lightBlueColor
            elif hydrogenAtomColor == "Light Gray":
                hydrogenAtomColor = lightGrayColor
            elif hydrogenAtomColor == "Green":
                hydrogenAtomColor = greenColor
            else:
                hydrogenAtomColor = lightBlueColor
            carbonAtomColor = values.get("initCarbonColor", "Black")
            if carbonAtomColor == "Black":
                carbonAtomColor = blackColor
            elif carbonAtomColor == "Dark Blue":
                carbonAtomColor = darkBlueColor
            elif carbonAtomColor == "Dark Gray":
                carbonAtomColor = darkGrayColor
            elif carbonAtomColor == "Dark Green":
                carbonAtomColor = darkGreenColor
            else:
                carbonAtomColor = blackColor
            oxygenAtomColor = values.get("initOxygenColor", "Red") 
            if oxygenAtomColor == "Red":
                oxygenAtomColor = redColor
            elif oxygenAtomColor == "Dark Red":
                oxygenAtomColor = darkRedColor
            elif oxygenAtomColor == "Pink":
                oxygenAtomColor = pinkColor
            else:
                oxygenAtomColor = redColor
        else:
            selectedMolecule = "Glucose (C₆H₁₂O₆)"
            hydrogenAtomColor = lightBlueColor
            carbonAtomColor = blackColor
            oxygenAtomColor = redColor
else:
    selectedMolecule = "Glucose (C₆H₁₂O₆)"
    hydrogenAtomColor = lightBlueColor
    carbonAtomColor = blackColor
    oxygenAtomColor = redColor

if selectedMolecule == "Carbon Dioxide (CO₂)":
    moleculeScreenName = "Carbon Dioxide"
elif selectedMolecule == "Glucose (C₆H₁₂O₆)":
    moleculeScreenName = "Glucose"
elif selectedMolecule == "Ethanol (C₂H₅OH)":
    moleculeScreenName = "Ethanol"
elif selectedMolecule == "Acetone (C₃H₆O)":
    moleculeScreenName = "Acetone"
elif selectedMolecule == "Methanol (CH₃OH)":
    moleculeScreenName = "Methanol"
elif selectedMolecule == "Formaldehyde (CH₂O)":
    moleculeScreenName = "Formaldehyde"
else:
    moleculeScreenName = "Unknown"

#Function to draw the spherical carbon dioxide molecule
def sphericalCarbonDioxideMolecule():
    pygame.draw.circle(screen, oxygenAtomColor, (carbonAtomPos_x - 60, 300), oxygenAtomRadius)
    pygame.draw.circle(screen, oxygenAtomColor, (carbonAtomPos_x + 60, 300), oxygenAtomRadius)
    pygame.draw.circle(screen, carbonAtomColor, (carbonAtomPos_x, 300), carbonAtomRadius)
    carbonLabel = regularFont.render("C", True, whiteColor)
    carbonLabelRect = carbonLabel.get_rect(center = (carbonAtomPos_x, 300))
    oxygen1Label = regularFont.render("O", True, whiteColor)
    oxygen1LabelRect = carbonLabel.get_rect(center = (carbonAtomPos_x - 60, 300))
    oxygen2Label = regularFont.render("O", True, whiteColor)
    oxygen2LabelRect = carbonLabel.get_rect(center = (carbonAtomPos_x + 60, 300))
    screen.blit(carbonLabel, carbonLabelRect)
    screen.blit(oxygen1Label, oxygen1LabelRect)
    screen.blit(oxygen2Label, oxygen2LabelRect)

#Function to draw the Lewis carbon dioxide molecule
def lewisCarbonDioxideMolecule():
    pygame.draw.line(screen, lewisLineColor, ((carbonAtomPos_x * 4) - 150, 300), (carbonAtomPos_x * 4, 300), lewisDoubleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (carbonAtomPos_x * 4, 300), ((carbonAtomPos_x * 4) + 150, 300), lewisDoubleConnexionLineThickness)
    pygame.draw.circle(screen, oxygenAtomColor, ((carbonAtomPos_x * 4) - 150, 300), oxygenAtomRadius)
    pygame.draw.circle(screen, oxygenAtomColor, ((carbonAtomPos_x * 4) + 150, 300), oxygenAtomRadius)
    pygame.draw.circle(screen, carbonAtomColor, (carbonAtomPos_x * 4, 300), carbonAtomRadius)
    carbonLabel = regularFont.render("C", True, whiteColor)
    carbonLabelRect = carbonLabel.get_rect(center = (carbonAtomPos_x * 4, 300))
    oxygen1Label = regularFont.render("O", True, whiteColor)
    oxygen1LabelRect = carbonLabel.get_rect(center = ((carbonAtomPos_x * 4) - 150, 300))
    oxygen2Label = regularFont.render("O", True, whiteColor)
    oxygen2LabelRect = carbonLabel.get_rect(center = ((carbonAtomPos_x * 4) + 150, 300))
    screen.blit(carbonLabel, carbonLabelRect)
    screen.blit(oxygen1Label, oxygen1LabelRect)
    screen.blit(oxygen2Label, oxygen2LabelRect)

#Function to draw the Lewis glucose molecule
def lewisGlucoseMolecule():
    pygame.draw.line(screen, lewisLineColor, (50, 150), (150, windowHeight // 2), lewisDoubleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (50, 430), (150, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (150, windowHeight // 2), (300, windowHeight // 2), lewisSingleConnexionLineThickness)
    
    
    pygame.draw.line(screen, lewisLineColor, (300, windowHeight // 2), (300, (windowHeight // 2) - 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (300, windowHeight // 2), (300, (windowHeight // 2) + 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (300, (windowHeight // 2) + 100), (300, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (300, windowHeight // 2), (450, windowHeight // 2), lewisSingleConnexionLineThickness)

    pygame.draw.line(screen, lewisLineColor, (450, windowHeight // 2), (450, (windowHeight // 2) - 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (450, windowHeight // 2), (450, (windowHeight // 2) + 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (450, (windowHeight // 2)), (450, (windowHeight // 2) - 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (450, windowHeight // 2), (600, windowHeight // 2), lewisSingleConnexionLineThickness)

    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (600, (windowHeight // 2) - 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (600, (windowHeight // 2) + 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, (windowHeight // 2) + 100), (600, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (750, windowHeight // 2), lewisSingleConnexionLineThickness)
    
    pygame.draw.line(screen, lewisLineColor, (750, windowHeight // 2), (750, (windowHeight // 2) - 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (750, windowHeight // 2), (750, (windowHeight // 2) + 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (750, (windowHeight // 2) + 100), (750, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (750, windowHeight // 2), (1000, windowHeight // 2), lewisSingleConnexionLineThickness)

    pygame.draw.line(screen, lewisLineColor, (900, windowHeight // 2), (900, (windowHeight // 2) - 100), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (900, windowHeight // 2), (900, (windowHeight // 2) + 100), lewisSingleConnexionLineThickness)

    pygame.draw.line(screen, lewisLineColor, (900, windowHeight // 2), (1000, windowHeight // 2), lewisSingleConnexionLineThickness)

    pygame.draw.line(screen, lewisLineColor, (1000, windowHeight // 2), (1070, windowHeight // 2), lewisSingleConnexionLineThickness)
    
    pygame.draw.circle(screen, oxygenAtomColor, (50, 150), oxygenAtomRadius - 20)
    oxygenLabel = regularFont.render("O", True, whiteColor)
    oxygenLabelRect = oxygenLabel.get_rect(center = (50, 150))
    screen.blit(oxygenLabel, oxygenLabelRect)
    for i in range(6):
        pygame.draw.circle(screen, carbonAtomColor, (150 + (i * 150), windowHeight // 2), carbonAtomRadius - 20)
        carbonLabel = regularFont.render("C", True, whiteColor)
        carbonLabelRect = carbonLabel.get_rect(center = (150 + (i * 150), windowHeight // 2))
        screen.blit(carbonLabel, carbonLabelRect)
    
    pygame.draw.circle(screen, hydrogenAtomColor, (50, 430), hydrogenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (300, (windowHeight // 2) - 100), hydrogenAtomRadius - 20)
    hydrogen1Label = regularFont.render("H", True, whiteColor)
    hydrogen1LabelRect = hydrogen1Label.get_rect(center = (50, 430))
    hydrogen2Label = regularFont.render("H", True, whiteColor)
    hydrogen2LabelRect = hydrogen1Label.get_rect(center = (300, (windowHeight // 2) - 100))
    screen.blit(hydrogen1Label, hydrogen1LabelRect)
    screen.blit(hydrogen2Label, hydrogen2LabelRect)
    
    pygame.draw.circle(screen, oxygenAtomColor, (300, (windowHeight // 2) + 100), oxygenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (300, (windowHeight // 2) + 200), hydrogenAtomRadius - 20)
    oxygen1Label = regularFont.render("O", True, whiteColor)
    oxygen1LabelRect = oxygen1Label.get_rect(center = (300, (windowHeight // 2) + 100))
    hydrogen3Label = regularFont.render("H", True, whiteColor)
    hydrogen3LabelRect = hydrogen3Label.get_rect(center = (300, (windowHeight // 2) + 200))
    screen.blit(oxygen1Label, oxygen1LabelRect)
    screen.blit(hydrogen3Label, hydrogen3LabelRect)

    pygame.draw.circle(screen, oxygenAtomColor, (450, (windowHeight // 2) - 100), oxygenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (450, (windowHeight // 2) - 200), hydrogenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (450, (windowHeight // 2) + 100), hydrogenAtomRadius - 20)
    oxygen2Label = regularFont.render("O", True, whiteColor)
    oxygen2LabelRect = oxygen2Label.get_rect(center = (450, (windowHeight // 2) - 100))
    hydrogen4Label = regularFont.render("H", True, whiteColor)
    hydrogen4LabelRect = hydrogen4Label.get_rect(center = (450, (windowHeight // 2) - 200))
    hydrogen5Label = regularFont.render("H", True, whiteColor)
    hydrogen5LabelRect = hydrogen5Label.get_rect(center = (450, (windowHeight // 2) + 100))
    screen.blit(oxygen2Label, oxygen2LabelRect)
    screen.blit(hydrogen4Label, hydrogen4LabelRect)
    screen.blit(hydrogen5Label, hydrogen5LabelRect)
    
    pygame.draw.circle(screen, hydrogenAtomColor, (600, (windowHeight // 2) - 100), hydrogenAtomRadius - 20)
    pygame.draw.circle(screen, oxygenAtomColor, (600, (windowHeight // 2) + 100), oxygenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (600, (windowHeight // 2) + 200), hydrogenAtomRadius - 20)
    hydrogen6Label = regularFont.render("H", True, whiteColor)
    hydrogen6LabelRect = hydrogen6Label.get_rect(center = (600, (windowHeight // 2) - 100))
    oxygen3Label = regularFont.render("O", True, whiteColor)
    oxygen3LabelRect = oxygen3Label.get_rect(center = (600, (windowHeight // 2) + 100))
    hydrogen7Label = regularFont.render("H", True, whiteColor)
    hydrogen7LabelRect = hydrogen7Label.get_rect(center = (600, (windowHeight // 2) + 200))
    screen.blit(hydrogen6Label, hydrogen6LabelRect)
    screen.blit(oxygen3Label, oxygen3LabelRect)
    screen.blit(hydrogen7Label, hydrogen7LabelRect)

    pygame.draw.circle(screen, hydrogenAtomColor, (750, (windowHeight // 2) - 100), hydrogenAtomRadius - 20)
    pygame.draw.circle(screen, oxygenAtomColor, (750, (windowHeight // 2) + 100), oxygenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (750, (windowHeight // 2) + 200), hydrogenAtomRadius - 20)
    hydrogen8Label = regularFont.render("H", True, whiteColor)
    hydrogen8LabelRect = hydrogen8Label.get_rect(center = (750, (windowHeight // 2) - 100))
    oxygen4Label = regularFont.render("O", True, whiteColor)
    oxygen4LabelRect = oxygen4Label.get_rect(center = (750, (windowHeight // 2) + 100))
    hydrogen9Label = regularFont.render("H", True, whiteColor)
    hydrogen9LabelRect = hydrogen9Label.get_rect(center = (750, (windowHeight // 2) + 200))
    screen.blit(hydrogen8Label, hydrogen8LabelRect)
    screen.blit(oxygen4Label, oxygen4LabelRect)
    screen.blit(hydrogen9Label, hydrogen9LabelRect)

    pygame.draw.circle(screen, hydrogenAtomColor, (900, (windowHeight // 2) - 100), hydrogenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (900, (windowHeight // 2) + 100), hydrogenAtomRadius - 20)
    hydrogen10Label = regularFont.render("H", True, whiteColor)
    hydrogen10LabelRect = hydrogen10Label.get_rect(center = (900, (windowHeight // 2) - 100))
    hydrogen11Label = regularFont.render("H", True, whiteColor)
    hydrogen11LabelRect = hydrogen11Label.get_rect(center = (900, (windowHeight // 2) + 100))
    screen.blit(hydrogen10Label, hydrogen10LabelRect)
    screen.blit(hydrogen11Label, hydrogen11LabelRect)

    pygame.draw.circle(screen, oxygenAtomColor, (1000, windowHeight // 2), oxygenAtomRadius - 20)
    pygame.draw.circle(screen, hydrogenAtomColor, (1070, windowHeight // 2), hydrogenAtomRadius - 20)
    oxygen5Label = regularFont.render("O", True, whiteColor)
    oxygen5LabelRect = oxygen5Label.get_rect(center = (1000, windowHeight // 2))
    hydrogen12Label = regularFont.render("H", True, whiteColor)
    hydrogen12LabelRect = hydrogen12Label.get_rect(center = (1070, windowHeight // 2))
    screen.blit(oxygen5Label, oxygen5LabelRect)
    screen.blit(hydrogen12Label, hydrogen12LabelRect)

#Function to draw the Lewis ethanol molecule
def lewisEthanolMolecule():
    pygame.draw.line(screen, lewisLineColor, (50, windowHeight // 2), (350, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (350, (windowHeight // 2) - 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (350, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (600, (windowHeight // 2) - 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (600, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (600, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (850, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (850, windowHeight // 2), (1050, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (820, (windowHeight // 2) - 50), (880, (windowHeight // 2) - 50), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (820, (windowHeight // 2) + 50), (880, (windowHeight // 2) + 50), lewisSingleConnexionLineThickness)
    
    pygame.draw.circle(screen, hydrogenAtomColor, (50, windowHeight // 2), hydrogenAtomRadius)
    hydrogen13Label = regularFont.render("H", True, whiteColor)
    hydrogen13LabelRect = hydrogen13Label.get_rect(center = (50, windowHeight // 2))
    screen.blit(hydrogen13Label, hydrogen13LabelRect)
    
    for i in range(2):
        pygame.draw.circle(screen, carbonAtomColor, (350 + (i * 250), windowHeight // 2), carbonAtomRadius)
        carbon1Label = regularFont.render("C", True, whiteColor)
        carbon1LabelRect = carbon1Label.get_rect(center = (350 + (i * 250), windowHeight // 2))
        screen.blit(carbon1Label, carbon1LabelRect)

    pygame.draw.circle(screen, oxygenAtomColor, (850, windowHeight // 2), oxygenAtomRadius)
    oxygen6Label = regularFont.render("O", True, whiteColor)
    oxygen6LabelRect = oxygen6Label.get_rect(center = (850, windowHeight // 2))
    screen.blit(oxygen6Label, oxygen6LabelRect)

    pygame.draw.circle(screen, hydrogenAtomColor, (1050, windowHeight // 2), hydrogenAtomRadius)
    hydrogen14Label = regularFont.render("H", True, whiteColor)
    hydrogen14LabelRect = hydrogen14Label.get_rect(center = (1050, windowHeight // 2))
    screen.blit(hydrogen14Label, hydrogen14LabelRect)
    
    for i in range(2):
        pygame.draw.circle(screen, hydrogenAtomColor, (350 + (i * 250), (windowHeight // 2) - 200), hydrogenAtomRadius)
        hydrogen15Label = regularFont.render("H", True, whiteColor)
        hydrogen15LabelRect = hydrogen15Label.get_rect(center = (350 + (i * 250), (windowHeight // 2) - 200))
        screen.blit(hydrogen15Label, hydrogen15LabelRect)
        pygame.draw.circle(screen, hydrogenAtomColor, (350 + (i * 250), (windowHeight // 2) + 200), hydrogenAtomRadius)
        hydrogen16Label = regularFont.render("H", True, whiteColor)
        hydrogen16LabelRect = hydrogen16Label.get_rect(center = (350 + (i * 250), (windowHeight // 2) + 200))
        screen.blit(hydrogen16Label, hydrogen16LabelRect)

#Function to draw the Lewis acetone molecule
def lewisAcetoneMolecule():
    pygame.draw.line(screen, lewisLineColor, (50, windowHeight // 2), (350, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (350, (windowHeight // 2) - 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (350, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (600, (windowHeight // 2) - 200), lewisDoubleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (850, windowHeight // 2), (850, (windowHeight // 2) - 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (850, windowHeight // 2), (850, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (600, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (600, windowHeight // 2), (850, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (850, windowHeight // 2), (1050, windowHeight // 2), lewisSingleConnexionLineThickness)

    pygame.draw.circle(screen, hydrogenAtomColor, (50, windowHeight // 2), hydrogenAtomRadius)
    hydrogen17Label = regularFont.render("H", True, whiteColor)
    hydrogen17LabelRect = hydrogen17Label.get_rect(center = (50, windowHeight // 2))
    screen.blit(hydrogen17Label, hydrogen17LabelRect)
        
    for i in range(3):
        pygame.draw.circle(screen, carbonAtomColor, (350 + (i * 250), windowHeight // 2), carbonAtomRadius)
        carbon2Label = regularFont.render("C", True, whiteColor)
        carbon2LabelRect = carbon2Label.get_rect(center = (350 + (i * 250), windowHeight // 2))
        screen.blit(carbon2Label, carbon2LabelRect)

    for i in range(2):
        pygame.draw.circle(screen, hydrogenAtomColor, (350 + (i * 500), (windowHeight // 2) - 200), hydrogenAtomRadius)
        hydrogen18Label = regularFont.render("H", True, whiteColor)
        hydrogen18LabelRect = hydrogen18Label.get_rect(center = (350 + (i * 500), (windowHeight // 2) - 200))
        screen.blit(hydrogen18Label, hydrogen18LabelRect)
        pygame.draw.circle(screen, hydrogenAtomColor, (350 + (i * 500), (windowHeight // 2) + 200), hydrogenAtomRadius)
        hydrogen19Label = regularFont.render("H", True, whiteColor)
        hydrogen19LabelRect = hydrogen19Label.get_rect(center = (350 + (i * 500), (windowHeight // 2) + 200))
        screen.blit(hydrogen19Label, hydrogen19LabelRect)

    pygame.draw.circle(screen, oxygenAtomColor, (600, (windowHeight // 2) - 200), oxygenAtomRadius)
    oxygen7Label = regularFont.render("O", True, whiteColor)
    oxygen7LabelRect = oxygen7Label.get_rect(center = (600, (windowHeight // 2) - 200))
    screen.blit(oxygen7Label, oxygen7LabelRect)
    
    pygame.draw.circle(screen, hydrogenAtomColor, (1050, windowHeight // 2), hydrogenAtomRadius)
    hydrogen20Label = regularFont.render("H", True, whiteColor)
    hydrogen20LabelRect = hydrogen20Label.get_rect(center = (1050, windowHeight // 2))
    screen.blit(hydrogen20Label, hydrogen20LabelRect)

#Function to draw the Lewis methanol molecule
def lewisMethanolMolecule():
    pygame.draw.line(screen, lewisLineColor, (50, windowHeight // 2), (350, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (350, (windowHeight // 2) - 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (350, (windowHeight // 2) + 200), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (750, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (750, windowHeight // 2), (1050, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (720, (windowHeight // 2) - 50), (780, (windowHeight // 2) - 50), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (720, (windowHeight // 2) + 50), (780, (windowHeight // 2) + 50), lewisSingleConnexionLineThickness)
    
    pygame.draw.circle(screen, hydrogenAtomColor, (50, windowHeight // 2), hydrogenAtomRadius)
    hydrogen21Label = regularFont.render("H", True, whiteColor)
    hydrogen21LabelRect = hydrogen21Label.get_rect(center = (50, windowHeight // 2))
    screen.blit(hydrogen21Label, hydrogen21LabelRect)
        
    pygame.draw.circle(screen, carbonAtomColor, (350, windowHeight // 2), carbonAtomRadius)
    carbon3Label = regularFont.render("C", True, whiteColor)
    carbon3LabelRect = carbon3Label.get_rect(center = (350, windowHeight // 2))
    screen.blit(carbon3Label, carbon3LabelRect)        

    pygame.draw.circle(screen, oxygenAtomColor, (750, windowHeight // 2), oxygenAtomRadius)
    oxygen7Label = regularFont.render("O", True, whiteColor)
    oxygen7LabelRect = oxygen7Label.get_rect(center = (750, windowHeight // 2))
    screen.blit(oxygen7Label, oxygen7LabelRect)

    pygame.draw.circle(screen, hydrogenAtomColor, (1050, windowHeight // 2), hydrogenAtomRadius)
    hydrogen22Label = regularFont.render("H", True, whiteColor)
    hydrogen22LabelRect = hydrogen22Label.get_rect(center = (1050, windowHeight // 2))
    screen.blit(hydrogen22Label, hydrogen22LabelRect)

    pygame.draw.circle(screen, hydrogenAtomColor, (350, (windowHeight // 2) - 200), hydrogenAtomRadius)
    hydrogen23Label = regularFont.render("H", True, whiteColor)
    hydrogen23LabelRect = hydrogen23Label.get_rect(center = (350, (windowHeight // 2) - 200))
    screen.blit(hydrogen23Label, hydrogen23LabelRect)

    pygame.draw.circle(screen, hydrogenAtomColor, (350, (windowHeight // 2) + 200), hydrogenAtomRadius)
    hydrogen24Label = regularFont.render("H", True, whiteColor)
    hydrogen24LabelRect = hydrogen24Label.get_rect(center = (350, (windowHeight // 2) + 200))
    screen.blit(hydrogen24Label, hydrogen24LabelRect)

#Function to draw the Lewis formaldehyde molecule
def lewisFormaldehydeMolecule():
    pygame.draw.line(screen, lewisLineColor, (350, windowHeight // 2), (550, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (550, windowHeight // 2), (750, windowHeight // 2), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (550, windowHeight // 2), (550, (windowHeight // 2) - 200), lewisDoubleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (505, (windowHeight // 2) - 230), (505, (windowHeight // 2) - 170), lewisSingleConnexionLineThickness)
    pygame.draw.line(screen, lewisLineColor, (595, (windowHeight // 2) - 230), (595, (windowHeight // 2) - 170), lewisSingleConnexionLineThickness)

    
    for i in range(2):
        pygame.draw.circle(screen, hydrogenAtomColor, (350 + (i * 400), windowHeight // 2), hydrogenAtomRadius)
        hydrogen25Label = regularFont.render("H", True, whiteColor)
        hydrogen25LabelRect = hydrogen25Label.get_rect(center = (350 + (i * 400), windowHeight // 2))
        screen.blit(hydrogen25Label, hydrogen25LabelRect)

    pygame.draw.circle(screen, carbonAtomColor, (550, windowHeight // 2), carbonAtomRadius)
    carbon4Label = regularFont.render("C", True, whiteColor)
    carbon4LabelRect = carbon4Label.get_rect(center = (550, windowHeight // 2))
    screen.blit(carbon4Label, carbon4LabelRect)   

    pygame.draw.circle(screen, oxygenAtomColor, (550, (windowHeight // 2) - 200), oxygenAtomRadius)
    oxygen8Label = regularFont.render("O", True, whiteColor)
    oxygen8LabelRect = oxygen8Label.get_rect(center = (550, (windowHeight // 2) - 200))
    screen.blit(oxygen8Label, oxygen8LabelRect)

#Main loop here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #These lines load the molecule with respect to the values extracted from the launcher
    if selectedMolecule == "Carbon Dioxide (CO₂)":
        sphericalCarbonDioxideMolecule()
        lewisCarbonDioxideMolecule()
        sphericalRepresentationLabel = titleFont.render(f"Spherical Representation", True, whiteColor)
        lewisRepresentationLabel = titleFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(sphericalRepresentationLabel, (80, 370))
        screen.blit(lewisRepresentationLabel, (690, 370))
    elif selectedMolecule == "Glucose (C₆H₁₂O₆)":
        lewisGlucoseMolecule()
        lewisRepresentationLabel = regularFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(lewisRepresentationLabel, (20, 75))
    elif selectedMolecule == "Ethanol (C₂H₅OH)":
        lewisEthanolMolecule()
        lewisRepresentationLabel = regularFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(lewisRepresentationLabel, (20, 75))
    elif selectedMolecule == "Acetone (C₃H₆O)":
        lewisAcetoneMolecule()
        lewisRepresentationLabel = regularFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(lewisRepresentationLabel, (20, 75))
    elif selectedMolecule == "Methanol (CH₃OH)":
        lewisMethanolMolecule()
        lewisRepresentationLabel = regularFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(lewisRepresentationLabel, (20, 75))
    elif selectedMolecule == "Formaldehyde (CH₂O)":
        lewisFormaldehydeMolecule()
        lewisRepresentationLabel = regularFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(lewisRepresentationLabel, (20, 75))
    else:
        lewisGlucoseMolecule()
        lewisRepresentationLabel = regularFont.render(f"Lewis Representation", True, whiteColor)
        screen.blit(lewisRepresentationLabel, (20, 75))

    #Title, selected molecule and FPS labels
    upperLabel = titleFont.render("Molecular Lab", True, whiteColor)
    simulatedLabel = regularFont.render(f"Molecule: {moleculeScreenName}", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #Adds said labels to the screen
    screen.blit(upperLabel, (20, 20))
    screen.blit(simulatedLabel, (20, 50))
    screen.blit(fpsLabel, (1030, 20))

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)