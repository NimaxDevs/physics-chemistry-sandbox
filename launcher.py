#Do I even have to describe these two lines
import customtkinter, tkinter
from tkinter import * 

#The CTk appearance settings go here
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("themes/rime.json")

#The CTk settings go here
app = customtkinter.CTk()
app.geometry("1100x580")
app.resizable(False, False)
app.title("Physics & Chemistry Sandbox Launcher")

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

#The button events (functions) go here
def physicsSelectorButtonEvent():
    physicsTabSelected = True
    chemistryTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    physicsTab(physicsTabSelected)

def chemistrySelectorButtonEvent():
    chemistryTabSelected = True
    physicsTabSelected = False
    thePlaceTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    chemistryTab(chemistryTabSelected)
    
def thePlaceSelectorButtonEvent():
    thePlaceTabSelected = True
    physicsTabSelected = False
    chemistryTabSelected = False
    launcherSettingsSelected = False
    creditsTabSelected = False
    for child in mainFrame.winfo_children():
        child.destroy()
    thePlaceTab(thePlaceTabSelected)

def launcherSettingsButtonEvent():
    launcherSettingsSelected = True
    physicsTabSelected = False
    chemistryTabSelected = False
    thePlaceTabSelected = False
    creditsTabSelected = False
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
    for child in mainFrame.winfo_children():
        child.destroy()
    creditsTab(creditsTabSelected)

def quitLauncherButtonEvent():
    print("Launcher quit")
    app.quit()

#The tab functions go here
def physicsTab(bool):
    if bool == True:
        projectileSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                           width = 210,
                                                           height = 210,
                                                           corner_radius = 5,
                                                           border_width = 1)
        projectileSimulationFrame.place(relx = 0.15, rely = 0.2, anchor = tkinter.CENTER)

        pendulumSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                         width = 210,
                                                         height = 210,
                                                         corner_radius = 5,
                                                         border_width = 1)
        pendulumSimulationFrame.place(relx = 0.39, rely = 0.2, anchor = tkinter.CENTER)

        springSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                       width = 210,
                                                       height = 210,
                                                       corner_radius = 5,
                                                       border_width = 1)
        springSimulationFrame.place(relx = 0.63, rely = 0.2, anchor = tkinter.CENTER)

        planetOrbitsSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                             width = 210,
                                                             height = 210,
                                                             corner_radius = 5,
                                                             border_width = 1)
        planetOrbitsSimulationFrame.place(relx = 0.87, rely = 0.2, anchor = tkinter.CENTER)

        gravitySimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                        width = 210,
                                                        height = 210,
                                                        corner_radius = 5,
                                                        border_width = 1)
        gravitySimulationFrame.place(relx = 0.15, rely = 0.7, anchor = tkinter.CENTER)

        refractionSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                           width = 210,
                                                           height = 210,
                                                           corner_radius = 5,
                                                           border_width = 1)
        refractionSimulationFrame.place(relx = 0.39, rely = 0.7, anchor = tkinter.CENTER)

        fluidSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                      width = 210,
                                                      height = 210,
                                                      corner_radius = 5,
                                                      border_width = 1)
        fluidSimulationFrame.place(relx = 0.63, rely = 0.7, anchor = tkinter.CENTER)

        temperatureSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                            width = 210,
                                                            height = 210,
                                                            corner_radius = 5,
                                                            border_width = 1)
        temperatureSimulationFrame.place(relx = 0.87, rely = 0.7, anchor = tkinter.CENTER)

        

def chemistryTab(bool):
    if bool == True:
        bohrAtomSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                         width = 210,
                                                         height = 210,
                                                         corner_radius = 5,
                                                         border_width = 1)
        bohrAtomSimulationFrame.place(relx = 0.15, rely = 0.2, anchor = tkinter.CENTER)

        solutionMakerFrame = customtkinter.CTkFrame(master = mainFrame,
                                                    width = 210,
                                                    height = 210,
                                                    corner_radius = 5,
                                                    border_width = 1)
        solutionMakerFrame.place(relx = 0.39, rely = 0.2, anchor = tkinter.CENTER)

        molecularLabFrame = customtkinter.CTkFrame(master = mainFrame,
                                                   width = 210,
                                                   height = 210,
                                                   corner_radius = 5,
                                                   border_width = 1)
        molecularLabFrame.place(relx = 0.63, rely = 0.2, anchor = tkinter.CENTER)

        reactionLabFrame = customtkinter.CTkFrame(master = mainFrame,
                                                  width = 210,
                                                  height = 210,
                                                  corner_radius = 5,
                                                  border_width = 1)
        reactionLabFrame.place(relx = 0.87, rely = 0.2, anchor = tkinter.CENTER)

        combustionSimulationFrame = customtkinter.CTkFrame(master = mainFrame,
                                                           width = 210,
                                                           height = 210,
                                                           corner_radius = 5,
                                                           border_width = 1)
        combustionSimulationFrame.place(relx = 0.15, rely = 0.7, anchor = tkinter.CENTER)

        smokeSimulation = customtkinter.CTkFrame(master = mainFrame,
                                                 width = 210,
                                                 height = 210,
                                                 corner_radius = 5,
                                                 border_width = 1)
        smokeSimulation.place(relx = 0.39, rely = 0.7, anchor = tkinter.CENTER)

        atomCollisionSimulation = customtkinter.CTkFrame(master = mainFrame,
                                                         width = 210,
                                                         height = 210,
                                                         corner_radius = 5,
                                                         border_width = 1)
        atomCollisionSimulation.place(relx = 0.63, rely = 0.7, anchor = tkinter.CENTER)

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
    pass

def pendulumSimulationConfigTab(bool):
    pass

def springSimulationConfigTab(bool):
    pass

def planetOrbitsSimulationConfigTab(bool):
    pass

def gravitySimulationConfigTab(bool):
    pass

def refractionSimulationConfigTab(bool):
    pass

def fluidSimulationConfigTab(bool):
    pass

def temperatureSimulationConfigTab(bool):
    pass

#The sub tabs of the chemistry tab (chemistry simulations) are here
def bohrAtomSimulationConfigTab(bool):
    pass

def solutionMakerConfigTab(bool):
    pass

def molecularLabConfigTab(bool):
    pass

def reactionLabConfigTab(bool):
    pass

def combustionSimulationConfigTab(bool):
    pass

def smokeSimulationConfigTab(bool):
    pass

def atomCollisionSimulationTab(bool):
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