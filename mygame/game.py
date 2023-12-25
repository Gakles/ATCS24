import pygame
import sys
from createvehicle import create_vehicle
from graphics.drawbackground import DrawBackground
from graphics.drawconvoy import DrawConvoy
from gameobjects.convoy import Convoy

all_sprites = pygame.sprite.Group()

supply_truck = create_vehicle("supply_truck")
uraltruck1 = create_vehicle("ural_truck")
uraltruck2 = create_vehicle("ural_truck")
t801 = create_vehicle("t80")

convoy = Convoy([uraltruck1, uraltruck2, t801])

all_sprites.add(supply_truck, uraltruck1,uraltruck2, t801)

class Game:
    def __init__(self):
        self.window_width = 1440
        self.window_height = 780
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        self.drawbackground = DrawBackground(self.screen, self.window_size)
        convoy.update_convoy_order()
        self.drawconvoy = DrawConvoy(self.screen, self.window_size, convoy)
        pygame.display.set_caption("My Game")
        self.keys_pressed = set()

        # Initialize clock for FPS limiting
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while True:
            self.handle_events()

            # Update game logic here
            
            convoy.update(self.keys_pressed)

            # Draw game elements here

            self.drawbackground.update(convoy.currentspeed)
            self.drawfpscounter()
            self.drawconvoy.drawvehicles()
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

    def drawfpscounter(self):
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))