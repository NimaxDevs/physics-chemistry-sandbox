import pygame
import math
from random import randint, gauss
from sys import exit

windowWidth = 1100
windowHeight = 580
frameRate = 60

pygame.init()
screen  = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Temperature Simulation")
clock = pygame.time.Clock()
pygame.font.init()

titleFont = pygame.font.Font(None, 30)
regularFont = pygame.font.Font(None, 20)
backgroundColor = (43, 45, 47)
particleColor = (134, 141, 145)
coldColor = (0, 0, 255)
heatColor = (255, 0, 0)
whiteColor = (255, 255, 255)

particlesList_x = []
particlesList_y = []

sizeFactor = 3e11
initParticleNumber = 1000
initParticleDiameter = 5
initTemperature = 20
diffusionCoef = 0.0
boltzmannConstant = 1.380649e-23
initDynamicViscosity = 1e1
particleColor = coldColor

t = 0
dt = 0.1

def createParticles():
    global particlesList_x
    global particlesList_y
    for i in range(initParticleNumber):
        particlesList_x.append((randint(10, 1090)))
        particlesList_y.append(randint(10, 570))

def updateViscosity(initTemperatureKelvin):
    referenceAirViscosity = 1.716e-5
    referenceTemp = 273.15
    sutherlandConstant = 110.4 #For air

    viscosity = referenceAirViscosity * ((initTemperatureKelvin / referenceTemp) ** 1.5) * ((referenceTemp + sutherlandConstant) / (initTemperatureKelvin + sutherlandConstant))
    
    return viscosity

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

def brownianMovement():
    meanSqrt = math.sqrt(2 * diffusionCoef * dt)
    for i in range(len(particlesList_x)):
        Z_x = gauss(0, 1)
        Z_y = gauss(0, 1)
        particlesList_x[i] += meanSqrt * Z_x
        particlesList_y[i] += meanSqrt * Z_y
        pygame.draw.circle(screen, particleColor, (int(particlesList_x[i]), int(particlesList_y[i])), initParticleDiameter)

createParticles()
updateDiffusionCoef()

while True:
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

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

    if initTemperatureUpdate == True:
        updateDiffusionCoef()

    brownianMovement()
    
    upperLabel = titleFont.render("Simulating Temperature", True, whiteColor)
    instructionsLabel = regularFont.render("Click on [UP ARROW] to increase the temperature or [DOWN ARROW] to decrease it", True, whiteColor)
    particleNumberLabel = regularFont.render(f"Number Of Particles: {initParticleNumber}", True, whiteColor)
    particleDiameterLabel = regularFont.render(f"Particle Diameter: {initParticleDiameter:.1f} µm", True, whiteColor)
    initTemperatureLabel = regularFont.render(f"Temperature (°C): {initTemperature:.1f}°C", True, whiteColor)
    initTemperatureKelvinsLabel = regularFont.render(f"Temperature (°K): {initTemperature + 273.15:.1f}°K", True, whiteColor)

    screen.blit(upperLabel, (20, 20))
    screen.blit(instructionsLabel, (20, 45))
    screen.blit(particleNumberLabel, (20, 75))
    screen.blit(particleDiameterLabel, (20, 100))
    screen.blit(initTemperatureLabel, (20, 125))
    screen.blit(initTemperatureKelvinsLabel, (20, 150))
    
    t += dt

    pygame.display.update()
    clock.tick(frameRate)