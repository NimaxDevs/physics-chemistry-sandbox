#Do I even have to describe these lines
import customtkinter, tkinter
from tkinter import * 
from PIL import Image, ImageDraw
import webbrowser
import json
import os
import subprocess
from pygame import mixer
import time

#The CTk appearance settings go here
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("themes/rime.json")

#The CTk settings go here
app = customtkinter.CTk()
app.geometry("1100x580")
app.resizable(False, False)
app.title("Physics & Chemistry Sandbox Launcher")
if os.path.exists("images/icons/launcherIcon.ico"):
    app.iconbitmap("images/icons/launcherIcon.ico")

#This line initializes the Pygame mixer for the launcher UI sounds
mixer.init()

#These lines define some variables to control the functions creating those sounds
buttonClick = 0
buttonHover = 0
lastHoverTime = 0
hoverCooldown = 0.3

#Function to add rounded corners to CustomTkinter images (not by default so uses the ImageDraw module from the Pillow library)
def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

#Function to create the sounds when clicking on the launcher buttons and arrange them into a simple melody
def buttonClickSound(variable):
    global buttonClick
    if variable == 1:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick1.mp3"):
            buttonClickSound1Path = "sounds/ui/buttonClicks/buttonClick1.mp3"
            buttonClickSound1 = mixer.Sound(buttonClickSound1Path)
            mixer.Channel(0).play(buttonClickSound1)
    if variable == 2:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick2.mp3"):
            buttonClickSound2Path = "sounds/ui/buttonClicks/buttonClick2.mp3"
            buttonClickSound2 = mixer.Sound(buttonClickSound2Path)
            mixer.Channel(0).play(buttonClickSound2)
    if variable == 3:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick3.mp3"):
            buttonClickSound3Path = "sounds/ui/buttonClicks/buttonClick3.mp3"
            buttonClickSound3 = mixer.Sound(buttonClickSound3Path)
            mixer.Channel(0).play(buttonClickSound3)
    if variable == 4:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick4.mp3"):
            buttonClickSound4Path = "sounds/ui/buttonClicks/buttonClick4.mp3"
            buttonClickSound4 = mixer.Sound(buttonClickSound4Path)
            mixer.Channel(0).play(buttonClickSound4)
    if variable == 5:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick1.mp3"):
            buttonClickSound1Path = "sounds/ui/buttonClicks/buttonClick1.mp3"
            buttonClickSound1 = mixer.Sound(buttonClickSound1Path)
            mixer.Channel(0).play(buttonClickSound1)
    if variable == 6:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick2.mp3"):
            buttonClickSound2Path = "sounds/ui/buttonClicks/buttonClick2.mp3"
            buttonClickSound2 = mixer.Sound(buttonClickSound2Path)
            mixer.Channel(0).play(buttonClickSound2)
    if variable == 7:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick3.mp3"):
            buttonClickSound3Path = "sounds/ui/buttonClicks/buttonClick3.mp3"
            buttonClickSound3 = mixer.Sound(buttonClickSound3Path)
            mixer.Channel(0).play(buttonClickSound3)
    if variable == 8:
        if os.path.exists("sounds/ui/buttonClicks/buttonClick5.mp3"):
            buttonClickSound5Path = "sounds/ui/buttonClicks/buttonClick5.mp3"
            buttonClickSound5 = mixer.Sound("sounds/ui/buttonClicks/buttonClick5.mp3")
            mixer.Channel(0).play(buttonClickSound5)
        buttonClick = 0

#Function to create the sounds when hovering the launcher buttons and arrange them into a simple melody
def buttonHoverSound(variable):
    global buttonHover
    if variable == 1:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover1.mp3"):
            buttonHoverSound1Path = "sounds/ui/buttonHovers/buttonHover1.mp3"
            buttonHoverSound1 = mixer.Sound(buttonHoverSound1Path)
            mixer.Channel(1).play(buttonHoverSound1)
    if variable == 2:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover2.mp3"):
            buttonHoverSound2Path = "sounds/ui/buttonHovers/buttonHover2.mp3"
            buttonHoverSound2 = mixer.Sound("sounds/ui/buttonHovers/buttonHover2.mp3")
            mixer.Channel(1).play(buttonHoverSound2)
    if variable == 3:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover1.mp3"):
            buttonHoverSound1Path = "sounds/ui/buttonHovers/buttonHover1.mp3"
            buttonHoverSound1 = mixer.Sound(buttonHoverSound1Path)
            mixer.Channel(1).play(buttonHoverSound1)
    if variable == 4:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover2.mp3"):
            buttonHoverSound2Path = "sounds/ui/buttonHovers/buttonHover2.mp3"
            buttonHoverSound2 = mixer.Sound("sounds/ui/buttonHovers/buttonHover2.mp3")
            mixer.Channel(1).play(buttonHoverSound2)
    if variable == 5:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover3.mp3"):
            buttonHoverSound3Path = "sounds/ui/buttonHovers/buttonHover3.mp3"
            buttonHoverSound3 = mixer.Sound(buttonHoverSound3Path)
            mixer.Channel(1).play(buttonHoverSound3)
    if variable == 6:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover4.mp3"):
            buttonHoverSound4Path = "sounds/ui/buttonHovers/buttonHover4.mp3"
            buttonHoverSound4 = mixer.Sound(buttonHoverSound4Path)
            mixer.Channel(1).play(buttonHoverSound4)
    if variable == 7:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover5.mp3"):
            buttonHoverSound5Path = "sounds/ui/buttonHovers/buttonHover5.mp3"
            buttonHoverSound5 = mixer.Sound(buttonHoverSound5Path)
            mixer.Channel(1).play(buttonHoverSound5)
    if variable == 8:
        if os.path.exists("sounds/ui/buttonHovers/buttonHover6.mp3"):
            buttonHoverSound6Path = "sounds/ui/buttonHovers/buttonHover6.mp3"
            buttonHoverSound6 = mixer.Sound(buttonHoverSound6Path)
            mixer.Channel(1).play(buttonHoverSound6)
        buttonHover = 0

#Function to play the sounds when hovering the launcher buttons
def onButtonHover(value):
    global buttonHover, lastHoverTime
    currentTime = time.time()
    if currentTime - lastHoverTime < hoverCooldown:
        return

    lastHoverTime = currentTime
    buttonHover += 1
    buttonHoverSound(buttonHover)

#These lines define the thumbnail images for the physics simulations (those seen when selecting the physics simulation tab)
placeholderImage = customtkinter.CTkImage(light_image = Image.open("images/placeholders/atom_image.png"),
                                          dark_image = Image.open("images/placeholders/atom_image.png"),
                                          size = (150, 100))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_projectileSimulation.jpg"):
    projectileSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_projectileSimulation.jpg"
else:
    projectileSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
projectileSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(projectileSimulationThumbnailImagePath), 50),
                                          dark_image = add_corners(Image.open(projectileSimulationThumbnailImagePath), 50),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_pendulumSimulation.jpg"):
    pendulumSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_pendulumSimulation.jpg"
else:
    pendulumSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
pendulumSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(pendulumSimulationThumbnailImagePath), 150),
                                          dark_image = add_corners(Image.open(pendulumSimulationThumbnailImagePath), 150),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_springSimulation.jpg"):
    springSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_springSimulation.jpg"
else:
    springSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
springSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(springSimulationThumbnailImagePath), 50),
                                          dark_image = add_corners(Image.open(springSimulationThumbnailImagePath), 50),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_planetOrbitsSimulation.png"):
    planetOrbitsSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_planetOrbitsSimulation.png"
else:
    planetOrbitsSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
planetOrbitsSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(planetOrbitsSimulationThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(planetOrbitsSimulationThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_gravitySimulation.png"):
    gravitySimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_gravitySimulation.png"
else:
    gravitySimulationThumbnailImagePath = "images/placeholders/atom_image.png"
gravitySimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(gravitySimulationThumbnailImagePath), 50),
                                          dark_image = add_corners(Image.open(gravitySimulationThumbnailImagePath), 50),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_refractionSimulation.png"):
    refractionSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_refractionSimulation.png"
else:
    refractionSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
refractionSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(refractionSimulationThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(refractionSimulationThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_fluidSimulation.jpg"):
    fluidSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_fluidSimulation.jpg"
else:
    fluidSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
fluidSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(fluidSimulationThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(fluidSimulationThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/physicsSimulations/thumbnail_temperatureSimulation.jpg"):
    temperatureSimulationThumbnailImagePath = "images/thumbnails/physicsSimulations/thumbnail_temperatureSimulation.jpg"
else:
    temperatureSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
temperatureSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(temperatureSimulationThumbnailImagePath), 150),
                                          dark_image = add_corners(Image.open(temperatureSimulationThumbnailImagePath), 150),
                                          size = (190, 125))

#These lines define the simulation preview images for each simulation (those seen on the simulation configuration tabs)
if os.path.exists("images/previews/physicsSimulations/preview_projectileSimulation.png"):
    projectileSimulationPreviewImagePath = "images/previews/physicsSimulations/preview_projectileSimulation.png"
else:
    projectileSimulationPreviewImagePath = "images/placeholders/atom_image.png"
projectileSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(projectileSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(projectileSimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/physicsSimulations/preview_pendulumSimulation.png"):
    pendulumSimulationPreviewImagePath = "images/previews/physicsSimulations/preview_pendulumSimulation.png"
else:
    pendulumSimulationPreviewImagePath = "images/placeholders/atom_image.png"
pendulumSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(pendulumSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(pendulumSimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/physicsSimulations/preview_springSimulation.png"):
    springSimulationPreviewImagePath = "images/previews/physicsSimulations/preview_springSimulation.png"
else:
    springSimulationPreviewImagePath = "images/placeholders/atom_image.png"
springSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(springSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(springSimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/physicsSimulations/preview_planetOrbitsSimulation.png"):
    planetOrbitsSimulationPreviewImagePath = "images/previews/physicsSimulations/preview_planetOrbitsSimulation.png"
else:
    planetOrbitsSimulationPreviewImagePath = "images/placeholders/atom_image.png"
planetOrbitsSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(planetOrbitsSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(planetOrbitsSimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/physicsSimulations/preview_gravitySimulation.png"):
    gravitySimulationPreviewImagePath = "images/previews/physicsSimulations/preview_gravitySimulation.png"
else:
    gravitySimulationPreviewImagePath = "images/placeholders/atom_image.png"
gravitySimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(gravitySimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(gravitySimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/physicsSimulations/preview_refractionSimulation.png"):
    refractionSimulationPreviewImagePath = "images/previews/physicsSimulations/preview_refractionSimulation.png"
else:
    refractionSimulationPreviewImagePath = "images/placeholders/atom_image.png"
refractionSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(refractionSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(refractionSimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/physicsSimulations/preview_temperatureSimulation.png"):
    temperatureSimulationPreviewImagePath = "images/previews/physicsSimulations/preview_temperatureSimulation.png"
else:
    temperatureSimulationPreviewImagePath = "images/placeholders/atom_image.png"
temperatureSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(temperatureSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(temperatureSimulationPreviewImagePath), 15),
                                          size = (530, 280))

#These lines also define the thumbnail images for the chemistry simulations (those seen when selecting the chemistry simulation tab)
if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_bohrAtomSimulation.jpg"):
    bohrAtomSimulationThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_bohrAtomSimulation.jpg"
else:
    bohrAtomSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
bohrAtomSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(bohrAtomSimulationThumbnailImagePath), 50),
                                          dark_image = add_corners(Image.open(bohrAtomSimulationThumbnailImagePath), 50),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_solutionMaker.jpg"):
    solutionMakerThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_solutionMaker.jpg"
else:
    solutionMakerThumbnailImagePath = "images/placeholders/atom_image.png"
solutionMakerThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(solutionMakerThumbnailImagePath), 50),
                                          dark_image = add_corners(Image.open(solutionMakerThumbnailImagePath), 50),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_molecularLab.png"):
    molecularLabThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_molecularLab.png"
else:
    molecularLabThumbnailImagePath = "images/placeholders/atom_image.png"
molecularLabThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(molecularLabThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(molecularLabThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_reactionLab.png"):
    reactionLabThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_reactionLab.png"
else:
    reactionLabThumbnailImagePath = "images/placeholders/atom_image.png"
reactionLabThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(reactionLabThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(reactionLabThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_combustionSimulation.png"):
    combustionSimulationThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_combustionSimulation.png"
else:
    combustionSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
combustionSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(combustionSimulationThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(combustionSimulationThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_smokeSimulation.jpg"):
    smokeSimulationThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_smokeSimulation.jpg"
else:
    smokeSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
smokeSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(smokeSimulationThumbnailImagePath), 150),
                                          dark_image = add_corners(Image.open(smokeSimulationThumbnailImagePath), 150),
                                          size = (190, 125))

if os.path.exists("images/thumbnails/chemistrySimulations/thumbnail_atomCollisionSimulation.png"):
    atomCollisionSimulationThumbnailImagePath = "images/thumbnails/chemistrySimulations/thumbnail_atomCollisionSimulation.png"
else:
    atomCollisionSimulationThumbnailImagePath = "images/placeholders/atom_image.png"
atomCollisionSimulationThumbnailImage = customtkinter.CTkImage(light_image = add_corners(Image.open(atomCollisionSimulationThumbnailImagePath), 30),
                                          dark_image = add_corners(Image.open(atomCollisionSimulationThumbnailImagePath), 30),
                                          size = (190, 125))

if os.path.exists("images/previews/chemistrySimulations/preview_bohrAtomSimulation.png"):
    bohrAtomSimulationPreviewImagePath = "images/previews/chemistrySimulations/preview_bohrAtomSimulation.png"
else:
    bohrAtomSimulationPreviewImagePath = "images/placeholders/atom_image.png"
bohrAtomSimulationPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(bohrAtomSimulationPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(bohrAtomSimulationPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/chemistrySimulations/preview_solutionMaker.png"):
    solutionMakerPreviewImagePath = "images/previews/chemistrySimulations/preview_solutionMaker.png"
else:
    solutionMakerPreviewImagePath = "images/placeholders/atom_image.png"
solutionMakerPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(solutionMakerPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(solutionMakerPreviewImagePath), 15),
                                          size = (530, 280))

if os.path.exists("images/previews/chemistrySimulations/preview_molecularLab.png"):
    molecularLabPreviewImagePath = "images/previews/chemistrySimulations/preview_molecularLab.png"
else:
    molecularLabPreviewImagePath = "images/placeholders/atom_image.png"
molecularLabPreviewImage = customtkinter.CTkImage(light_image = add_corners(Image.open(molecularLabPreviewImagePath), 15),
                                          dark_image = add_corners(Image.open(molecularLabPreviewImagePath), 15),
                                          size = (530, 280))

#The main menu state variables go here
physicsTabSelected = False
chemistryTabSelected = False
thePlaceTabSelected = False
launcherSettingsSelected = False
creditsTabSelected = False

#The sub menu state variables go here
##The physics simulation tabs state variables here
projectileSimulationConfigTabSelected = False
pendulumSimulationConfigTabSelected = False
springSimulationConfigTabSelected = False
planetOrbitsSimulationConfigTabSelected = False
gravitySimulationConfigTabSelected = False
refractionSimulationConfigTabSelected = False
fluidSimulationConfigTabSelected = False
temperatureSimulationConfigTabSelected = False

##The chemistry simulation tabs state variables here
bohrAtomSimulationConfigTabSelected = False
solutionMakerConfigTabSelected = False
molecularLabConfigTabSelected = False
reactionLabConfigTabSelected = False
combustionSimulationConfigTabSelected = False
smokeSimulationConfigTabSelected = False
atomCollisionSimulationTabSelected = False

#The variables (default slider, checkbox, option menus, etc...) of the configuration tabs are here
##The variables for the physics simulations go here
###The variables of the Projectile Simulation go here
projectileSimulationConfigTabInitAirResistCheckboxVar = tkinter.StringVar(value = "off")
projectileSimulationConfigTabInitVelocitySliderValueVar = tkinter.StringVar(value = "")
projectileSimulationConfigTabInitAngleSliderValueVar = tkinter.StringVar(value = "")
projectileSimulationConfigTabInitGravAccSliderValueVar = tkinter.StringVar(value = "")
projectileSimulationConfigTabInitMassSliderValueVar = tkinter.StringVar(value = "")
projectileSimulationConfigTabInitDiameterSliderValueVar = tkinter.StringVar(value = "")
projectileSimulationConfigTabInitDragCoefSliderValueVar = tkinter.StringVar(value = "")

###The variables of the Pendulum Simulation go here
pendulumSimulationConfigTabInitAngleSliderValueVar = tkinter.StringVar(value = "")
pendulumSimulationConfigTabInitAngularVelSliderValueVar = tkinter.StringVar(value = "")
pendulumSimulationConfigTabInitLengthSliderValueVar = tkinter.StringVar(value = "")
pendulumSimulationConfigTabInitMassSliderValueVar = tkinter.StringVar(value = "")
pendulumSimulationConfigTabInitGravAccSliderValueVar = tkinter.StringVar(value = "")
pendulumSimulationConfigTabInitDampingCoefSliderValueVar = tkinter.StringVar(value = "")

###The variables of the Spring Simulation go here
springSimulationConfigTabInitMassSliderValueVar = tkinter.StringVar(value = "")
springSimulationConfigTabInitGravAccSliderValueVar = tkinter.StringVar(value = "")
springSimulationConfigTabInitLengthSliderValueVar = tkinter.StringVar(value = "")
springSimulationConfigTabInitStiffSliderValueVar = tkinter.StringVar(value = "")
springSimulationConfigTabInitDampingCoefSliderValueVar = tkinter.StringVar(value = "")

###The variables of the Planet Orbits go here
planetConfigValuesList = []
planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabPlanetInitialVySliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabPlanetInitialAySliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabShowOrbitTrailSwitchVar = tkinter.StringVar(value = False)
planetOrbitsSimulationConfigTabShowPlanetNameSwitchVar = tkinter.StringVar(value = False)
planetNumber = 0

###The variables of the Gravity Simulation go here
gravitySimulationConfigTabInitMassSliderValueVar = tkinter.StringVar(value = "")
gravitySimulationConfigTabInitGravAccSliderValueVar = tkinter.StringVar(value = "")
gravitySimulationConfigTabInitHeightSliderValueVar = tkinter.StringVar(value = "")

###The variables of the Refraction Simulation go here
refractionSimulationConfigTabInitRefractiveIndex1OptionMenuVar = tkinter.StringVar(value = "Select Refractive Index 1")
refractionSimulationConfigTabInitRefractiveIndex2OptionMenuVar = tkinter.StringVar(value = "Select Refractive Index 2")
refractionSimulationConfigTabInitIncidenceAngleSliderValueVar = tkinter.StringVar(value = "")
refractionSimulationConfigRayColorOptionMenuVar = tkinter.StringVar(value = "Select Ray Color")

###The variables of the Fluid Simulation go here
fluidSimulationConfigTabInitVolumeSliderValueVar = tkinter.StringVar(value = "")
fluidSimulationConfigInitDensityOptionMenuVar = tkinter.StringVar(value = "Select Density")
fluidSimulationConfigInitViscosityOptionMenuVar = tkinter.StringVar(value = "Select Viscosity")
fluidSimulationConfigTabInitPressureSliderValueVar = tkinter.StringVar(value = "")
fluidSimulationConfigInitColorOptionMenuVar = tkinter.StringVar(value = "Select Color")
fluidSimulationConfigTabShowLatticeSwitchVar = tkinter.StringVar(value = "off")

###The variables of the Temperature Simulation go here
temperatureSimulationConfigTabInitParticleNumberSliderValueVar = tkinter.StringVar(value = "")
temperatureSimulationConfigTabInitParticleDiameterSliderValueVar = tkinter.StringVar(value = "")
temperatureSimulationConfigTabInitTempSliderValueVar = tkinter.StringVar(value = "")

##The variables for the chemistry simulations go here
###The variables of the Bohr Atom Simulation go here
bohrAtomSimulationConfigTabAtomSelectionIndex = 0
bohrAtomSimulationConfigTabAtomSelected = False

###The variables of the Solution Maker go here
solutionMakerConfigTabInitSolventOptionMenuVar = tkinter.StringVar(value = "Select Solvent")
solutionMakerConfigTabInitSolventVolSliderValueVar = tkinter.StringVar(value = "")
solutionMakerConfigTabInitSoluteOptionMenuVar = tkinter.StringVar(value = "Select Solute")
solutionMakerConfigTabInitSoluteMassSliderValueVar = tkinter.StringVar(value = "")

###The variables of the Molecular Lab go here
molecularLabConfigTabInitMoleculeOptionMenuVar = tkinter.StringVar(value = "Select Molecule")
molecularLabConfigTabInitHydrogenColorOptionMenuVar = tkinter.StringVar(value = "Select Color")
molecularLabConfigTabInitCarbonColorOptionMenuVar = tkinter.StringVar(value = "Select Color")
molecularLabConfigTabInitOxygenColorOptionMenuVar = tkinter.StringVar(value = "Select Color")

###The variables of the Launcher Settings tab go here
launcherSettingsFPSCapOptionMenuVar = tkinter.StringVar(value = "60")
launcherSettingsVSyncSwitchEventVar = tkinter.StringVar(value = "0")

#Every button event (functions when pressing the launcher buttons) of the launcher is under these lines
def physicsSelectorButtonEvent():
    global buttonClick
    physicsTabSelected = True
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    physicsTab(physicsTabSelected)
    buttonClick += 1
    buttonClickSound(buttonClick)

def chemistrySelectorButtonEvent():
    global buttonClick
    chemistryTabSelected = True
    physicsTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    chemistryTab(chemistryTabSelected)
    buttonClick += 1
    buttonClickSound(buttonClick)
    
def thePlaceSelectorButtonEvent():
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    thePlaceTabSelected = True
    physicsTabSelected = False
    chemistryTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    thePlaceTab(thePlaceTabSelected)

def launcherSettingsButtonEvent():
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    launcherSettingsSelected = True
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    creditsTabSelected = False
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    launcherSettingsTab(launcherSettingsSelected)

def gitHubButtonEvent():
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    #opens the URL of my GitHub
    webbrowser.open("https://github.com/NimaxDevs/physics-chemistry-sandbox")
    pass

def creditsButtonEvent():
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    creditsTabSelected = True
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    creditsTab(creditsTabSelected)

def quitLauncherButtonEvent():
    launcherQuit = mixer.Sound("sounds/ui/buttonClicks/launcherQuit.mp3")
    mixer.Channel(2).play(launcherQuit)
    quitLauncherButton.after(900, app.quit())

#The buttons to configure the physics simulations are here
def projectileSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    projectileSimulationConfigTabSelected = True
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    projectileSimulationConfigTab(projectileSimulationConfigTabSelected)

def pendulumSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    pendulumSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    pendulumSimulationConfigTab(pendulumSimulationConfigTabSelected)

def springSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    springSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    springSimulationConfigTab(springSimulationConfigTabSelected)

def planetOrbitsSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    planetOrbitsSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()    
    planetOrbitsSimulationConfigTab(planetOrbitsSimulationConfigTabSelected)

def gravitySimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    gravitySimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    gravitySimulationConfigTab(gravitySimulationConfigTabSelected)    

def refractionSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    refractionSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    refractionSimulationConfigTab(refractionSimulationConfigTabSelected)

def fluidSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    fluidSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    fluidSimulationConfigTab(fluidSimulationConfigTabSelected)

def temperatureSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    temperatureSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    temperatureSimulationConfigTab(temperatureSimulationConfigTabSelected)

#The buttons to configure the chemistry simulations are here
def bohrAtomSimulationConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    bohrAtomSimulationConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    bohrAtomSimulationConfigTab(bohrAtomSimulationConfigTabSelected)    

def solutionMakerConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    solutionMakerConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    molecularLabConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    solutionMakerConfigTab(solutionMakerConfigTabSelected)

def molecularLabConfigButtonEvent():
    #Plays a sound when clicked, updates the state variables of the menus and submenus and loads the simulation configuration tab
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    molecularLabConfigTabSelected = True
    projectileSimulationConfigTabSelected = False
    pendulumSimulationConfigTabSelected = False
    springSimulationConfigTabSelected = False
    planetOrbitsSimulationConfigTabSelected = False
    gravitySimulationConfigTabSelected = False
    refractionSimulationConfigTabSelected = False
    fluidSimulationConfigTabSelected = False
    temperatureSimulationConfigTabSelected = False
    bohrAtomSimulationConfigTabSelected = False
    solutionMakerConfigTabSelected = False
    reactionLabConfigTabSelected = False
    combustionSimulationConfigTabSelected = False
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    molecularLabConfigTab(molecularLabConfigTabSelected)

def reactionLabConfigButtonEvent():
    #Plays an error sound when clicked because the simulation has not been implemented yet but checks if the file exists
    if os.path.exists("sounds/ui/buttonClicks/launcherQuit.mp3"):
        errorSoundPath = "sounds/ui/buttonClicks/launcherQuit.mp3"
        errorSound = mixer.Sound(errorSoundPath)
        mixer.Channel(2).play(errorSound)

def combustionSimulationConfigButtonEvent():
    #Plays an error sound when clicked because the simulation has not been implemented yet but checks if the file exists
    if os.path.exists("sounds/ui/buttonClicks/launcherQuit.mp3"):
        errorSoundPath = "sounds/ui/buttonClicks/launcherQuit.mp3"
        errorSound = mixer.Sound(errorSoundPath)
        mixer.Channel(2).play(errorSound)

def smokeSimulationConfigButtonEvent():
    #Plays an error sound when clicked because the simulation has not been implemented yet but checks if the file exists
    if os.path.exists("sounds/ui/buttonClicks/launcherQuit.mp3"):
        errorSoundPath = "sounds/ui/buttonClicks/launcherQuit.mp3"
        errorSound = mixer.Sound(errorSoundPath)
        mixer.Channel(2).play(errorSound)

def atomCollisionSimulationConfigButtonEvent():
    #Plays an error sound when clicked because the simulation has not been implemented yet but checks if the file exists
    if os.path.exists("sounds/ui/buttonClicks/launcherQuit.mp3"):
        errorSoundPath = "sounds/ui/buttonClicks/launcherQuit.mp3"
        errorSound = mixer.Sound(errorSoundPath)
        mixer.Channel(2).play(errorSound)

#The buttons to launch the simulations go here
##The buttons of the physics simulations go here
def projectileSimulationConfigTabLaunchButtonEvent():
    #Plays a sound when clicked
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    configValues = {
                    "simulationID": "projectileSimulation",
                    "initVelocity": int(projectileSimulationConfigTabInitVelocitySlider.get()),
                    "initAngle": int(projectileSimulationConfigTabInitAngleSlider.get()),
                    "initGravAcc": round(projectileSimulationConfigTabInitGravAccSlider.get(), 1),
                    "initMass": int(projectileSimulationConfigTabInitMassSlider.get()),
                    "initDiameter": int(projectileSimulationConfigTabInitDiameterSlider.get()),
                    "dragCoef": round(projectileSimulationConfigTabInitDragCoefSlider.get(), 1)
    }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)
    projectileSimulationConfigTabLaunchButton.configure(state = "disabled")
    projectileSimulationConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder
    simulationPath = os.path.join("physicsSimulations", "projectileSimulation.py")
    subprocess.run(["python", simulationPath])
    projectileSimulationConfigTabLaunchButton.configure(state = "normal")
    projectileSimulationConfigTabLaunchButton.configure(text = "Launch")

def pendulumSimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    configValues = {
                    "simulationID": "pendulumSimulation",
                    "initAngle": int(pendulumSimulationConfigTabInitAngleSlider.get()),
                    "initAngularVel": round(pendulumSimulationConfigTabInitAngularVelSlider.get(), 1),
                    "initLength": round(pendulumSimulationConfigTabInitLengthSlider.get(), 1),
                    "initMass": round(pendulumSimulationConfigTabInitMassSlider.get(), 1),
                    "initGravAcc": round(pendulumSimulationConfigTabInitGravAccSlider.get(), 1),
                    "dampingCoef": round(pendulumSimulationConfigTabInitDampingCoefSlider.get(), 1)
    }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)
    pendulumSimulationConfigTabLaunchButton.configure(state = "disabled")
    pendulumSimulationConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder    
    simulationPath = os.path.join("physicsSimulations", "pendulumSimulation.py")
    subprocess.run(["python", simulationPath])
    pendulumSimulationConfigTabLaunchButton.configure(state = "normal")
    pendulumSimulationConfigTabLaunchButton.configure(text = "Launch")

def springSimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    configValues = {
                    "simulationID": "springSimulation",
                    "initMass": round(springSimulationConfigTabInitMassSlider.get(), 1),
                    "initGravAcc": round(springSimulationConfigTabInitGravAccSlider.get(), 1),
                    "initLength": int(springSimulationConfigTabInitLengthSlider.get()),
                    "initStiffness": round(springSimulationConfigTabInitStiffSlider.get(), 1),
                    "dampingCoef": round(springSimulationConfigTabInitDampingCoefSlider.get(), 1)
    }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
            json.dump(configValues, f)
    springSimulationConfigTabLaunchButton.configure(state = "disabled")
    springSimulationConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder
    simulationPath = os.path.join("physicsSimulations", "springSimulation.py")
    subprocess.run(["python", simulationPath])
    springSimulationConfigTabLaunchButton.configure(state = "normal")
    springSimulationConfigTabLaunchButton.configure(text = "Launch")

def planetOrbitsSimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    global planetsConfigValuesList
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        planetsConfigValues = {
                               "simulationID": "planetOrbitsSimulation",
                               "planets": planetConfigValuesList
        }
        json.dump(planetsConfigValues, f)
    planetOrbitsSimulationConfigTabLaunchButton.configure(state = "disabled")
    planetOrbitsSimulationConfigTabLaunchButton.configure(text = "Running...")
    
    #Runs its respective simulation by opening its folder
    simulationPath = os.path.join("physicsSimulations", "planetOrbitsSimulation.py")
    subprocess.run(["python", simulationPath])
    planetOrbitsSimulationConfigTabLaunchButton.configure(state = "normal")
    planetOrbitsSimulationConfigTabLaunchButton.configure(text = "Launch")

def gravitySimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        configValues = {
                        "simulationID": "gravitySimulation",
                        "initMass": int(gravitySimulationConfigTabInitMassSlider.get()),
                        "initGravAcc": round(gravitySimulationConfigTabInitGravAccSlider.get(), 1),
                        "initHeight": int(gravitySimulationConfigTabInitHeightSlider.get())
        }
        json.dump(configValues, f)
    gravitySimulationConfigTabLaunchButton.configure(state = "disabled")
    gravitySimulationConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder    
    simulationPath = os.path.join("physicsSimulations", "gravitySimulation.py")
    subprocess.run(["python", simulationPath])
    gravitySimulationConfigTabLaunchButton.configure(state = "normal")
    gravitySimulationConfigTabLaunchButton.configure(text = "Launch")

def refractionSimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
            configValues = {
                            "simulationID": "refractionSimulation",
                            "initRefractiveIndex1": "1.0" if refractionSimulationConfigInitRefractiveIndex1OptionMenu.get() == "Select Refractive Index 1" or (refractionSimulationConfigInitRefractiveIndex1OptionMenu.get() == "Custom" and refractionSimulationConfigInitRefractiveIndex1CustomEntry.get() == "") else refractionSimulationConfigInitRefractiveIndex1OptionMenu.get() if refractionSimulationConfigInitRefractiveIndex1OptionMenu.get() != "Custom" else refractionSimulationConfigInitRefractiveIndex1CustomEntry.get(),
                            "initRefractiveIndex2": "1.0" if refractionSimulationConfigInitRefractiveIndex2OptionMenu.get() == "Select Refractive Index 2" or (refractionSimulationConfigInitRefractiveIndex2OptionMenu.get() == "Custom" and refractionSimulationConfigInitRefractiveIndex2CustomEntry.get() == "") else refractionSimulationConfigInitRefractiveIndex2OptionMenu.get() if refractionSimulationConfigInitRefractiveIndex2OptionMenu.get() != "Custom" else refractionSimulationConfigInitRefractiveIndex2CustomEntry.get(),
                            "initIncidenceAngle": round(refractionSimulationConfigTabInitIncidenceAngleSlider.get(), 1),
                            "rayColor": "White" if refractionSimulationConfigTabRayColorOptionMenu.get() == "Select Ray Color" else refractionSimulationConfigTabRayColorOptionMenu.get()
            }
            json.dump(configValues, f)
    refractionSimulationConfigTabLaunchButton.configure(state = "disabled")
    refractionSimulationConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder        
    simulationPath = os.path.join("physicsSimulations", "refractionSimulation.py")
    subprocess.run(["python", simulationPath])
    refractionSimulationConfigTabLaunchButton.configure(state = "normal")
    refractionSimulationConfigTabLaunchButton.configure(text = "Launch")

def fluidSimulationConfigTabLaunchButtonEvent():
    #Plays an error sound when clicked because the simulation has not been implemented yet but checks if the file exists
    if os.path.exists("sounds/ui/buttonClicks/launcherQuit.mp3"):
        errorSoundPath = "sounds/ui/buttonClicks/launcherQuit.mp3"
        errorSound = mixer.Sound(errorSoundPath)
        mixer.Channel(2).play(errorSound)

def temperatureSimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    configValues = {
                    "simulationID": "temperatureSimulation",
                    "initParticleNumber": int(temperatureSimulationConfigTabInitParticleNumberSlider.get()),
                    "initParticleDiameter": int(temperatureSimulationConfigTabInitParticleDiameterSlider.get()),
                    "initTemperature": round(temperatureSimulationConfigTabInitTempSlider.get(), 1),
        }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)
    temperatureSimulationConfigTabLaunchButton.configure(state = "disabled")
    temperatureSimulationConfigTabLaunchButton.configure(text = "Running...")
    
    #Runs its respective simulation by opening its folder
    simulationPath = os.path.join("physicsSimulations", "temperatureSimulation.py")
    subprocess.run(["python", simulationPath])
    temperatureSimulationConfigTabLaunchButton.configure(state = "normal")
    temperatureSimulationConfigTabLaunchButton.configure(text = "Launch")

##The buttons of the chemistry simulations go here
def bohrAtomSimulationConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    configValues = {
                    "simulationID": "bohrAtomSimulation",
                    "atomSelectionIndex": bohrAtomSimulationConfigTabAtomSelectionIndex
            }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)
    bohrAtomSimulationConfigTabLaunchButton.configure(state = "disabled")
    bohrAtomSimulationConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder       
    simulationPath = os.path.join("chemistrySimulations", "bohrAtomicSimulation.py")
    subprocess.run(["python", simulationPath])
    bohrAtomSimulationConfigTabLaunchButton.configure(state = "normal")
    bohrAtomSimulationConfigTabLaunchButton.configure(text = "Launch")
    bohrAtomSimulationConfigTabAtomSelectionIndex = 0
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)

def solutionMakerConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    configValues = {
                    "simulationID": "solutionMaker",
                    "initSolvent": "Water (H₂O)" if solutionMakerConfigTabInitSolventOptionMenu.get() == "Select Solvent" else solutionMakerConfigTabInitSolventOptionMenu.get(),
                    "initSolventVolume": int(solutionMakerConfigTabInitSolventVolSlider.get()),
                    "initSolute": "Sodium Chloride (NaCl)" if solutionMakerConfigTabInitSoluteOptionMenu.get() == "Select Solute" else solutionMakerConfigTabInitSoluteOptionMenu.get(),
                    "initSoluteMass": int(solutionMakerConfigTabInitSoluteMassSlider.get())
                }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)
    solutionMakerConfigTabLaunchButton.configure(state = "disabled")
    solutionMakerConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder        
    simulationPath = os.path.join("chemistrySimulations", "solutionMaker.py")
    subprocess.run(["python", simulationPath])
    solutionMakerConfigTabLaunchButton.configure(state = "normal")
    solutionMakerConfigTabLaunchButton.configure(text = "Launch")

def molecularLabConfigTabLaunchButtonEvent():
    #Sends the values selected in the configuration tab to the .json file containing the simulation configuration values
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    configValues = {
                    "simulationID": "molecularLab",
                    "initMolecule": "Glucose (C₆H₁₂O₆)" if molecularLabConfigTabInitMoleculeOptionMenu.get() == "Select Molecule" else molecularLabConfigTabInitMoleculeOptionMenu.get(),
                    "initHydrogenColor": "Light Blue" if molecularLabConfigTabInitHydrogenColorOptionMenu.get() == "Select Color" else molecularLabConfigTabInitHydrogenColorOptionMenu.get(),
                    "initCarbonColor": "Black" if molecularLabConfigTabInitCarbonColorOptionMenu.get() == "Select Color" else molecularLabConfigTabInitCarbonColorOptionMenu.get(),
                    "initOxygenColor": "Red" if molecularLabConfigTabInitOxygenColorOptionMenu.get() == "Select Color" else molecularLabConfigTabInitOxygenColorOptionMenu.get()
                    }
    with open("simulationConfigValues/simulationConfigValues.json", "w") as f:
        json.dump(configValues, f)
    molecularLabConfigTabLaunchButton.configure(state = "disabled")
    molecularLabConfigTabLaunchButton.configure(text = "Running...")

    #Runs its respective simulation by opening its folder             
    simulationPath = os.path.join("chemistrySimulations", "molecularLab.py")
    subprocess.run(["python", simulationPath])
    molecularLabConfigTabLaunchButton.configure(state = "normal")
    molecularLabConfigTabLaunchButton.configure(text = "Launch")

#The events of the configurators (sliders, buttons, switches, etc...) from the simulation configuration tabs go here
##The configurator events of the physics simulations go here
###The configurator events of the Projectile Simulation go here
def projectileSimulationConfigTabInitVelocitySliderEvent(value):
    projectileSimulationConfigTabInitVelocitySliderValueVar.set(int(value))

def projectileSimulationConfigTabInitAngleSliderEvent(value):
    projectileSimulationConfigTabInitAngleSliderValueVar.set(int(value))

def projectileSimulationConfigTabInitGravAccSliderEvent(value):
    projectileSimulationConfigTabInitGravAccSliderValueVar.set(round(value, 1))

def projectileSimulationConfigTabInitMassSliderEvent(value):
    projectileSimulationConfigTabInitMassSliderValueVar.set(int(value))

def projectileSimulationConfigTabInitDiameterSliderEvent(value):
    projectileSimulationConfigTabInitDiameterSliderValueVar.set(int(value))

def projectileSimulationConfigTabInitDragCoefSliderEvent(value):
    projectileSimulationConfigTabInitDragCoefSliderValueVar.set(round(value, 1))

###The configurator events of the Pendulum Simulation go here
def pendulumSimulationConfigTabInitAngleSliderEvent(value):
    pendulumSimulationConfigTabInitAngleSliderValueVar.set(int(value))

def pendulumSimulationConfigTabInitAngularVelSliderEvent(value):
    pendulumSimulationConfigTabInitAngularVelSliderValueVar.set(round(value, 1))

def pendulumSimulationConfigTabInitLengthSliderEvent(value):
    pendulumSimulationConfigTabInitLengthSliderValueVar.set(round(value, 1))

def pendulumSimulationConfigTabInitMassSliderEvent(value):
    pendulumSimulationConfigTabInitMassSliderValueVar.set(round(value, 1))

def pendulumSimulationConfigTabInitGravAccSliderEvent(value):
    pendulumSimulationConfigTabInitGravAccSliderValueVar.set(round(value, 1))

def pendulumSimulationConfigTabInitDampingCoefSliderEvent(value):
    pendulumSimulationConfigTabInitDampingCoefSliderValueVar.set(round(value, 1))

###The configurator events of the Spring Simulation go here
def springSimulationConfigTabInitMassSliderEvent(value):
    springSimulationConfigTabInitMassSliderValueVar.set(round(value, 1))

def springSimulationConfigTabInitGravAccSliderEvent(value):
    springSimulationConfigTabInitGravAccSliderValueVar.set(round(value, 1))

def springSimulationConfigTabInitLengthSliderEvent(value):
    springSimulationConfigTabInitLengthSliderValueVar.set(int(value))

def springSimulationConfigTabInitStiffSliderEvent(value):
    springSimulationConfigTabInitStiffSliderValueVar.set(round(value, 1))

def springSimulationConfigTabInitDampingCoefSliderEvent(value):
    springSimulationConfigTabInitDampingCoefSliderValueVar.set(round(value, 1))

###The configurator events of the Planet Orbits (simulation) go here
def planetOrbitsSimulationConfigTabResetPlanetListButtonEvent():
    #Plays a sound when clicked and resets the planet list sent to the .json file
    global planetConfigValuesList, buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    planetConfigValuesList = []

def planetOrbitsSimulationConfigTabShowOrbitTrailSwitchEvent():
    pass

def planetOrbitsSimulationConfigTabShowPlanetNameSwitchEvent():
    pass

def planetOrbitsSimulationConfigTabPlanetInitialVxSliderEvent(value):
    planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueVar.set(round(value, 3))

def planetOrbitsSimulationConfigTabPlanetInitialVySliderEvent(value):
    planetOrbitsSimulationConfigTabPlanetInitialVySliderValueVar.set(round(value, 3))

def planetOrbitsSimulationConfigTabPlanetInitialAxSliderEvent(value):
    planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueVar.set(round(value, 3))

def planetOrbitsSimulationConfigTabPlanetInitialAySliderEvent(value):
    planetOrbitsSimulationConfigTabPlanetInitialAySliderValueVar.set(round(value, 3))

###The configurator events of the Gravity Simulation go here
def gravitySimulationConfigTabInitMassSliderEvent(value):
    gravitySimulationConfigTabInitMassSliderValueVar.set(int(value))

def gravitySimulationConfigTabInitGravAccSliderEvent(value):
    gravitySimulationConfigTabInitGravAccSliderValueVar.set(round(value, 1))

def gravitySimulationConfigTabInitHeightSliderEvent(value):
    gravitySimulationConfigTabInitHeightSliderValueVar.set(int(value))

###The configurator events of the Refraction Simulation go here
def refractionSimulationConfigTabInitIncidenceAngleSliderEvent(value):
    refractionSimulationConfigTabInitIncidenceAngleSliderValueVar.set(round(value, 1))

###The configurator events of the Fluid Simulation go here
def fluidSimulationConfigTabInitVolumeSliderEvent(value):
    fluidSimulationConfigTabInitVolumeSliderValueVar.set(round(value, 1))

def fluidSimulationConfigTabInitPressureSliderEvent(value):
    fluidSimulationConfigTabInitPressureSliderValueVar.set(int(value))

def fluidSimulationConfigTabShowLatticeSwitchEvent():
    pass

###The configurator events of the Temperature Simulation go here
def temperatureSimulationConfigTabInitParticleNumberSliderEvent(value):
    temperatureSimulationConfigTabInitParticleNumberSliderValueVar.set(int(value))

def temperatureSimulationConfigTabInitParticleDiameterSliderEvent(value):
    temperatureSimulationConfigTabInitParticleDiameterSliderValueVar.set(int(value))

def temperatureSimulationConfigTabInitTempSliderEvent(value):
    temperatureSimulationConfigTabInitTempSliderValueVar.set(round(value, 1))

##The configurator events of the chemistry simulations go here
###The configurator events of the Solution Maker go here
def solutionMakerConfigTabInitSolventOptionMenuEvent(value):
    pass

def solutionMakerConfigTabInitSolventVolSliderEvent(value):
    solutionMakerConfigTabInitSolventVolSliderValueVar.set(int(value))

def solutionMakerConfigTabInitSoluteOptionMenuEvent(value):
    pass

def solutionMakerConfigTabInitSoluteMassSliderEvent(value):
    solutionMakerConfigTabInitSoluteMassSliderValueVar.set(int(value))

###The configurator events of the Molecular Lab go here:
def molecularLabConfigTabInitMoleculeOptionMenuEvent(value):
    pass

def molecularLabConfigTabInitHydrogenColorOptionMenuEvent(value):
    pass

def molecularLabConfigTabInitCarbonColorOptionMenuEvent(value):
    pass

def molecularLabConfigTabInitOxygenColorOptionMenuEvent(value):
    pass


def ctkThemesGithubRepoButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://github.com/a13xe/CTkThemesPack")

def projectileSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://www.pexels.com/@bohdan-hyrovych-796614725/")

def pendulumSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://www.pexels.com/@pixabay/")

def springSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://pixabay.com/users/kalhh-86169/")

def planetOrbitsSimulationThumbnailButtonEvent():
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://pixabay.com/users/luis_humanoide-12661853/")

def gravitySimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://commons.wikimedia.org/w/index.php?curid=2880974")

def refractionSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://flickr.com/people/19607761@N00")

def fluidSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://pixabay.com/users/kidsnewshu-5999490/")

def temperatureSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://www.pexels.com/@marek-piwnicki-3907296/")

def bohrAtomSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://pixabay.com/users/geralt-9301/")

def solutionMakerThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://pixabay.com/users/publicdomainpictures-14/")

def molecularLabThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://news.mit.edu/2017/computer-system-predicts-products-chemical-reactions-0627")

def reactionLabThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://www.flickr.com/photos/electro_n1k/")

def combustionSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://commons.wikimedia.org/wiki/File:Coloured_flames_of_methanol_solutions_of_metal_salts_and_compounds.jpg")

def smokeSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://www.pexels.com/@thales13/")

def atomsCollisionSimulationThumbnailButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://commons.wikimedia.org/w/index.php?curid=516106")

def snapticPageButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://store.steampowered.com/app/5201040/SNAPTIC/")

def segoeUIPageButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://learn.microsoft.com/en-us/typography/font-list/segoe-ui")

def ctkPageButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://customtkinter.tomschimansky.com/")

def tkinterPageButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://docs.python.org/3/library/tkinter.html")

def pillowPageButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://pypi.org/project/pillow/")

def pygamePageButtonEvent():
    #Plays a sound when clicked and opens a credits link (image, author, game page , GitHub repository or official website)
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    webbrowser.open("https://www.pygame.org/docs/")

###The configurator events of the Launcher Settings tab go here
def launcherSettingsFPSCapOptionMenuEvent(value):
    pass

def launcherSettingsVSyncSwitchEvent():
    pass

def launcherSettingsApplyButtonEvent():
    #Plays a sound and sends the selected settings to the launcher settings .json file
    global buttonClick
    buttonClick += 1
    buttonClickSound(buttonClick)
    launcherSettings = {
            "fpsCap": int(launcherSettingsFPSCapOptionMenu.get()),
            "vsyncActivated": int(launcherSettingsVSyncSwitch.get()),
        }
    with open("launcherSettings/launcherSettings.json", "w") as f:
        json.dump(launcherSettings, f)

#The general simulation tab functions go here
def physicsTab(bool):
    global projectileSimulationConfigButton, pendulumSimulationConfigButton, springSimulationConfigButton, planetOrbitsSimulationConfigButton, gravitySimulationConfigButton, refractionSimulationConfigButton, fluidSimulationConfigButton, temperatureSimulationConfigButton
    if bool == True:
        #The frames for the simulations are here
        projectileSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                           width = 210,
                                                           height = 280,
                                                           corner_radius = 5,
                                                           border_width = 1)
        projectileSimulationFrame.place(relx = 0.15, rely = 0.25, anchor = tkinter.CENTER)

        pendulumSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                         width = 210,
                                                         height = 280,
                                                         corner_radius = 5,
                                                         border_width = 1)
        pendulumSimulationFrame.place(relx = 0.39, rely = 0.25, anchor = tkinter.CENTER)

        springSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                       width = 210,
                                                       height = 280,
                                                       corner_radius = 5,
                                                       border_width = 1)
        springSimulationFrame.place(relx = 0.63, rely = 0.25, anchor = tkinter.CENTER)

        planetOrbitsSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                             width = 210,
                                                             height = 280,
                                                             corner_radius = 5,
                                                             border_width = 1)
        planetOrbitsSimulationFrame.place(relx = 0.87, rely = 0.25, anchor = tkinter.CENTER)

        gravitySimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                        width = 210,
                                                        height = 280,
                                                        corner_radius = 5,
                                                        border_width = 1)
        gravitySimulationFrame.place(relx = 0.15, rely = 0.75, anchor = tkinter.CENTER)

        refractionSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                           width = 210,
                                                           height = 280,
                                                           corner_radius = 5,
                                                           border_width = 1)
        refractionSimulationFrame.place(relx = 0.39, rely = 0.75, anchor = tkinter.CENTER)

        fluidSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                      width = 210,
                                                      height = 280,
                                                      corner_radius = 5,
                                                      border_width = 1)
        fluidSimulationFrame.place(relx = 0.63, rely = 0.75, anchor = tkinter.CENTER)

        temperatureSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                            width = 210,
                                                            height = 280,
                                                            corner_radius = 5,
                                                            border_width = 1)
        temperatureSimulationFrame.place(relx = 0.87, rely = 0.75, anchor = tkinter.CENTER)

        #The buttons to configure the simulations are here
        projectileSimulationConfigButton = customtkinter.CTkButton(master = projectileSimulationFrame,
                                                                   text = "Configure",
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                   width = 200,
                                                                   height = 50,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = projectileSimulationConfigButtonEvent)
        projectileSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        pendulumSimulationConfigButton = customtkinter.CTkButton(master = pendulumSimulationFrame,
                                                                 text = "Configure",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                 width = 200,
                                                                 height = 50,
                                                                 corner_radius = 5,
                                                                 border_width = 1,
                                                                 command = pendulumSimulationConfigButtonEvent)
        pendulumSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        springSimulationConfigButton = customtkinter.CTkButton(master = springSimulationFrame,
                                                               text = "Configure",
                                                               font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                               width = 200,
                                                               height = 50,
                                                               corner_radius = 5,
                                                               border_width = 1,
                                                               command = springSimulationConfigButtonEvent)
        springSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        planetOrbitsSimulationConfigButton = customtkinter.CTkButton(master = planetOrbitsSimulationFrame,
                                                                     text = "Configure",
                                                                     font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                     width = 200,
                                                                     height = 50,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     command = planetOrbitsSimulationConfigButtonEvent)
        planetOrbitsSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        gravitySimulationConfigButton = customtkinter.CTkButton(master = gravitySimulationFrame,
                                                                text = "Configure",
                                                                font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                width = 200,
                                                                height = 50,
                                                                corner_radius = 5,
                                                                border_width = 1,
                                                                command = gravitySimulationConfigButtonEvent)
        gravitySimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        refractionSimulationConfigButton = customtkinter.CTkButton(master = refractionSimulationFrame,
                                                                   text = "Configure",
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                   width = 200,
                                                                   height = 50,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = refractionSimulationConfigButtonEvent)
        refractionSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        fluidSimulationConfigButton = customtkinter.CTkButton(master = fluidSimulationFrame,
                                                              text = "Configure",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                              width = 200,
                                                              height = 50,
                                                              corner_radius = 5,
                                                              border_width = 1,
                                                              command = fluidSimulationConfigButtonEvent)
        fluidSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        temperatureSimulationConfigButton = customtkinter.CTkButton(master = temperatureSimulationFrame,
                                                                    text = "Configure",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                    width = 200,
                                                                    height = 50,
                                                                    corner_radius = 5,
                                                                    border_width = 1,
                                                                    command = temperatureSimulationConfigButtonEvent)
        temperatureSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        #The image labels for the simulations are here
        projectileSimulationImageLabel = customtkinter.CTkLabel(master = projectileSimulationFrame,
                                                                image = projectileSimulationThumbnailImage,
                                                                text = "")
        projectileSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        pendulumSimulationImageLabel = customtkinter.CTkLabel(master = pendulumSimulationFrame,
                                                              image = pendulumSimulationThumbnailImage,
                                                              text = "")
        pendulumSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        springSimulationImageLabel = customtkinter.CTkLabel(master = springSimulationFrame,
                                                            image = springSimulationThumbnailImage,
                                                            text = "")
        springSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        planetOrbitsSimulationImageLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationFrame,
                                                                  image = planetOrbitsSimulationThumbnailImage,
                                                                  text = "")
        planetOrbitsSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        gravitySimulationImageLabel = customtkinter.CTkLabel(master = gravitySimulationFrame,
                                                             image = gravitySimulationThumbnailImage,
                                                             text = "")
        gravitySimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        refractionSimulationImageLabel = customtkinter.CTkLabel(master = refractionSimulationFrame,
                                                                image = refractionSimulationThumbnailImage,
                                                                text = "")
        refractionSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        fluidSimulationImageLabel = customtkinter.CTkLabel(master = fluidSimulationFrame,
                                                           image = fluidSimulationThumbnailImage,
                                                           text = "")
        fluidSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        temperatureSimulationImageLabel = customtkinter.CTkLabel(master = temperatureSimulationFrame,
                                                                 image = temperatureSimulationThumbnailImage,
                                                                 text = "")
        temperatureSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        #The title and description labels for the simulations are here
        projectileSimulationTitleLabel = customtkinter.CTkLabel(master = projectileSimulationFrame,
                                                                justify = LEFT,
                                                                text = "Projectile Simulation",
                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        projectileSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        projectileSimulationDescriptionLabel = customtkinter.CTkLabel(master = projectileSimulationFrame,
                                                                      justify = LEFT,
                                                                      text = "Simulates a projectile being\nthrown by changing specific\nphysical properties.",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        projectileSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        pendulumSimulationTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationFrame,
                                                              justify = LEFT,
                                                              text = "Pendulum Simulation",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        pendulumSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        pendulumSimulationDescriptionLabel = customtkinter.CTkLabel(master = pendulumSimulationFrame,
                                                                    justify = LEFT,
                                                                    text = "Simulates a mass suspended\nto a fixed point swinging back\nand forth.",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        pendulumSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        springSimulationTitleLabel = customtkinter.CTkLabel(master = springSimulationFrame,
                                                            justify = LEFT,
                                                            text = "Spring Simulation",
                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        springSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        springSimulationDescriptionLabel = customtkinter.CTkLabel(master = springSimulationFrame,
                                                                  justify = LEFT,
                                                                  text = "Simulates a mass attached to a\nspring suspended to a fixed point\nunder the influence of gravity.",
                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        springSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        planetOrbitsSimulationTitleLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationFrame,
                                                                  justify = LEFT,
                                                                  text = "Planet Orbits",
                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        planetOrbitsSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        planetOrbitsSimulationDescriptionLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationFrame,
                                                                        justify = LEFT,
                                                                        text = "Solves the N-body problem\nto simulate your favorite planets \nbut also your own ones.",
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        planetOrbitsSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        gravitySimulationTitleLabel = customtkinter.CTkLabel(master = gravitySimulationFrame,
                                                             justify = LEFT,
                                                             text = "Gravity Simulator",
                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        gravitySimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        gravitySimulationDescriptionLabel = customtkinter.CTkLabel(master = gravitySimulationFrame,
                                                                   justify = LEFT,
                                                                   text = "Simulates an object falling\nunder the influence of\ngravity.",
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        gravitySimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        refractionSimulationTitleLabel = customtkinter.CTkLabel(master = refractionSimulationFrame,
                                                                justify = LEFT,
                                                                text = "Refraction Simulation",
                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        refractionSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        refractionSimulationDescriptionLabel = customtkinter.CTkLabel(master = refractionSimulationFrame,
                                                                      justify = LEFT,
                                                                      text = "Simulates light changing velocity\nand angle under the influence of\na fluid.",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        refractionSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        fluidSimulationTitleLabel = customtkinter.CTkLabel(master = fluidSimulationFrame,
                                                           justify = LEFT,
                                                           text = "Fluid Simulation",
                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        fluidSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        fluidSimulationDescriptionLabel = customtkinter.CTkLabel(master = fluidSimulationFrame,
                                                                 justify = LEFT,
                                                                 text = "Simulates a given fluid whose\ndensity, viscosity and volume can\nbe changed.",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        fluidSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        temperatureSimulationTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationFrame,
                                                                 justify = LEFT,
                                                                 text = "Temperature Simulation",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "bold"))
        temperatureSimulationTitleLabel.place(relx = 0.04, rely = 0.55, anchor = tkinter.W)

        temperatureSimulationDescriptionLabel = customtkinter.CTkLabel(master = temperatureSimulationFrame,
                                                                       justify = LEFT,
                                                                       text = "Simulates the increase\nor decrease of entropy when\napplying heat or cold.",
                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        temperatureSimulationDescriptionLabel.place(relx = 0.05, rely = 0.68, anchor = tkinter.W)

        #These lines bind an event to the buttons from the tab when they are hovered (in this case, they play a sound)
        projectileSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        pendulumSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        springSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        planetOrbitsSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        gravitySimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        refractionSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        fluidSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        temperatureSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        
def chemistryTab(bool):
    global bohrAtomSimulationConfigButton, solutionMakerConfigButton, molecularLabConfigButton, reactionLabConfigButton, combustionSimulationConfigButton, smokeSimulationConfigButton, atomCollisionSimulationConfigButton
    if bool == True:
        #The frames for the simulations are here
        bohrAtomSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                         width = 210,
                                                         height = 280,
                                                         corner_radius = 5,
                                                         border_width = 1)
        bohrAtomSimulationFrame.place(relx = 0.15, rely = 0.25, anchor = tkinter.CENTER)

        solutionMakerFrame = customtkinter.CTkFrame(master = mainFrame,
                                                    width = 210,
                                                    height = 280,
                                                    corner_radius = 5,
                                                    border_width = 1)
        solutionMakerFrame.place(relx = 0.39, rely = 0.25, anchor = tkinter.CENTER)

        molecularLabFrame = customtkinter.CTkFrame(master = mainFrame,
                                                   width = 210,
                                                   height = 280,
                                                   corner_radius = 5,
                                                   border_width = 1)
        molecularLabFrame.place(relx = 0.63, rely = 0.25, anchor = tkinter.CENTER)

        reactionLabFrame = customtkinter.CTkFrame(master = mainFrame,
                                                  width = 210,
                                                  height = 280,
                                                  corner_radius = 5,
                                                  border_width = 1)
        reactionLabFrame.place(relx = 0.87, rely = 0.25, anchor = tkinter.CENTER)

        combustionSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                           width = 210,
                                                           height = 280,
                                                           corner_radius = 5,
                                                           border_width = 1)
        combustionSimulationFrame.place(relx = 0.15, rely = 0.75, anchor = tkinter.CENTER)

        smokeSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                      width = 210,
                                                      height = 280,
                                                      corner_radius = 5,
                                                      border_width = 1)
        smokeSimulationFrame.place(relx = 0.39, rely = 0.75, anchor = tkinter.CENTER)

        atomCollisionSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                              width = 210,
                                                              height = 280,
                                                              corner_radius = 5,
                                                              border_width = 1)
        atomCollisionSimulationFrame.place(relx = 0.63, rely = 0.75, anchor = tkinter.CENTER)

        #The buttons to configure the simulations are here
        bohrAtomSimulationConfigButton = customtkinter.CTkButton(master = bohrAtomSimulationFrame,
                                                                 text = "Configure",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                 width = 200,
                                                                 height = 50,
                                                                 corner_radius = 5,
                                                                 border_width = 1,
                                                                 command = bohrAtomSimulationConfigButtonEvent)
        bohrAtomSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        solutionMakerConfigButton = customtkinter.CTkButton(master = solutionMakerFrame,
                                                            text = "Configure",
                                                            font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                            width = 200,
                                                            height = 50,
                                                            corner_radius = 5,
                                                            border_width = 1,
                                                            command = solutionMakerConfigButtonEvent)
        solutionMakerConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        molecularLabConfigButton = customtkinter.CTkButton(master = molecularLabFrame,
                                                           text = "Configure",
                                                           font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                           width = 200,
                                                           height = 50,
                                                           corner_radius = 5,
                                                           border_width = 1,
                                                           command = molecularLabConfigButtonEvent)
        molecularLabConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        reactionLabConfigButton = customtkinter.CTkButton(master = reactionLabFrame,
                                                          text = "Configure",
                                                          font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                          width = 200,
                                                          height = 50,
                                                          corner_radius = 5,
                                                          border_width = 1,
                                                          command = reactionLabConfigButtonEvent)
        reactionLabConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        combustionSimulationConfigButton = customtkinter.CTkButton(master = combustionSimulationFrame,
                                                                   text = "Configure",
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                   width = 200,
                                                                   height = 50,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = combustionSimulationConfigButtonEvent)
        combustionSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        smokeSimulationConfigButton = customtkinter.CTkButton(master = smokeSimulationFrame,
                                                              text = "Configure",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                              width = 200,
                                                              height = 50,
                                                              corner_radius = 5,
                                                              border_width = 1,
                                                              command = smokeSimulationConfigButtonEvent)
        smokeSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        atomCollisionSimulationConfigButton = customtkinter.CTkButton(master = atomCollisionSimulationFrame,
                                                                      text = "Configure",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                                      width = 200,
                                                                      height = 50,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      command = atomCollisionSimulationConfigButtonEvent)
        atomCollisionSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        #The image labels for the simulations are here
        bohrAtomSimulationImageLabel = customtkinter.CTkLabel(master = bohrAtomSimulationFrame,
                                                              image = bohrAtomSimulationThumbnailImage,
                                                              text = "")
        bohrAtomSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        solutionMakerImageLabel = customtkinter.CTkLabel(master = solutionMakerFrame,
                                                         image = solutionMakerThumbnailImage,
                                                         text = "")
        solutionMakerImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        molecularLabImageLabel = customtkinter.CTkLabel(master = molecularLabFrame,
                                                        image = molecularLabThumbnailImage,
                                                        text = "")
        molecularLabImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        reactionLabImageLabel = customtkinter.CTkLabel(master = reactionLabFrame,
                                                       image = reactionLabThumbnailImage,
                                                       text = "")
        reactionLabImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        combustionSimulationImageLabel = customtkinter.CTkLabel(master = combustionSimulationFrame,
                                                                image = combustionSimulationThumbnailImage,
                                                                text = "")
        combustionSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        smokeSimulationImageLabel = customtkinter.CTkLabel(master = smokeSimulationFrame,
                                                           image = smokeSimulationThumbnailImage,
                                                           text = "")
        smokeSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor= tkinter.N)

        atomCollisionSimulationImageLabel = customtkinter.CTkLabel(master = atomCollisionSimulationFrame,
                                                                   image = atomCollisionSimulationThumbnailImage,
                                                                   text = "")
        atomCollisionSimulationImageLabel.place(relx = 0.5, rely = 0.03, anchor = tkinter.N)

        #The title and description labels for the simulations are here
        bohrAtomSimulationTitleLabel = customtkinter.CTkLabel(master = bohrAtomSimulationFrame,
                                                              justify = LEFT,
                                                              text = "Bohr Representation",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        bohrAtomSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)
        
        bohrAtomSimulationDescriptionLabel = customtkinter.CTkLabel(master = bohrAtomSimulationFrame,
                                                                    justify = LEFT,
                                                                    text = "Simulates an atom according to\nNiels Bohr's model including\nits electron orbits and nucleons.",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        bohrAtomSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        solutionMakerTitleLabel = customtkinter.CTkLabel(master = solutionMakerFrame,
                                                         justify = LEFT,
                                                         text = "Solution Maker",
                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        solutionMakerTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        solutionMakerDescriptionLabel = customtkinter.CTkLabel(master = solutionMakerFrame,
                                                               justify = LEFT,
                                                               text = "Simulates a bunch of solvants and\nsolutes that can be mixed to\nobtain solutions.",
                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        solutionMakerDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        molecularLabTitleLabel = customtkinter.CTkLabel(master = molecularLabFrame,
                                                        justify = LEFT,
                                                        text = "Molecular Lab",
                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        molecularLabTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        molecularLabDescriptionLabel = customtkinter.CTkLabel(master = molecularLabFrame,
                                                              justify = LEFT,
                                                              text = "Simulates a bunch of elements in\nthe periodic table that can be\ncombined into molecules.",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        molecularLabDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        reactionLabTitleLabel = customtkinter.CTkLabel(master = reactionLabFrame,
                                                       justify = LEFT,
                                                       text = "Reaction Lab",
                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        reactionLabTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        reactionLabDescriptionLabel = customtkinter.CTkLabel(master = reactionLabFrame,
                                                             justify = LEFT,
                                                             text = "Simulates some reactants that\ncan be put together to\ncreate chemical reactions.",
                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        reactionLabDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        combustionSimulationTitleLabel = customtkinter.CTkLabel(master = combustionSimulationFrame,
                                                                justify = LEFT,
                                                                text = "Combustion Simulation",
                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "bold"))
        combustionSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        combustionSimulationDescriptionLabel = customtkinter.CTkLabel(master = combustionSimulationFrame,
                                                                      justify = LEFT,
                                                                      text = "Simulates the combustion of some\nchemical solutes producing a\ncolorful flame.",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        combustionSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        smokeSimulationTitleLabel = customtkinter.CTkLabel(master = smokeSimulationFrame,
                                                           justify = LEFT,
                                                           text = "Smoke Simulation",
                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        smokeSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        smokeSimulationDesccriptionLabel = customtkinter.CTkLabel(master = smokeSimulationFrame,
                                                                  justify = LEFT,
                                                                  text = "Simulates smoke coming from the\ncombustion of different chemical\nsolutes.",
                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        smokeSimulationDesccriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        atomCollisionSimulationTitleLabel = customtkinter.CTkLabel(master = atomCollisionSimulationFrame,
                                                                   justify = LEFT,
                                                                   text = "Atom Collision",
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
        atomCollisionSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        atomCollisionSimulationDescriptionLabel = customtkinter.CTkLabel(master = atomCollisionSimulationFrame,
                                                                         justify = LEFT,
                                                                         text = "Simulates different kinds of atoms\nof the periodic table colliding\ninto each other.",
                                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
        atomCollisionSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        #These lines bind an event to the buttons from the tab when they are hovered (in this case, they play a sound)
        bohrAtomSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        solutionMakerConfigButton.bind("<Enter>", onButtonHover, add = "+")
        molecularLabConfigButton.bind("<Enter>", onButtonHover, add = "+")
        reactionLabConfigButton.bind("<Enter>", onButtonHover, add = "+")
        combustionSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        smokeSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")
        atomCollisionSimulationConfigButton.bind("<Enter>", onButtonHover, add = "+")

def thePlaceTab(bool):
    #These lines create a label when the "The Place" button is clicked
    global thePlaceMainLabel
    if bool == True:
        thePlaceMainLabel = customtkinter.CTkLabel(master = mainFrame,
                                                  text = "Invisible place",
                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 30, weight = "bold"))
        thePlaceMainLabel.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

def launcherSettingsTab(bool):
    #These lines define the labels from the launcher settings tab
    global launcherSettingsFPSCapOptionMenu, launcherSettingsVSyncSwitch
    launcherSettingsPerformanceSettingsLabel = customtkinter.CTkLabel(master = mainFrame,
                                                                      text = "Performance Settings",
                                                                      justify = LEFT,
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 30, weight = "bold"))
    launcherSettingsPerformanceSettingsLabel.place(relx = 0.02, rely = 0.05, anchor = tkinter.W)

    launcherSettingsFPSCapLabel = customtkinter.CTkLabel(master = mainFrame,
                                                         text = "Maximum FPS",
                                                         justify = LEFT,
                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
    launcherSettingsFPSCapLabel.place(relx = 0.02, rely = 0.15, anchor = tkinter.W)

    #These lines define their description labels
    launcherSettingsFPSCapDescriptionLabel = customtkinter.CTkLabel(master = mainFrame,
                                                                    text = "Limits the maximum frame rate of the simulations.",
                                                                    justify = LEFT,
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
    launcherSettingsFPSCapDescriptionLabel.place(relx = 0.02, rely = 0.19, anchor = tkinter.W)

    launcherSettingsVSyncDescriptionLabel = customtkinter.CTkLabel(master = mainFrame,
                                                                   text = "Activates or deactivates vertical sync (screen tearing).\nRecommended for powerful PCs using low refresh rate screens.",
                                                                   justify = LEFT,
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 12, weight = "normal"))
    launcherSettingsVSyncDescriptionLabel.place(relx = 0.02, rely = 0.37, anchor = tkinter.W)

    #And these lines define the configurators of the launcher settings tab
    launcherSettingsFPSCapOptionMenu = customtkinter.CTkOptionMenu(master = mainFrame,
                                                                   width = 150,
                                                                   height = 25,
                                                                   variable = launcherSettingsFPSCapOptionMenuVar,
                                                                   font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                   values = ["30", "60", "120", "144", "180", "200", "240", "300"],
                                                                   command = launcherSettingsFPSCapOptionMenuEvent)
    launcherSettingsFPSCapOptionMenu.place(relx = 0.02, rely = 0.23, anchor = tkinter.W)

    launcherSettingsVSyncSwitch = customtkinter.CTkSwitch(master = mainFrame,
                                                          text = "V-Sync Activation",
                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"),
                                                          variable = launcherSettingsVSyncSwitchEventVar,
                                                          onvalue = "1",
                                                          offvalue = "0",
                                                          command = launcherSettingsVSyncSwitchEvent)
    launcherSettingsVSyncSwitch.place(relx = 0.02, rely = 0.32, anchor = tkinter.W)

    launcherSettingsApplyButton = customtkinter.CTkButton(master = mainFrame,
                                                          text = "Apply Settings",
                                                          font = customtkinter.CTkFont(family = "Segoe UI"),
                                                          width = 885,
                                                          height = 50,
                                                          border_width = 1,
                                                          corner_radius = 5,
                                                          command = launcherSettingsApplyButtonEvent)
    launcherSettingsApplyButton.place(relx = 0.01, rely = 0.94, anchor = tkinter.W)

def creditsTab(bool):
    if bool == True:
        #These lines define the frames of the credits tab
        creditsFrame = customtkinter.CTkFrame(master = mainFrame,
                                              width = 1010,
                                              height = 580,
                                              fg_color = "transparent")
        creditsFrame.place(relx = 0.5, rely = 0.54, anchor = tkinter.CENTER)
        creditsScrollableFrame = customtkinter.CTkScrollableFrame(master = creditsFrame,
                                                                  width = 880,
                                                                  height = 580,
                                                                  fg_color = "transparent")
        creditsScrollableFrame.pack(padx = 0, pady = 0, expand = True)

        #These lines create the text labels of the credits tab
        projectTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                   text = "Physics & Chemistry Sandbox",
                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 30, weight = "bold"))
        projectTitleLabel.pack(padx = 0, pady = 0)

        eventTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                 text = "A project built for the Stardance Challenge, an event made by Hack Club & NASA.",
                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        eventTitleLabel.pack(padx = 0, pady = 0)

        mainDevLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                              text = "Main Developper: NimaxDevs (Amin B.)",
                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        mainDevLabel.pack(padx = 0, pady = (0, 50))

        assetsUsedTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                      text = "Assets Used",
                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 30, weight = "bold"))
        assetsUsedTitleLabel.pack(padx = 0, pady = (0, 10))

        themesTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                  text = "Themes",
                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 25, weight = "bold"))
        themesTitleLabel.pack(padx = 0, pady = (0, 10))

        #These lines create the title of the asset used and the buttons to credit the authors of said assets 
        ctkThemesLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                text = "CTkThemesPack: Rime, made by a13xe and webbrain-one (WebBrain)",
                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        ctkThemesLabel.pack(padx = 0, pady = (0, 5))

        ctkThemesGithubRepoButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                            text = "GitHub Repository",
                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                            width = 145,
                                                            height = 25,
                                                            corner_radius = 5,
                                                            border_width = 1,
                                                            command = ctkThemesGithubRepoButtonEvent)
        ctkThemesGithubRepoButton.pack(padx = 0, pady = (0, 15))

        imagesTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                  text = "Images",
                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 25, weight = "bold"))
        imagesTitleLabel.pack(padx = 0, pady = (0, 10))

        projectileSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                    text = "Projectile Simulation Thumbnail: Bohdan Hyrovych",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        projectileSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
        
        projectileSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                      text = "Author Page",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                      width = 145,
                                                                      height = 25,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      command = projectileSimulationThumbnailButtonEvent)
        projectileSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        pendulumSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                              text = "Pendulum Simulation Thumbnail: Pixabay",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        pendulumSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                
        pendulumSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                    text = "Author Page",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                    width = 145,
                                                                    height = 25,
                                                                    corner_radius = 5,
                                                                    border_width = 1,
                                                                    command = pendulumSimulationThumbnailButtonEvent)
        pendulumSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        springSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                text = "Spring Simulation Thumbnail: kalhh",
                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        springSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                        
        springSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                  text = "Author Page",
                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                  width = 145,
                                                                  height = 25,
                                                                  corner_radius = 5,
                                                                  border_width = 1,
                                                                  command = springSimulationThumbnailButtonEvent)
        springSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        planetOrbitsSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                      text = "Planet Simulation Thumbnail: Luis_Humanoide",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        planetOrbitsSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                
        planetOrbitsSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                        text = "Author Page",
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                        width = 145,
                                                                        height = 25,
                                                                        corner_radius = 5,
                                                                        border_width = 1,
                                                                        command = planetOrbitsSimulationThumbnailButtonEvent)
        planetOrbitsSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        gravitySimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                 text = "Gravity Simulation Thumbnail: MichaelMaggs (edit by Richard Bartz), CC BY-SA 3.0",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        gravitySimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                        
        gravitySimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                   text = "Image Page",
                                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                   width = 145,
                                                                   height = 25,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = gravitySimulationThumbnailButtonEvent)
        gravitySimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        refractionSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                    text = "Refraction Simulation Thumbnail: Mark Woodbury, Creative Commons Attribution 2.0",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        refractionSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                
        refractionSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                      text = "Author Page",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                      width = 145,
                                                                      height = 25,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      command = refractionSimulationThumbnailButtonEvent)
        refractionSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        fluidSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                               text = "Fluid Simulation Thumbnail: kidsnewshu",
                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        fluidSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                        
        fluidSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                 text = "Author Page",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                 width = 145,
                                                                 height = 25,
                                                                 corner_radius = 5,
                                                                 border_width = 1,
                                                                 command = fluidSimulationThumbnailButtonEvent)
        fluidSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        temperatureSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                     text = "Temperature Simulation Thumbnail: Marek Piwnicki",
                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        temperatureSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                
        temperatureSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                       text = "Author Page",
                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                       width = 145,
                                                                       height = 25,
                                                                       corner_radius = 5,
                                                                       border_width = 1,
                                                                       command = temperatureSimulationThumbnailButtonEvent)
        temperatureSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        bohrAtomSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                  text = "Bohr Atomic Representation Simulation Thumbnail: Gerd Altmann",
                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        bohrAtomSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                        
        bohrAtomSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                    text = "Author Page",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                    width = 145,
                                                                    height = 25,
                                                                    corner_radius = 5,
                                                                    border_width = 1,
                                                                    command = bohrAtomSimulationThumbnailButtonEvent)
        bohrAtomSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        solutionMakerThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                             text = "Solution Maker Thumbnail: PublicDomainPictures",
                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        solutionMakerThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                                
        solutionMakerThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                               text = "Author Page",
                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                               width = 145,
                                                               height = 25,
                                                               corner_radius = 5,
                                                               border_width = 1,
                                                               command = solutionMakerThumbnailButtonEvent)
        solutionMakerThumbnailButton.pack(padx = 0, pady = (0, 15))

        molecularLabThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                            text = "Molecular Lab Thumbnail: Courtesy of MIT News",
                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        molecularLabThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                                        
        molecularLabThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                              text = "Image Page",
                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                              width = 145,
                                                              height = 25,
                                                              corner_radius = 5,
                                                              border_width = 1,
                                                              command = molecularLabThumbnailButtonEvent)
        molecularLabThumbnailButton.pack(padx = 0, pady = (0, 15))

        reactionLabThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                           text = "Reaction Lab Thumbnail: Nikthestunned (also at Flickr), CC BY-SA 3.0",
                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        reactionLabThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                                                
        reactionLabThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                             text = "Author Page",
                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                             width = 145,
                                                             height = 25,
                                                             corner_radius = 5,
                                                             border_width = 1,
                                                              command = reactionLabThumbnailButtonEvent)
        reactionLabThumbnailButton.pack(padx = 0, pady = (0, 15))

        combustionSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                    text = "Combustion Simulation Thumbnail: Hegelrast, Creative Commons Attribution-Share Alike 4.0",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        combustionSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                                                        
        combustionSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                      text = "Image Page",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                      width = 145,
                                                                      height = 25,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      command = combustionSimulationThumbnailButtonEvent)
        combustionSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        smokeSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                               text = "Smoke Simulation Thumbnail: Rafael Minguet Delgado",
                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        smokeSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                                                                
        smokeSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                 text = "Author Page",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                 width = 145,
                                                                 height = 25,
                                                                 corner_radius = 5,
                                                                 border_width = 1,
                                                                 command = smokeSimulationThumbnailButtonEvent)
        smokeSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        atomsCollisionSimulationThumbnailLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                                        text = "Atoms Collision Simulation Thumbnail: NASA, ESA, J. Hester and A. Loll (Arizona State University),\nPublic Domain",
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        atomsCollisionSimulationThumbnailLabel.pack(padx = 0, pady = (0, 5))
                                                                                                                        
        atomsCollisionSimulationThumbnailButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                                          text = "Image Page",
                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                          width = 145,
                                                                          height = 25,
                                                                          corner_radius = 5,
                                                                          border_width = 1,
                                                                          command = atomsCollisionSimulationThumbnailButtonEvent)
        atomsCollisionSimulationThumbnailButton.pack(padx = 0, pady = (0, 15))

        soundsTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                  text = "Sounds",
                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 25, weight = "bold"))
        soundsTitleLabel.pack(padx = 0, pady = (0, 10))

        uiSoundsLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                               text = "UI Sounds: Snaptic, modified by EQ frequency tweaking",
                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        uiSoundsLabel.pack(padx = 0, pady = (0, 5))
        
        snapticPageButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                    text = "Steam Page",
                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                    width = 145,
                                                    height = 25,
                                                    corner_radius = 5,
                                                    border_width = 1,
                                                    command = snapticPageButtonEvent)
        snapticPageButton.pack(padx = 0, pady = (0, 15))

        fontsTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                 text = "Fonts",
                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 25, weight = "bold"))
        fontsTitleLabel.pack(padx = 0, pady = (0, 10))

        segoeUILabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                              text = "Segoe UI: Courtesy of Microsoft Corporation",
                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        segoeUILabel.pack(padx = 0, pady = (0, 5))
                
        segoeUIPageButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                    text = "Official Page",
                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                    width = 145,
                                                    height = 25,
                                                    corner_radius = 5,
                                                    border_width = 1,
                                                    command = segoeUIPageButtonEvent)
        segoeUIPageButton.pack(padx = 0, pady = (0, 50))

        externalLibrariesTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                             text = "External Libraries",
                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 30, weight = "bold"))
        externalLibrariesTitleLabel.pack(padx = 0, pady = (0, 10))

        ctkLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                          text = "CustomTkinter: Whole Launcher",
                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        ctkLabel.pack(padx = 0, pady = (0, 5))
        
        ctkPageButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                text = "Official Page",
                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                width = 145,
                                                height = 25,
                                                corner_radius = 5,
                                                border_width = 1,
                                                command = ctkPageButtonEvent)
        ctkPageButton.pack(padx = 0, pady = (0, 15))

        tkinterLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                              text = "Tkinter: Functions needed for CustomTkinter (anchor points, variables)",
                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        tkinterLabel.pack(padx = 0, pady = (0, 5))
                
        tkinterPageButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                    text = "Official Page",
                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                    width = 145,
                                                    height = 25,
                                                    corner_radius = 5,
                                                    border_width = 1,
                                                    command = tkinterPageButtonEvent)
        tkinterPageButton.pack(padx = 0, pady = (0, 15))
        
        pillowLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                             text = "Pillow: Image Manager (import, rounded corners)",
                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        pillowLabel.pack(padx = 0, pady = (0, 5))
                
        pillowPageButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                   text = "Official Page",
                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                   width = 145,
                                                   height = 25,
                                                   corner_radius = 5,
                                                   border_width = 1,
                                                   command = pillowPageButtonEvent)
        pillowPageButton.pack(padx = 0, pady = (0, 15))

        pygameLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                             text = "Pygame: Simulations (windows, rendering, real-time calculations)",
                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        pygameLabel.pack(padx = 0, pady = (0, 5))
                        
        pygamePageButton = customtkinter.CTkButton(master = creditsScrollableFrame,
                                                   text = "Official Page",
                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                   width = 145,
                                                   height = 25,
                                                   corner_radius = 5,
                                                   border_width = 1,
                                                   command = pygamePageButtonEvent)
        pygamePageButton.pack(padx = 0, pady = (0, 50))

        #These lines create the labels containing the title of the special thanks and the said special thanks
        specialThanksTitleLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                              text = "Special Thanks",
                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 30, weight = "bold"))
        specialThanksTitleLabel.pack(padx = 0, pady = (0, 10))

        thanksLabel = customtkinter.CTkLabel(master = creditsScrollableFrame,
                                                      text = "I would like to thank Hack Club and NASA as well as the other partnership members\n(GitHub, AMD) for making this project possible. In fact, it has been a chance to put\nthe recent CustomTkinter, Pygame and Python skills that I've acquired into use.\nMoreover, I would also like to thank everyone for following me through my journey by\nreading my devlogs; it really means a lot to me. Lastly, I would like to thank my family\nfor motivating me to continue working on this project, even when a ton of bugs\nand errors had to be fixed.",
                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "normal"))
        thanksLabel.pack(padx = 25, pady = (0, 50))
    #And these lines bind some events to every button of the credits tab to play a hover sound
    ctkThemesGithubRepoButton.bind("<Enter>", onButtonHover, add = "+")
    projectileSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    pendulumSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    springSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    planetOrbitsSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    gravitySimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    refractionSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    fluidSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    temperatureSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    bohrAtomSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")  
    solutionMakerThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    molecularLabThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    reactionLabThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    combustionSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    smokeSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    atomsCollisionSimulationThumbnailButton.bind("<Enter>", onButtonHover, add = "+")
    snapticPageButton.bind("<Enter>", onButtonHover, add = "+")
    segoeUIPageButton.bind("<Enter>", onButtonHover, add = "+")
    ctkPageButton.bind("<Enter>", onButtonHover, add = "+")
    tkinterPageButton.bind("<Enter>", onButtonHover, add = "+")
    pillowPageButton.bind("<Enter>", onButtonHover, add = "+")
    pygamePageButton.bind("<Enter>", onButtonHover, add = "+")  

