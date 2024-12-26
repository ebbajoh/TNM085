import pygame
import math
from constants import *
import sys
from config import chosen_planet

newFont = pygame.font.Font('images/fonts/Anta-Regular.ttf', 18)

# Button class
class Button():
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect")

FPS = 60
SHIP_MASS = 5
OBJ_SIZE = 5
VEL_SCALE = 50

# Add quit button coordinates and image path
quit_button_image_path = 'images/quit1.png'
quit_button = Button(25, 10, quit_button_image_path)

# Add spaceship image path
spaceship_image_path = 'images/raket.png'
spaceship_image = pygame.image.load(spaceship_image_path)

planet_names = list(planets.keys())
chosen_planet_name = planet_names[chosen_planet-1]
chosen_planet_values = planets[chosen_planet_name]
PLANET_MASS = chosen_planet_values["mass"]
G = chosen_planet_values["gravity"]
MIN_G = 1
MAX_G = 15
PLANET_SIZE = chosen_planet_values["planet_size"]


planet_images = {
    1: pygame.transform.scale(pygame.image.load('images/1.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2)),
    2: pygame.transform.scale(pygame.image.load('images/2.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2)),
    3: pygame.transform.scale(pygame.image.load('images/3.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2)),
    4: pygame.transform.scale(pygame.image.load('images/4.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2))
}

BG = pygame.transform.scale(pygame.image.load('images/background.jpg'), (WIDTH, HEIGHT))
PLANET = planet_images[chosen_planet]

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (110, 23, 171)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x  # (0,0) is top left corner, (400,300) is center, (800,600) is bottom right
        self.y = y
        self.mass = mass

    def draw(self):
        planet_rect = PLANET.get_rect(center=(self.x, self.y))
        win.blit(PLANET, planet_rect.topleft)

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def move(self, planet1=None):
        # Reset acceleration
        acceleration_x = 0
        acceleration_y = 0

        # Calculate gravitational force and acceleration due to both planets
        if planet1:
            # Calculate force and angle for planet 1
            distance_to_planet1 = math.sqrt((self.x - planet1.x) ** 2 + (self.y - planet1.y) ** 2)
            force_from_planet1 = (G * self.mass * planet1.mass) / distance_to_planet1 ** 2
            angle_to_planet1 = math.atan2(planet1.y - self.y, planet1.x - self.x)

            # Calculate total force and acceleration
            total_force_x = (force_from_planet1 * math.cos(angle_to_planet1))
            total_force_y = (force_from_planet1 * math.sin(angle_to_planet1))
            acceleration_x = total_force_x / self.mass
            acceleration_y = total_force_y / self.mass

        # Update velocity
        self.vel_x += acceleration_x
        self.vel_y += acceleration_y

        # Update position
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self):
        rotated_image = pygame.transform.rotate(spaceship_image, -math.degrees(math.atan2(self.vel_y, self.vel_x)))
        new_rect = rotated_image.get_rect(center=spaceship_image.get_rect(topleft=(int(self.x - OBJ_SIZE), int(self.y - OBJ_SIZE))).center)
        win.blit(rotated_image, new_rect.topleft)

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (t_x - m_x) / VEL_SCALE
    vel_y = (t_y - m_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj

def draw_slider(x, y, width, height, value):
    slider_rect_gravity = pygame.Rect(x, y, width, height)
    pygame.draw.rect(win, WHITE, slider_rect_gravity)
    slider_inner_rect = pygame.Rect(x, y, width * value, height)
    pygame.draw.rect(win, PURPLE, slider_inner_rect)
    return slider_rect_gravity

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    global G
    running = True
    clock = pygame.time.Clock()
    planet1 = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    objects = []
    temp_obj_pos = None

    slider_width = 200
    slider_height = 20
    slider_x = WIDTH - slider_width - 20
    slider_y = 30
    slider_value = (G - MIN_G) / (MAX_G - MIN_G)
    font = pygame.font.Font(None, 24)

    while running:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        slider_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if slider_rect.collidepoint(mouse_pos):
                    continue
                if temp_obj_pos is None:
                    temp_obj_pos = mouse_pos
                # Check if quit button is clicked
                if quit_button.clicked(mouse_pos):
                    print('Returning to startpage...')
                    running = False
                    # reset all these variables or else it will not work when pressing quit
                    global PLANET
                    global planet_images
                    global chosen_planet
                    global PLANET_SIZE

                    global SECOND_PLANET
                    global second_planet_images
                    global second_planet
                    global SECOND_PLANET_SIZE
                    global SECOND_PLANET_MASS

                    PLANET = None
                    planet_images = None
                    chosen_planet = None
                    PLANET_SIZE = None

                    SECOND_PLANET = None
                    second_planet_images = None
                    second_planet = None
                    SECOND_PLANET_SIZE = None
                    SECOND_PLANET_MASS = None

                    # Execute start.py when the quit button is clicked
                    # exec(open("start.py").read())
                    # quit the application
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if temp_obj_pos is not None:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None


        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)

        for obj in objects[:]:
            obj.draw()
            obj.move(planet1)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet1.x) ** 2 + (obj.y - planet1.y) ** 2) <= PLANET_SIZE

            if off_screen or collided:
                objects.remove(obj)

        planet1.draw()
        slider_rect = draw_slider(slider_x, slider_y, slider_width, slider_height, slider_value)

        if mouse_clicked and slider_rect.collidepoint(mouse_pos):
            normalized_pos = (mouse_pos[0] - slider_x) / slider_width
            slider_value = max(0, min(1, normalized_pos))
            G = MIN_G + slider_value * (MAX_G - MIN_G)

        if chosen_planet == 1:
            draw_text("Jupiter Gravity: {:.2f}".format(G), newFont, WHITE, win, slider_x, slider_y - 20)
        elif chosen_planet == 2:
            draw_text("Moon Gravity: {:.2f}".format(G), newFont, WHITE, win, slider_x, slider_y - 20)
        elif chosen_planet == 3:
            draw_text("Earth Gravity: {:.2f}".format(G), newFont, WHITE, win, slider_x, slider_y - 20)
        elif chosen_planet == 4:
            draw_text("Laesker Gravity: {:.2f}".format(G), newFont, WHITE, win, slider_x, slider_y - 20)

        quit_button.draw(win)  # Draw the quit button

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
