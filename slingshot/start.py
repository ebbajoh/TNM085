import pygame
import button
# Initialize pygame
pygame.init()

# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Start page')

# Load background image NEW
background_img = pygame.image.load('images/background.jpg')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
title_img = pygame.transform.scale(pygame.image.load('images/logga2.png'), (600, 600))

# load button images
start_img = pygame.image.load('images/START.png').convert_alpha()
# create button instances
start_button_start = button.Button(285, 370, start_img, 0.8)

# game loop
run = True
while run:
	screen.fill((202, 228, 241))

	# Blit background image NEW
	screen.blit(background_img, (0, 0))
	screen.blit(title_img, (80, -200))

	if start_button_start.draw(screen):
		print('Start button pressed...')
		# Execute chooseplanet.py when the start button is pressed
		exec(open("chooseplanet.py").read())

	# event handler
	for event in pygame.event.get():
		# quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()