#The sub tabs of the physics tab (physics simulations) are here
def projectileSimulationConfigTab(bool):
    global projectileSimulationConfigTabLaunchButton, projectileSimulationConfigTabInitVelocitySlider, projectileSimulationConfigTabInitAngleSlider, projectileSimulationConfigTabInitGravAccSlider, projectileSimulationConfigTabInitMassSlider, projectileSimulationConfigTabInitDiameterSlider, projectileSimulationConfigTabInitDragCoefSlider
    if bool == True:
        #The air resistance checkbox logic goes here
        def projectileSimulationConfigTabInitAirResistCheckboxEvent():
            if projectileSimulationConfigTabInitAirResistCheckbox.get() == "on":
                projectileSimulationConfigTabInitDragCoefTitleLabel.place(relx = 0.51, rely = 0.8, anchor = tkinter.W)
                projectileSimulationConfigTabInitDragCoefSliderValueLabel.place(relx = 0.85, rely = 0.8, anchor = tkinter.W)
                projectileSimulationConfigTabInitDragCoefSlider.place(relx = 0.5, rely = 0.9, anchor = tkinter.W)
            else:
                projectileSimulationConfigTabInitDragCoefTitleLabel.place_forget()
                projectileSimulationConfigTabInitDragCoefSliderValueLabel.place_forget()
                projectileSimulationConfigTabInitDragCoefSlider.place_forget()
        
        #Here are the frames for each element of the config tab
        projectileSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 550,
                                                                         height = 300,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        projectileSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)

        projectileSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 335,
                                                                         height = 100,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        projectileSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)

        projectileSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                               width = 335,
                                                                               height = 200,
                                                                               corner_radius = 5,
                                                                               border_width = 1)
        projectileSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)

        projectileSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 550,
                                                                         height = 265,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        projectileSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)

        projectileSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                width = 335,
                                                                                height = 100,
                                                                                corner_radius = 5,
                                                                                border_width = 1)
        projectileSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
        
        #The buttons go here
        projectileSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = projectileSimulationConfigTabLaunchButtonFrame,
                                                                            text = "Launch",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                            width = 335,
                                                                            height = 100,
                                                                            corner_radius = 5,
                                                                            border_width = 1,
                                                                            command = projectileSimulationConfigTabLaunchButtonEvent)
        projectileSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
        
        #The configurators (items) of the simulation go here
        projectileSimulationConfigTabInitVelocitySlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                  height = 20,
                                                                                  from_ = 1, 
                                                                                  to = 100,
                                                                                  corner_radius = 8,
                                                                                  command = projectileSimulationConfigTabInitVelocitySliderEvent)
        projectileSimulationConfigTabInitVelocitySlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                               height = 20,
                                                                               from_ = 0, 
                                                                               to = 90,
                                                                               corner_radius = 8,
                                                                               command = projectileSimulationConfigTabInitAngleSliderEvent)
        projectileSimulationConfigTabInitAngleSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                 height = 20,
                                                                                 from_ = 0.1, 
                                                                                 to = 20,
                                                                                 corner_radius = 8,
                                                                                 command = projectileSimulationConfigTabInitGravAccSliderEvent)
        projectileSimulationConfigTabInitGravAccSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                              height = 20,
                                                                              from_ = 1, 
                                                                              to = 5000,
                                                                              corner_radius = 8,
                                                                              command = projectileSimulationConfigTabInitMassSliderEvent)
        projectileSimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                  width = 250,
                                                                                  height = 20,
                                                                                  from_ = 1, 
                                                                                  to = 5,
                                                                                  corner_radius = 8,
                                                                                  command = projectileSimulationConfigTabInitDiameterSliderEvent)
        projectileSimulationConfigTabInitDiameterSlider.place(relx = 0.5, rely = 0.2, anchor = tkinter.W)

        projectileSimulationConfigTabInitAirResistCheckbox = customtkinter.CTkCheckBox(master = projectileSimulationConfigTabItemsFrame,
                                                                                       text = "Air Resistance",
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"),
                                                                                       variable = projectileSimulationConfigTabInitAirResistCheckboxVar,
                                                                                       onvalue = "on",
                                                                                       offvalue = "off",
                                                                                       command = projectileSimulationConfigTabInitAirResistCheckboxEvent)
        projectileSimulationConfigTabInitAirResistCheckbox.place(relx = 0.61, rely = 0.66, anchor = tkinter.CENTER)

        projectileSimulationConfigTabInitDragCoefSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                  width = 250,
                                                                                  height = 20,
                                                                                  from_ = 0, 
                                                                                  to = 1,
                                                                                  corner_radius = 8,
                                                                                  command = projectileSimulationConfigTabInitDragCoefSliderEvent)

        #The images of the config tab go here
        projectileSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = projectileSimulationConfigTabImageFrame,
                                                                         image = projectileSimulationPreviewImage,
                                                                         text = "")
        projectileSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
        
        #The labels of the config tab go here
        projectileSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabTitleFrame,
                                                                         justify = LEFT,
                                                                         text = "Projectile\nSimulation",
                                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        projectileSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        projectileSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabDescriptionFrame,
                                                                               justify = LEFT,
                                                                               text = "Simulates a projectile being thrown at a\nspecific velocity, angle, gravitational\nacceleration, mass, diameter and air\nresistance.",
                                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        projectileSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.21, anchor = tkinter.W)

        projectileSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = "Field of physics: Newtonian Mechanics",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        projectileSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.55, anchor = tkinter.W)

        projectileSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabDescriptionFrame,
                                                                                justify = LEFT,
                                                                                text = 'Change and select the physical properties\nthat you want to include then press\non "Launch" to start the simulation.',
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        projectileSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        projectileSimulationConfigTabInitVelocityTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Velocity (m/s): ",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitVelocityTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitVelocitySliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = projectileSimulationConfigTabInitVelocitySliderValueVar,
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitVelocitySliderValueLabel.place(relx = 0.355, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Angle (°): ",
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitAngleTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                        justify = LEFT,
                                                                                        textvariable = projectileSimulationConfigTabInitAngleSliderValueVar,
                                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitAngleSliderValueLabel.place(relx = 0.28, rely = 0.3, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          textvariable = projectileSimulationConfigTabInitGravAccSliderValueVar,
                                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.63, rely = 0.5, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Mass (kg): ",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       textvariable = projectileSimulationConfigTabInitMassSliderValueVar,
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.7, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Diameter (m): ",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitDiameterTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = projectileSimulationConfigTabInitDiameterSliderValueVar,
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        projectileSimulationConfigTabInitDiameterSliderValueLabel.place(relx = 0.81, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitDragCoefTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Drag Coefficient: ",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))

        projectileSimulationConfigTabInitDragCoefSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = projectileSimulationConfigTabInitDragCoefSliderValueVar,
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))

    #This line binds an event to the launch button to play a sound when it's hovered
    projectileSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")

def pendulumSimulationConfigTab(bool):
    global pendulumSimulationConfigTabLaunchButton, pendulumSimulationConfigTabInitAngleSlider, pendulumSimulationConfigTabInitAngularVelSlider, pendulumSimulationConfigTabInitLengthSlider, pendulumSimulationConfigTabInitMassSlider, pendulumSimulationConfigTabInitGravAccSlider, pendulumSimulationConfigTabInitDampingCoefSlider
    if bool == True:
        #Here are the frames for each element of the config tab
        pendulumSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 550,
                                                                       height = 300,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        pendulumSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
        
        pendulumSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 335,
                                                                       height = 100,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        pendulumSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)

        pendulumSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                             width = 335,
                                                                             height = 200,
                                                                             corner_radius = 5,
                                                                             border_width = 1)
        pendulumSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)

        pendulumSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 550,
                                                                       height = 265,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        pendulumSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)

        pendulumSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                              width = 335,
                                                                              height = 100,
                                                                              corner_radius = 5,
                                                                              border_width = 1)
        pendulumSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)

        #The buttons go here
        pendulumSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = pendulumSimulationConfigTabLaunchButtonFrame,
                                                                          text = "Launch",
                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                          width = 335,
                                                                          height = 100,
                                                                          corner_radius = 5,
                                                                          border_width = 1,
                                                                          command = pendulumSimulationConfigTabLaunchButtonEvent)
        pendulumSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The configurators (items) of the simulation go here
        pendulumSimulationConfigTabInitAngleSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                height = 20,
                                                                                from_ = -90, 
                                                                                to = 90,
                                                                                corner_radius = 8,
                                                                                command = pendulumSimulationConfigTabInitAngleSliderEvent)
        pendulumSimulationConfigTabInitAngleSlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                  height = 20,
                                                                                  from_ = -0.5, 
                                                                                  to = 0.5,
                                                                                  corner_radius = 8,
                                                                                  command = pendulumSimulationConfigTabInitAngularVelSliderEvent)
        pendulumSimulationConfigTabInitAngularVelSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                 width = 495,
                                                                                 height = 20,
                                                                                 from_ = 0.1, 
                                                                                 to = 1,
                                                                                 corner_radius = 8,
                                                                                 command = pendulumSimulationConfigTabInitLengthSliderEvent)
        pendulumSimulationConfigTabInitLengthSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        pendulumSimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                            width = 495,
                                                                            height = 20,
                                                                            from_ = 0.1, 
                                                                            to = 1.5,
                                                                            corner_radius = 8,
                                                                            command = pendulumSimulationConfigTabInitMassSliderEvent)
        pendulumSimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                               width = 250,
                                                                               height = 20,
                                                                               from_ = 0.1, 
                                                                               to = 20,
                                                                               corner_radius = 8,
                                                                               command = pendulumSimulationConfigTabInitGravAccSliderEvent)
        pendulumSimulationConfigTabInitGravAccSlider.place(relx = 0.48, rely = 0.2, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                   width = 250,
                                                                                   height = 20,
                                                                                   from_ = 0, 
                                                                                   to = 1,
                                                                                   corner_radius = 8,
                                                                                   command = pendulumSimulationConfigTabInitDampingCoefSliderEvent)
        pendulumSimulationConfigTabInitDampingCoefSlider.place(relx = 0.48, rely = 0.4, anchor = tkinter.W)

        #The images of the simulation go here
        pendulumSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = pendulumSimulationConfigTabImageFrame,
                                                                       image = pendulumSimulationPreviewImage,
                                                                       text = "")
        pendulumSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        pendulumSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabTitleFrame,
                                                                       justify = LEFT,
                                                                       text = "Pendulum\nSimulation",
                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        pendulumSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                
        pendulumSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = "Simulates a mass suspended to a fixed point\nswinging back and forth whose initial angle,\nangular velocity, length to the fixed point,\nmass, gravitational acceleration and damping\ncoefficient can be changed.",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        pendulumSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.25, anchor = tkinter.W)

        pendulumSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabDescriptionFrame,
                                                                          justify = LEFT,
                                                                          text = "Field of physics: Newtonian Mechanics",
                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        pendulumSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.59, anchor = tkinter.W)

        pendulumSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabDescriptionFrame,
                                                                              justify = LEFT,
                                                                              text = 'Change the physical properties that you want\nto include then press on "Launch" to start the\nsimulation.',
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        pendulumSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
        pendulumSimulationConfigTabInitAngleTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Angle (°): ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitAngleTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngleSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = pendulumSimulationConfigTabInitAngleSliderValueVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitAngleSliderValueLabel.place(relx = 0.28, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Angular Velocity (rad/s): ",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"))
        pendulumSimulationConfigTabInitAngularVelTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = pendulumSimulationConfigTabInitAngularVelSliderValueVar,
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"))
        pendulumSimulationConfigTabInitAngularVelSliderValueLabel.place(relx = 0.43, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Length (m): ",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitLengthTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       textvariable = pendulumSimulationConfigTabInitLengthSliderValueVar,
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitLengthSliderValueLabel.place(relx = 0.31, rely = 0.5, anchor = tkinter.W)
        
        pendulumSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Mass (kg): ",
                                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        pendulumSimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     textvariable = pendulumSimulationConfigTabInitMassSliderValueVar,
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.7, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 14, weight = "normal"))
        pendulumSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.49, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                        justify = LEFT,
                                                                                        textvariable = pendulumSimulationConfigTabInitGravAccSliderValueVar,
                                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 14, weight = "normal"))
        pendulumSimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.94, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Initial Damping Coefficient: ",
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitDampingCoefTitleLabel.place(relx = 0.49, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                            justify = LEFT,
                                                                                            textvariable = pendulumSimulationConfigTabInitDampingCoefSliderValueVar,
                                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitDampingCoefSliderValueLabel.place(relx = 0.89, rely = 0.3, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    pendulumSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")

def springSimulationConfigTab(bool):
    global springSimulationConfigTabLaunchButton, springSimulationConfigTabInitMassSlider, springSimulationConfigTabInitGravAccSlider, springSimulationConfigTabInitLengthSlider, springSimulationConfigTabInitStiffSlider, springSimulationConfigTabInitDampingCoefSlider
    if bool == True:
        #Here are the frames for each element of the config tab
        springSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                     width = 550,
                                                                     height = 300,
                                                                     corner_radius = 5,
                                                                     border_width = 1)
        springSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)

        springSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                     width = 335,
                                                                     height = 100,
                                                                     corner_radius = 5,
                                                                     border_width = 1)
        springSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)

        springSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                           width = 335,
                                                                           height = 200,
                                                                           corner_radius = 5,
                                                                           border_width = 1)
        springSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
        
        springSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                     width = 550,
                                                                     height = 265,
                                                                     corner_radius = 5,
                                                                     border_width = 1)
        springSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)

        springSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                            width = 335,
                                                                            height = 100,
                                                                            corner_radius = 5,
                                                                            border_width = 1)
        springSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)

        #The buttons go here
        springSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = springSimulationConfigTabLaunchButtonFrame,
                                                                        text = "Launch",
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                        width = 335,
                                                                        height = 100,
                                                                        corner_radius = 5,
                                                                        border_width = 1,
                                                                        command = springSimulationConfigTabLaunchButtonEvent)
        springSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The configurators (items) of the simulation go here
        springSimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                          height = 20,
                                                                          from_ = 0.1, 
                                                                          to = 1,
                                                                          corner_radius = 8,
                                                                          command = springSimulationConfigTabInitMassSliderEvent)
        springSimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                             width = 495,
                                                                             height = 20,
                                                                             from_ = 0.1, 
                                                                             to = 20,
                                                                             corner_radius = 8,
                                                                             command = springSimulationConfigTabInitGravAccSliderEvent)
        springSimulationConfigTabInitGravAccSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        springSimulationConfigTabInitLengthSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                            width = 495,
                                                                            height = 20,
                                                                            from_ = 1, 
                                                                            to = 10,
                                                                            corner_radius = 8,
                                                                            command = springSimulationConfigTabInitLengthSliderEvent)
        springSimulationConfigTabInitLengthSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        springSimulationConfigTabInitStiffSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                           width = 495,
                                                                           height = 20,
                                                                           from_ = 4, 
                                                                           to = 10,
                                                                           corner_radius = 8,
                                                                           command = springSimulationConfigTabInitStiffSliderEvent)
        springSimulationConfigTabInitStiffSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        springSimulationConfigTabInitDampingCoefSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                             width = 250,
                                                                             height = 20,
                                                                             from_ = 0, 
                                                                             to = 1,
                                                                             corner_radius = 8,
                                                                             command = springSimulationConfigTabInitDampingCoefSliderEvent)
        springSimulationConfigTabInitDampingCoefSlider.place(relx = 0.5, rely = 0.2, anchor = tkinter.W)

        #The images of the simulation go here
        springSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = springSimulationConfigTabImageFrame,
                                                                     image = springSimulationPreviewImage,
                                                                     text = "")
        springSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        springSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabTitleFrame,
                                                                     justify = LEFT,
                                                                     text = "Spring\nSimulation",
                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        springSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)

        springSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = springSimulationConfigTabDescriptionFrame,
                                                                           justify = LEFT,
                                                                           text = "Simulates a mass (increasable or decreasable)\nattached to a spring suspended to a fixed point\nunder the influence of gravity whose length,\nstiffness and damping can be changed.",
                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"))
        springSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.2, anchor = tkinter.W)

        springSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = springSimulationConfigTabDescriptionFrame,
                                                                        justify = LEFT,
                                                                        text = "Field of physics: Newtonian Mechanics",
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        springSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.54, anchor = tkinter.W)

        springSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = springSimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = 'Change the physical properties that you want\nto include then press on "Launch" to start the\nsimulation.',
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        springSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        springSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Mass (kg): ",
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        springSimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                   justify = LEFT,
                                                                                   textvariable = springSimulationConfigTabInitMassSliderValueVar,
                                                                                   font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.11, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = springSimulationConfigTabInitGravAccSliderValueVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.63, rely = 0.3, anchor = tkinter.W)
        
        springSimulationConfigTabInitLengthTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Length (cm): ",
                                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitLengthTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        springSimulationConfigTabInitLengthSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     textvariable = springSimulationConfigTabInitLengthSliderValueVar,
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitLengthSliderValueLabel.place(relx = 0.33, rely = 0.5, anchor = tkinter.W)
                
        springSimulationConfigTabInitStiffTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Stiffness (N/m): ",
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitStiffTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        springSimulationConfigTabInitStiffSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    textvariable = springSimulationConfigTabInitStiffSliderValueVar,
                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitStiffSliderValueLabel.place(relx = 0.38, rely = 0.7, anchor = tkinter.W)
        
        springSimulationConfigTabInitDampingCoefTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Initial Damping Coefficient: ",
                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitDampingCoefTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)

        springSimulationConfigTabInitDampingCoefSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          textvariable = springSimulationConfigTabInitDampingCoefSliderValueVar,
                                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        springSimulationConfigTabInitDampingCoefSliderValueLabel.place(relx = 0.91, rely = 0.11, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    springSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")
        
def planetOrbitsSimulationConfigTab(bool):
    global planetConfigValuesList, planetOrbitsSimulationConfigTabLaunchButton, planetOrbitsSimulationConfigTabPlanetNameEntry, planetOrbitsSimulationConfigTabPlanetColorEntry, planetOrbitsSimulationConfigTabPlanetMassEntry, planetOrbitsSimulationConfigTabPlanetRadiusEntry, planetOrbitsSimulationConfigTabPlanetInitialVxSlider, planetOrbitsSimulationConfigTabPlanetInitialVySlider, planetOrbitsSimulationConfigTabPlanetInitialAxSlider, planetOrbitsSimulationConfigTabPlanetInitialAySlider, planetOrbitsSimulationConfigTabShowOrbitTrailSwitch, planetOrbitsSimulationConfigTabShowPlanetNameSwitch
    if bool == True:
        #Function to add & save the infos of the planets on the simulation config values .json file as well as playing a sound
        def planetOrbitsSimulationConfigTabAddPlanetButtonEvent():
            global buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            configValues = {
                "planetName": planetOrbitsSimulationConfigTabPlanetNameEntry.get(),
                "planetColor": planetOrbitsSimulationConfigTabPlanetColorEntry.get(),
                "planetMass": planetOrbitsSimulationConfigTabPlanetMassEntry.get(),
                "planetRadius": planetOrbitsSimulationConfigTabPlanetRadiusEntry.get(),
                "initVx": round(planetOrbitsSimulationConfigTabPlanetInitialVxSlider.get(), 3),
                "initVy": round(planetOrbitsSimulationConfigTabPlanetInitialVySlider.get(), 3),
                "initAx": round(planetOrbitsSimulationConfigTabPlanetInitialAxSlider.get(), 3),
                "initAy": round(planetOrbitsSimulationConfigTabPlanetInitialAySlider.get(), 3),
                "showOrbitTrail": planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.get(),
                "showPlanetName": planetOrbitsSimulationConfigTabShowPlanetNameSwitch.get()
            }
            planetConfigValuesList.append(configValues)
            planetOrbitsSimulationConfigTabPlanetNameEntry.set("")
            planetOrbitsSimulationConfigTabPlanetColorEntry.set("")
            planetOrbitsSimulationConfigTabPlanetMassEntry.set("")
            planetOrbitsSimulationConfigTabPlanetRadiusEntry.set("")
            planetOrbitsSimulationConfigTabPlanetInitialVxSlider.set(0)
            planetOrbitsSimulationConfigTabPlanetInitialVySlider.set(0)
            planetOrbitsSimulationConfigTabPlanetInitialAxSlider.set(0)
            planetOrbitsSimulationConfigTabPlanetInitialAySlider.set(0)
            planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.set("False")
            planetOrbitsSimulationConfigTabShowPlanetNameSwitch.set("False")
        
        #The frames for each element of the tab go here
        planetOrbitsSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                           width = 550,
                                                                           height = 300,
                                                                           corner_radius = 5,
                                                                           border_width = 1)
        planetOrbitsSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
        
        planetOrbitsSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                           width = 335,
                                                                           height = 100,
                                                                           corner_radius = 5,
                                                                           border_width = 1)
        planetOrbitsSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)

        planetOrbitsSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                 width = 335,
                                                                                 height = 200,
                                                                                 corner_radius = 5,
                                                                                 border_width = 1)
        planetOrbitsSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)

        planetOrbitsSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                           width = 550,
                                                                           height = 265,
                                                                           corner_radius = 5,
                                                                           border_width = 1)
        planetOrbitsSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                  width = 335,
                                                                                  height = 100,
                                                                                  corner_radius = 5,
                                                                                  border_width = 1)
        planetOrbitsSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
        
        #The buttons go here
        planetOrbitsSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = planetOrbitsSimulationConfigTabLaunchButtonFrame,
                                                                              text = "Launch",
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                              width = 335,
                                                                              height = 100,
                                                                              corner_radius = 5,
                                                                              border_width = 1,
                                                                              command = planetOrbitsSimulationConfigTabLaunchButtonEvent)
        planetOrbitsSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        planetOrbitsSimulationConfigTabAddPlanetButton = customtkinter.CTkButton(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                 text = "+ Add",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"),
                                                                                 width = 50,
                                                                                 height = 25,
                                                                                 corner_radius = 5,
                                                                                 border_width = 1,
                                                                                 command = planetOrbitsSimulationConfigTabAddPlanetButtonEvent)
        planetOrbitsSimulationConfigTabAddPlanetButton.place(relx = 0.01, rely = 0.08, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabResetPlanetListButton = customtkinter.CTkButton(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       text = "Reset Planet List",
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"),
                                                                                       width = 50,
                                                                                       height = 25,
                                                                                       corner_radius = 5,
                                                                                       border_width = 1,
                                                                                       command = planetOrbitsSimulationConfigTabResetPlanetListButtonEvent)
        planetOrbitsSimulationConfigTabResetPlanetListButton.place(relx = 0.64, rely = 0.08, anchor = tkinter.W)

        #The configurators (items) of the simulation go here
        planetOrbitsSimulationConfigTabPlanetNameEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                 width = 150,
                                                                                 height = 25,
                                                                                 placeholder_text = "Planet Name",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                                 corner_radius = 5,
                                                                                 border_width = 1)
        planetOrbitsSimulationConfigTabPlanetNameEntry.place(relx = 0.01, rely = 0.39, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetColorEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                 width = 150,
                                                                                 height = 25,
                                                                                 placeholder_text = "This form: R, G, B",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"),
                                                                                 corner_radius = 5,
                                                                                 border_width = 1)
        planetOrbitsSimulationConfigTabPlanetColorEntry.place(relx = 0.01, rely = 0.64, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetMassEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                width = 150,
                                                                                height = 25,
                                                                                placeholder_text = 'Enter the whole number',
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 14, weight = "normal"),
                                                                                corner_radius = 5,
                                                                                border_width = 1)
        planetOrbitsSimulationConfigTabPlanetMassEntry.place(relx = 0.01, rely = 0.89, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetRadiusEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                  width = 150,
                                                                                  height = 25,
                                                                                  placeholder_text = "No massive radii",
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 14, weight = "normal"),
                                                                                  corner_radius = 5,
                                                                                  border_width = 1)
        planetOrbitsSimulationConfigTabPlanetRadiusEntry.place(relx = 0.35, rely = 0.39, anchor = tkinter.W)
        
        planetOrbitsSimulationConfigTabPlanetInitialVxSlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       height = 20,
                                                                                       from_ = -0.005,
                                                                                       to = 0.005,
                                                                                       corner_radius = 5,
                                                                                       command = planetOrbitsSimulationConfigTabPlanetInitialVxSliderEvent)
        planetOrbitsSimulationConfigTabPlanetInitialVxSlider.place(relx = 0.35, rely = 0.64, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                      width = 150,
                                                                                      height = 20,
                                                                                      from_ = -0.005,
                                                                                      to = 0.005,
                                                                                      corner_radius = 5,
                                                                                      command = planetOrbitsSimulationConfigTabPlanetInitialVySliderEvent)
        planetOrbitsSimulationConfigTabPlanetInitialVySlider.place(relx = 0.35, rely = 0.89, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       height = 20,
                                                                                       from_ = -0.005,
                                                                                       to = 0.005,
                                                                                       corner_radius = 5,
                                                                                       command = planetOrbitsSimulationConfigTabPlanetInitialAxSliderEvent)
        planetOrbitsSimulationConfigTabPlanetInitialAxSlider.place(relx = 0.68, rely = 0.39, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       height = 20,
                                                                                       from_ = -0.005,
                                                                                       to = 0.005,
                                                                                       corner_radius = 5,
                                                                                       command = planetOrbitsSimulationConfigTabPlanetInitialAySliderEvent)
        planetOrbitsSimulationConfigTabPlanetInitialAySlider.place(relx = 0.68, rely = 0.6, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabShowOrbitTrailSwitch = customtkinter.CTkSwitch(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 50,
                                                                                       height = 50,
                                                                                       bg_color = "transparent",
                                                                                       text = "Show Orbit Trail",
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                       onvalue = True,
                                                                                       offvalue = False,
                                                                                       variable = planetOrbitsSimulationConfigTabShowOrbitTrailSwitchVar,
                                                                                       command = planetOrbitsSimulationConfigTabShowOrbitTrailSwitchEvent)
        planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.place(relx = 0.68, rely = 0.74, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabShowPlanetNameSwitch = customtkinter.CTkSwitch(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                      width = 50,
                                                                                      height = 50,
                                                                                      bg_color = "transparent",
                                                                                      text = "Show Planet Name",
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                      onvalue = True,
                                                                                      offvalue = False,
                                                                                      variable = planetOrbitsSimulationConfigTabShowPlanetNameSwitchVar,
                                                                                      command = planetOrbitsSimulationConfigTabShowPlanetNameSwitchEvent)
        planetOrbitsSimulationConfigTabShowPlanetNameSwitch.place(relx = 0.68, rely = 0.89, anchor = tkinter.W)

        #The images of the simulation go here
        planetOrbitsSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabImageFrame,
                                                                           image = planetOrbitsSimulationPreviewImage,
                                                                           text = "")
        planetOrbitsSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        planetOrbitsSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabTitleFrame,
                                                                             justify = LEFT,
                                                                             text = "Planet\nOrbits",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        planetOrbitsSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabDescriptionFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Solves the N-body problem to simulate your\nfavorite planets but also your own ones by\nadding their name, color, mass, radius, initial\nvelocity and initial acceleration.",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.2, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabDescriptionFrame,
                                                                              justify = LEFT,
                                                                              text = "Field of physics: Newtonian Mechanics",
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.54, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabDescriptionFrame,
                                                                                    justify = LEFT,
                                                                                    text = 'Edit the given values of the planets that\nyou want, press on the "+ ADD" button to add the\nplanet and click on "Launch" start the simulation.',
                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"))
        planetOrbitsSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetNameEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Name:",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetNameEntryTitle.place(relx = 0.011, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetColorEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Color:",
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetColorEntryTitle.place(relx = 0.011, rely = 0.52, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetMassEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Mass (kg):",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetMassEntryTitle.place(relx = 0.011, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetRadiusEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       text = "Radius (m):",
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetRadiusEntryTitle.place(relx = 0.35, rely = 0.27, anchor = tkinter.W)
        
        planetOrbitsSimulationConfigTabPlanetInitialVxSliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          text = "Initial Vx (m/s):",
                                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVxSliderTitle.place(relx = 0.35, rely = 0.52, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueVar,
                                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueLabel.place(relx = 0.56, rely = 0.52, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial Vy (m/s):",
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVySliderTitle.place(relx = 0.35, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialVySliderValueVar,
                                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVySliderValueLabel.place(relx = 0.56, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          text = "Initial ax (m/s²):",
                                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAxSliderTitle.place(relx = 0.68, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueVar,
                                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueLabel.place(relx = 0.9, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial ay (m/s²):",
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAySliderTitle.place(relx = 0.68, rely = 0.48, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialAySliderValueVar,
                                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAySliderValueLabel.place(relx = 0.9, rely = 0.48, anchor = tkinter.W)
    #These lines bind events to the buttons of the tab to play a sound when they are hovered
    planetOrbitsSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")
    planetOrbitsSimulationConfigTabAddPlanetButton.bind("<Enter>", onButtonHover, add = "+")
    planetOrbitsSimulationConfigTabResetPlanetListButton.bind("<Enter>", onButtonHover, add = "+")

def gravitySimulationConfigTab(bool):
    global gravitySimulationConfigTabLaunchButton, gravitySimulationConfigTabInitMassSlider, gravitySimulationConfigTabInitGravAccSlider, gravitySimulationConfigTabInitHeightSlider
    if bool == True:
        #The frames for each element of the tab go here
        gravitySimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                      width = 550,
                                                                      height = 300,
                                                                      corner_radius = 5,
                                                                      border_width = 1)
        gravitySimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                
        gravitySimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                      width = 335,
                                                                      height = 100,
                                                                      corner_radius = 5,
                                                                      border_width = 1)
        gravitySimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
        
        gravitySimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                            width = 335,
                                                                            height = 200,
                                                                            corner_radius = 5,
                                                                            border_width = 1)
        gravitySimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
        
        gravitySimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                      width = 550,
                                                                      height = 265,
                                                                      corner_radius = 5,
                                                                      border_width = 1)
        gravitySimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
        
        gravitySimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                             width = 335,
                                                                             height = 100,
                                                                             corner_radius = 5,
                                                                             border_width = 1)
        gravitySimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
        
        #The buttons go here
        gravitySimulationConfigTabLaunchButton = customtkinter.CTkButton(master = gravitySimulationConfigTabLaunchButtonFrame,
                                                                         text = "Launch",
                                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                         width = 335,
                                                                         height = 100,
                                                                         corner_radius = 5,
                                                                         border_width = 1,
                                                                         command = gravitySimulationConfigTabLaunchButtonEvent)
        gravitySimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The configurators (items) of the simulation go here
        gravitySimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = gravitySimulationConfigTabItemsFrame,
                                                                              width = 495,
                                                                              height = 20,
                                                                              from_ = 1,
                                                                              to = 1000,
                                                                              command = gravitySimulationConfigTabInitMassSliderEvent)
        gravitySimulationConfigTabInitMassSlider.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = gravitySimulationConfigTabItemsFrame,
                                                                              width = 495,
                                                                              height = 20,
                                                                              from_ = 0.1,
                                                                              to = 20,
                                                                              command = gravitySimulationConfigTabInitGravAccSliderEvent)
        gravitySimulationConfigTabInitGravAccSlider.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightSlider = customtkinter.CTkSlider(master = gravitySimulationConfigTabItemsFrame,
                                                                             width = 495,
                                                                             height = 20,
                                                                             from_ = 0.1,
                                                                             to = 10,
                                                                             command = gravitySimulationConfigTabInitHeightSliderEvent)
        gravitySimulationConfigTabInitHeightSlider.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)

        #The images of the simulation go here
        gravitySimulationConfigTabInSimImage = customtkinter.CTkLabel(master = gravitySimulationConfigTabImageFrame,
                                                                           image = gravitySimulationPreviewImage,
                                                                           text = "")
        gravitySimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        gravitySimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabTitleFrame,
                                                                      justify = LEFT,
                                                                      text = "Gravity\nSimulation",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        gravitySimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        gravitySimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = "Simulates an object of a changeable mass\nfalling under the influence of gravity at a\nspecific height.",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        gravitySimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
        
        gravitySimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabDescriptionFrame,
                                                                         justify = LEFT,
                                                                         text = "Field of physics: Newtonian Mechanics",
                                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        gravitySimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.52, anchor = tkinter.W)
        
        gravitySimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = 'Change the physical properties that you want\nto include then press on "Launch" to start the\nsimulation.',
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        gravitySimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        gravitySimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Mass (kg): ",
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        gravitySimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        gravitySimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    textvariable = gravitySimulationConfigTabInitMassSliderValueVar,
                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        gravitySimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.11, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        gravitySimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       textvariable = gravitySimulationConfigTabInitGravAccSliderValueVar,
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        gravitySimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.63, rely = 0.38, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Height (m): ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        gravitySimulationConfigTabInitHeightTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightSliderValueLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = gravitySimulationConfigTabInitHeightSliderValueVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        gravitySimulationConfigTabInitHeightSliderValueLabel.place(relx = 0.31, rely = 0.66, anchor = tkinter.W)
    
    #This line binds an event to the launch button to play a sound when it's hovered
    gravitySimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")
        
