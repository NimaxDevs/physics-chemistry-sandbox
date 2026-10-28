import pygame
import math
from sys import exit

windowWidth = 1100
windowHeight = 580
frameRate = 60

pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Molecular Lab")
clock = pygame.time.Clock()
pygame.font.init()

titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
lewisLineColor = (99, 113, 123)
lightBlueColor = (3, 165, 252)
lightGrayColor = (148, 148, 148)
greenColor = (0, 204, 24)
blackColor = (0, 0, 0)
darkBlue = (0, 27, 204)
darkGrayColor = (77, 77, 77)
darkGreenColor = (0, 94, 19)
redColor = (255, 0, 0)
darkRedColor = (150, 0, 0)
pinkColor = (255, 194, 194)
whiteColor = (255, 255, 255)

carbonAtomRadius = 40
hydrogenAtomRadius = 30
oxygenAtomRadius = 35
hydrogenAtomColor = lightBlueColor
carbonAtomColor = blackColor
oxygenAtomColor = redColor

carbonAtomPos_x = 200
lewisSingleConnexionLineThickness = 5
lewisDoubleConnexionLineThickness = 15

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


        

while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #sphericalCarbonDioxideMolecule()
    #lewisCarbonDioxideMolecule()
    #lewisGlucoseMolecule()
    #lewisEthanolMolecule()
    #lewisAcetoneMolecule()
    #lewisMethanolMolecule()
    lewisFormaldehydeMolecule()

    pygame.display.update()
    clock.tick(frameRate)