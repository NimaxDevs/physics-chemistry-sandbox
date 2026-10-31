import pygame
import math
from random import randint
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

#These lines define the window variables
frameRate = 60
vsyncActivated = 0
flags = pygame.SCALED
windowWidth = 1100
windowHeight = 580
if os.path.exists("images/icons/png/launcherIcon.png"):
    iconSurface = pygame.image.load("images/icons/png/launcherIcon.png")
    pygame.display.set_icon(iconSurface)

#While these lines extract settings from the launcher
launcherSettingsPath = os.path.join ("launcherSettings", "launcherSettings.json")
if os.path.exists(launcherSettingsPath) and os.path.getsize(launcherSettingsPath) > 0:
    with open("launcherSettings/launcherSettings.json", "r") as f:
        launcherSettings = json.load(f)
        frameRate = launcherSettings.get("fpsCap")
        vsyncActivated = launcherSettings.get("vsyncActivated")
else:
    frameRate = 60
    vsyncActivated = 0

#These lines initialize the Pygame window (screen) and change some of its properties (title) as well as the clock
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight), flags, vsync = vsyncActivated)
pygame.display.set_caption("Planet Orbits Simulation (N-body problem solver)")
clock = pygame.time.Clock()
pygame.font.init()

#Sets the font of the simulation labels
titleFontPath = "fonts/segoeuib.ttf"
regularFontPath = "fonts/segoeui.ttf"

#These lines define the "art" variables
titleFont = pygame.font.Font(ressource_path(titleFontPath), 25)
regularFont = pygame.font.Font(ressource_path(regularFontPath), 15)
planetNameFont = pygame.font.Font(ressource_path(regularFontPath), 10)
whiteColor = (255, 255, 255)
blackColor = (0, 0, 0)

#And these lines define some lists concerning the planets (planets themselves and the points plotted by their orbit)
planetGlobalRadius = 50
planets = []
orbitTrailPoints = []
selectedPlanet = None #However, this line defines a state variable that checks if a planet has been selected with the mouse to show its properties
planetMass = 0
planetRadius = 0

#These lines define the values of some physical properties (universal gravitational constant) as well as a scale factor for the planet distances
scaleFactor = 500e6 #500 000 000 meters correspond to 1 pixel
G = 6.674e-11

#These lines define some simulation control variables
t = 0
dt = 3600*200

#"Why didn't you use OOP-" no OOP for this project; this function creates the planets based on a dictionary whose key values are the configurator values of the launcher
def planetCreation(name, color, mass, radius, x, y, vx, vy, ax, ay, showOrbitTrail, showPlanetName):
    planet = {
        "Name": name,
        "Color": color,
        "Mass": mass,
        "Radius": radius,
        "x": x,
        "y": y,
        "vx": vx,
        "vy": vy,
        "ax": ax,
        "ay": ay,
        "showOrbitTrail": showOrbitTrail,
        "showPlanetName": showPlanetName,
        "screenRadius": planetGlobalRadius #This line defines the radius of the planet shown on the screen (hence screen radius) by using the value returned by the "screenRadius" function
    }
    
    return planet