def refractionSimulationConfigTab(bool):
    global refractionSimulationConfigTabLaunchButton, refractionSimulationConfigInitRefractiveIndex1OptionMenu, refractionSimulationConfigInitRefractiveIndex2OptionMenu, refractionSimulationConfigTabInitIncidenceAngleSlider, refractionSimulationConfigTabRayColorOptionMenu, refractionSimulationConfigInitRefractiveIndex1CustomEntry, refractionSimulationConfigInitRefractiveIndex2CustomEntry
    if bool == True:
        #Thse functions show a text entry if the "Custom" option from the option menus are selected
        def refractionSimulationConfigInitRefractiveIndex1OptionMenuEvent(value):
            if value == "Custom":
                refractionSimulationConfigInitRefractiveIndex1CustomEntry.place(relx = 0.38, rely = 0.23, anchor = tkinter.W)
            else:
                refractionSimulationConfigInitRefractiveIndex1CustomEntry.place_forget()

        def refractionSimulationConfigInitRefractiveIndex2OptionMenuEvent(value):
            if value == "Custom":
                refractionSimulationConfigInitRefractiveIndex2CustomEntry.place(relx = 0.38, rely = 0.5, anchor = tkinter.W)
            else:
                refractionSimulationConfigInitRefractiveIndex2CustomEntry.place_forget()

        #The frames for each element of the tab go here
        refractionSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 550,
                                                                         height = 300,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        refractionSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                        
        refractionSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 335,
                                                                         height = 100,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        refractionSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                
        refractionSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                               width = 335,
                                                                               height = 200,
                                                                               corner_radius = 5,
                                                                               border_width = 1)
        refractionSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                
        refractionSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 550,
                                                                         height = 265,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        refractionSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                
        refractionSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                width = 335,
                                                                                height = 100,
                                                                                corner_radius = 5,
                                                                                border_width = 1)
        refractionSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
        
        #The buttons go here
        refractionSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = refractionSimulationConfigTabLaunchButtonFrame,
                                                                            text = "Launch",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                            width = 335,
                                                                            height = 100,
                                                                            corner_radius = 5,
                                                                            border_width = 1,
                                                                            command = refractionSimulationConfigTabLaunchButtonEvent)
        refractionSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The configurators (items) of the simulation go here
        refractionSimulationConfigInitRefractiveIndex1OptionMenu = customtkinter.CTkOptionMenu(master = refractionSimulationConfigTabItemsFrame,
                                                                                               width = 150,
                                                                                               height = 25,
                                                                                               variable = refractionSimulationConfigTabInitRefractiveIndex1OptionMenuVar,
                                                                                               font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                               values = ["Air (1.0)", "Water (1.33)", "Glass (1.52)", "Ethanol (1.36)", "Diamond (2.417)", "Plastic (1.59)", "Custom"],
                                                                                               command = refractionSimulationConfigInitRefractiveIndex1OptionMenuEvent)
        refractionSimulationConfigInitRefractiveIndex1OptionMenu.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)

        refractionSimulationConfigInitRefractiveIndex2OptionMenu = customtkinter.CTkOptionMenu(master = refractionSimulationConfigTabItemsFrame,
                                                                                               width = 150,
                                                                                               height = 25,
                                                                                               variable = refractionSimulationConfigTabInitRefractiveIndex2OptionMenuVar,
                                                                                               font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                               values = ["Air (1.0)", "Water (1.33)", "Glass (1.52)", "Ethanol (1.36)", "Diamond (2.417)", "Plastic (1.59)", "Custom"],
                                                                                               command = refractionSimulationConfigInitRefractiveIndex2OptionMenuEvent)
        refractionSimulationConfigInitRefractiveIndex2OptionMenu.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        refractionSimulationConfigTabInitIncidenceAngleSlider = customtkinter.CTkSlider(master = refractionSimulationConfigTabItemsFrame,
                                                                                        width = 495,
                                                                                        height = 20,
                                                                                        from_ = 0,
                                                                                        to = 90,
                                                                                        command = refractionSimulationConfigTabInitIncidenceAngleSliderEvent)
        refractionSimulationConfigTabInitIncidenceAngleSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        refractionSimulationConfigTabRayColorOptionMenu = customtkinter.CTkOptionMenu(master = refractionSimulationConfigTabItemsFrame,
                                                                                      width = 150,
                                                                                      height = 25,
                                                                                      variable = refractionSimulationConfigRayColorOptionMenuVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                      values = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"])
        refractionSimulationConfigTabRayColorOptionMenu.place(relx = 0.7, rely = 0.23, anchor = tkinter.W)

        refractionSimulationConfigInitRefractiveIndex1CustomEntry = customtkinter.CTkEntry(master = refractionSimulationConfigTabItemsFrame,
                                                                                           placeholder_text = "Float between 1.0 and 2",
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                           width = 150,
                                                                                           height = 25,
                                                                                           corner_radius = 5,
                                                                                           border_width = 1)

        refractionSimulationConfigInitRefractiveIndex2CustomEntry = customtkinter.CTkEntry(master = refractionSimulationConfigTabItemsFrame,
                                                                                           placeholder_text = "Float between 1.0 and 2",
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                           width = 150,
                                                                                           height = 25,
                                                                                           corner_radius = 5,
                                                                                           border_width = 1)
        
        #The images of the simulation go here
        refractionSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = refractionSimulationConfigTabImageFrame,
                                                                         image = refractionSimulationPreviewImage,
                                                                         text = "")
        refractionSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        refractionSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabTitleFrame,
                                                                         justify = LEFT,
                                                                         text = "Refraction\nSimulation",
                                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        refractionSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                
        refractionSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabDescriptionFrame,
                                                                               justify = LEFT,
                                                                               text = "Simulates a ray of light whose initial angle\nand color can be changed passing through\ntwo refractive mediums of specific\nrefractive indexes based on the Snell-Descartes\nlaw.",
                                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"))
        refractionSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.25, anchor = tkinter.W)
                
        refractionSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = "Field of physics: Optics",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        refractionSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.59, anchor = tkinter.W)

        refractionSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabDescriptionFrame,
                                                                                justify = LEFT,
                                                                                text = 'Select or change the physical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        refractionSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
        refractionSimulationConfigTabInitRefractiveIndex1TitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                             justify = LEFT,
                                                                                             text = "Initial Refractive Index 1: ",
                                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        refractionSimulationConfigTabInitRefractiveIndex1TitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        refractionSimulationConfigTabInitRefractiveIndex2TitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                             justify = LEFT,
                                                                                             text = "Initial Refractive Index 2: ",
                                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        refractionSimulationConfigTabInitRefractiveIndex2TitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)
        
        refractionSimulationConfigTabInitIncidenceAngleTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial Incidence Angle (°): ",
                                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        refractionSimulationConfigTabInitIncidenceAngleTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        refractionSimulationConfigTabInitIncidenceAngleSliderValueLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                                 justify = LEFT,
                                                                                                 textvariable = refractionSimulationConfigTabInitIncidenceAngleSliderValueVar,
                                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        refractionSimulationConfigTabInitIncidenceAngleSliderValueLabel.place(relx = 0.43, rely = 0.66, anchor = tkinter.W)

        refractionSimulationConfigTabRayColorTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Ray Color: ",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        refractionSimulationConfigTabRayColorTitleLabel.place(relx = 0.7, rely = 0.11, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered    
    refractionSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")
        
