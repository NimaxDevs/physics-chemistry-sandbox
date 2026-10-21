#Do I even have to describe these lines
import customtkinter, tkinter
from tkinter import * 
from PIL import Image

#The CTk appearance settings go here
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("themes/rime.json")

#The CTk settings go here
app = customtkinter.CTk()
app.geometry("1100x580")
app.resizable(False, False)
app.title("Physics & Chemistry Sandbox Launcher")

placeholderImage = customtkinter.CTkImage(light_image = Image.open("images/placeholders/atom_image.png"),
                                          dark_image = Image.open("images/placeholders/atom_image.png"),
                                          size = (150, 100))

#The main menu variables go here
physicsTabSelected = False
chemistryTabSelected = False
thePlaceTabSelected = False
launcherSettingsSelected = False
creditsTabSelected = False

#The sub menu variables go here
##The physics simulations here
projectileSimulationConfigTabSelected = False
pendulumSimulationConfigTabSelected = False
springSimulationConfigTabSelected = False
planetOrbitsSimulationConfigTabSelected = False
gravitySimulationConfigTabSelected = False
refractionSimulationConfigTabSelected = False
fluidSimulationConfigTabSelected = False
temperatureSimulationConfigTabSelected = False

##The chemistry simulations here
bohrAtomSimulationConfigTabSelected = False
solutionMakerConfigTabSelected = False
molecularLabConfigTabSelected = False
reactionLabConfigTabSelected = False
combustionSimulationConfigTabSelected = False
smokeSimulationConfigTabSelected = False
atomCollisionSimulationTabSelected = False

#The config variables are here
##The physics variables go here
###The variables of the Projectile Simulation go here
projectileSimulationConfigTabInitAirResistCheckboxVar = tkinter.StringVar(value = "off")

###The variables of the Planet Orbits go here
planetOrbitsSimulationConfigTabShowOrbitTrailSwitchVar = tkinter.StringVar(value = "off")
planetOrbitsSimulationConfigTabShowPlanetNameSwitchVar = tkinter.StringVar(value = "off")
planetNumber = 0

###The variables of the Refraction Simulation go here
refractionSimulationConfigTabInitRefractiveIndex1OptionMenuVar = tkinter.StringVar(value = "Select Refractive Index 1")
refractionSimulationConfigTabInitRefractiveIndex2OptionMenuVar = tkinter.StringVar(value = "Select Refractive Index 2")
refractionSimulationConfigRayColorOptionMenuVar = tkinter.StringVar(value = "Select Ray Color")


#The button events (functions) go here
def physicsSelectorButtonEvent():
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

def chemistrySelectorButtonEvent():
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
    
def thePlaceSelectorButtonEvent():
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
    #opens the URL of my GitHub
    print("The GitHub page will NOT open right now")
    pass

def creditsButtonEvent():
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
    print("Launcher quit")
    app.quit()

#The buttons to configure the physics simulations are here
def projectileSimulationConfigButtonEvent():
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
    reactionLabConfigTabSelected = True
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
    reactionLabConfigTab(reactionLabConfigTabSelected)

def combustionSimulationConfigButtonEvent():
    combustionSimulationConfigTabSelected = True
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
    smokeSimulationConfigTabSelected = False
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    combustionSimulationConfigTab(combustionSimulationConfigTabSelected)

def smokeSimulationConfigButtonEvent():
    smokeSimulationConfigTabSelected = True
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
    atomCollisionSimulationTabSelected = False
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()   
    smokeSimulationConfigTab(smokeSimulationConfigTabSelected)

def atomCollisionSimulationConfigButtonEvent():
    atomCollisionSimulationTabSelected = True
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
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    atomCollisionSimulationTab(atomCollisionSimulationTabSelected)   

#The buttons to launch the simulations go here
##The buttons of the physics simulations go here
def projectileSimulationConfigTabLaunchButtonEvent():
    print("projectile simulation launched")

def pendulumSimulationConfigTabLaunchButtonEvent():
    print("pendulum simulation launched")

def springSimulationConfigTabLaunchButtonEvent():
    print("spring simulation launched")

def planetOrbitsSimulationConfigTabLaunchButtonEvent():
    print("planet orbits simulation launched")

def gravitySimulationConfigTabLaunchButtonEvent():
    print("gravity simulation launched")    

def refractionSimulationConfigTabLaunchButtonEvent():
    print("refraction simulation launched")

##The buttons of the chemistry simulations go here


#The configurator (items) events of the simulations go here
##The configurator events of the physics simulations go here
###The configurator events of the Projectile Simulation go here
def projectileSimulationConfigTabInitVelocitySliderEvent(value):
    pass

def projectileSimulationConfigTabInitAngleSliderEvent(value):
    pass

def projectileSimulationConfigTabInitGravAccSliderEvent(value):
    pass

def projectileSimulationConfigTabInitMassSliderEvent(value):
    pass

def projectileSimulationConfigTabInitDiameterSliderEvent(value):
    pass

def projectileSimulationConfigTabInitDragCoefSliderEvent(value):
    pass

###The configurator events of the Pendulum Simulation go here
def pendulumSimulationConfigTabInitAngleSliderEvent(value):
    pass

def pendulumSimulationConfigTabInitAngularVelSliderEvent(value):
    pass

def pendulumSimulationConfigTabInitLengthSliderEvent(value):
    pass

def pendulumSimulationConfigTabInitMassSliderEvent(value):
    pass

def pendulumSimulationConfigTabInitGravAccSliderEvent(value):
    pass

def pendulumSimulationConfigTabInitDampingCoefSliderEvent(value):
    pass

###The configurator events of the Spring Simulation go here
def springSimulationConfigTabInitMassSliderEvent(value):
    pass

def springSimulationConfigTabInitGravAccSliderEvent(value):
    pass

def springSimulationConfigTabInitLengthSliderEvent(value):
    pass

def springSimulationConfigTabInitStiffSliderEvent(value):
    pass

def springSimulationConfigTabInitDampingCoefSliderEvent(value):
    pass

###The configurator events of the Planet Orbits (imulation) go here
def planetOrbitsSimulationConfigTabShowOrbitTrailSwitchEvent():
    pass

def planetOrbitsSimulationConfigTabShowPlanetNameSwitchEvent():
    pass

###The configurator events of the Gravity Simulation go here
def gravitySimulationConfigTabInitMassSliderEvent(value):
    pass

def gravitySimulationConfigTabInitGravAccSliderEvent(value):
    pass

def gravitySimulationConfigTabInitHeightSliderEvent(value):
    pass

###The configurator events of the Refraction Simulation go here
def refractionSimulationConfigTabInitIncidenceAngleSliderEvent(value):
    pass

##The configurator events of the chemistry simulations go here

