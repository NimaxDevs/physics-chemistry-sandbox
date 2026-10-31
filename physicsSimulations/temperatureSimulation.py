import pygame
import math
from random import randint, gauss
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
screen  = pygame.display.set_mode((windowWidth, windowHeight), flags, vsync = vsyncActivated)
pygame.display.set_caption("Temperature Simulation")
clock = pygame.time.Clock()
pygame.font.init()

#Sets the font of the simulation labels
titleFontPath = "fonts/segoeuib.ttf"
regularFontPath = "fonts/segoeui.ttf"

#Defines the "art" variables
titleFont = pygame.font.Font(ressource_path(titleFontPath), 25)
regularFont = pygame.font.Font(ressource_path(regularFontPath), 15)
backgroundColor = (43, 45, 47)
particleColor = (134, 141, 145)
coldColor = (0, 0, 255)
heatColor = (255, 0, 0)
whiteColor = (255, 255, 255)

#Defines some lists to store the positions (x, y) of the simulated particles
particlesList_x = []
particlesList_y = []

#Defines some simulation variables
sizeFactor = 3e11
initParticleNumber = 50
initParticleDiameter = 5
initTemperature = 30.0
diffusionCoef = 0.0
boltzmannConstant = 1.380649e-23
initDynamicViscosity = 1e1
particleColor = coldColor

#Extracts the values selected from the launcher simulation configuration tab
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(simulationConfigValuesPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        values = json.load(f)
        if values.get("simulationID") == "temperatureSimulation":
            initParticleNumber = int(values.get("initParticleNumber", 50))
            initParticleDiameter = int(values.get("initParticleDiameter", 5))
            initTemperature = float(values.get("initTemperature", 30.0))
        else:
            initParticleNumber = 1000
            initParticleDiameter = 5
            initTemperature = 30.0
else:
    initParticleNumber = 1000
    initParticleDiameter = 5
    initTemperature = 30.0

#Defines some simulation control variables
t = 0
dt = 0.1

#Function to create the simulated particle initial positions by adding them to their respective x and y lists
def createParticles():
    global particlesList_x
    global particlesList_y
    for i in range(initParticleNumber):
        particlesList_x.append((randint(10, 1090)))
        particlesList_y.append(randint(10, 570))

#Function to update the viscosity of the virtual air dynamically on the screen by using Sutherland's Law for gases (in this case, air) by taking into account a reference air viscosity, temperature (constant) as well as Sutherland's constant for air
def updateViscosity(initTemperatureKelvin):
    referenceAirViscosity = 1.716e-5
    referenceTemp = 273.15
    sutherlandConstant = 110.4 #For air

    viscosity = referenceAirViscosity * ((initTemperatureKelvin / referenceTemp) ** 1.5) * ((referenceTemp + sutherlandConstant) / (initTemperatureKelvin + sutherlandConstant))
    
    return viscosity

#Function to update the diffusion coefficient of the particles by getting the current viscosity (using the function above), defining a "safe" check (Sutherland's Law tends to break when reaching absolute zero: in fact, the viscosity reaches a minimum then starts increasing very fast) then calculating the absolute temperature in order to use their results to calculate the real diffusion coefficient (physical) by using Stokes-Einstein equation then converting it to the screen's scale
def updateDiffusionCoef():
    global diffusionCoef
    
    initTemperatureKelvin = initTemperature + 273.15
    if initTemperatureKelvin <= 300:
        dampingFactor = max(0.0, initTemperatureKelvin / 90.0)
        diffusionCoef = 0.2 * dampingFactor
        return diffusionCoef

    currentViscosity = updateViscosity(initTemperatureKelvin)
    
    absoluteTemp = initTemperature + 273.15
    realDiffusionCoef = (boltzmannConstant * absoluteTemp) / (6 * math.pi * currentViscosity * ((initParticleDiameter / 2)) * 1e-6)
    diffusionCoef = realDiffusionCoef * sizeFactor
    
    return diffusionCoef

#Function to calculate Brownian Motion for the particles (random jitter by using Standard Normal Distribution) based on the diffusion coefficient calculated by the function above
def brownianMotion():
    meanSqrt = math.sqrt(2 * diffusionCoef * dt)
    for i in range(len(particlesList_x)):
        Z_x = gauss(0, 1)
        Z_y = gauss(0, 1)
        particlesList_x[i] += meanSqrt * Z_x
        particlesList_y[i] += meanSqrt * Z_y
        pygame.draw.circle(screen, particleColor, (int(particlesList_x[i]), int(particlesList_y[i])), initParticleDiameter)

#These lines create the particles with the functions mentioned above and update the diffusion coefficient by using the calculations defined on the previous function
createParticles()
updateDiffusionCoef()

#Main loop here
while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Checks if the up and down arrow keys are pressed to increase or decrease the simulation temperature
    keys = pygame.key.get_pressed()
    initTemperatureUpdate = False
    if keys[pygame.K_UP]:
        if initTemperature < 1500:
            initTemperature += 1.0
            initTemperatureUpdate = True
        else:
            initTemperatureUpdate = False

    if keys[pygame.K_DOWN]:
        if initTemperature > -273.0:
            initTemperature -= 1.0
            initTemperatureUpdate = True
        else:
            updateDiffusionCoef()
            initTemperatureUpdate = False

    #Updates the diffusion coefficient only if the temperature is increased or decreased by the user for better performance (the diffusion coefficient calculation contains operations that need significant processing power if repeated every frame such as the math.sqrt() function)
    if initTemperatureUpdate == True:
        updateDiffusionCoef()

    #Updates the position of the particles with the function generating Brownian Motion
    brownianMotion()

    #Creates labels describing some simulation informations (title, instructions, etc...)
    upperLabel = titleFont.render("Simulating Temperature", True, whiteColor)
    instructionsLabel = regularFont.render("Click on [UP ARROW] to increase the temperature or [DOWN ARROW] to decrease it", True, whiteColor)
    particleNumberLabel = regularFont.render(f"Number Of Particles: {initParticleNumber}", True, whiteColor)
    particleDiameterLabel = regularFont.render(f"Particle Diameter: {initParticleDiameter:.1f} µm", True, whiteColor)
    initTemperatureLabel = regularFont.render(f"Temperature (°C): {initTemperature:.1f}°C", True, whiteColor)
    initTemperatureKelvinsLabel = regularFont.render(f"Temperature (°K): {initTemperature + 273.15:.1f}°K", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)

    #Adds said labels to the screen
    screen.blit(upperLabel, (20, 15))
    screen.blit(instructionsLabel, (20, 45))
    screen.blit(particleNumberLabel, (20, 75))
    screen.blit(particleDiameterLabel, (20, 100))
    screen.blit(initTemperatureLabel, (20, 125))
    screen.blit(initTemperatureKelvinsLabel, (20, 150))
    screen.blit(fpsLabel, (1030, 20))

    #Updates the time variable with a time step for Euler's Method
    t += dt

    #Updates the screen and clock
    pygame.display.update()
    clock.tick(frameRate)