def fluidSimulationConfigTab(bool):
    if bool == True:
        #These functions show a text entry if the "Custom" option from the option menus are selected
        def fluidSimulationConfigInitDensityOptionMenuEvent(value):
            if value == "Custom":
                fluidSimulationConfigInitDensityCustomEntry.place(relx = 0.33, rely = 0.5, anchor = tkinter.W)
            else:
                fluidSimulationConfigInitDensityCustomEntry.place_forget()

        def fluidSimulationConfigInitViscosityOptionMenuEvent(value):
            if value == "Custom":
                fluidSimulationConfigInitViscosityCustomEntry.place(relx = 0.33, rely = 0.8, anchor = tkinter.W)
            else:
                fluidSimulationConfigInitViscosityCustomEntry.place_forget()

        #The frames for each element of the tab go here
        fluidSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                    width = 550,
                                                                    height = 300,
                                                                    corner_radius = 5,
                                                                    border_width = 1)
        fluidSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                
        fluidSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                    width = 335,
                                                                    height = 100,
                                                                    corner_radius = 5,
                                                                    border_width = 1)
        fluidSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                        
        fluidSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                          width = 335,
                                                                          height = 200,
                                                                          corner_radius = 5,
                                                                          border_width = 1)
        fluidSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                        
        fluidSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                    width = 550,
                                                                    height = 265,
                                                                    corner_radius = 5,
                                                                    border_width = 1)
        fluidSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                        
        fluidSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                           width = 335,
                                                                           height = 100,
                                                                           corner_radius = 5,
                                                                           border_width = 1)
        fluidSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                
        #The buttons go here
        fluidSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = fluidSimulationConfigTabLaunchButtonFrame,
                                                                       text = "Launch",
                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                       width = 335,
                                                                       height = 100,
                                                                       corner_radius = 5,
                                                                       border_width = 1,
                                                                       command = fluidSimulationConfigTabLaunchButtonEvent)
        fluidSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)        
        
        #The configurators (items) of the simulation go here
        fluidSimulationConfigTabInitVolumeSlider = customtkinter.CTkSlider(master = fluidSimulationConfigTabItemsFrame,
                                                                           width = 150,
                                                                           height = 20,
                                                                           from_ = 0.1,
                                                                           to = 5,
                                                                           command = fluidSimulationConfigTabInitVolumeSliderEvent)
        fluidSimulationConfigTabInitVolumeSlider.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)

        fluidSimulationConfigInitDensityOptionMenu = customtkinter.CTkOptionMenu(master = fluidSimulationConfigTabItemsFrame,
                                                                                 width = 150,
                                                                                 height = 25,
                                                                                 variable = fluidSimulationConfigInitDensityOptionMenuVar,
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                 values = ["Water", "Honey", "Olive Oil", "Ethanol", "Iced Tea", "Chocolate Milk", "Custom"],
                                                                                 command = fluidSimulationConfigInitDensityOptionMenuEvent)
        fluidSimulationConfigInitDensityOptionMenu.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        fluidSimulationConfigInitDensityCustomEntry = customtkinter.CTkEntry(master = fluidSimulationConfigTabItemsFrame,
                                                                             placeholder_text = "Between 0.1 and 3",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                             width = 120,
                                                                             height = 25,
                                                                             corner_radius = 5,
                                                                             border_width = 1)        

        fluidSimulationConfigInitViscosityOptionMenu = customtkinter.CTkOptionMenu(master = fluidSimulationConfigTabItemsFrame,
                                                                                   width = 150,
                                                                                   height = 25,
                                                                                   variable = fluidSimulationConfigInitViscosityOptionMenuVar,
                                                                                   font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                   values = ["Water", "Honey", "Olive Oil", "Ethanol", "Iced Tea", "Chocolate Milk", "Custom"],
                                                                                   command = fluidSimulationConfigInitViscosityOptionMenuEvent)
        fluidSimulationConfigInitViscosityOptionMenu.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)

        fluidSimulationConfigInitViscosityCustomEntry = customtkinter.CTkEntry(master = fluidSimulationConfigTabItemsFrame,
                                                                               placeholder_text = "Between 0.1 and 1",
                                                                               font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                               width = 120,
                                                                               height = 25,
                                                                               corner_radius = 5,
                                                                               border_width = 1)

        fluidSimulationConfigTabInitPressureSlider = customtkinter.CTkSlider(master = fluidSimulationConfigTabItemsFrame,
                                                                             width = 150,
                                                                             height = 20,
                                                                             from_ = 0.1,
                                                                             to = 100,
                                                                             command = fluidSimulationConfigTabInitPressureSliderEvent)
        fluidSimulationConfigTabInitPressureSlider.place(relx = 0.6, rely = 0.23, anchor = tkinter.W)

        fluidSimulationConfigInitColorOptionMenu = customtkinter.CTkOptionMenu(master = fluidSimulationConfigTabItemsFrame,
                                                                               width = 150,
                                                                               height = 25,
                                                                               variable = fluidSimulationConfigInitColorOptionMenuVar,
                                                                               font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                               values = ["Water", "Honey", "Olive Oil", "Ethanol", "Iced Tea", "Chocolate Milk"])
        fluidSimulationConfigInitColorOptionMenu.place(relx = 0.6, rely = 0.5, anchor = tkinter.W) 

        fluidSimulationConfigTabShowLatticeSwitch = customtkinter.CTkSwitch(master = fluidSimulationConfigTabItemsFrame,
                                                                            width = 50,
                                                                            height = 50,
                                                                            bg_color = "transparent",
                                                                            text = "Show Lattice",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                            onvalue = "on",
                                                                            offvalue = "off",
                                                                            variable = fluidSimulationConfigTabShowLatticeSwitchVar,
                                                                            command = fluidSimulationConfigTabShowLatticeSwitchEvent)
        fluidSimulationConfigTabShowLatticeSwitch.place(relx = 0.6, rely = 0.75, anchor = tkinter.W)

        #The images of the simulation go here
        fluidSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = fluidSimulationConfigTabImageFrame,
                                                                    image = placeholderImage,
                                                                    text = "")
        fluidSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)        
        
        #The labels of the config tab go here
        fluidSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabTitleFrame,
                                                                    justify = LEFT,
                                                                    text = "Fluid\nSimulation",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        fluidSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                        
        fluidSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabDescriptionFrame,
                                                                          justify = LEFT,
                                                                          text = "Simulates a fluid whose physical properties\nsuch as its volume, density, viscosity and\npressure can be changed.",
                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        fluidSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                        
        fluidSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabDescriptionFrame,
                                                                       justify = LEFT,
                                                                       text = "Field of physics: Fluid Mechanics & CFD",
                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        fluidSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        fluidSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabDescriptionFrame,
                                                                           justify = LEFT,
                                                                           text = 'Select or change the physical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                           font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        fluidSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        fluidSimulationConfigTabInitVolumeTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Volume (L): ",
                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitVolumeTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitVolumeSliderValueLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    textvariable = fluidSimulationConfigTabInitVolumeSliderValueVar,
                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitVolumeSliderValueLabel.place(relx = 0.31, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitDensityTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Density (kg/m³): ",
                                                                               font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitDensityTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)

        fluidSimulationConfigTabInitViscosityTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Viscosity: ",
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitViscosityTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        fluidSimulationConfigTabInitPressureTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Pressure (Pa): ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitPressureTitleLabel.place(relx = 0.6, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitPressureSliderValueLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = fluidSimulationConfigTabInitPressureSliderValueVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitPressureSliderValueLabel.place(relx = 0.9, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitColorTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                             justify = LEFT,
                                                                             text = "Initial Color: ",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        fluidSimulationConfigTabInitColorTitleLabel.place(relx = 0.6, rely = 0.38, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    fluidSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")
        
def temperatureSimulationConfigTab(bool):
    global temperatureSimulationConfigTabLaunchButton, temperatureSimulationConfigTabInitParticleNumberSlider, temperatureSimulationConfigTabInitParticleDiameterSlider, temperatureSimulationConfigTabInitTempSlider
    if bool == True:
        #The frames for each element of the tab go here
        temperatureSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                          width = 550,
                                                                          height = 300,
                                                                          corner_radius = 5,
                                                                          border_width = 1)
        temperatureSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                        
        temperatureSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                          width = 335,
                                                                          height = 100,
                                                                          corner_radius = 5,
                                                                          border_width = 1)
        temperatureSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                
        temperatureSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                width = 335,
                                                                                height = 200,
                                                                                corner_radius = 5,
                                                                                border_width = 1)
        temperatureSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                
        temperatureSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                          width = 550,
                                                                          height = 265,
                                                                          corner_radius = 5,
                                                                          border_width = 1)
        temperatureSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                
        temperatureSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                 width = 335,
                                                                                 height = 100,
                                                                                 corner_radius = 5,
                                                                                 border_width = 1)
        temperatureSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                        
        #The buttons go here
        temperatureSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = temperatureSimulationConfigTabLaunchButtonFrame,
                                                                             text = "Launch",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                             width = 335,
                                                                             height = 100,
                                                                             corner_radius = 5,
                                                                             border_width = 1,
                                                                             command = temperatureSimulationConfigTabLaunchButtonEvent)
        temperatureSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                  
                
        #The configurators (items) of the simulation go here
        temperatureSimulationConfigTabInitParticleNumberSlider = customtkinter.CTkSlider(master = temperatureSimulationConfigTabItemsFrame,
                                                                                         width = 495,
                                                                                         height = 20,
                                                                                         from_ = 1,
                                                                                         to = 1000,
                                                                                         command = temperatureSimulationConfigTabInitParticleNumberSliderEvent)
        temperatureSimulationConfigTabInitParticleNumberSlider.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)     

        temperatureSimulationConfigTabInitParticleDiameterSlider = customtkinter.CTkSlider(master = temperatureSimulationConfigTabItemsFrame,
                                                                                           width = 495,
                                                                                           height = 20,
                                                                                           from_ = 1,
                                                                                           to = 5,
                                                                                           command = temperatureSimulationConfigTabInitParticleDiameterSliderEvent)
        temperatureSimulationConfigTabInitParticleDiameterSlider.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        temperatureSimulationConfigTabInitTempSlider = customtkinter.CTkSlider(master = temperatureSimulationConfigTabItemsFrame,
                                                                               width = 495,
                                                                               height = 20,
                                                                               from_ = -273.15,
                                                                               to = 1500,
                                                                               command = temperatureSimulationConfigTabInitTempSliderEvent)
        temperatureSimulationConfigTabInitTempSlider.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)             
                
        #The images of the simulation go here
        temperatureSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = temperatureSimulationConfigTabImageFrame,
                                                                          image = temperatureSimulationPreviewImage,
                                                                          text = "")
        temperatureSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)        
                                
        #The labels of the config tab go here
        temperatureSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabTitleFrame,
                                                                          justify = LEFT,
                                                                          text = "Temperature\nSimulation",
                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        temperatureSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                                
        temperatureSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabDescriptionFrame,
                                                                                justify = LEFT,
                                                                                text = "Simulates a large number of customizable\nparticles interacting with each other under the\ninfluence of heat or cold.",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        temperatureSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                                
        temperatureSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = "Field of physics: Thermodynamics",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        temperatureSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                
        temperatureSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabDescriptionFrame,
                                                                                 justify = LEFT,
                                                                                 text = 'Change the physical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        temperatureSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
        temperatureSimulationConfigTabInitParticleNumberTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                            justify = LEFT,
                                                                                            text = "Initial Particle Number: ",
                                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleNumberTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        temperatureSimulationConfigTabInitParticleNumberSliderValueLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                                  justify = LEFT,
                                                                                                  textvariable = temperatureSimulationConfigTabInitParticleNumberSliderValueVar,
                                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleNumberSliderValueLabel.place(relx = 0.39, rely = 0.11, anchor = tkinter.W)

        temperatureSimulationConfigTabInitParticleDiameterTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                              justify = LEFT,
                                                                                              text = "Initial Particle Diameter (µm): ",
                                                                                              font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleDiameterTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)

        temperatureSimulationConfigTabInitParticleDiameterSliderValueLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                                    justify = LEFT,
                                                                                                    textvariable = temperatureSimulationConfigTabInitParticleDiameterSliderValueVar,
                                                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleDiameterSliderValueLabel.place(relx = 0.48, rely = 0.38, anchor = tkinter.W)

        temperatureSimulationConfigTabInitTempTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Temperature (°C): ",
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitTempTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        temperatureSimulationConfigTabInitTempSliderValueLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                        justify = LEFT,
                                                                                        textvariable = temperatureSimulationConfigTabInitTempSliderValueVar,
                                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitTempSliderValueLabel.place(relx = 0.41, rely = 0.66, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    temperatureSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")

#The sub tabs of the chemistry tab (chemistry simulations) are here
def bohrAtomSimulationConfigTab(bool):
    global bohrAtomSimulationConfigTabLaunchButton
    if bool == True:
        #The following lines play a sound, disable the rest of the element buttons and define an atom index for some atoms from the Periodic Table when clicked
        def bohrAtomSimulationConfigTabHButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 0
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabHeButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 1
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabLiButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 2
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabBeButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 3
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabBButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 4
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabCButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 5
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabNButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 6
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabOButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 7
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabFButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 8
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabNeButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 9
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabNaButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick 
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 10
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabMgButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 11
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabAlButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick 
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 12
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabSiButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 13
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabPButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 14
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabSButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected, bohrAtomSimulationConfigTabAtomSelectionIndex, buttonClick 
            buttonClick += 1
            buttonClickSound(buttonClick)
            if bohrAtomSimulationConfigTabAtomSelected == True:
                bohrAtomSimulationConfigTabHButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabHeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabLiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabBButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabCButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabOButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabFButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNeButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabNaButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabMgButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAlButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSiButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabPButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabSButton.configure(state = "disabled")
                bohrAtomSimulationConfigTabAtomSelectionIndex = 15
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True  
        
        #The frames for each element of the tab go here
        bohrAtomSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 550,
                                                                       height = 300,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        bohrAtomSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                
        bohrAtomSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 335,
                                                                       height = 100,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        bohrAtomSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                        
        bohrAtomSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                             width = 335,
                                                                             height = 200,
                                                                             corner_radius = 5,
                                                                             border_width = 1)
        bohrAtomSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                        
        bohrAtomSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 550,
                                                                       height = 265,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        bohrAtomSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                        
        bohrAtomSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                              width = 335,
                                                                              height = 100,
                                                                              corner_radius = 5,
                                                                              border_width = 1)
        bohrAtomSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                
        #The buttons go here
        bohrAtomSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabLaunchButtonFrame,
                                                                          text = "Launch",
                                                                          font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                          width = 335,
                                                                          height = 100,
                                                                          corner_radius = 5,
                                                                          border_width = 1,
                                                                          fg_color = "green",
                                                                          command = bohrAtomSimulationConfigTabLaunchButtonEvent)
        bohrAtomSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                            
                        
        #The configurators (items) of the simulation go here
        bohrAtomSimulationConfigTabHButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "1       \n   H\n1       ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabHButtonEvent)
        bohrAtomSimulationConfigTabHButton.place(relx = 0.1, rely = 0.2, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabHeButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "4       \n   He\n2       ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabHeButtonEvent)
        bohrAtomSimulationConfigTabHeButton.place(relx = 0.843, rely = 0.2, anchor = tkinter.CENTER)   

        bohrAtomSimulationConfigTabLiButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "7       \n   Li\n3       ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabLiButtonEvent)
        bohrAtomSimulationConfigTabLiButton.place(relx = 0.1, rely = 0.5, anchor = tkinter.CENTER) 

        bohrAtomSimulationConfigTabBeButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "9       \n   Be\n4       ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabBeButtonEvent)
        bohrAtomSimulationConfigTabBeButton.place(relx = 0.223, rely = 0.5, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabBButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "11     \n  B\n5    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabBButtonEvent)
        bohrAtomSimulationConfigTabBButton.place(relx = 0.347, rely = 0.5, anchor = tkinter.CENTER)           

        bohrAtomSimulationConfigTabCButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "12     \n  C\n6    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabCButtonEvent)
        bohrAtomSimulationConfigTabCButton.place(relx = 0.47, rely = 0.5, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabNButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "14     \n  N\n7    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabNButtonEvent)
        bohrAtomSimulationConfigTabNButton.place(relx = 0.595, rely = 0.5, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabOButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "16     \n  O\n8    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabOButtonEvent)
        bohrAtomSimulationConfigTabOButton.place(relx = 0.719, rely = 0.5, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabFButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "19     \n  F\n9    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabFButtonEvent)
        bohrAtomSimulationConfigTabFButton.place(relx = 0.842, rely = 0.5, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabNeButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "20     \n  Ne\n10    ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabNeButtonEvent)
        bohrAtomSimulationConfigTabNeButton.place(relx = 0.1, rely = 0.804, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabNaButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "23     \n  Na\n11    ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabNaButtonEvent)
        bohrAtomSimulationConfigTabNaButton.place(relx = 0.223, rely = 0.804, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabMgButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "24     \n  Mg\n12    ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabMgButtonEvent)
        bohrAtomSimulationConfigTabMgButton.place(relx = 0.347, rely = 0.804, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabAlButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "27     \n  Al\n13    ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabAlButtonEvent)
        bohrAtomSimulationConfigTabAlButton.place(relx = 0.47, rely = 0.804, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabSiButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                      text = "28     \n  Si\n14    ",
                                                                      font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                      width = 60,
                                                                      height = 30,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      fg_color = "green",
                                                                      command = bohrAtomSimulationConfigTabSiButtonEvent)
        bohrAtomSimulationConfigTabSiButton.place(relx = 0.595, rely = 0.804, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabPButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "31     \n  P\n15    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabPButtonEvent)
        bohrAtomSimulationConfigTabPButton.place(relx = 0.719, rely = 0.804, anchor = tkinter.CENTER)

        bohrAtomSimulationConfigTabSButton = customtkinter.CTkButton(master = bohrAtomSimulationConfigTabItemsFrame,
                                                                     text = "32     \n  S\n16    ",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                     width = 60,
                                                                     height = 30,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = bohrAtomSimulationConfigTabSButtonEvent)
        bohrAtomSimulationConfigTabSButton.place(relx = 0.842, rely = 0.804, anchor = tkinter.CENTER)
                
        #The images of the simulation go here
        bohrAtomSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabImageFrame,
                                                                       image = bohrAtomSimulationPreviewImage,
                                                                       text = "")
        bohrAtomSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                         
                        
        #The labels of the config tab go here
        bohrAtomSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabTitleFrame,
                                                                      justify = LEFT,
                                                                      text = "Bohr\nRepresentation",
                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        bohrAtomSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                                        
        bohrAtomSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabDescriptionFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Simulates some of the atoms of the periodic\ntable according to Niels Bohr's representation\nmodel by showing their electron shells and\nnucleons.",
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        bohrAtomSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.2, anchor = tkinter.W)
                                        
        bohrAtomSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabDescriptionFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Field of chemistry: Matter Study",
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        bohrAtomSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.55, anchor = tkinter.W)
                        
        bohrAtomSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabDescriptionFrame,
                                                                                      justify = LEFT,
                                                                                      text = 'Select the element of the periodic table\nthat you want to include then press on\n"Launch" to start the simulation.',
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        bohrAtomSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    bohrAtomSimulationConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")  

def solutionMakerConfigTab(bool):
    global solutionMakerConfigTabLaunchButton, solutionMakerConfigTabInitSolventOptionMenu, solutionMakerConfigTabInitSolventVolSlider, solutionMakerConfigTabInitSoluteOptionMenu, solutionMakerConfigTabInitSoluteMassSlider
    if bool == True:
        #The frames for each element of the tab go here
        solutionMakerConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                  width = 550,
                                                                  height = 300,
                                                                  corner_radius = 5,
                                                                  border_width = 1)
        solutionMakerConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                        
        solutionMakerConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                  width = 335,
                                                                  height = 100,
                                                                  corner_radius = 5,
                                                                  border_width = 1)
        solutionMakerConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                                
        solutionMakerConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                        width = 335,
                                                                        height = 200,
                                                                        corner_radius = 5,
                                                                        border_width = 1)
        solutionMakerConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                                
        solutionMakerConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                  width = 550,
                                                                  height = 265,
                                                                  corner_radius = 5,
                                                                  border_width = 1)
        solutionMakerConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                                
        solutionMakerConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 335,
                                                                         height = 100,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        solutionMakerConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                        
        #The buttons go here
        solutionMakerConfigTabLaunchButton = customtkinter.CTkButton(master = solutionMakerConfigTabLaunchButtonFrame,
                                                                     text = "Launch",
                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                     width = 335,
                                                                     height = 100,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     fg_color = "green",
                                                                     command = solutionMakerConfigTabLaunchButtonEvent)
        solutionMakerConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                                   
                                
        #The configurators (items) of the simulation go here
        solutionMakerConfigTabInitSolventOptionMenu = customtkinter.CTkOptionMenu(master = solutionMakerConfigTabItemsFrame,
                                                                                  width = 150,
                                                                                  height = 25,
                                                                                  fg_color = "green",
                                                                                  variable = solutionMakerConfigTabInitSolventOptionMenuVar,
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                  values = ["Water (H₂O)", "Ethanol (C₂H₅OH)", "Cyclohexane (C₆H₁₂)", "Hexane (C₆H₁₄)", "Acetone (C₃H₆O)"],
                                                                                  command = solutionMakerConfigTabInitSolventOptionMenuEvent)
        solutionMakerConfigTabInitSolventOptionMenu.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)

        solutionMakerConfigTabInitSolventVolSlider = customtkinter.CTkSlider(master = solutionMakerConfigTabItemsFrame,
                                                                             width = 495,
                                                                             height = 20,
                                                                             from_ = 100,
                                                                             to = 1000,
                                                                             command = solutionMakerConfigTabInitSolventVolSliderEvent)
        solutionMakerConfigTabInitSolventVolSlider.place(relx = 0.05, rely = 0.45, anchor = tkinter.W)

        solutionMakerConfigTabInitSoluteOptionMenu = customtkinter.CTkOptionMenu(master = solutionMakerConfigTabItemsFrame,
                                                                                 width = 150,
                                                                                 height = 25,
                                                                                 fg_color = "green",
                                                                                 variable = solutionMakerConfigTabInitSoluteOptionMenuVar,
                                                                                 font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                 values = ["Sodium Chloride (NaCl)", "Glucose (C₆H₁₂O₆)","Potassium Permanganate (KMnO₄)", "Copper Sulfate (CuSO₄)", "Sodium Hydroxide (NaOH)"],
                                                                                 command = solutionMakerConfigTabInitSoluteOptionMenuEvent)
        solutionMakerConfigTabInitSoluteOptionMenu.place(relx = 0.05, rely = 0.67, anchor = tkinter.W)

        solutionMakerConfigTabInitSoluteMassSlider = customtkinter.CTkSlider(master = solutionMakerConfigTabItemsFrame,
                                                                             width = 495,
                                                                             height = 20,
                                                                             from_ = 100,
                                                                             to = 1000,
                                                                             command = solutionMakerConfigTabInitSoluteMassSliderEvent)
        solutionMakerConfigTabInitSoluteMassSlider.place(relx = 0.05, rely = 0.9, anchor = tkinter.W)

        #The images of the simulation go here
        solutionMakerConfigTabInSimImage = customtkinter.CTkLabel(master = solutionMakerConfigTabImageFrame,
                                                                  image = solutionMakerPreviewImage,
                                                                  text = "")
        solutionMakerConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                                
                                
        #The labels of the config tab go here
        solutionMakerConfigTabTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabTitleFrame,
                                                                  justify = LEFT,
                                                                  text = "Solution\nMaker",
                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        solutionMakerConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                        
        solutionMakerConfigTabDescriptionLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabDescriptionFrame,
                                                                        justify = LEFT,
                                                                        text = "Simulates a solution of a choosable volume\nwhose solvent, solute and solute mass can be\nchanged.",
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        solutionMakerConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                        
        solutionMakerConfigTabCategoryLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabDescriptionFrame,
                                                                     justify = LEFT,
                                                                     text = "Field of chemistry: Molecular Dynamics",
                                                                     font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        solutionMakerConfigTabCategoryLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        solutionMakerConfigTabInstructionsLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabDescriptionFrame,
                                                                         justify = LEFT,
                                                                         text = 'Select or change the chemical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        solutionMakerConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        solutionMakerConfigTabInitSolventTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                             justify = LEFT,
                                                                             text = "Initial Solvent: ",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        solutionMakerConfigTabInitSolventTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)
        
        solutionMakerConfigTabInitSolventVolTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Solvent Volume (mL): ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        solutionMakerConfigTabInitSolventVolTitleLabel.place(relx = 0.05, rely = 0.35, anchor = tkinter.W)

        solutionMakerConfigTabInitSolventVolSliderValueLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = solutionMakerConfigTabInitSolventVolSliderValueVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        solutionMakerConfigTabInitSolventVolSliderValueLabel.place(relx = 0.46, rely = 0.35, anchor = tkinter.W)

        solutionMakerConfigTabInitSoluteTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                            justify = LEFT,
                                                                            text = "Initial Solute (solid): ",
                                                                            font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        solutionMakerConfigTabInitSoluteTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        solutionMakerConfigTabInitSoluteMassTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Solute Mass (g): ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        solutionMakerConfigTabInitSoluteMassTitleLabel.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)


        solutionMakerConfigTabInitSoluteMassSliderValueLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = solutionMakerConfigTabInitSoluteMassSliderValueVar,
                                                                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        solutionMakerConfigTabInitSoluteMassSliderValueLabel.place(relx = 0.38, rely = 0.8, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    solutionMakerConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")    

def molecularLabConfigTab(bool):
    global molecularLabConfigTabLaunchButton, molecularLabConfigTabInitMoleculeOptionMenu, molecularLabConfigTabInitHydrogenColorOptionMenu, molecularLabConfigTabInitCarbonColorOptionMenu, molecularLabConfigTabInitOxygenColorOptionMenu
    if bool == True:
        #The frames for each element of the tab go here
        molecularLabConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                 width = 550,
                                                                 height = 300,
                                                                 corner_radius = 5,
                                                                 border_width = 1)
        molecularLabConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                                
        molecularLabConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                 width = 335,
                                                                 height = 100,
                                                                 corner_radius = 5,
                                                                 border_width = 1)
        molecularLabConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                                        
        molecularLabConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 335,
                                                                       height = 200,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        molecularLabConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                                        
        molecularLabConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                 width = 550,
                                                                 height = 265,
                                                                 corner_radius = 5,
                                                                 border_width = 1)
        molecularLabConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                                        
        molecularLabConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                        width = 335,
                                                                        height = 100,
                                                                        corner_radius = 5,
                                                                        border_width = 1)
        molecularLabConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                                
        #The buttons go here
        molecularLabConfigTabLaunchButton = customtkinter.CTkButton(master = molecularLabConfigTabLaunchButtonFrame,
                                                                    text = "Launch",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"),
                                                                    width = 335,
                                                                    height = 100,
                                                                    corner_radius = 5,
                                                                    border_width = 1,
                                                                    fg_color = "green",
                                                                    command = molecularLabConfigTabLaunchButtonEvent)
        molecularLabConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                                        
                                        
        #The configurators (items) of the simulation go here
        molecularLabConfigTabInitMoleculeOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                  width = 150,
                                                                                  height = 25,
                                                                                  fg_color = "green",
                                                                                  variable = molecularLabConfigTabInitMoleculeOptionMenuVar,
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                  values = ["Carbon Dioxide (CO₂)", "Glucose (C₆H₁₂O₆)", "Ethanol (C₂H₅OH)", "Acetone (C₃H₆O)", "Methanol (CH₃OH)", "Formaldehyde (CH₂O)"],
                                                                                  command = molecularLabConfigTabInitMoleculeOptionMenuEvent)
        molecularLabConfigTabInitMoleculeOptionMenu.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)
        
        molecularLabConfigTabInitHydrogenColorOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       height = 25,
                                                                                       fg_color = "green",
                                                                                       variable = molecularLabConfigTabInitHydrogenColorOptionMenuVar,
                                                                                       font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                       values = ["Light Blue", "Light Gray", "Green"],
                                                                                       command = molecularLabConfigTabInitHydrogenColorOptionMenuEvent)
        molecularLabConfigTabInitHydrogenColorOptionMenu.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        molecularLabConfigTabInitCarbonColorOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                     width = 150,
                                                                                     height = 25,
                                                                                     fg_color = "green",
                                                                                     variable = molecularLabConfigTabInitCarbonColorOptionMenuVar,
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                     values = ["Black", "Dark Blue", "Dark Gray", "Dark Green"],
                                                                                     command = molecularLabConfigTabInitCarbonColorOptionMenuEvent)
        molecularLabConfigTabInitCarbonColorOptionMenu.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)

        molecularLabConfigTabInitOxygenColorOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                     width = 150,
                                                                                     height = 25,
                                                                                     fg_color = "green",
                                                                                     variable = molecularLabConfigTabInitOxygenColorOptionMenuVar,
                                                                                     font = customtkinter.CTkFont(family = "Segoe UI"),
                                                                                     values = ["Red", "Dark Red", "Pink"],
                                                                                     command = molecularLabConfigTabInitOxygenColorOptionMenuEvent)
        molecularLabConfigTabInitOxygenColorOptionMenu.place(relx = 0.6, rely = 0.23, anchor = tkinter.W)                                          
                                        
        #The images of the simulation go here
        molecularLabConfigTabInSimImage = customtkinter.CTkLabel(master = molecularLabConfigTabImageFrame,
                                                                 image = molecularLabPreviewImage,
                                                                 text = "")
        molecularLabConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                                           
                                        
        #The labels of the config tab go here
        molecularLabConfigTabTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabTitleFrame,
                                                                 justify = LEFT,
                                                                 text = "Molecular\nLab",
                                                                 font = customtkinter.CTkFont(family = "Segoe UI", size = 35, weight = "bold"))
        molecularLabConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                                
        molecularLabConfigTabDescriptionLabel = customtkinter.CTkLabel(master = molecularLabConfigTabDescriptionFrame,
                                                                       justify = LEFT,
                                                                       text = "Simulates a bunch of molecules made from\nassembled elements of the periodic table\nwhose colors can be changed.",
                                                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        molecularLabConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                                
        molecularLabConfigTabCategoryLabel = customtkinter.CTkLabel(master = molecularLabConfigTabDescriptionFrame,
                                                                    justify = LEFT,
                                                                    text = "Field of chemistry: Molecular Dynamics",
                                                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        molecularLabConfigTabCategoryLabel.place(relx = 0.01, rely = 0.45, anchor = tkinter.W)
                
        molecularLabConfigTabInstructionsLabel = customtkinter.CTkLabel(master = molecularLabConfigTabDescriptionFrame,
                                                                        justify = LEFT,
                                                                        text = 'Select one of the molecules that\nyou want to include, change the colors of the\natoms to your liking then press on "Launch" to\nstart the simulation.',
                                                                        font = customtkinter.CTkFont(family = "Segoe UI", size = 16, weight = "normal"))
        molecularLabConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.8, anchor = tkinter.W)

        molecularLabConfigTabInitMoleculeTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                             justify = LEFT,
                                                                             text = "Initial Molecule: ",
                                                                             font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        molecularLabConfigTabInitMoleculeTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        molecularLabConfigTabInitHydrogenColorTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Hydrogen Atom Color: ",
                                                                                  font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        molecularLabConfigTabInitHydrogenColorTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)
        
        molecularLabConfigTabInitCarbonColorTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Carbon Atom Color: ",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        molecularLabConfigTabInitCarbonColorTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        molecularLabConfigTabInitOxygenColorTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Oxygen Atom Color:",
                                                                                font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "normal"))
        molecularLabConfigTabInitOxygenColorTitleLabel.place(relx = 0.6, rely = 0.11, anchor = tkinter.W)

    #This line binds an event to the launch button to play a sound when it's hovered
    molecularLabConfigTabLaunchButton.bind("<Enter>", onButtonHover, add = "+")   