#The tab functions go here
def physicsTab(bool):
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
                                                                   width = 200,
                                                                   height = 50,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = projectileSimulationConfigButtonEvent)
        projectileSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        pendulumSimulationConfigButton = customtkinter.CTkButton(master = pendulumSimulationFrame,
                                                                 text = "Configure",
                                                                 width = 200,
                                                                 height = 50,
                                                                 corner_radius = 5,
                                                                 border_width = 1,
                                                                 command = pendulumSimulationConfigButtonEvent)
        pendulumSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        springSimulationConfigButton = customtkinter.CTkButton(master = springSimulationFrame,
                                                               text = "Configure",
                                                               width = 200,
                                                               height = 50,
                                                               corner_radius = 5,
                                                               border_width = 1,
                                                               command = springSimulationConfigButtonEvent)
        springSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        planetOrbitsSimulationConfigButton = customtkinter.CTkButton(master = planetOrbitsSimulationFrame,
                                                                     text = "Configure",
                                                                     width = 200,
                                                                     height = 50,
                                                                     corner_radius = 5,
                                                                     border_width = 1,
                                                                     command = planetOrbitsSimulationConfigButtonEvent)
        planetOrbitsSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        gravitySimulationConfigButton = customtkinter.CTkButton(master = gravitySimulationFrame,
                                                                text = "Configure",
                                                                width = 200,
                                                                height = 50,
                                                                corner_radius = 5,
                                                                border_width = 1,
                                                                command = gravitySimulationConfigButtonEvent)
        gravitySimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        refractionSimulationConfigButton = customtkinter.CTkButton(master = refractionSimulationFrame,
                                                                   text = "Configure",
                                                                   width = 200,
                                                                   height = 50,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = refractionSimulationConfigButtonEvent)
        refractionSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        fluidSimulationConfigButton = customtkinter.CTkButton(master = fluidSimulationFrame,
                                                              text = "Configure",
                                                              width = 200,
                                                              height = 50,
                                                              corner_radius = 5,
                                                              border_width = 1,
                                                              command = fluidSimulationConfigButtonEvent)
        fluidSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        temperatureSimulationConfigButton = customtkinter.CTkButton(master = temperatureSimulationFrame,
                                                                    text = "Configure",
                                                                    width = 200,
                                                                    height = 50,
                                                                    corner_radius = 5,
                                                                    border_width = 1,
                                                                    command = temperatureSimulationConfigButtonEvent)
        temperatureSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        #The image labels for the simulations are here
        projectileSimulationImageLabel = customtkinter.CTkLabel(master = projectileSimulationFrame,
                                                                image = placeholderImage,
                                                                text = "")
        projectileSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        pendulumSimulationImageLabel = customtkinter.CTkLabel(master = pendulumSimulationFrame,
                                                              image = placeholderImage,
                                                              text = "")
        pendulumSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        springSimulationImageLabel = customtkinter.CTkLabel(master = springSimulationFrame,
                                                            image = placeholderImage,
                                                            text = "")
        springSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        planetOrbitsSimulationImageLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationFrame,
                                                                  image = placeholderImage,
                                                                  text = "")
        planetOrbitsSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        gravitySimulationImageLabel = customtkinter.CTkLabel(master = gravitySimulationFrame,
                                                             image = placeholderImage,
                                                             text = "")
        gravitySimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        refractionSimulationImageLabel = customtkinter.CTkLabel(master = refractionSimulationFrame,
                                                                image = placeholderImage,
                                                                text = "")
        refractionSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        fluidSimulationImageLabel = customtkinter.CTkLabel(master = fluidSimulationFrame,
                                                           image = placeholderImage,
                                                           text = "")
        fluidSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        temperatureSimulationImageLabel = customtkinter.CTkLabel(master = temperatureSimulationFrame,
                                                                 image = placeholderImage,
                                                                 text = "")
        temperatureSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        #The title and description labels for the simulations are here
        projectileSimulationTitleLabel = customtkinter.CTkLabel(master = projectileSimulationFrame,
                                                                justify = LEFT,
                                                                text = "Projectile Simulation",
                                                                font = customtkinter.CTkFont(size = 18, weight = "bold"))
        projectileSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        projectileSimulationDescriptionLabel = customtkinter.CTkLabel(master = projectileSimulationFrame,
                                                                      justify = LEFT,
                                                                      text = "Simulates a projectile being\nthrown by changing specific\nphysical properties.",
                                                                      font = customtkinter.CTkFont(size = 12, weight = "normal"))
        projectileSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        pendulumSimulationTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationFrame,
                                                              justify = LEFT,
                                                              text = "Pendulum Simulation",
                                                              font = customtkinter.CTkFont(size = 18, weight = "bold"))
        pendulumSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        pendulumSimulationDescriptionLabel = customtkinter.CTkLabel(master = pendulumSimulationFrame,
                                                                    justify = LEFT,
                                                                    text = "Simulates a mass suspended\nto a fixed point swinging back\nand forth.",
                                                                    font = customtkinter.CTkFont(size = 12, weight = "normal"))
        pendulumSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        springSimulationTitleLabel = customtkinter.CTkLabel(master = springSimulationFrame,
                                                            justify = LEFT,
                                                            text = "Spring Simulation",
                                                            font = customtkinter.CTkFont(size = 18, weight = "bold"))
        springSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        springSimulationDescriptionLabel = customtkinter.CTkLabel(master = springSimulationFrame,
                                                                  justify = LEFT,
                                                                  text = "Simulates a mass attached to a\nspring suspended to a fixed point\nunder the influence of gravity.",
                                                                  font = customtkinter.CTkFont(size = 12, weight = "normal"))
        springSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        planetOrbitsSimulationTitleLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationFrame,
                                                                  justify = LEFT,
                                                                  text = "Planet Orbits",
                                                                  font = customtkinter.CTkFont(size = 18, weight = "bold"))
        planetOrbitsSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        planetOrbitsSimulationDescriptionLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationFrame,
                                                                        justify = LEFT,
                                                                        text = "Solves the N-body problem\nto simulate your favorite planets \nbut also your own ones.",
                                                                        font = customtkinter.CTkFont(size = 12, weight = "normal"))
        planetOrbitsSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        gravitySimulationTitleLabel = customtkinter.CTkLabel(master = gravitySimulationFrame,
                                                             justify = LEFT,
                                                             text = "Gravity Simulator",
                                                             font = customtkinter.CTkFont(size = 18, weight = "bold"))
        gravitySimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        gravitySimulationDescriptionLabel = customtkinter.CTkLabel(master = gravitySimulationFrame,
                                                                   justify = LEFT,
                                                                   text = "Simulates an object falling\nunder the influence of\ngravity.",
                                                                   font = customtkinter.CTkFont(size = 12, weight = "normal"))
        gravitySimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        refractionSimulationTitleLabel = customtkinter.CTkLabel(master = refractionSimulationFrame,
                                                                justify = LEFT,
                                                                text = "Refraction Simulation",
                                                                font = customtkinter.CTkFont(size = 18, weight = "bold"))
        refractionSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        refractionSimulationDescriptionLabel = customtkinter.CTkLabel(master = refractionSimulationFrame,
                                                                      justify = LEFT,
                                                                      text = "Simulates light changing velocity\nand angle under the influence of\na fluid.",
                                                                      font = customtkinter.CTkFont(size = 12, weight = "normal"))
        refractionSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        fluidSimulationTitleLabel = customtkinter.CTkLabel(master = fluidSimulationFrame,
                                                           justify = LEFT,
                                                           text = "Fluid Simulation",
                                                           font = customtkinter.CTkFont(size = 18, weight = "bold"))
        fluidSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        fluidSimulationDescriptionLabel = customtkinter.CTkLabel(master = fluidSimulationFrame,
                                                                 justify = LEFT,
                                                                 text = "Simulates a given fluid whose\ndensity, viscosity and volume can\nbe changed.",
                                                                 font = customtkinter.CTkFont(size = 12, weight = "normal"))
        fluidSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        temperatureSimulationTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationFrame,
                                                                 justify = LEFT,
                                                                 text = "Temperature Simulation",
                                                                 font = customtkinter.CTkFont(size = 16, weight = "bold"))
        temperatureSimulationTitleLabel.place(relx = 0.04, rely = 0.55, anchor = tkinter.W)

        temperatureSimulationDescriptionLabel = customtkinter.CTkLabel(master = temperatureSimulationFrame,
                                                                       justify = LEFT,
                                                                       text = "Simulates the increase\nor decrease of entropy when\napplying heat or cold.",
                                                                       font = customtkinter.CTkFont(size = 12, weight = "normal"))
        temperatureSimulationDescriptionLabel.place(relx = 0.05, rely = 0.68, anchor = tkinter.W)
        