#These lines extract the values from the configuration tab of this simulation in the launcher while applying data checks, conversions and planning cases
simulationConfigValuesPath = os.path.join ("simulationConfigValues", "simulationConfigValues.json")
if os.path.exists(simulationConfigValuesPath) and os.path.getsize(simulationConfigValuesPath) > 0:
    with open("simulationConfigValues/simulationConfigValues.json", "r") as f:
        configValues = json.load(f)
        if configValues.get("simulationID") == "planetOrbitsSimulation":
            planetConfigValues = configValues.get("planets", [])
            for planet in planetConfigValues:
                rawColor = planet.get("planetColor", ("255, 255, 255"))
                rawColorParts = rawColor.replace(" ", "").split(",")
                if len(rawColorParts) == 3 and rawColorParts[0].isdigit() and rawColorParts[1].isdigit() and rawColorParts[2].isdigit():
                    if 0 <= int(rawColorParts[0]) <= 255 and 0 <= int(rawColorParts[1]) <= 255 and 0 <= int(rawColorParts[2]) <= 255:
                        cleanColor = (int(rawColorParts[0]), int(rawColorParts[1]), int(rawColorParts[2]))
                else:
                    cleanColor = (255, 255, 255)

                rawMassStr = planet.get("planetMass", "10000000000000000000000000")
                if rawMassStr.replace(".", "", 1).isdigit() != True:
                        planetMass = 1e25
                else:
                    planetMass = float(rawMassStr)
                    if planetMass > 1e30:
                        planetMass = 1e30
                
                rawRadiusStr = planet.get("planetRadius", "5000000")
                if rawRadiusStr.replace(".", "", 1).isdigit() != True or len(rawRadiusStr.strip()) == 0:
                    planetRadius = 5e6
                else:
                    planetRadius = float(rawRadiusStr)
                    if planetRadius > 70e6: 
                        planetRadius = 70e6

                currentPlanetName = planet.get("planetName", "Unknown")
                if len(currentPlanetName.strip()) == 0:
                    currentPlanetName = "Unknown"
                
                createdPlanet = planetCreation(
                    currentPlanetName,
                    cleanColor,
                    float(planetMass),
                    float(planetRadius),
                    randint(10, 1090) * scaleFactor,
                    randint(10, 570) * scaleFactor,
                    float(planet.get("initVx", 0)),
                    float(planet.get("initVy", 0)),
                    float(planet.get("initAx", 0)),
                    float(planet.get("initAy", 0)),
                    planet.get("showOrbitTrail"),
                    planet.get("showPlanetName")
                )
                planets.append(createdPlanet)
        else:
            planets = []
else:
    planets = []

#This function solves the N-body problem to simulate more than two bodies interacting upon each other
def NBodyProblemSolver(planets):
    #Resets the acceleration components of each planet using a for loop
    for planet in planets:
        planet["ax"] = 0
        planet["ay"] = 0

    #This nested for loop runs through the "planets" list to solve the N-body problem
    for i in range(len(planets)):
        planet.setdefault("F", [])
        for j in range(i + 1, len(planets)):
            planet.setdefault("F", [])
            dx = planets[j]["x"]-planets[i]["x"] #Calculates delta x (x distance between the planets of each loop)
            dy = planets[j]["y"]-planets[i]["y"] #Calculates delta y (y distance between the planets of each loop)
            r = math.sqrt(dx**2+dy**2) #Calculates the distance between the planets of each loop
            if r == 0:
                r = 0.1
            ux = dx / r #Calculates the x unit vector of the planets of each loop
            uy = dy / r#Calculates the y unit vector of the planets of each loop
            planets[i]["F"] = (G*planets[i]["Mass"]*planets[j]["Mass"]/r**2) #Calculates the magnitude of the force vector using Newton's Law of Universal Gravitation
            planets[j]["F"] = planets[i]["F"] #Same thing for the planet of the second loop (even if they are equal)
            planets[i]["ax"] += (planets[i]["F"] / planets[i]["Mass"]) * ux #Creates the acceleration vector of the planets of the first loop (broken down into the x component)
            planets[i]["ay"] += (planets[i]["F"] / planets[i]["Mass"]) * uy #And y component
            planets[j]["ax"] += -((planets[j]["F"] / planets[j]["Mass"]) * ux) #Same thing here for the planets of the second loop (x)
            planets[j]["ay"] += -((planets[j]["F"] / planets[j]["Mass"]) * uy) #And here (y)

#As the name of the function suggests, its purpose is to update the velocities of each planet of the "planets" list as well as their position using Euler's Method to integrate their values numerically
def eulerIntegrator(planet):
    planet["vx"] += (planet["ax"] * dt)          
    planet["vy"] += (planet["ay"] * dt) 
    planet["x"] += (planet["vx"] * dt)          
    planet["y"] += (planet["vy"] * dt)