def reactionLabConfigTab(bool):
    if bool == True:
        #The frames for each element of the tab go here
        reactionLabConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                width = 550,
                                                                height = 300,
                                                                corner_radius = 5,
                                                                border_width = 1)
        reactionLabConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                                        
        reactionLabConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                width = 335,
                                                                height = 100,
                                                                corner_radius = 5,
                                                                border_width = 1)
        reactionLabConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                                                
        reactionLabConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                      width = 335,
                                                                      height = 200,
                                                                      corner_radius = 5,
                                                                      border_width = 1)
        reactionLabConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                                                
        reactionLabConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                width = 550,
                                                                height = 265,
                                                                corner_radius = 5,
                                                                border_width = 1)
        reactionLabConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                                                
        reactionLabConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                       width = 335,
                                                                       height = 100,
                                                                       corner_radius = 5,
                                                                       border_width = 1)
        reactionLabConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                                        
        #The buttons go here (nothing)
                                                        
                                                
        #The configurators (items) of the simulation go here (nothing)
                                                        
                                                
        #The images of the simulation go here (nothing)
                                                        
                                                
        #The labels of the config tab go here (nothing)
        
def combustionSimulationConfigTab(bool):
    if bool == True:
        #The frames for each element of the tab go here
        combustionSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 550,
                                                                         height = 300,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        combustionSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                                                
        combustionSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 335,
                                                                         height = 100,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        combustionSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                                                        
        combustionSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                               width = 335,
                                                                               height = 200,
                                                                               corner_radius = 5,
                                                                               border_width = 1)
        combustionSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                                                        
        combustionSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                         width = 550,
                                                                         height = 265,
                                                                         corner_radius = 5,
                                                                         border_width = 1)
        combustionSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                                                        
        combustionSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                width = 335,
                                                                                height = 100,
                                                                                corner_radius = 5,
                                                                                border_width = 1)
        combustionSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                                                
        #The buttons go here (nothing)
                                                                
                                                        
        #The configurators (items) of the simulation go here (nothing)
                                                                
                                                        
        #The images of the simulation go here (nothing)
                                                                
                                                        
        #The labels of the config tab go here (nothing)
        