def chemistryTab(bool):
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
                                                                 width = 200,
                                                                 height = 50,
                                                                 corner_radius = 5,
                                                                 border_width = 1,
                                                                 command = bohrAtomSimulationConfigButtonEvent)
        bohrAtomSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        solutionMakerConfigButton = customtkinter.CTkButton(master = solutionMakerFrame,
                                                            text = "Configure",
                                                            width = 200,
                                                            height = 50,
                                                            corner_radius = 5,
                                                            border_width = 1,
                                                            command = solutionMakerConfigButtonEvent)
        solutionMakerConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        molecularLabConfigButton = customtkinter.CTkButton(master = molecularLabFrame,
                                                           text = "Configure",
                                                           width = 200,
                                                           height = 50,
                                                           corner_radius = 5,
                                                           border_width = 1,
                                                           command = molecularLabConfigButtonEvent)
        molecularLabConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        reactionLabConfigButton = customtkinter.CTkButton(master = reactionLabFrame,
                                                          text = "Configure",
                                                          width = 200,
                                                          height = 50,
                                                          corner_radius = 5,
                                                          border_width = 1,
                                                          command = reactionLabConfigButtonEvent)
        reactionLabConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        combustionSimulationConfigButton = customtkinter.CTkButton(master = combustionSimulationFrame,
                                                                   text = "Configure",
                                                                   width = 200,
                                                                   height = 50,
                                                                   corner_radius = 5,
                                                                   border_width = 1,
                                                                   command = combustionSimulationConfigButtonEvent)
        combustionSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        smokeSimulationConfigButton = customtkinter.CTkButton(master = smokeSimulationFrame,
                                                              text = "Configure",
                                                              width = 200,
                                                              height = 50,
                                                              corner_radius = 5,
                                                              border_width = 1,
                                                              command = smokeSimulationConfigButtonEvent)
        smokeSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        atomCollisionSimulationConfigButton = customtkinter.CTkButton(master = atomCollisionSimulationFrame,
                                                                      text = "Configure",
                                                                      width = 200,
                                                                      height = 50,
                                                                      corner_radius = 5,
                                                                      border_width = 1,
                                                                      command = atomCollisionSimulationConfigButtonEvent)
        atomCollisionSimulationConfigButton.place(relx = 0.5, rely = 0.98, anchor = tkinter.S)

        #The image labels for the simulations are here
        bohrAtomSimulationImageLabel = customtkinter.CTkLabel(master = bohrAtomSimulationFrame,
                                                              image = placeholderImage,
                                                              text = "")
        bohrAtomSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        solutionMakerImageLabel = customtkinter.CTkLabel(master = solutionMakerFrame,
                                                         image = placeholderImage,
                                                         text = "")
        solutionMakerImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        molecularLabImageLabel = customtkinter.CTkLabel(master = molecularLabFrame,
                                                        image = placeholderImage,
                                                        text = "")
        molecularLabImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        reactionLabImageLabel = customtkinter.CTkLabel(master = reactionLabFrame,
                                                       image = placeholderImage,
                                                       text = "")
        reactionLabImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        combustionSimulationImageLabel = customtkinter.CTkLabel(master = combustionSimulationFrame,
                                                                image = placeholderImage,
                                                                text = "")
        combustionSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        smokeSimulationImageLabel = customtkinter.CTkLabel(master = smokeSimulationFrame,
                                                           image = placeholderImage,
                                                           text = "")
        smokeSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor= tkinter.N)

        atomCollisionSimulationImageLabel = customtkinter.CTkLabel(master = atomCollisionSimulationFrame,
                                                                   image = placeholderImage,
                                                                   text = "")
        atomCollisionSimulationImageLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.N)

        #The title and description labels for the simulations are here
        bohrAtomSimulationTitleLabel = customtkinter.CTkLabel(master = bohrAtomSimulationFrame,
                                                              justify = LEFT,
                                                              text = "Bohr Representation",
                                                              font = customtkinter.CTkFont(size = 18, weight = "bold"))
        bohrAtomSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)
        
        bohrAtomSimulationDescriptionLabel = customtkinter.CTkLabel(master = bohrAtomSimulationFrame,
                                                                    justify = LEFT,
                                                                    text = "Simulates an atom according to\nNiels Bohr's model including\nits electron orbits and nucleons.",
                                                                    font = customtkinter.CTkFont(size = 12, weight = "normal"))
        bohrAtomSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        solutionMakerTitleLabel = customtkinter.CTkLabel(master = solutionMakerFrame,
                                                         justify = LEFT,
                                                         text = "Solution Maker",
                                                         font = customtkinter.CTkFont(size = 18, weight = "bold"))
        solutionMakerTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        solutionMakerDescriptionLabel = customtkinter.CTkLabel(master = solutionMakerFrame,
                                                               justify = LEFT,
                                                               text = "Simulates a bunch of solvants and\nsolutes that can be mixed to\nobtain solutions.",
                                                               font = customtkinter.CTkFont(size = 12, weight = "normal"))
        solutionMakerDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        molecularLabTitleLabel = customtkinter.CTkLabel(master = molecularLabFrame,
                                                        justify = LEFT,
                                                        text = "Molecular Lab",
                                                        font = customtkinter.CTkFont(size = 18, weight = "bold"))
        molecularLabTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        molecularLabDescriptionLabel = customtkinter.CTkLabel(master = molecularLabFrame,
                                                              justify = LEFT,
                                                              text = "Simulates a bunch of elements in\nthe periodic table that can be\ncombined into molecules.",
                                                              font = customtkinter.CTkFont(size = 12, weight = "normal"))
        molecularLabDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        reactionLabTitleLabel = customtkinter.CTkLabel(master = reactionLabFrame,
                                                       justify = LEFT,
                                                       text = "Reaction Lab",
                                                       font = customtkinter.CTkFont(size = 18, weight = "bold"))
        reactionLabTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        reactionLabDescriptionLabel = customtkinter.CTkLabel(master = reactionLabFrame,
                                                             justify = LEFT,
                                                             text = "Simulates some reactants that\ncan be put together to\ncreate chemical reactions.",
                                                             font = customtkinter.CTkFont(size = 12, weight = "normal"))
        reactionLabDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        combustionSimulationTitleLabel = customtkinter.CTkLabel(master = combustionSimulationFrame,
                                                                justify = LEFT,
                                                                text = "Combustion Simulation",
                                                                font = customtkinter.CTkFont(size = 16, weight = "bold"))
        combustionSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        combustionSimulationDescriptionLabel = customtkinter.CTkLabel(master = combustionSimulationFrame,
                                                                      justify = LEFT,
                                                                      text = "Simulates the combustion of some\nchemical solutes producing a\ncolorful flame.",
                                                                      font = customtkinter.CTkFont(size = 12, weight = "normal"))
        combustionSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        smokeSimulationTitleLabel = customtkinter.CTkLabel(master = smokeSimulationFrame,
                                                           justify = LEFT,
                                                           text = "Smoke Simulation",
                                                           font = customtkinter.CTkFont(size = 18, weight = "bold"))
        smokeSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        smokeSimulationDesccriptionLabel = customtkinter.CTkLabel(master = smokeSimulationFrame,
                                                                  justify = LEFT,
                                                                  text = "Simulates smoke coming from the\ncombustion of different chemical\nsolutes.",
                                                                  font = customtkinter.CTkFont(size = 12, weight = "normal"))
        smokeSimulationDesccriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

        atomCollisionSimulationTitleLabel = customtkinter.CTkLabel(master = atomCollisionSimulationFrame,
                                                                   justify = LEFT,
                                                                   text = "Atom Collision",
                                                                   font = customtkinter.CTkFont(size = 18, weight = "bold"))
        atomCollisionSimulationTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        atomCollisionSimulationDescriptionLabel = customtkinter.CTkLabel(master = atomCollisionSimulationFrame,
                                                                         justify = LEFT,
                                                                         text = "Simulates different kinds of atoms\nof the periodic table colliding\ninto each other.",
                                                                         font = customtkinter.CTkFont(size = 12, weight = "normal"))
        atomCollisionSimulationDescriptionLabel.place(relx = 0.06, rely = 0.68, anchor = tkinter.W)

