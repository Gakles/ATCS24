import pygame
import sys
from createvehicle import create_vehicle

supply_truck = create_vehicle("supply_truck")
print(supply_truck.stats["fuel"])
uraltruck = create_vehicle("ural_truck")

class game():
    def __init__(self):
        self.window_width = 1440
        self.window_height = 780
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("My Game")
    def run(self):
        while True:
            self.mouse_clicks = []
            self.keys_pressed = set()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()