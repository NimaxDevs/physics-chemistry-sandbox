#Do I even have to describe these lines
import customtkinter, tkinter
from tkinter import * 
from PIL import Image
import webbrowser
import json
import os
import subprocess

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
planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabPlanetInitialVySliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabPlanetInitialAySliderValueVar = tkinter.StringVar(value = "")
planetOrbitsSimulationConfigTabShowOrbitTrailSwitchVar = tkinter.StringVar(value = "off")
planetOrbitsSimulationConfigTabShowPlanetNameSwitchVar = tkinter.StringVar(value = "off")
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

##The chemistry variables go here
###The variables of the Bohr Atom Simulation go here
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
    webbrowser.open("https://github.com/NimaxDevs/physics-chemistry-sandbox")
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
    configValues = {
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
    
    simulationPath = os.path.join("physicsSimulations", "projectileSimulation.py")
    subprocess.run(["python", simulationPath])
    projectileSimulationConfigTabLaunchButton.configure(state = "normal")
    projectileSimulationConfigTabLaunchButton.configure(text = "Launch")
    print("projectile simulation launched")

def pendulumSimulationConfigTabLaunchButtonEvent():
    configValues = {
        "initAngle":
    }
    print("pendulum simulation launched")

def springSimulationConfigTabLaunchButtonEvent():
    print("spring simulation launched")

def planetOrbitsSimulationConfigTabLaunchButtonEvent():
    print("planet orbits simulation launched")

def gravitySimulationConfigTabLaunchButtonEvent():
    print("gravity simulation launched")    

def refractionSimulationConfigTabLaunchButtonEvent():
    print("refraction simulation launched")

def fluidSimulationConfigTabLaunchButtonEvent():
    print("fluid simulation launched")

def temperatureSimulationConfigTabLaunchButtonEvent():
    print("temperature simulation launched")

##The buttons of the chemistry simulations go here
def bohrAtomSimulationConfigTabLaunchButtonEvent():
    print("Bohr atom simulation launched")

def solutionMakerConfigTabLaunchButtonEvent():
    print("solution maker simulation launched")

def molecularLabConfigTabLaunchButtonEvent():
    print("molecular lab simulation launched")

#The configurator (items) events of the simulations go here
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

###The configurator events of the Planet Orbits (imulation) go here
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
                                                                            font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                                       font = customtkinter.CTkFont(size = 18, weight = "normal"),
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

        projectileSimulationConfigTabInitVelocitySliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = projectileSimulationConfigTabInitVelocitySliderValueVar,
                                                                                           font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitVelocitySliderValueLabel.place(relx = 0.355, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Angle (°): ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitAngleTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        projectileSimulationConfigTabInitAngleSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                                   justify = LEFT,
                                                                                                   textvariable = projectileSimulationConfigTabInitAngleSliderValueVar,
                                                                                                   font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitAngleSliderValueLabel.place(relx = 0.28, rely = 0.3, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        projectileSimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                                           justify = LEFT,
                                                                                                           textvariable = projectileSimulationConfigTabInitGravAccSliderValueVar,
                                                                                                           font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.63, rely = 0.5, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Mass (kg): ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        projectileSimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       textvariable = projectileSimulationConfigTabInitMassSliderValueVar,
                                                                                       font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.7, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Diameter (m): ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitDiameterTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitDiameterSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = projectileSimulationConfigTabInitDiameterSliderValueVar,
                                                                                           font = customtkinter.CTkFont(size = 18, weight = "normal"))
        projectileSimulationConfigTabInitDiameterSliderValueLabel.place(relx = 0.81, rely = 0.11, anchor = tkinter.W)

        projectileSimulationConfigTabInitDragCoefTitleLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Initial Drag Coefficient: ",
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))

        projectileSimulationConfigTabInitDragCoefSliderValueLabel = customtkinter.CTkLabel(master = projectileSimulationConfigTabItemsFrame,
                                                                                                   justify = LEFT,
                                                                                                   textvariable = projectileSimulationConfigTabInitDragCoefSliderValueVar,
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

        pendulumSimulationConfigTabInitAngleSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = pendulumSimulationConfigTabInitAngleSliderValueVar,
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitAngleSliderValueLabel.place(relx = 0.28, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Angular Velocity (rad/s): ",
                                                                                     font = customtkinter.CTkFont(size = 15, weight = "normal"))
        pendulumSimulationConfigTabInitAngularVelTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitAngularVelSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           textvariable = pendulumSimulationConfigTabInitAngularVelSliderValueVar,
                                                                                           font = customtkinter.CTkFont(size = 15, weight = "normal"))
        pendulumSimulationConfigTabInitAngularVelSliderValueLabel.place(relx = 0.43, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Length (m): ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitLengthTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        pendulumSimulationConfigTabInitLengthSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       textvariable = pendulumSimulationConfigTabInitLengthSliderValueVar,
                                                                                       font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitLengthSliderValueLabel.place(relx = 0.31, rely = 0.5, anchor = tkinter.W)
        
        pendulumSimulationConfigTabInitMassTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Mass (kg): ",
                                                                               font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitMassTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        pendulumSimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     textvariable = pendulumSimulationConfigTabInitMassSliderValueVar,
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.7, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                  font = customtkinter.CTkFont(size = 14, weight = "normal"))
        pendulumSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.49, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                        justify = LEFT,
                                                                                        textvariable = pendulumSimulationConfigTabInitGravAccSliderValueVar,
                                                                                        font = customtkinter.CTkFont(size = 14, weight = "normal"))
        pendulumSimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.94, rely = 0.11, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefTitleLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      text = "Initial Damping Coefficient: ",
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitDampingCoefTitleLabel.place(relx = 0.49, rely = 0.3, anchor = tkinter.W)

        pendulumSimulationConfigTabInitDampingCoefSliderValueLabel = customtkinter.CTkLabel(master = pendulumSimulationConfigTabItemsFrame,
                                                                                            justify = LEFT,
                                                                                            textvariable = pendulumSimulationConfigTabInitDampingCoefSliderValueVar,
                                                                                            font = customtkinter.CTkFont(size = 18, weight = "normal"))
        pendulumSimulationConfigTabInitDampingCoefSliderValueLabel.place(relx = 0.89, rely = 0.3, anchor = tkinter.W)

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

        springSimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                   justify = LEFT,
                                                                                   textvariable = springSimulationConfigTabInitMassSliderValueVar,
                                                                                   font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.11, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.3, anchor = tkinter.W)

        springSimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = springSimulationConfigTabInitGravAccSliderValueVar,
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.63, rely = 0.3, anchor = tkinter.W)
        
        springSimulationConfigTabInitLengthTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Length (cm): ",
                                                                               font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitLengthTitleLabel.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        springSimulationConfigTabInitLengthSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     textvariable = springSimulationConfigTabInitLengthSliderValueVar,
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitLengthSliderValueLabel.place(relx = 0.33, rely = 0.5, anchor = tkinter.W)
                
        springSimulationConfigTabInitStiffTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Stiffness (N/m): ",
                                                                              font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitStiffTitleLabel.place(relx = 0.05, rely = 0.7, anchor = tkinter.W)

        springSimulationConfigTabInitStiffSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    textvariable = springSimulationConfigTabInitStiffSliderValueVar,
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitStiffSliderValueLabel.place(relx = 0.38, rely = 0.7, anchor = tkinter.W)
        
        springSimulationConfigTabInitDampingCoefTitleLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Initial Damping Coefficient: ",
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitDampingCoefTitleLabel.place(relx = 0.51, rely = 0.11, anchor = tkinter.W)

        springSimulationConfigTabInitDampingCoefSliderValueLabel = customtkinter.CTkLabel(master = springSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          textvariable = springSimulationConfigTabInitDampingCoefSliderValueVar,
                                                                                          font = customtkinter.CTkFont(size = 18, weight = "normal"))
        springSimulationConfigTabInitDampingCoefSliderValueLabel.place(relx = 0.91, rely = 0.11, anchor = tkinter.W)
        
