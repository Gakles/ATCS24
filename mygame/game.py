import pygame
import sys
from createvehicle import create_vehicle
from graphics.drawbackground import DrawBackground
from gameobjects.convoy import Convoy

supply_truck = create_vehicle("supply_truck")
print(supply_truck.stats["fuel"])
uraltruck1 = create_vehicle("ural_truck")
uraltruck1.honk_horn()
uraltruck2 = create_vehicle("ural_truck")

convoy = Convoy([uraltruck1, uraltruck2])
print(convoy.acceleration)

class Game:
    def __init__(self):
        self.window_width = 1440
        self.window_height = 780
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        self.drawbackground = DrawBackground(self.screen, self.window_size)
        pygame.display.set_caption("My Game")
        self.keys_pressed = set()

        # Initialize clock for FPS limiting
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while True:
            self.handle_events()

            # Update game logic here

            if "right" in self.keys_pressed and not "left" in self.keys_pressed:
                convoy.accelerate()
            if "left" in self.keys_pressed and not "right" in self.keys_pressed:
                convoy.decelerate()
            
            print(convoy.currentspeed)

            # Draw game elements here

            self.drawbackground.update(convoy.currentspeed)

            pygame.display.flip()

            # FPS limiter
            self.clock.tick(self.fps)

    def handle_events(self):
        self.mouse_clicks = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Keydown and Keyup events for arrow keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.keys_pressed.add("left")
                elif event.key == pygame.K_RIGHT:
                    self.keys_pressed.add("right")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.keys_pressed.discard("left")
                elif event.key == pygame.K_RIGHT:
                    self.keys_pressed.discard("right")