def thePlaceTab(bool):
    if bool == True:
        thePlaceFrame = customtkinter.CTkFrame(master = mainFrame,
                                               width = 550,
                                               height = 400,
                                               corner_radius = 5,
                                               border_width = 1)
        thePlaceFrame.place(relx = 0.32, rely = 0.36, anchor = tkinter.CENTER)

        thePlacePlaceholderLabel = customtkinter.CTkLabel(master = thePlaceFrame,
                                                  text = "Invisible place",
                                                  font = customtkinter.CTkFont(size = 20, weight = "bold"))
        thePlacePlaceholderLabel.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

def launcherSettingsTab(bool):
    print("The launcher settings are in this tab")
    launcherSettingsPlaceholderLabel = customtkinter.CTkLabel(master = mainFrame,
                                          text = "Launcher Settings\n(the settings are OBVIOUSLY here but you just can't see them...)",
                                          font = customtkinter.CTkFont(size = 20, weight = "bold"))
    launcherSettingsPlaceholderLabel.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
    pass

def creditsTab(bool):
    if bool == True:
        #I'll write the credits here (developper, assets, themes, libraries)
        print("The credits are in this tab")
        creditsPlaceholderLabel = customtkinter.CTkLabel(master = mainFrame,
                                      text = "Credits\n(nothing for now)",
                                      font = customtkinter.CTkFont(size = 20, weight = "bold"))
        creditsPlaceholderLabel.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

#The sub tabs of the physics tab (physics simulations) are here
def projectileSimulationConfigTab(bool):
    if bool == True:
        #The air resistance checkbox logic goes here
        def projectileSimulationConfigTabInitAirResistCheckboxEvent():
            if projectileSimulationConfigTabInitAirResistCheckbox.get() == "on":
                projectileSimulationConfigTabInitDragCoefTitleLabel.place(relx = 0.51, rely = 0.8, anchor = tkinter.W)
                projectileSimulationConfigTabInitDragCoefSlider.place(relx = 0.5, rely = 0.9, anchor = tkinter.W)
            else:
                projectileSimulationConfigTabInitDragCoefTitleLabel.place_forget()
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
                                                                            font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                            width = 335,
                                                                            height = 100,
                                                                            corner_radius = 5,
                                                                            border_width = 1,
                                                                            command = projectileSimulationConfigTabLaunchButtonEvent)
        projectileSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
        
        #The configurators (items) of the simulation go here
        projectileSimulationConfigTabInitVelocitySlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                  from_ = 1, 
                                                                                  to = 100,
                                                                                  corner_radius = 8,
                                                                                  command = projectileSimulationConfigTabInitVelocitySliderEvent)
        projectileSimulationConfigTabInitVelocitySlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                               from_ = 0, 
                                                                               to = 90,
                                                                               corner_radius = 8,
                                                                               command = projectileSimulationConfigTabInitAngleSliderEvent)
        projectileSimulationConfigTabInitAngleSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                 from_ = 0.1, 
                                                                                 to = 20,
                                                                                 corner_radius = 8,
                                                                                 command = projectileSimulationConfigTabInitGravAccSliderEvent)
        projectileSimulationConfigTabInitGravAccSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                 from_ = 0.1, 
                                                                                 to = 5000,
                                                                                 corner_radius = 8,
                                                                                 command = projectileSimulationConfigTabInitMassSliderEvent)
        projectileSimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                         from_ = 0.1, 
                                                                                         to = 5000,
                                                                                         corner_radius = 8,
                                                                                         command = projectileSimulationConfigTabInitDiameterSliderEvent)
        projectileSimulationConfigTabInitDiameterSlider.place(relx = 0.5, rely = 0.2, anchor = tkinter.W)

        projectileSimulationConfigTabInitAirResistCheckbox = customtkinter.CTkCheckBox(master = projectileSimulationConfigTabItemsFrame,
                                                                                   text = "Air Resistance",
                                                                                   font = customtkinter.CTkFont(size = 18, weight = "normal"),
                                                                                   variable = projectileSimulationConfigTabInitAirResistCheckboxVar,
                                                                                   onvalue = "on",
                                                                                   offvalue = "off",
                                                                                   command = projectileSimulationConfigTabInitAirResistCheckboxEvent)
        projectileSimulationConfigTabInitAirResistCheckbox.place(relx = 0.61, rely = 0.66, anchor = tkinter.CENTER)

        projectileSimulationConfigTabInitDragCoefSlider = customtkinter.CTkSlider(master = projectileSimulationConfigTabItemsFrame,
                                                                                  from_ = 0, 
                                                                                  to = 1,
                                                                                  corner_radius = 8,
                                                                                  command = projectileSimulationConfigTabInitDragCoefSliderEvent)

        #The images of the config tab go here
        projectileSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = projectileSimulationConfigTabImageFrame,
                                                                         image = placeholderImage,
                                                                         text = "")
        projectileSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)
        
        #The labels of the config tab go here
        projectileSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabTitleFrame,
                                                                         justify = LEFT,
                                                                         text = "Projectile\nSimulation",
                                                                         font = customtkinter.CTkFont(size = 35, weight = "bold"))
        projectileSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        projectileSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabDescriptionFrame,
                                                                               justify = LEFT,
                                                                               text = "Simulates a projectile being thrown at a\nspecific velocity, angle, gravitational\nacceleration, mass, diameter and air\nresistance.",
                                                                               font = customtkinter.CTkFont(size = 16, weight = "normal"))
        projectileSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.21, anchor = tkinter.W)

        projectileSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = "Field of physics: Newtonian Mechanics",
                                                                            font = customtkinter.CTkFont(size = 16, weight = "normal"))
        projectileSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.55, anchor = tkinter.W)

        projectileSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabDescriptionFrame,
                                                                                justify = LEFT,
                                                                                text = 'Change and select the physical properties\nthat you want to include then press\non "Launch" to start the simulation.',
                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        projectileSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        projectileSimulationConfigTabInitVelocityTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Velocity (m/s): ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitVelocityTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Angle (°): ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitAngleTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Mass (kg): ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Diameter (m): ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitDiameterTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitDragCoefTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Initial Drag Coefficient: ",
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))

