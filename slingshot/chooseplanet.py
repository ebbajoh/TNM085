import pygame
import button
from config import set_chosen_planet
from config import set_second_planet

# Define planet names mapping
planet_names = {1: "JUPITER", 2: "MOON", 3: "EARTH", 4: "LAESKER"}

# Initialize pygame
pygame.init()

# Define what planet is chosen, jupiter is standard
chosen_planet = None  # 1 is jupiter, 2 is earth etc
second_planet = None

# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Start page')

# load background image
background_img = pygame.image.load('images/background.jpg')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# load title image NEW
title_img = pygame.transform.scale(pygame.image.load('images/logga2.png'), (600, 600))
start_img = pygame.image.load('images/start_btn.png')

# load button images
jupiter = pygame.image.load('images/1.png').convert_alpha()
moon = pygame.image.load('images/2.png').convert_alpha()
earth = pygame.image.load('images/3.png').convert_alpha()
lask = pygame.image.load('images/4.png').convert_alpha()

# create button instances
jupiter_button = button.Button(50, 200, jupiter, 0.12)
moon_button = button.Button(245, 200, moon, 0.12)
earth_button = button.Button(440, 200, earth, 0.12)
lask_button = button.Button(640, 200, lask, 0.12)
start_button_chooseplanet = button.Button(280, 350, start_img, 0.8)


PURPLE = (78, 0, 78)
LIGHT_PURPLE = (230, 230, 250)
TRANSPARENT = (0, 0, 0, 0)

my_surface = pygame.Surface((200, 200), pygame.SRCALPHA)

def draw_circle(surface, color, center, radius, border_width):
    pygame.draw.circle(surface, color, center, radius, border_width)

jupiter_pressed = False
moon_pressed = False
earth_pressed = False
lask_pressed = False

# game loop
run = True
while run:

    screen.fill((202, 228, 241))
    screen.blit(background_img, (0, 0))
    screen.blit(title_img, (80, -200))

    if jupiter_button.draw(screen):
        if earth_pressed == False and moon_pressed == False and lask_pressed == False:
            print('Jupiter chosen as first planet')
            chosen_planet = 1
            jupiter_pressed = True
        if earth_pressed == True or moon_pressed == True or lask_pressed == True:
            print('Jupiter chosen as second planet')
            second_planet = 1
            jupiter_pressed = True

    if moon_button.draw(screen):
        if earth_pressed == False and lask_pressed == False and jupiter_pressed == False:
            print('Moon chosen as first planet')
            chosen_planet = 2
            moon_pressed = True
        if earth_pressed == True or lask_pressed == True or jupiter_pressed == True:
            print('Moon chosen as second planet')
            second_planet = 2
            moon_pressed = True

    if earth_button.draw(screen):
        if lask_pressed == False and moon_pressed == False and jupiter_pressed == False:
            print('Earth chosen as first planet')
            chosen_planet = 3
            earth_pressed = True
        if lask_pressed == True or moon_pressed == True or jupiter_pressed == True:
            print('Earth chosen as second planet')
            second_planet = 3
            earth_pressed = True

    if lask_button.draw(screen):
        if earth_pressed == False and moon_pressed == False and jupiter_pressed == False:
            print('Laesker chosen as first planet')
            chosen_planet = 4
            lask_pressed = True
        if earth_pressed == True or moon_pressed == True or jupiter_pressed == True:
            print('Laesker chosen as second planet')
            second_planet = 4
            lask_pressed = True

    # Display text
    if (chosen_planet is not None) and (second_planet is not None) and (start_button_chooseplanet.draw(screen)):
        print("Game starting with 2 planets...")
        # Execute application when the start button is pressed
        exec(open("main_two_planets.py").read())
    elif (chosen_planet is not None) and (start_button_chooseplanet.draw(screen)):
        print("Game starting with 1 planet...")
        # Execute application when the start button is pressed
        exec(open("main_one_planet.py").read())

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    if jupiter_pressed:
        draw_circle(my_surface, PURPLE, (115, 265), 20, 5)
        draw_circle(screen, PURPLE, (119, 266), 66, 5)
        draw_circle(screen, LIGHT_PURPLE, (119, 266), 71, 5)

    if earth_pressed:
        draw_circle(my_surface, PURPLE, (505, 265), 20, 5)
        draw_circle(screen, PURPLE, (505, 266), 66, 5)
        draw_circle(screen, LIGHT_PURPLE, (505, 266), 71, 5)

    if moon_pressed:
        draw_circle(my_surface, PURPLE, (310, 265), 20, 5)
        draw_circle(screen, PURPLE, (310, 266), 66, 5)
        draw_circle(screen, LIGHT_PURPLE, (310, 266), 71, 5)

    if lask_pressed:
        draw_circle(my_surface, PURPLE, (700, 265), 20, 5)
        draw_circle(screen, PURPLE, (700, 266), 66, 5)
        draw_circle(screen, LIGHT_PURPLE, (700, 266), 71, 5)

    set_chosen_planet(chosen_planet)
    set_second_planet(second_planet)
    pygame.display.update()