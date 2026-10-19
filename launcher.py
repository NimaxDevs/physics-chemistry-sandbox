import customtkinter, tkinter
from tkinter import * 

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1100x580")
app.resizable(False, False)
app.title("Physics & Chemistry Sandbox Launcher")

def physicsSelectorButtonEvent():
    pass

def chemistrySelectorButtonEvent():
    pass

def thePlaceSelectorButtonEvent():
    pass

def launcherSettingsButtonEvent():
    pass

def gitHubButtonEvent():
    pass

def quitLauncherButtonEvent():
    pass

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
launcherSettingsButton.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)

gitHubButton = customtkinter.CTkButton(master = optionsFrame,
                                       text = "GitHub",
                                       width = 130,
                                       height = 25,
                                       corner_radius = 5,
                                       border_width = 1,
                                       command = gitHubButtonEvent)
gitHubButton.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)

quitLauncherButton = customtkinter.CTkButton(master = optionsFrame,
                                             text = "Quit Launcher",
                                             width = 130,
                                             height = 25,
                                             corner_radius = 5,
                                             border_width = 1,
                                             command = quitLauncherButtonEvent)
quitLauncherButton.place(relx = 0.5, rely = 0.9, anchor = tkinter.CENTER)

app.mainloop()