def pendulumSimulationConfigTab(bool):
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
                                                                          font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                          width = 335,
                                                                          height = 100,
                                                                          corner_radius = 5,
                                                                          border_width = 1,
                                                                          command = pendulumSimulationConfigTabLaunchButtonEvent)
        pendulumSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The configurators (items) of the simulation go here
        pendulumSimulationConfigTabInitAngleSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                from_ = -90, 
                                                                                to = 90,
                                                                                corner_radius = 8,
                                                                                command = pendulumSimulationConfigTabInitAngleSliderEvent)
        pendulumSimulationConfigTabInitAngleSlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                  from_ = 0.1, 
                                                                                  to = 90,
                                                                                  corner_radius = 8,
                                                                                  command = pendulumSimulationConfigTabInitAngularVelSliderEvent)
        pendulumSimulationConfigTabInitAngularVelSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                 from_ = 0.1, 
                                                                                 to = 1,
                                                                                 corner_radius = 8,
                                                                                 command = pendulumSimulationConfigTabInitLengthSliderEvent)
        pendulumSimulationConfigTabInitLengthSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        pendulumSimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                            from_ = 0.1, 
                                                                            to = 1.5,
                                                                            corner_radius = 8,
                                                                            command = pendulumSimulationConfigTabInitMassSliderEvent)
        pendulumSimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                               from_ = 0.1, 
                                                                               to = 20,
                                                                               corner_radius = 8,
                                                                               command = pendulumSimulationConfigTabInitGravAccSliderEvent)
        pendulumSimulationConfigTabInitGravAccSlider.place(relx = 0.5, rely = 0.2, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefSlider = customtkinter.CTkSlider(master = pendulumSimulationConfigTabItemsFrame,
                                                                                   from_ = 0, 
                                                                                   to = 1,
                                                                                   corner_radius = 8,
                                                                                   command = pendulumSimulationConfigTabInitDampingCoefSliderEvent)
        pendulumSimulationConfigTabInitDampingCoefSlider.place(relx = 0.5, rely = 0.4, anchor = tkinter.W)

        #The images of the simulation go here
        pendulumSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = pendulumSimulationConfigTabImageFrame,
                                                                       image = placeholderImage,
                                                                       text = "")
        pendulumSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        pendulumSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabTitleFrame,
                                                                       justify = LEFT,
                                                                       text = "Pendulum\nSimulation",
                                                                       font = customtkinter.CTkFont(size = 35, weight = "bold"))
        pendulumSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                
        pendulumSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = "Simulates a mass suspended to a fixed point\nswinging back and forth whose initial angle,\nangular velocity, length to the fixed point,\nmass, gravitational acceleration and damping\ncoefficient can be changed.",
                                                                             font = customtkinter.CTkFont(size = 16, weight = "normal"))
        pendulumSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.25, anchor = tkinter.W)

        pendulumSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabDescriptionFrame,
                                                                          justify = LEFT,
                                                                          text = "Field of physics: Newtonian Mechanics",
                                                                          font = customtkinter.CTkFont(size = 16, weight = "normal"))
        pendulumSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.59, anchor = tkinter.W)

        pendulumSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabDescriptionFrame,
                                                                              justify = LEFT,
                                                                              text = 'Change the physical properties that you want\nto include then press on "Launch" to start the\nsimulation.',
                                                                              font = customtkinter.CTkFont(size = 16, weight = "normal"))
        pendulumSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
        pendulumSimulationConfigTabInitAngleTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Angle (°): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitAngleTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Angular Velocity (rad/s): ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitAngularVelTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Length (m): ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitLengthTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)
        
        pendulumSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Mass (kg): ",
                                                                               font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                  font = customtkinter.CTkFont(size = 14, weight = "normal"))
        pendulumSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Initial Damping Coefficient: ",
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitDampingCoefTitleLabel.place(relx = 0.51, rely = 0.3, anchor = tkinter.W)

def springSimulationConfigTab(bool):
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
                                                                                  font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                                  width = 335,
                                                                                  height = 100,
                                                                                  corner_radius = 5,
                                                                                  border_width = 1,
                                                                                  command = springSimulationConfigTabLaunchButtonEvent)
        springSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The configurators (items) of the simulation go here
        springSimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                          from_ = 0.1, 
                                                                          to = 1,
                                                                          corner_radius = 8,
                                                                          command = springSimulationConfigTabInitMassSliderEvent)
        springSimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                             from_ = 0.1, 
                                                                             to = 20,
                                                                             corner_radius = 8,
                                                                             command = springSimulationConfigTabInitGravAccSliderEvent)
        springSimulationConfigTabInitGravAccSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        springSimulationConfigTabInitLengthSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                            from_ = 0.1, 
                                                                            to = 1,
                                                                            corner_radius = 8,
                                                                            command = springSimulationConfigTabInitLengthSliderEvent)
        springSimulationConfigTabInitLengthSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        springSimulationConfigTabInitStiffSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                           from_ = 0.1, 
                                                                           to = 5,
                                                                           corner_radius = 8,
                                                                           command = springSimulationConfigTabInitStiffSliderEvent)
        springSimulationConfigTabInitStiffSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        springSimulationConfigTabInitDampingCoefSlider = customtkinter.CTkSlider(master = springSimulationConfigTabItemsFrame,
                                                                             from_ = 0.1, 
                                                                             to = 20,
                                                                             corner_radius = 8,
                                                                             command = springSimulationConfigTabInitDampingCoefSliderEvent)
        springSimulationConfigTabInitDampingCoefSlider.place(relx = 0.5, rely = 0.2, anchor = tkinter.W)

        #The images of the simulation go here
        springSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = springSimulationConfigTabImageFrame,
                                                                     image = placeholderImage,
                                                                     text = "")
        springSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        springSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabTitleFrame,
                                                                     justify = LEFT,
                                                                     text = "Spring\nSimulation",
                                                                     font = customtkinter.CTkFont(size = 35, weight = "bold"))
        springSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)

        springSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = springSimulationConfigTabDescriptionFrame,
                                                                           justify = LEFT,
                                                                           text = "Simulates a mass (increasable or decreasable)\nattached to a spring suspended to a fixed point\nunder the influence of gravity whose length,\nstiffness and damping can be changed.",
                                                                           font = customtkinter.CTkFont(size = 15, weight = "normal"))
        springSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.2, anchor = tkinter.W)

        springSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = springSimulationConfigTabDescriptionFrame,
                                                                        justify = LEFT,
                                                                        text = "Field of physics: Newtonian Mechanics",
                                                                        font = customtkinter.CTkFont(size = 16, weight = "normal"))
        springSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.54, anchor = tkinter.W)

        springSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = springSimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = 'Change the physical properties that you want\nto include then press on "Launch" to start the\nsimulation.',
                                                                            font = customtkinter.CTkFont(size = 16, weight = "normal"))
        springSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        springSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Mass (kg): ",
                                                                              font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)
        
        springSimulationConfigTabInitLengthTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Length (m): ",
                                                                               font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitLengthTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)
                
        springSimulationConfigTabInitStiffTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Stiffness: ",
                                                                              font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitStiffTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)
        
        springSimulationConfigTabInitDampingCoefTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Initial Damping Coefficient: ",
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitDampingCoefTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)
        
