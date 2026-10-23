import pygame
import math
from sys import exit
import random

#The window variables go here
frameRate = 60
windowWidth = 1100
windowHeight = 580

#These lines initialize the Pygame window as well as the clock and the font
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Projectile Simualtion")
clock = pygame.time.Clock()
pygame.font.init()

#The "art" variables go here
font = pygame.font.Font(None, 24)
grayColor = (128, 128, 128)
lightGrayColor = (200, 200, 200)
darkGrayColor = (80, 80, 80)
yellowColor = (255, 255, 0)
whiteColor = (255, 255, 255)
redColor = (255, 0, 0)
blackColor = (0, 0, 0)

#The physical variables go here
sizeScale = 4 #1 meter corresponds to 4 pixels
init_g = 9.8 #The values from the launcher will be here
start_x = 100
start_y = 530
initVelocity = 50 #The values from the launcher will be here
initAngle = 45 #The values from the launcher will be here
initMass = 1000 #The values from the launcher will be here
initDiameter = 5 #The values from the launcher will be here
dragCoef = 0 #The values from the launcher will be here
initialSurfaceArea = math.pi * (initDiameter/2)**2
airRho = 1.225

#This variable stores the points plotted by the projectile trajectory
trajectoryPoints = []

#The simulation control variables go here
time = 0
dt = 0.1

#This functions creates an explosion when the projectile hits the ground
def drawExplosion(x, y):
    for i in range(10):
        pygame.draw.circle(screen, yellowColor, (x + random.randint(-10, 10), y + random.randint(-10, 10)), 5)

#These lines of code initialize the variables needed to make the physics calculations
initAngleRad = math.radians(initAngle) #converting degrees to radians
initVelocity_x = initVelocity * math.cos(initAngleRad) #creates the x-component of the velocity
initVelocity_y = -initVelocity * math.sin(initAngleRad) #creates the y-component of the velocity
x = start_x
y = start_y

#The main loop is here
while True:
    screen.fill(whiteColor) #Fills the screen with a white background
    
    #Checks if the "X" button of the windows is pressed and if so: the window closes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Calculates the total velocity of the projectile (I know that I should have used vectors instead of this, I might change the logic later)
    totalVelocity = math.sqrt(initVelocity_x**2 + initVelocity_y**2)

    #Calculates the total drag force using the air density, drag coefficient, surface area of the projectile and the total velocity squared   
    totalDragForce = 0.5 * airRho * dragCoef * initialSurfaceArea * (totalVelocity**2)
    dragForce_x = totalDragForce * (initVelocity_x / totalVelocity) #creates the x-component of the drag force
    dragForce_y = totalDragForce * (initVelocity_y / totalVelocity) #creates the y-component of the drag force

    #These lines protect the simulation from breaking (launching a hot air balloon at Mach 1 for example) by checking the value of the x-component of the velocity
    if abs((dragForce_x / initMass) * dt) > abs(initVelocity_x):
        initVelocity_x = 0
        warningLabel = font.render("bro, the values are so unrealistic that the simulation would actually break", True, redColor)
        warningLabelRect = warningLabel.get_rect(center = (windowWidth // 2, windowHeight // 2))
        screen.blit(warningLabel, warningLabelRect)
    else:
        initVelocity_x -= (dragForce_x / initMass) * dt

    #These lines also protect the simulation from breaking by checking the value of the -component of the velocity
    if abs((dragForce_y / initMass) * dt) > abs (initVelocity_y):
        initVelocity_y = 0
        warningLabel = font.render("bro, the values are so unrealistic that the simulation would actually break", True, redColor)
        warningLabelRect = warningLabel.get_rect(center = (windowWidth // 2, windowHeight // 2))
        screen.blit(warningLabel, warningLabelRect)
    else:
        initVelocity_y -= (dragForce_y / initMass) * dt

    #Applies the gravitational acceleration to the y-component of the velocity (the x-component isn't affected by gravity; therefore, this isn't done for the x-component)
    initVelocity_y += init_g * dt

    #Updates the position of the projectile by using the Euler's method (by integrating them numerically)
    x += (initVelocity_x  * dt) #Updates the x position
    y += (initVelocity_y * dt) #Updates the y position

    #Adds the predefined time step to the simulation time variable
    time += dt

    #Sticks the projectile to the ground and creates an explosion by checking if it reaches the y position of the ground line (sort of collision checking)    
    if y > windowHeight - 50:
        y = windowHeight - 50
        drawExplosion (x, y)
        trajectoryPoints.clear()

    #Draws the points plotted by the projectile trajectory if the simulation time variable is greater than 0
    if time > 0:
        trajectoryPoints.append((int(x), int(y)))
    for point in trajectoryPoints:
        pygame.draw.circle(screen, lightGrayColor, point, 2)

    #Well, this line draws the projectile
    pygame.draw.circle(screen, redColor, (int(x), int(y)), initDiameter * 4)

    #And this one draws the floor (a line)
    pygame.draw.line(screen, blackColor, (0, windowHeight - 50), (windowWidth, windowHeight - 50), 2)

    #These lines create the labels representing the values of the physical properties of the simulation
    upperLabel = font.render("Simulating Projectile", True, blackColor)
    gLabel = font.render(f"Gravitational Acceleration: {init_g:.1f} m/s²", True, blackColor)
    velocityLabel = font.render(f"Velocity: {initVelocity:.1f} m/s", True, blackColor)
    angleLabel = font.render(f"Angle: {initAngle:.1f}°", True, blackColor)
    massLabel = font.render(f"Mass: {initMass} kg", True, blackColor)
    diameterLabel = font.render(f"Diameter: {initDiameter} m", True, blackColor)
    distanceTraveledLabel = font.render(f"Distance Traveled (m): {x/5:.1f} m", True, blackColor)
    currentHeightLabel = font.render(f"Current Height (m): {-(y - (windowHeight - 50))/5:.1f} m", True, blackColor)

    #And these lines add them to the main window (screen)
    screen.blit(upperLabel, (50, 20))
    screen.blit(gLabel, (50, 50))
    screen.blit(velocityLabel, (50, 75))
    screen.blit(angleLabel, (50, 100))
    screen.blit(massLabel, (50, 125))
    screen.blit(diameterLabel, (50, 150))
    screen.blit(distanceTraveledLabel, (50, 175))
    screen.blit(currentHeightLabel, (50, 200))

    #These lines update the whole window
    pygame.display.update()
    clock.tick(frameRate)