def planetOrbitsSimulationConfigTab(bool):
    if bool == True:
        #Function to add & save the infos of the planets
        def planetOrbitsSimulationConfigTabAddPlanetButtonEvent():
            global planetNumber
            if (planetOrbitsSimulationConfigTabPlanetNameEntry.get() != "") and (planetOrbitsSimulationConfigTabPlanetColorEntry.get() != "") and (planetOrbitsSimulationConfigTabPlanetMassEntry.get() != "") and (planetOrbitsSimulationConfigTabPlanetRadiusEntry.get() != ""):
                planetNumber += 1
                print(f"Planet {planetNumber}:\nName: {planetOrbitsSimulationConfigTabPlanetNameEntry.get()}\nColor: {planetOrbitsSimulationConfigTabPlanetColorEntry.get()}\nMass: {planetOrbitsSimulationConfigTabPlanetMassEntry.get()}\nRadius: {planetOrbitsSimulationConfigTabPlanetRadiusEntry.get()}\nInitial Vx: {round(planetOrbitsSimulationConfigTabPlanetInitialVxSlider.get(), 3)}\nInitial Vy: {round(planetOrbitsSimulationConfigTabPlanetInitialVySlider.get(), 3)}\nInitial ax: {round(planetOrbitsSimulationConfigTabPlanetInitialAxSlider.get(), 3)}\nInitial ay: {round(planetOrbitsSimulationConfigTabPlanetInitialAySlider.get(), 3)}\nShow Orbit Trail: {planetOrbitsSimulationConfigTabShowOrbitTrailSwitch.get()}\nShow Planet Name: {planetOrbitsSimulationConfigTabShowPlanetNameSwitch.get()}")
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
                                                                                 placeholder_text = "This form: R, G, B",
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

        planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueVar,
                                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVxSliderValueLabel.place(relx = 0.56, rely = 0.52, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial Vy (m/s):",
                                                                                           font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVySliderTitle.place(relx = 0.35, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialVySliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialVySliderValueVar,
                                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialVySliderValueLabel.place(relx = 0.56, rely = 0.77, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                          justify = LEFT,
                                                                                          text = "Initial ax (m/s²):",
                                                                                          font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAxSliderTitle.place(relx = 0.68, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueVar,
                                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAxSliderValueLabel.place(relx = 0.9, rely = 0.27, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySliderTitle = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                           justify = LEFT,
                                                                                           text = "Initial ay (m/s²):",
                                                                                           font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAySliderTitle.place(relx = 0.68, rely = 0.48, anchor = tkinter.W)

        planetOrbitsSimulationConfigTabPlanetInitialAySliderValueLabel = customtkinter.CTkLabel(master = planetOrbitsSimulationConfigTabItemsFrame,
                                                                                                justify = LEFT,
                                                                                                textvariable = planetOrbitsSimulationConfigTabPlanetInitialAySliderValueVar,
                                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        planetOrbitsSimulationConfigTabPlanetInitialAySliderValueLabel.place(relx = 0.9, rely = 0.48, anchor = tkinter.W)
        
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

        gravitySimulationConfigTabInitMassSliderValueLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    textvariable = gravitySimulationConfigTabInitMassSliderValueVar,
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitMassSliderValueLabel.place(relx = 0.3, rely = 0.11, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Gravitational Acceleration (m/s²): ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitGravAccTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)

        gravitySimulationConfigTabInitGravAccSliderValueLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                       justify = LEFT,
                                                                                       textvariable = gravitySimulationConfigTabInitGravAccSliderValueVar,
                                                                                       font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitGravAccSliderValueLabel.place(relx = 0.63, rely = 0.38, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightTitleLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Height (m): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitHeightTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        gravitySimulationConfigTabInitHeightSliderValueLabel = customtkinter.CTkLabel(master = gravitySimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = gravitySimulationConfigTabInitHeightSliderValueVar,
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        gravitySimulationConfigTabInitHeightSliderValueLabel.place(relx = 0.31, rely = 0.66, anchor = tkinter.W)

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
                                                                                               values = ["Air (1.0)", "Water (1.33)", "Glass (1.52)", "Ethanol (1.36)", "Diamond (2.417)", "Plastic (1.59)", "Custom"],
                                                                                               command = refractionSimulationConfigInitRefractiveIndex1OptionMenuEvent)
        refractionSimulationConfigInitRefractiveIndex1OptionMenu.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)

        refractionSimulationConfigInitRefractiveIndex2OptionMenu = customtkinter.CTkOptionMenu(master = refractionSimulationConfigTabItemsFrame,
                                                                                               width = 150,
                                                                                               height = 25,
                                                                                               variable = refractionSimulationConfigTabInitRefractiveIndex2OptionMenuVar,
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
        refractionSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabTitleFrame,
                                                                              justify = LEFT,
                                                                              text = "Refraction\nSimulation",
                                                                              font = customtkinter.CTkFont(size = 35, weight = "bold"))
        refractionSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                
        refractionSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabDescriptionFrame,
                                                                                    justify = LEFT,
                                                                                    text = "Simulates a ray of light whose initial angle\nand color can be changed passing through\ntwo refractive mediums of specific\nrefractive indexes based on the Snell-Descartes\nlaw.",
                                                                                    font = customtkinter.CTkFont(size = 15, weight = "normal"))
        refractionSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.25, anchor = tkinter.W)
                
        refractionSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabDescriptionFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Field of physics: Optics",
                                                                                 font = customtkinter.CTkFont(size = 16, weight = "normal"))
        refractionSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.59, anchor = tkinter.W)

        refractionSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabDescriptionFrame,
                                                                                     justify = LEFT,
                                                                                     text = 'Select or change the physical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                                     font = customtkinter.CTkFont(size = 16, weight = "normal"))
        refractionSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
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

        refractionSimulationConfigTabInitIncidenceAngleSliderValueLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                                 justify = LEFT,
                                                                                                 textvariable = refractionSimulationConfigTabInitIncidenceAngleSliderValueVar,
                                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        refractionSimulationConfigTabInitIncidenceAngleSliderValueLabel.place(relx = 0.43, rely = 0.66, anchor = tkinter.W)

        refractionSimulationConfigTabRayColorTitleLabel = customtkinter.CTkLabel(master = refractionSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Ray Color: ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        refractionSimulationConfigTabRayColorTitleLabel.place(relx = 0.7, rely = 0.11, anchor = tkinter.W)
        
        print("the refraction config tab works")
        pass

def fluidSimulationConfigTab(bool):
    if bool == True:
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
                                                                       font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                                 values = ["Water", "Honey", "Olive Oil", "Ethanol", "Iced Tea", "Chocolate Milk", "Custom"],
                                                                                 command = fluidSimulationConfigInitDensityOptionMenuEvent)
        fluidSimulationConfigInitDensityOptionMenu.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        fluidSimulationConfigInitDensityCustomEntry = customtkinter.CTkEntry(master = fluidSimulationConfigTabItemsFrame,
                                                                             placeholder_text = "Between 0.1 and 3",
                                                                             width = 120,
                                                                             height = 25,
                                                                             corner_radius = 5,
                                                                             border_width = 1)        

        fluidSimulationConfigInitViscosityOptionMenu = customtkinter.CTkOptionMenu(master = fluidSimulationConfigTabItemsFrame,
                                                                                   width = 150,
                                                                                   height = 25,
                                                                                   variable = fluidSimulationConfigInitViscosityOptionMenuVar,
                                                                                   values = ["Water", "Honey", "Olive Oil", "Ethanol", "Iced Tea", "Chocolate Milk", "Custom"],
                                                                                   command = fluidSimulationConfigInitViscosityOptionMenuEvent)
        fluidSimulationConfigInitViscosityOptionMenu.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)

        fluidSimulationConfigInitViscosityCustomEntry = customtkinter.CTkEntry(master = fluidSimulationConfigTabItemsFrame,
                                                                               placeholder_text = "Between 0.1 and 1",
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
                                                                               values = ["Water", "Honey", "Olive Oil", "Ethanol", "Iced Tea", "Chocolate Milk"])
        fluidSimulationConfigInitColorOptionMenu.place(relx = 0.6, rely = 0.5, anchor = tkinter.W) 

        fluidSimulationConfigTabShowLatticeSwitch = customtkinter.CTkSwitch(master = fluidSimulationConfigTabItemsFrame,
                                                                            width = 50,
                                                                            height = 50,
                                                                            bg_color = "transparent",
                                                                            text = "Show Lattice",
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
                                                                    font = customtkinter.CTkFont(size = 35, weight = "bold"))
        fluidSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                        
        fluidSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabDescriptionFrame,
                                                                          justify = LEFT,
                                                                          text = "Simulates a fluid whose physical properties\nsuch as its volume, density, viscosity and\npressure can be changed.",
                                                                          font = customtkinter.CTkFont(size = 16, weight = "normal"))
        fluidSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                        
        fluidSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabDescriptionFrame,
                                                                       justify = LEFT,
                                                                       text = "Field of physics: Fluid Mechanics & CFD",
                                                                       font = customtkinter.CTkFont(size = 16, weight = "normal"))
        fluidSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        fluidSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabDescriptionFrame,
                                                                           justify = LEFT,
                                                                           text = 'Select or change the physical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                           font = customtkinter.CTkFont(size = 16, weight = "normal"))
        fluidSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        fluidSimulationConfigTabInitVolumeTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                              justify = LEFT,
                                                                              text = "Initial Volume (L): ",
                                                                              font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitVolumeTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitVolumeSliderValueLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                    justify = LEFT,
                                                                                    textvariable = fluidSimulationConfigTabInitVolumeSliderValueVar,
                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitVolumeSliderValueLabel.place(relx = 0.31, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitDensityTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                               justify = LEFT,
                                                                               text = "Initial Density (kg/m³): ",
                                                                               font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitDensityTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)

        fluidSimulationConfigTabInitViscosityTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                 justify = LEFT,
                                                                                 text = "Initial Viscosity: ",
                                                                                 font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitViscosityTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        fluidSimulationConfigTabInitPressureTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Pressure (Pa): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitPressureTitleLabel.place(relx = 0.6, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitPressureSliderValueLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = fluidSimulationConfigTabInitPressureSliderValueVar,
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitPressureSliderValueLabel.place(relx = 0.9, rely = 0.11, anchor = tkinter.W)

        fluidSimulationConfigTabInitColorTitleLabel = customtkinter.CTkLabel(master = fluidSimulationConfigTabItemsFrame,
                                                                             justify = LEFT,
                                                                             text = "Initial Color: ",
                                                                             font = customtkinter.CTkFont(size = 18, weight = "normal"))
        fluidSimulationConfigTabInitColorTitleLabel.place(relx = 0.6, rely = 0.38, anchor = tkinter.W)

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
        temperatureSimulationConfigTabLaunchButton = customtkinter.CTkButton(master = temperatureSimulationConfigTabLaunchButtonFrame,
                                                                             text = "Launch",
                                                                             font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                          image = placeholderImage,
                                                                          text = "")
        temperatureSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)        
                                
        #The labels of the config tab go here
        temperatureSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabTitleFrame,
                                                                          justify = LEFT,
                                                                          text = "Temperature\nSimulation",
                                                                          font = customtkinter.CTkFont(size = 35, weight = "bold"))
        temperatureSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                                
        temperatureSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabDescriptionFrame,
                                                                                justify = LEFT,
                                                                                text = "Simulates a large number of customizable\nparticles interacting with each other under the\ninfluence of heat or cold.",
                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        temperatureSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                                
        temperatureSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = "Field of physics: Thermodynamics",
                                                                             font = customtkinter.CTkFont(size = 16, weight = "normal"))
        temperatureSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                
        temperatureSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabDescriptionFrame,
                                                                                 justify = LEFT,
                                                                                 text = 'Change the physical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                                 font = customtkinter.CTkFont(size = 16, weight = "normal"))
        temperatureSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
        temperatureSimulationConfigTabInitParticleNumberTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                            justify = LEFT,
                                                                                            text = "Initial Particle Number: ",
                                                                                            font = customtkinter.CTkFont(size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleNumberTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        temperatureSimulationConfigTabInitParticleNumberSliderValueLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                                  justify = LEFT,
                                                                                                  textvariable = temperatureSimulationConfigTabInitParticleNumberSliderValueVar,
                                                                                                  font = customtkinter.CTkFont(size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleNumberSliderValueLabel.place(relx = 0.39, rely = 0.11, anchor = tkinter.W)

        temperatureSimulationConfigTabInitParticleDiameterTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                              justify = LEFT,
                                                                                              text = "Initial Particle Diameter (µm): ",
                                                                                              font = customtkinter.CTkFont(size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleDiameterTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)

        temperatureSimulationConfigTabInitParticleDiameterSliderValueLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                                    justify = LEFT,
                                                                                                    textvariable = temperatureSimulationConfigTabInitParticleDiameterSliderValueVar,
                                                                                                    font = customtkinter.CTkFont(size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitParticleDiameterSliderValueLabel.place(relx = 0.48, rely = 0.38, anchor = tkinter.W)

        temperatureSimulationConfigTabInitTempTitleLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Temperature (°C): ",
                                                                                  font = customtkinter.CTkFont(size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitTempTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        temperatureSimulationConfigTabInitTempSliderValueLabel = customtkinter.CTkLabel(master = temperatureSimulationConfigTabItemsFrame,
                                                                                        justify = LEFT,
                                                                                        textvariable = temperatureSimulationConfigTabInitTempSliderValueVar,
                                                                                        font = customtkinter.CTkFont(size = 18, weight = "normal"))
        temperatureSimulationConfigTabInitTempSliderValueLabel.place(relx = 0.41, rely = 0.66, anchor = tkinter.W)

        print("the temperature config tab works")
        pass

#The sub tabs of the chemistry tab (chemistry simulations) are here
def bohrAtomSimulationConfigTab(bool):
    if bool == True:
        def bohrAtomSimulationConfigTabHButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("H atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabHeButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("He atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabLiButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Li atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabBeButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Be atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabBButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("B atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabCButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("C atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabNButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("N atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabOButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("O atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabFButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("F atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabNeButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Ne atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabNaButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Na atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabMgButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Mg atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabAlButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Al atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabSiButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("Si atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabPButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("P atom selected")
            if bohrAtomSimulationConfigTabAtomSelected == False:
                bohrAtomSimulationConfigTabAtomSelected = True

        def bohrAtomSimulationConfigTabSButtonEvent():
            global bohrAtomSimulationConfigTabAtomSelected 
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
                print("S atom selected")
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
                                                                          font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                       image = placeholderImage,
                                                                       text = "")
        bohrAtomSimulationConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                         
                        
        #The labels of the config tab go here
        bohrAtomSimulationConfigTabTitleLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabTitleFrame,
                                                                      justify = LEFT,
                                                                      text = "Bohr\nRepresentation",
                                                                      font = customtkinter.CTkFont(size = 35, weight = "bold"))
        bohrAtomSimulationConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                                        
        bohrAtomSimulationConfigTabDescriptionLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabDescriptionFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Simulates some of the atoms of the periodic\ntable according to Niels Bohr's representation\nmodel by showing their electron shells and\nnucleons.",
                                                                                     font = customtkinter.CTkFont(size = 16, weight = "normal"))
        bohrAtomSimulationConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.2, anchor = tkinter.W)
                                        
        bohrAtomSimulationConfigTabCategoryLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabDescriptionFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Field of chemistry: Matter Study",
                                                                                  font = customtkinter.CTkFont(size = 16, weight = "normal"))
        bohrAtomSimulationConfigTabCategoryLabel.place(relx = 0.01, rely = 0.55, anchor = tkinter.W)
                        
        bohrAtomSimulationConfigTabInstructionsLabel = customtkinter.CTkLabel(master = bohrAtomSimulationConfigTabDescriptionFrame,
                                                                                      justify = LEFT,
                                                                                      text = 'Select the element of the periodic table\nthat you want to include then press on\n"Launch" to start the simulation.',
                                                                                      font = customtkinter.CTkFont(size = 16, weight = "normal"))
        bohrAtomSimulationConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)
        
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
        solutionMakerConfigTabLaunchButton = customtkinter.CTkButton(master = solutionMakerConfigTabLaunchButtonFrame,
                                                                     text = "Launch",
                                                                     font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                  image = placeholderImage,
                                                                  text = "")
        solutionMakerConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                                
                                
        #The labels of the config tab go here
        solutionMakerConfigTabTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabTitleFrame,
                                                                  justify = LEFT,
                                                                  text = "Solution\nMaker",
                                                                  font = customtkinter.CTkFont(size = 35, weight = "bold"))
        solutionMakerConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                        
        solutionMakerConfigTabDescriptionLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabDescriptionFrame,
                                                                                justify = LEFT,
                                                                                text = "Simulates a solution of a choosable volume\nwhose solvent, solute and solute mass can be\nchanged.",
                                                                                font = customtkinter.CTkFont(size = 16, weight = "normal"))
        solutionMakerConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                        
        solutionMakerConfigTabCategoryLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabDescriptionFrame,
                                                                             justify = LEFT,
                                                                             text = "Field of chemistry: Molecular Dynamics",
                                                                             font = customtkinter.CTkFont(size = 16, weight = "normal"))
        solutionMakerConfigTabCategoryLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
        
        solutionMakerConfigTabInstructionsLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabDescriptionFrame,
                                                                                 justify = LEFT,
                                                                                 text = 'Select or change the chemical properties that\nyou want to include then press on "Launch" to\nstart the simulation.',
                                                                                 font = customtkinter.CTkFont(size = 16, weight = "normal"))
        solutionMakerConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.83, anchor = tkinter.W)

        solutionMakerConfigTabInitSolventTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                             justify = LEFT,
                                                                             text = "Initial Solvent: ",
                                                                             font = customtkinter.CTkFont(size = 18, weight = "normal"))
        solutionMakerConfigTabInitSolventTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)
        
        solutionMakerConfigTabInitSolventVolTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Solvent Volume (mL): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        solutionMakerConfigTabInitSolventVolTitleLabel.place(relx = 0.05, rely = 0.35, anchor = tkinter.W)

        solutionMakerConfigTabInitSolventVolSliderValueLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = solutionMakerConfigTabInitSolventVolSliderValueVar,
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        solutionMakerConfigTabInitSolventVolSliderValueLabel.place(relx = 0.46, rely = 0.35, anchor = tkinter.W)

        solutionMakerConfigTabInitSoluteTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                            justify = LEFT,
                                                                            text = "Initial Solute (solid): ",
                                                                            font = customtkinter.CTkFont(size = 18, weight = "normal"))
        solutionMakerConfigTabInitSoluteTitleLabel.place(relx = 0.05, rely = 0.55, anchor = tkinter.W)

        solutionMakerConfigTabInitSoluteMassTitleLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Solute Mass (g): ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        solutionMakerConfigTabInitSoluteMassTitleLabel.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)


        solutionMakerConfigTabInitSoluteMassSliderValueLabel = customtkinter.CTkLabel(master = solutionMakerConfigTabItemsFrame,
                                                                                      justify = LEFT,
                                                                                      textvariable = solutionMakerConfigTabInitSoluteMassSliderValueVar,
                                                                                      font = customtkinter.CTkFont(size = 18, weight = "normal"))
        solutionMakerConfigTabInitSoluteMassSliderValueLabel.place(relx = 0.38, rely = 0.8, anchor = tkinter.W)

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
        molecularLabConfigTabLaunchButton = customtkinter.CTkButton(master = molecularLabConfigTabLaunchButtonFrame,
                                                                    text = "Launch",
                                                                    font = customtkinter.CTkFont(size = 20, weight = "bold"),
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
                                                                                  values = ["Carbon Dioxide (CO₂)", "Glucose (C₆H₁₂O₆)", "Ethanol (C₂H₅OH)", "Acetone (C₃H₆O)", "Methanol (CH₃OH)", "Formaldehyde (CH₂O)"],
                                                                                  command = molecularLabConfigTabInitMoleculeOptionMenuEvent)
        molecularLabConfigTabInitMoleculeOptionMenu.place(relx = 0.05, rely = 0.23, anchor = tkinter.W)
        
        molecularLabConfigTabInitHydrogenColorOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                       width = 150,
                                                                                       height = 25,
                                                                                       fg_color = "green",
                                                                                       variable = molecularLabConfigTabInitHydrogenColorOptionMenuVar,
                                                                                       values = ["White", "Light Blue", "Light Gray", "Green"],
                                                                                       command = molecularLabConfigTabInitHydrogenColorOptionMenuEvent)
        molecularLabConfigTabInitHydrogenColorOptionMenu.place(relx = 0.05, rely = 0.5, anchor = tkinter.W)

        molecularLabConfigTabInitCarbonColorOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                     width = 150,
                                                                                     height = 25,
                                                                                     fg_color = "green",
                                                                                     variable = molecularLabConfigTabInitCarbonColorOptionMenuVar,
                                                                                     values = ["Black", "Dark Blue", "Dark Gray", "Dark Green"],
                                                                                     command = molecularLabConfigTabInitCarbonColorOptionMenuEvent)
        molecularLabConfigTabInitCarbonColorOptionMenu.place(relx = 0.05, rely = 0.8, anchor = tkinter.W)

        molecularLabConfigTabInitOxygenColorOptionMenu = customtkinter.CTkOptionMenu(master = molecularLabConfigTabItemsFrame,
                                                                                     width = 150,
                                                                                     height = 25,
                                                                                     fg_color = "green",
                                                                                     variable = molecularLabConfigTabInitOxygenColorOptionMenuVar,
                                                                                     values = ["Red", "Dark Red", "Dark Pink"],
                                                                                     command = molecularLabConfigTabInitOxygenColorOptionMenuEvent)
        molecularLabConfigTabInitOxygenColorOptionMenu.place(relx = 0.6, rely = 0.23, anchor = tkinter.W)                                          
                                        
        #The images of the simulation go here
        molecularLabConfigTabInSimImage = customtkinter.CTkLabel(master = molecularLabConfigTabImageFrame,
                                                                 image = placeholderImage,
                                                                 text = "")
        molecularLabConfigTabInSimImage.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)                                           
                                        
        #The labels of the config tab go here
        molecularLabConfigTabTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabTitleFrame,
                                                                 justify = LEFT,
                                                                 text = "Molecular\nLab",
                                                                 font = customtkinter.CTkFont(size = 35, weight = "bold"))
        molecularLabConfigTabTitleLabel.place(relx = 0.01, rely = 0.5, anchor = tkinter.W)
                                
        molecularLabConfigTabDescriptionLabel = customtkinter.CTkLabel(master = molecularLabConfigTabDescriptionFrame,
                                                                       justify = LEFT,
                                                                       text = "Simulates a bunch of molecules made from\nassembled elements of the periodic table\nwhose colors can be changed.",
                                                                       font = customtkinter.CTkFont(size = 16, weight = "normal"))
        molecularLabConfigTabDescriptionLabel.place(relx = 0.01, rely = 0.15, anchor = tkinter.W)
                                
        molecularLabConfigTabCategoryLabel = customtkinter.CTkLabel(master = molecularLabConfigTabDescriptionFrame,
                                                                    justify = LEFT,
                                                                    text = "Field of chemistry: Molecular Dynamics",
                                                                    font = customtkinter.CTkFont(size = 16, weight = "normal"))
        molecularLabConfigTabCategoryLabel.place(relx = 0.01, rely = 0.45, anchor = tkinter.W)
                
        molecularLabConfigTabInstructionsLabel = customtkinter.CTkLabel(master = molecularLabConfigTabDescriptionFrame,
                                                                        justify = LEFT,
                                                                        text = 'Select one of the molecules that\nyou want to include, change the colors of the\natoms to your liking then press on "Launch" to\nstart the simulation.',
                                                                        font = customtkinter.CTkFont(size = 16, weight = "normal"))
        molecularLabConfigTabInstructionsLabel.place(relx = 0.01, rely = 0.8, anchor = tkinter.W)

        molecularLabConfigTabInitMoleculeTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                     justify = LEFT,
                                                                                     text = "Initial Molecule: ",
                                                                                     font = customtkinter.CTkFont(size = 18, weight = "normal"))
        molecularLabConfigTabInitMoleculeTitleLabel.place(relx = 0.05, rely = 0.11, anchor = tkinter.W)

        molecularLabConfigTabInitHydrogenColorTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                  justify = LEFT,
                                                                                  text = "Initial Hydrogen Atom Color: ",
                                                                                  font = customtkinter.CTkFont(size = 18, weight = "normal"))
        molecularLabConfigTabInitHydrogenColorTitleLabel.place(relx = 0.05, rely = 0.38, anchor = tkinter.W)
        
        molecularLabConfigTabInitCarbonColorTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Carbon Atom Color: ",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        molecularLabConfigTabInitCarbonColorTitleLabel.place(relx = 0.05, rely = 0.66, anchor = tkinter.W)

        molecularLabConfigTabInitOxygenColorTitleLabel = customtkinter.CTkLabel(master = molecularLabConfigTabItemsFrame,
                                                                                justify = LEFT,
                                                                                text = "Initial Oxygen Atom Color:",
                                                                                font = customtkinter.CTkFont(size = 18, weight = "normal"))
        molecularLabConfigTabInitOxygenColorTitleLabel.place(relx = 0.6, rely = 0.11, anchor = tkinter.W)

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