def planetOrbitsSimulationConfigTab(bool):
    if bool == True:
        #Function to add & save the infos of the planets
        def planetOrbitsSimulationConfigTabAddPlanetButtonEvent():
            global planetNumber
            if (planetOrbitsSimulationConfigTabPlanetNameEntry.get() != "") and (planetOrbitsSimulationConfigTabPlanetColorEntry.get() != "") and (planetOrbitsSimulationConfigTabPlanetMassEntry.get() != "") and (planetOrbitsSimulationConfigTabPlanetRadiusEntry.get() != ""):
                planetNumber += 1
                print(f"Planet {planetNumber}:\nName: {planetOrbitsSimulationConfigTabPlanetNameEntry.get()}\nColor: {planetOrbitsSimulationConfigTabPlanetColorEntry.get()}\nMass: {planetOrbitsSimulationConfigTabPlanetMassEntry.get()}\nRadius: {planetOrbitsSimulationConfigTabPlanetRadiusEntry.get()}\nInitial Vx: {int(planetOrbitsSimulationConfigTabPlanetInitialVxSlider.get())}\nInitial Vy: {int(planetOrbitsSimulationConfigTabPlanetInitialVySlider.get())}\nInitial ax: {int(planetOrbitsSimulationConfigTabPlanetInitialAxSlider.get())}\nInitial ay: {int(planetOrbitsSimulationConfigTabPlanetInitialAySlider.get())}\nShow Orbit Trail: {planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.get()}\nShow Planet Name: {planetOrbitsSimulationConfigTabShowPlanetNameSwitch.get()}")
                planetOrbitsSimulationConfigTabPlanetNameEntry.set("")
                planetOrbitsSimulationConfigTabPlanetColorEntry.set("")
                planetOrbitsSimulationConfigTabPlanetMassEntry.set("")
                planetOrbitsSimulationConfigTabPlanetRadiusEntry.set("")
                planetOrbitsSimulationConfigTabPlanetInitialVxSlider.set(0)
                planetOrbitsSimulationConfigTabPlanetInitialVySlider.set(0)
                planetOrbitsSimulationConfigTabPlanetInitialAxSlider.set(0)
                planetOrbitsSimulationConfigTabPlanetInitialAySlider.set(0)
                planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.set("off")
                planetOrbitsSimulationConfigTabShowPlanetNameSwitch.set("off")
            else:
                print("error: no core values entered (name, color, mass, radius)")
        
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
                                                                              font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                              width = 335,
                                                                              height = 100,
                                                                              corner_radius = 5,
                                                                              border_width = 1,
                                                                              command = planetOrbitsSimulationConfigTabLaunchButtonEvent)
        planetOrbitsSimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        planetOrbitsSimulationConfigTabAddPlanetButton = customtkinter.CTkButton(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                 text = "+ ADD",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "bold"),
                                                                                 width = 50,
                                                                                 height = 25,
                                                                                 corner_radius = 5,
                                                                                 border_width = 1,
                                                                                 command = planetOrbitsSimulationConfigTabAddPlanetButtonEvent)
        planetOrbitsSimulationConfigTabAddPlanetButton.place(relx = 0.01, rely = 0.08, anchor = tkinter.W)

        #The configurators (items) of the simulation go here
        planetOrbitsSimulationConfigTabPlanetNameEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                 width = 150,
                                                                                 height = 25,
                                                                                 placeholder_text = "Planet Name",
                                                                                 font = customtkinter.CTkFont(size = 15, weight = "normal"),
                                                                                 corner_radius = 5,
                                                                                 border_width = 1)
        planetOrbitsSimulationConfigTabPlanetNameEntry.place(relx = 0.01, rely = 0.39, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetColorEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                 width = 150,
                                                                                 height = 25,
                                                                                 placeholder_text = "Color as a word",
                                                                                 font = customtkinter.CTkFont(size = 15, weight = "normal"),
                                                                                 corner_radius = 5,
                                                                                 border_width = 1)
        planetOrbitsSimulationConfigTabPlanetColorEntry.place(relx = 0.01, rely = 0.64, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetMassEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                width = 150,
                                                                                height = 25,
                                                                                placeholder_text = '"e" for the 10th power',
                                                                                font = customtkinter.CTkFont(size = 14, weight = "normal"),
                                                                                corner_radius = 5,
                                                                                border_width = 1)
        planetOrbitsSimulationConfigTabPlanetMassEntry.place(relx = 0.01, rely = 0.89, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetRadiusEntry = customtkinter.CTkEntry(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                  width = 150,
                                                                                  height = 25,
                                                                                  placeholder_text = "No massive radii",
                                                                                  font = customtkinter.CTkFont(size = 14, weight = "normal"),
                                                                                  corner_radius = 5,
                                                                                  border_width = 1)
        planetOrbitsSimulationConfigTabPlanetRadiusEntry.place(relx = 0.35, rely = 0.39, anchor = tkinter.W)
        
        planetOrbitsSimulationConfigTabPlanetInitialVxSlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       from_ = 0,
                                                                                       to = 300,
                                                                                       corner_radius = 5)
        planetOrbitsSimulationConfigTabPlanetInitialVxSlider.place(relx = 0.35, rely = 0.64, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                      width = 150,
                                                                                      from_ = 0,
                                                                                      to = 300,
                                                                                      corner_radius = 5)
        planetOrbitsSimulationConfigTabPlanetInitialVySlider.place(relx = 0.35, rely = 0.89, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                     width = 150,
                                                                                     from_ = 0,
                                                                                     to = 50,
                                                                                     corner_radius = 5)
        planetOrbitsSimulationConfigTabPlanetInitialAxSlider.place(relx = 0.68, rely = 0.39, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySlider = customtkinter.CTkSlider(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       from_ = 0,
                                                                                       to = 50,
                                                                                       corner_radius = 5)
        planetOrbitsSimulationConfigTabPlanetInitialAySlider.place(relx = 0.68, rely = 0.6, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabShowOrbitTrailSwitch = customtkinter.CTkSwitch(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       width = 50,
                                                                                       height = 50,
                                                                                       bg_color = "transparent",
                                                                                       text = "Show Orbit Trail",
                                                                                       onvalue = "on",
                                                                                       offvalue = "off",
                                                                                       variable = planetOrbitsSimulationConfigTabShowOrbitTrailSwitchVar,
                                                                                       command = planetOrbitsSimulationConfigTabShowOrbitTrailSwitchEvent)
        planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.place(relx = 0.68, rely = 0.74, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabShowPlanetNameSwitch = customtkinter.CTkSwitch(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                      width = 50,
                                                                                      height = 50,
                                                                                      bg_color = "transparent",
                                                                                      text = "Show Planet Name",
                                                                                      onvalue = "on",
                                                                                      offvalue = "off",
                                                                                      variable = planetOrbitsSimulationConfigTabShowPlanetNameSwitchVar,
                                                                                      command = planetOrbitsSimulationConfigTabShowPlanetNameSwitchEvent)
        planetOrbitsSimulationConfigTabShowPlanetNameSwitch.place(relx = 0.68, rely = 0.89, anchor = tkinter.W)


        #The images of the simulation go here
        planetOrbitsSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabImageFrame,
                                                                           image = placeholderImage,
                                                                           text = "")
        planetOrbitsSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        planetOrbitsSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabTitleFrame,
                                                                             justify = LEFT,
                                                                             text = "Planet\nOrbits",
                                                                             font = customtkinter.CTkFont(size = 35, weight = "bold"))
        planetOrbitsSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabDescriptionFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Solves the N-body problem to simulate your\nfavorite planets but also your own ones by\nadding their name, color, mass, radius, initial\nvelocity and initial acceleration.",
                                                                                 font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.2, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabDescriptionFrame,
                                                                              justify = LEFT,
                                                                              text = "Field of physics: Newtonian Mechanics",
                                                                              font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.54, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabDescriptionFrame,
                                                                                    justify = LEFT,
                                                                                    text = 'Edit the given values of the planets that\nyou want, press on the "+ ADD" button to add the\nplanet and click on "Launch" start the simulation.',
                                                                                    font = customtkinter.CTkFont(size = 15, weight = "normal"))
        planetOrbitsSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetNameEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Name:",
                                                                                     font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetNameEntryTitle.place(relx = 0.011, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetColorEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Color:",
                                                                                      font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetColorEntryTitle.place(relx = 0.011, rely = 0.52, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetMassEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Mass (kg):",
                                                                                     font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetMassEntryTitle.place(relx = 0.011, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetRadiusEntryTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       text = "Radius (m):",
                                                                                       font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetRadiusEntryTitle.place(relx = 0.35, rely = 0.27, anchor = tkinter.W)
        
        planetOrbitsSimulationConfigTabPlanetInitialVxSliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          text = "Initial Vx (m/s):",
                                                                                          font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVxSliderTitle.place(relx = 0.35, rely = 0.52, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          text = "Initial Vy (m/s):",
                                                                                          font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVySliderTitle.place(relx = 0.35, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          text = "Initial ax (m/s²):",
                                                                                          font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAxSliderTitle.place(relx = 0.68, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial ay (m/s²):",
                                                                                           font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAySliderTitle.place(relx = 0.68, rely = 0.48, anchor = tkinter.W)
        
        print("the planet orbits config tab works")
        pass

def gravitySimulationConfigTab(bool):
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
                                                                         font = customtkinter.CTkFont(size = 20, weight = "bold"),
                                                                         width = 335,
                                                                         height = 100,
                                                                         corner_radius = 5,
                                                                         border_width = 1,
                                                                         command = gravitySimulationConfigTabLaunchButtonEvent)
        gravitySimulationConfigTabLaunchButton.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)


        #The configurators (items) of the simulation go here
        gravitySimulationConfigTabInitMassSlider = customtkinter.CTkSlider(master = gravitySimulationConfigTabItemsFrame,
                                                                              width = 150,
                                                                              height = 20,
                                                                              from_ = 0.1,
                                                                              to = 1000,
                                                                              command = gravitySimulationConfigTabInitMassSliderEvent)
        gravitySimulationConfigTabInitMassSlider.place(relx = 0.04, rely = 0.2, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccSlider = customtkinter.CTkSlider(master = gravitySimulationConfigTabItemsFrame,
                                                                              width = 150,
                                                                              height = 20,
                                                                              from_ = 0.1,
                                                                              to = 20,
                                                                              command = gravitySimulationConfigTabInitGravAccSliderEvent)
        gravitySimulationConfigTabInitGravAccSlider.place(relx = 0.04, rely = 0.4, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightSlider = customtkinter.CTkSlider(master = gravitySimulationConfigTabItemsFrame,
                                                                             width = 150,
                                                                             height = 20,
                                                                             from_ = 0.1,
                                                                             to = 10,
                                                                             command = gravitySimulationConfigTabInitHeightSliderEvent)
        gravitySimulationConfigTabInitHeightSlider.place(relx = 0.04, rely = 0.6, anchor = tkinter.W)

        #The images of the simulation go here
        gravitySimulationConfigTabInSimImage = customtkinter.CTkLabel(master = gravitySimulationConfigTabImageFrame,
                                                                           image = placeholderImage,
                                                                           text = "")
        gravitySimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        gravitySimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabTitleFrame,
                                                                      justify = LEFT,
                                                                      text = "Gravity\nSimulation",
                                                                      font = customtkinter.CTkFont(size = 35, weight = "bold"))
        gravitySimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        gravitySimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabDescriptionFrame,
                                                                            justify = LEFT,
                                                                            text = "Simulates an object of a changeable mass\nfalling under the influence of gravity at a\nspecific height.",
                                                                            font = customtkinter.CTkFont(size = 16, weight = "normal"))
        gravitySimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
        
        gravitySimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabDescriptionFrame,
                                                                         justify = LEFT,
                                                                         text = "Field of physics: Newtonian Mechanics",
                                                                         font = customtkinter.CTkFont(size = 16, weight = "normal"))
        gravitySimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.52, anchor = tkinter.W)
        
        gravitySimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = 'Change the physical properties that you want\nto include then press on "Launch" to start the\nsimulation.',
                                                                             font = customtkinter.CTkFont(size = 16, weight = "normal"))
        gravitySimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        gravitySimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Mass (kg): ",
                                                                              font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Height (m): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitHeightTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)



        print("the gravity config tab works")
        pass