def smokeSimulationConfigTab(bool):
    if bool == True:
        #The frames for each element of the tab go here
        smokeSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                    width = 550,
                                                                    height = 300,
                                                                    corner_radius = 5,
                                                                    border_width = 1)
        smokeSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                                                        
        smokeSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                    width = 335,
                                                                    height = 100,
                                                                    corner_radius = 5,
                                                                    border_width = 1)
        smokeSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                                                                
        smokeSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                          width = 335,
                                                                          height = 200,
                                                                          corner_radius = 5,
                                                                          border_width = 1)
        smokeSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                                                                
        smokeSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                    width = 550,
                                                                    height = 265,
                                                                    corner_radius = 5,
                                                                    border_width = 1)
        smokeSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                                                                
        smokeSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                           width = 335,
                                                                           height = 100,
                                                                           corner_radius = 5,
                                                                           border_width = 1)
        smokeSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                                                        
        #The buttons go here (nothing)
                                                                        
                                                                
        #The configurators (items) of the simulation go here (nothing)
                                                                        
                                                                
        #The images of the simulation go here (nothing)
                                                                        
                                                                
        #The labels of the config tab go here (nothing)
        
def atomCollisionSimulationTab(bool):
    if bool == True:
        #The frames for each element of the tab go here
        atomCollisionSimulationConfigTabImageFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                            width = 550,
                                                                            height = 300,
                                                                            corner_radius = 5,
                                                                            border_width = 1)
        atomCollisionSimulationConfigTabImageFrame.place(relx = 0.01, rely = 0.27, anchor = tkinter.W)
                                                                                                
        atomCollisionSimulationConfigTabTitleFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                            width = 335,
                                                                            height = 100,
                                                                            corner_radius = 5,
                                                                            border_width = 1)
        atomCollisionSimulationConfigTabTitleFrame.place(relx = 0.811, rely = 0.01, anchor = tkinter.N)
                                                                                        
        atomCollisionSimulationConfigTabDescriptionFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                  width = 335,
                                                                                  height = 200,
                                                                                  corner_radius = 5,
                                                                                  border_width = 1)
        atomCollisionSimulationConfigTabDescriptionFrame.place(relx = 0.811, rely = 0.185, anchor = tkinter.N)
                                                                                        
        atomCollisionSimulationConfigTabItemsFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                            width = 550,
                                                                            height = 265,
                                                                            corner_radius = 5,
                                                                            border_width = 1)
        atomCollisionSimulationConfigTabItemsFrame.place(relx = 0.01, rely = 0.765, anchor = tkinter.W)
                                                                                        
        atomCollisionSimulationConfigTabLaunchButtonFrame = customtkinter.CTkFrame(master = mainFrame,
                                                                                   width = 335,
                                                                                   height = 100,
                                                                                   corner_radius = 5,
                                                                                   border_width = 1)
        atomCollisionSimulationConfigTabLaunchButtonFrame.place(relx = 0.811, rely = 0.991, anchor = tkinter.S)
                                                                                
        #The buttons go here (nothing)
                                                                                
                                                                        
        #The configurators (items) of the simulation go here (nothing)
                                                                                
                                                                        
        #The images of the simulation go here (nothing)
                                                                                
                                                                        
        #The labels of the config tab go here (nothing)
        
