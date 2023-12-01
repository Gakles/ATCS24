import pygame
import sys
import os
from info import draw_info
from desk import draw_desk
import homework

# Initialize Pygame
pygame.init()

# Set up the window size and zones
window_width = 1400
window_height = 750
window_size = (window_width, window_height)

# Zone dimensions
info_zone_height = window_height // 3
desk_zone_height = window_height - info_zone_height

# Subzone dimensions
calendar_width = window_width // 3
calendar_height = info_zone_height

static_image_width = window_width // 3
static_image_height = info_zone_height

schedule_width = window_width // 3
schedule_height = info_zone_height

# Set up the display
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Game Loop")

#homework
testhwk = homework.Homework("minor")

# Load images
current_path = os.path.dirname(__file__)
calendar_image_path = os.path.join(current_path, "images", "calendar.png")
static_image_path = os.path.join(current_path, "images", "desk.png")
pillow_image_path = os.path.join(current_path, "images", "pillow.png")

calendar_image = pygame.image.load(calendar_image_path)
calendar_image = pygame.transform.scale(calendar_image, (calendar_width, calendar_height))

static_image = pygame.image.load(static_image_path)
static_image = pygame.transform.scale(static_image, (static_image_width, static_image_height))

pillow_image = pygame.image.load(pillow_image_path)
# Resize the pillow image to fit the empty space
empty_space_width = window_width - (2 * window_width // 3 + 3 * schedule_width // 7)
pillow_image = pygame.transform.scale(pillow_image, (empty_space_width, info_zone_height // 4))

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Variables for logging keys and clicks
keys_pressed = set()
mouse_clicks = []

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Log key presses and releases
        elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(event.key)
            action = "pressed" if event.type == pygame.KEYDOWN else "released"
            keys_pressed.add((key, action))

        # Log mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicks.append(event.pos)

    # Update game logic here

    # Clear the screen
    screen.fill((200, 200, 200))  # Light gray background

    # Define box_width and box_height
    box_width = schedule_width // 7
    box_height = info_zone_height // 4

    draw_info(screen, window_width, window_height, info_zone_height, calendar_image, static_image, pillow_image, schedule_width, box_width, box_height)

    draw_desk(screen, info_zone_height, window_width, desk_zone_height, testhwk)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 fps
    clock.tick(60)