#I think that the name of this function is pretty explanatory
def drawPlanets(planet):
    planet.setdefault("Trail", []) #Creates a "Trail" key in the "planet" dictionary
    
    #Checks if the "showOrbitTrail" option is chosen in the launcher; if so, then it does what it says
    if planet["showOrbitTrail"] == True:
        planet["Trail"].append((planet["x"] / scaleFactor, planet["y"] / scaleFactor)) #Adds the points plotted by the planets which have the option activated to the "Trail" key (it works like a list)
    
    #Removes the orbit trail points if there is too many of them (to keep the simulation smooth)
    if len(planet["Trail"]) > 100:
        planet["Trail"].pop(0)

    #Draws the orbit trail (points plotted by the planets orbit) to the screen (window)
    for point in planet["Trail"]:
        pygame.draw.circle(screen, planet["Color"], point, 1)

    #Draws the planets based on their configurator values (the keys of the dictionary: still no OOP)
    pygame.draw.circle(screen, planet["Color"], (planet["x"] / scaleFactor, planet["y"] / scaleFactor), planet["screenRadius"])

    #Checks if the "showPlanetName" option is chosen in the launcher; if so, then it creates a surface label of the planet name then adds it to the screen
    if planet["showPlanetName"] == True:
        planetName = planetNameFont.render(planet["Name"], True, whiteColor)
        planetNameRect = planetName.get_rect(center = (planet["x"] / scaleFactor, (planet["y"] / scaleFactor) - planet["screenRadius"] - 10)) #Creates a rectangle to position the text easily
        screen.blit(planetName, planetNameRect)

#The main loop runs here
while True:
    screen.fill(blackColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #These lines check if the mouse presses a planet
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                selectedPlanet = None #Resets the "selectedPlanet" variable because it is checked on the main loop (so every frame)
                pos = pygame.Vector2(pygame.mouse.get_pos()) #Gets the position of the mouse
                for planet in planets:
                    planetCenter = pygame.Vector2(planet["x"] / scaleFactor, planet["y"] / scaleFactor) #Gets the coordinates (in pixels) of the planet centers
                    if planetCenter.distance_to(pos) < planet["screenRadius"]: #Calculates the 2D euclidian distance separating the planet center and the mouse (position) and compares it to the planet radius to check if the mouse is colliding with the planets
                        selectedPlanet = planet #Sets the "selectedPlanet" variable to the planet selected with the mouse
                        break

    #Runs the N-body problem solver
    NBodyProblemSolver(planets)

    #Integrates the values from the N-body problem for each planet of the "planets" list using the "eulerIntegrator" function
    for planet in planets:
        eulerIntegrator(planet)

    #Draws each planet from the "planets" list
    for planet in planets:
        drawPlanets(planet)

    #Shows the values of the physical properties of a planet if it is selected with the mouse
    if selectedPlanet is not None:
        planetNameLabel = regularFont.render(f"Planet Name: {selectedPlanet['Name']}", True, whiteColor)
        planetMassLabel = regularFont.render(f"Planet Mass: {selectedPlanet['Mass']} kg", True, whiteColor)
        planetRadiusLabel = regularFont.render(f"Planet Radius: {selectedPlanet['Radius']} m", True, whiteColor)
        planetVxLabel = regularFont.render(f"vx: {selectedPlanet['vx']:.5f} m/s", True, whiteColor)
        planetVyLabel = regularFont.render(f"vy: {selectedPlanet['vy']:.5f} m/s", True, whiteColor)
        planetAxLabel = regularFont.render(f"ax: {selectedPlanet['ax']:.10f} m/s²", True, whiteColor)
        planetAyLabel = regularFont.render(f"ay: {selectedPlanet['ay']:.10f} m/s²", True, whiteColor)
        #These lines add the text labels to the screen
        screen.blit(planetNameLabel, (20, 75))
        screen.blit(planetMassLabel, (20, 100))
        screen.blit(planetRadiusLabel, (20, 125))
        screen.blit(planetVxLabel, (20, 150))
        screen.blit(planetVyLabel, (20, 175))
        screen.blit(planetAxLabel, (20, 200))
        screen.blit(planetAyLabel, (20, 225))
    
    #Updates the simulation time by using a predefined time step for the Euler Method
    t += dt

    #These lines add the text labels of the simulation title as well as the instructions on how to use the simulator to the screen
    upperLabel = titleFont.render("Simulating Planet Orbits", True, whiteColor)
    instructionsLabel = regularFont.render("Click on one of the planets to see their physical values", True, whiteColor)
    fpsLabel = regularFont.render(f"FPS: {int(clock.get_fps())}", True, whiteColor)
    screen.blit(upperLabel, (20, 20))
    screen.blit(instructionsLabel, (20, 45))
    screen.blit(fpsLabel, (1030, 20))

    #And finally, these lines update the screen
    pygame.display.update()
    clock.tick(frameRate)