import pygame
import sys
import os
import info as Info
import desk
import homework
from helpers import*
import teacher
import gameinfo
import character

# Initialize Pygame
pygame.init()

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

button_width = window_width // 24
button_height = 30

empty_space_width = window_width - (2 * window_width // 3 + 3 * schedule_width // 7)

# Set up the display
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Game Loop")

#homework
testhwk1 = homework.Homework("major", "English", 240, "Bibliography")
testhwk2 = homework.Homework("minor", "Biology", 1050, "Mitochondria MCQ")
testhwk3 = homework.Homework("minor", "English", 50, "Freewrite")
testhwk4 = homework.Homework("minor", "Math", 550, "Online Quiz")

#teachers
teacher1 = teacher.Teacher("Monica", "English")
teacher2 = teacher.Teacher("Manuel", "Math")
teacher3 = teacher.Teacher("Marzano", "Biology")
teacher4 = teacher.Teacher("Mack", "Comp. Sci")
teacher5 = teacher.Teacher("Mcdougal", "History")

#time
time = 0
last_time  = 0
day = 0

# Load images
current_path = os.path.dirname(__file__)
calendar_image = Image(os.path.join(current_path, "images", "calendar.png"), calendar_width, calendar_height, (0, 0))
static_image = Image(os.path.join(current_path, "images", "desk.png"), static_image_width, static_image_height, (calendar_width, 0))
pillow_image = Image(os.path.join(current_path, "images", "pillow.png"), empty_space_width, info_zone_height // 4, (2 * window_width // 3 + 3 * schedule_width // 7, .75*info_zone_height))
button_image = Image(os.path.join(current_path, "images", "button.png"), button_width, button_height, (.554*window_width, info_zone_height-button_height))

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Set up the font for the FPS counter
font = pygame.font.Font(None, 36)

# Variables for logging keys and clicks
keys_pressed = set()
mouse_clicks = []


#Game tracker variables
homeworkQ = [testhwk1, testhwk2, testhwk3, testhwk4]
teachers = [teacher1, teacher2, teacher3, teacher4, teacher5]

#Desk graphics object
deskobj = desk.deskdrawer(screen, info_zone_height, window_width, window_height-info_zone_height)

#Mouse event handler
def handle_mouse_click(event, game):
    mouse_clicks.append(event.pos)
    for click in mouse_clicks:
        for hwk in game.homeworkQ:
            if hwk.queueclickrect.collidepoint(click):
                    print("clicked on " + hwk.title)
                    if not hwk.finished and not hwk.active:
                        game.changeactivehwk(hwk)
                        game.wholedeskdrawn = False
                    elif hwk.finished:
                        game.homeworkQ.remove(hwk)
                        game.wholedeskdrawn = False
            for teacher in game.teachers:
                if teacher.clickrect.collidepoint(click):
                    teacher.rgb = (100,100,100)
                    game.wholedeskdrawn = False

#make character
player = character.Character("John")
#Gameinfo Object
game = gameinfo.Game(homeworkQ, teachers, player)
game.activehwk = testhwk1
game.activehwk.active = True
# Boolean flags for drawing stuff
game.static_info_drawn = False
game.button_drawn = False
game.wholedeskdrawn = False
# Main game loop
while True:
    mouse_clicks = []
    keys_pressed = set()
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
            appendstr = ""
            for hwk in game.homeworkQ:
                appendstr += hwk.title + " "
            print(appendstr + "<-Thats the queue" + str(time))
            handle_mouse_click(event, game)
    # Update game logic here

    # Define box_width and box_height
    box_width = schedule_width // 7
    box_height = info_zone_height // 4

    # Draw static info if it hasn't been drawn
    if not game.static_info_drawn:
        Info.draw_static_info(screen, window_width, window_height, info_zone_height, calendar_image, static_image, pillow_image, schedule_width, box_width, box_height)
        game.static_info_drawn = True
    if not game.button_drawn:
        Info.draw_dynamic_info("drawbutton", screen, window_width, window_height, info_zone_height, time, button_image)
        game.button_drawn = True
    if not game.wholedeskdrawn:
        deskobj.draw_desk(game.activehwk, game.homeworkQ, game.teachers)
        game.wholedeskdrawn = True
    current_time = pygame.time.get_ticks()
    if current_time - last_time >= 33.3:
        time += 1
        last_time = current_time
        if time > 1440:
            day += 1
            time = 0
        Info.draw_dynamic_info("timeupdate", screen, window_width, window_height, info_zone_height, time, button_image)
        game.update()
        if game.redrawhomework:
            deskobj.draw_homeworkQ_zone(game.homeworkQ)
            deskobj.draw_active_hwk(game.activehwk)
            game.redrawhomework = False
        if game.activehwk is not None:
            deskobj.draw_active_hwk_progess_bar(game.activehwk)
    # Render FPS counter
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (0, 0, 0))  # Black color
    screen.blit(fps_text, (window_width - 120, 20))  # Position the FPS counter in the top right corner

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 fps
    clock.tick(60)