#The main frames go here
optionsFrame = customtkinter.CTkFrame(master = app,
                                      width = 200,
                                      height = 580,
                                      corner_radius = 5)
optionsFrame.place(relx = 0, rely = 0, anchor = tkinter.NW)

mainFrame = customtkinter.CTkFrame(master = app,
                                   width = 900,
                                   height = 580,
                                   fg_color = "transparent")
mainFrame.place(relx = 0.59, rely = 0.5, anchor = tkinter.CENTER)

#The main launcher labels (welcome, etc...) go here
titleLabel = customtkinter.CTkLabel(master = optionsFrame,
                                    text = "Physics & Chemistry\nSandbox Launcher",
                                    font = customtkinter.CTkFont(family = "Segoe UI", size = 18, weight = "bold"))
titleLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)

welcomeLabel = customtkinter.CTkLabel(master = mainFrame,
                                      text = "Welcome to the Physics & Chemistry\nSandbox Launcher!",
                                      font = customtkinter.CTkFont(family = "Segoe UI", size = 20, weight = "bold"))
welcomeLabel.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

welcomeSubLabel = customtkinter.CTkLabel(master = mainFrame,
                                         text = "Select one of the tabs on the left to start.",
                                         font = customtkinter.CTkFont(family = "Segoe UI", size = 15, weight = "normal"))
welcomeSubLabel.place(relx = 0.5, rely = 0.59, anchor = tkinter.CENTER)

postDataLabel = customtkinter.CTkLabel(master = mainFrame,
                                       text = "The name of the app is just a placeholder. I'll find a good one.",
                                       font = customtkinter.CTkFont(family = "Segoe UI", size = 10, weight = "normal"))
postDataLabel.place(relx = 0.5, rely = 0.95, anchor = tkinter.CENTER)

#The main launcher buttons go here
physicsSelectorButton = customtkinter.CTkButton(master = optionsFrame,
                                                text = "Physics Tab",
                                                font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"), 
                                                width = 130,
                                                height = 25,
                                                corner_radius = 5,
                                                border_width = 1,
                                                command = physicsSelectorButtonEvent)
physicsSelectorButton.place(relx = 0.5, rely = 0.2, anchor = tkinter.CENTER)

chemistrySelectorButton = customtkinter.CTkButton(master = optionsFrame,
                                                  text = "Chemistry Tab",
                                                  font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                  width = 130,
                                                  height = 25,
                                                  corner_radius = 5,
                                                  border_width = 1,
                                                  command = chemistrySelectorButtonEvent)
chemistrySelectorButton.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

thePlaceSelectorButton = customtkinter.CTkButton(master = optionsFrame,
                                                 text = "The Place",
                                                 font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                 width = 130,
                                                 height = 25,
                                                 corner_radius = 5,
                                                 border_width = 1,
                                                 command = thePlaceSelectorButtonEvent)
thePlaceSelectorButton.place(relx = 0.5, rely = 0.4, anchor = tkinter.CENTER)

launcherSettingsButton = customtkinter.CTkButton(master = optionsFrame,
                                                 text = "Launcher Settings",
                                                 font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                                 width = 130,
                                                 height = 25,
                                                 corner_radius = 5,
                                                 border_width = 1,
                                                 command = launcherSettingsButtonEvent)
launcherSettingsButton.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

gitHubButton = customtkinter.CTkButton(master = optionsFrame,
                                       text = "GitHub",
                                       font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                       width = 130,
                                       height = 25,
                                       corner_radius = 5,
                                       border_width = 1,
                                       command = gitHubButtonEvent)
gitHubButton.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

creditsButton = customtkinter.CTkButton(master = optionsFrame,
                                        text = "Credits",
                                        font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                        width = 130,
                                        height = 25,
                                        corner_radius = 5,
                                        border_width = 1,
                                        command = creditsButtonEvent)
creditsButton.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)

quitLauncherButton = customtkinter.CTkButton(master = optionsFrame,
                                             text = "Quit Launcher",
                                             font = customtkinter.CTkFont(family = "Segoe UI", weight = "normal"),
                                             width = 130,
                                             height = 25,
                                             corner_radius = 5,
                                             border_width = 1,
                                             command = quitLauncherButtonEvent)
quitLauncherButton.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

#These lines bind events to the main launcher buttons to play a sound when they are hovered
physicsSelectorButton.bind("<Enter>", onButtonHover, add = "+")
chemistrySelectorButton.bind("<Enter>", onButtonHover, add = "+")
thePlaceSelectorButton.bind("<Enter>", onButtonHover, add = "+")
launcherSettingsButton.bind("<Enter>", onButtonHover, add = "+")
gitHubButton.bind("<Enter>", onButtonHover, add = "+")
creditsButton.bind("<Enter>", onButtonHover, add = "+")
quitLauncherButton.bind("<Enter>", onButtonHover, add = "+")

#The main loop is ran here
app.mainloop()