def refractionSimulationConfigTab(bool):
    if bool == True:
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
                                                                            font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                                               values = ["Air", "Water", "Glass", "Ethanol", "Diamond", "Plastic", "Custom"],
                                                                                               command = refractionSimulationConfigInitRefractiveIndex1OptionMenuEvent)
        refractionSimulationConfigInitRefractiveIndex1OptionMenu.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)

        refractionSimulationConfigInitRefractiveIndex2OptionMenu = customtkinter.CTkOptionMenu(master = refractionSimulationConfigTabItemsFrame,
                                                                                               width = 150,
                                                                                               height = 25,
                                                                                               variable = refractionSimulationConfigTabInitRefractiveIndex2OptionMenuVar,
                                                                                               values = ["Air", "Water", "Glass", "Ethanol", "Diamond", "Plastic", "Custom"],
                                                                                               command = refractionSimulationConfigInitRefractiveIndex2OptionMenuEvent)
        refractionSimulationConfigInitRefractiveIndex2OptionMenu.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        refractionSimulationConfigTabInitIncidenceAngleSlider = customtkinter.CTkSlider(master = refractionSimulationConfigTabItemsFrame,
                                                                                        width = 150,
                                                                                        height = 20,
                                                                                        from_ = 0,
                                                                                        to = 90,
                                                                                        command = refractionSimulationConfigTabInitIncidenceAngleSliderEvent)
        refractionSimulationConfigTabInitIncidenceAngleSlider.place(relx = 0.04, rely = 0.8, anchor = tkinter.W)

        refractionSimulationConfigTabRayColorOptionMenu = customtkinter.CTkOptionMenu(master = refractionSimulationConfigTabItemsFrame,
                                                                                   width = 150,
                                                                                   height = 25,
                                                                                   variable = refractionSimulationConfigRayColorOptionMenuVar,
                                                                                   values = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"])
        refractionSimulationConfigTabRayColorOptionMenu.place(relx = 0.7, rely = 0.23, anchor = tkinter.W)

        refractionSimulationConfigInitRefractiveIndex1CustomEntry = customtkinter.CTkEntry(master = refractionSimulationConfigTabItemsFrame,
                                                                                           placeholder_text = "Float between 1.0 and 2",
                                                                                           width = 150,
                                                                                           height = 25,
                                                                                           corner_radius = 5,
                                                                                           border_width = 1)

        refractionSimulationConfigInitRefractiveIndex2CustomEntry = customtkinter.CTkEntry(master = refractionSimulationConfigTabItemsFrame,
                                                                                           placeholder_text = "Float between 1.0 and 2",
                                                                                           width = 150,
                                                                                           height = 25,
                                                                                           corner_radius = 5,
                                                                                           border_width = 1)
        
        #The images of the simulation go here
        refractionSimulationConfigTabInSimImage = customtkinter.CTkLabel(master = refractionSimulationConfigTabImageFrame,
                                                                         image = placeholderImage,
                                                                         text = "")
        refractionSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        #The labels of the config tab go here
        refractionSimulationConfigTabInitRefractiveIndex1TitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                             justify = LEFT,
                                                                                             text = "Initial Refractive Index 1: ",
                                                                                             font = customtkinter.CTkFont(size = 18, weight = "normal"))
        refractionSimulationConfigTabInitRefractiveIndex1TitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        refractionSimulationConfigTabInitRefractiveIndex2TitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                             justify = LEFT,
                                                                                             text = "Initial Refractive Index 2: ",
                                                                                             font = customtkinter.CTkFont(size = 18, weight = "normal"))
        refractionSimulationConfigTabInitRefractiveIndex2TitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)
        
        refractionSimulationConfigTabInitIncidenceAngleTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial Incidence Angle (°): ",
                                                                                           font = customtkinter.CTkFont(size = 18, weight = "normal"))
        refractionSimulationConfigTabInitIncidenceAngleTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        refractionSimulationConfigTabRayColorTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Ray Color: ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        refractionSimulationConfigTabRayColorTitleLabel.place(relx = 0.7, rely = 0.11, anchor = tkinter.W)
        
        print("the refraction config tab works")
        pass

def fluidSimulationConfigTab(bool):
    if bool == True:
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
                
        
        #The configurators (items) of the simulation go here
                
        
        #The images of the simulation go here
                
        
        #The labels of the config tab go here


        print("the fluid config tab works")
        pass

def temperatureSimulationConfigTab(bool):
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
                        
                
        #The configurators (items) of the simulation go here
                        
                
        #The images of the simulation go here
                        
                
        #The labels of the config tab go here
        

        print("the temperature config tab works")
        pass

#The sub tabs of the chemistry tab (chemistry simulations) are here
def bohrAtomSimulationConfigTab(bool):
    if bool == True:
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
                                
                        
        #The configurators (items) of the simulation go here
                                
                        
        #The images of the simulation go here
                                
                        
        #The labels of the config tab go here
        
        
        print("the Bohr atom config tab works")
        pass

def solutionMakerConfigTab(bool):
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
                                        
                                
        #The configurators (items) of the simulation go here
                                        
                                
        #The images of the simulation go here
                                        
                                
        #The labels of the config tab go here
        
        
        print("the solution maker config tab works")
        pass

def molecularLabConfigTab(bool):
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
                                                
                                        
        #The configurators (items) of the simulation go here
                                                
                                        
        #The images of the simulation go here
                                                
                                        
        #The labels of the config tab go here
        
        
        print("the molecular lab config tab works")
        pass

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
                                                        
        #The buttons go here
                                                        
                                                
        #The configurators (items) of the simulation go here
                                                        
                                                
        #The images of the simulation go here
                                                        
                                                
        #The labels of the config tab go here
        
        
        print("the reaction lab config tab works")
        pass

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
                                                                
        #The buttons go here
                                                                
                                                        
        #The configurators (items) of the simulation go here
                                                                
                                                        
        #The images of the simulation go here
                                                                
                                                        
        #The labels of the config tab go here
        
        
        print("the combustion config tab works")
        pass

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
                                                                        
        #The buttons go here
                                                                        
                                                                
        #The configurators (items) of the simulation go here
                                                                        
                                                                
        #The images of the simulation go here
                                                                        
                                                                
        #The labels of the config tab go here
        
        
        print("the smoke config tab works")
        pass

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
                                                                                
        #The buttons go here
                                                                                
                                                                        
        #The configurators (items) of the simulation go here
                                                                                
                                                                        
        #The images of the simulation go here
                                                                                
                                                                        
        #The labels of the config tab go here
        
        
        print("the atom collision config tab works")
        pass

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

#The labels go here
titleLabel = customtkinter.CTkLabel(master = optionsFrame,
                                    text = "Physics & Chemistry\nSandbox Launcher",
                                    font = customtkinter.CTkFont(size = 18, weight = "bold"))
titleLabel.place(relx = 0.5, rely = 0.1, anchor = tkinter.CENTER)

welcomeLabel = customtkinter.CTkLabel(master = mainFrame,
                                      text = "Welcome to the Physics & Chemistry\nSandbox Launcher!",
                                      font = customtkinter.CTkFont(size = 20, weight = "bold"))
welcomeLabel.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

welcomeSubLabel = customtkinter.CTkLabel(master = mainFrame,
                                         text = "Select one of the tabs on the left to start.",
                                         font = customtkinter.CTkFont(size = 15, weight = "normal"))
welcomeSubLabel.place(relx = 0.5, rely = 0.59, anchor = tkinter.CENTER)

postDataLabel = customtkinter.CTkLabel(master = mainFrame,
                                       text = "The name of the app is just a placeholder. I'll find a good one.",
                                       font = customtkinter.CTkFont(size = 10, weight = "normal"))
postDataLabel.place(relx = 0.5, rely = 0.95, anchor = tkinter.CENTER)

#The buttons go here
physicsSelectorButton = customtkinter.CTkButton(master = optionsFrame,
                                                text = "Physics Tab",
                                                width = 130,
                                                height = 25,
                                                corner_radius = 5,
                                                border_width = 1,
                                                command = physicsSelectorButtonEvent)
physicsSelectorButton.place(relx = 0.5, rely = 0.2, anchor = tkinter.CENTER)

chemistrySelectorButton = customtkinter.CTkButton(master = optionsFrame,
                                                  text = "Chemistry Tab",
                                                  width = 130,
                                                  height = 25,
                                                  corner_radius = 5,
                                                  border_width = 1,
                                                  command = chemistrySelectorButtonEvent)
chemistrySelectorButton.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

thePlaceSelectorButton = customtkinter.CTkButton(master = optionsFrame,
                                                 text = "The Place",
                                                 width = 130,
                                                 height = 25,
                                                 corner_radius = 5,
                                                 border_width = 1,
                                                 command = thePlaceSelectorButtonEvent)
thePlaceSelectorButton.place(relx = 0.5, rely = 0.4, anchor = tkinter.CENTER)

launcherSettingsButton = customtkinter.CTkButton(master = optionsFrame,
                                                 text = "Launcher Settings",
                                                 width = 130,
                                                 height = 25,
                                                 corner_radius = 5,
                                                 border_width = 1,
                                                 command = launcherSettingsButtonEvent)
launcherSettingsButton.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

gitHubButton = customtkinter.CTkButton(master = optionsFrame,
                                       text = "GitHub",
                                       width = 130,
                                       height = 25,
                                       corner_radius = 5,
                                       border_width = 1,
                                       command = gitHubButtonEvent)
gitHubButton.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

creditsButton = customtkinter.CTkButton(master = optionsFrame,
                                        text = "Credits",
                                        width = 130,
                                        height = 25,
                                        corner_radius = 5,
                                        border_width = 1,
                                        command = creditsButtonEvent)
creditsButton.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)

quitLauncherButton = customtkinter.CTkButton(master = optionsFrame,
                                             text = "Quit Launcher",
                                             width = 130,
                                             height = 25,
                                             corner_radius = 5,
                                             border_width = 1,
                                             command = quitLauncherButtonEvent)
quitLauncherButton.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

#The main loop is ran here
app.mainloop()