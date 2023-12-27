import pygame
import sys
from createvehicle import create_vehicle
from player import Player
from graphics.drawbackground import DrawBackground

all_sprites = pygame.sprite.Group()
turret_sprites = pygame.sprite.Group()


window_width = 1440
window_height = 780
window_size = (window_width, window_height)
#supply_truck = create_vehicle("supply_truck", window_size)
#uraltruck1 = create_vehicle("ural_truck", window_size)
#uraltruck2 = create_vehicle("ural_truck", window_size)
t801 = create_vehicle("t80", window_size, turret_sprites)

all_sprites.add(t801)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(window_size)
        self.drawbackground = DrawBackground(self.screen, window_size)
        self.player = Player(t801, self.drawbackground)
        pygame.display.set_caption("My Game")
        self.keys_pressed = set()

        # Initialize clock for FPS limiting
        self.clock = pygame.time.Clock()
        self.fps = 60

    def run(self):
        while True:
            self.handle_events()

            # Update game logic here
            self.player.updatevehicle(self.keys_pressed, pygame.mouse.get_pos())

            # Draw game elements here
            self.drawbackground.draw()
            self.drawfpscounter()
            all_sprites.update()
            all_sprites.draw(self.screen)
            turret_sprites.update()
            turret_sprites.draw(self.screen)
            pygame.draw.line(self.screen, (0,0,0), pygame.mouse.get_pos(), self.player.currentvehicle.position)
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
                if event.key == pygame.K_a:
                    self.keys_pressed.add("a")
                elif event.key == pygame.K_d:
                    self.keys_pressed.add("d")
                elif event.key == pygame.K_w:
                    self.keys_pressed.add("w")
                elif event.key == pygame.K_s:
                    self.keys_pressed.add("s")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.keys_pressed.discard("a")
                elif event.key == pygame.K_d:
                    self.keys_pressed.discard("d")
                elif event.key == pygame.K_w:
                    self.keys_pressed.discard("w")
                elif event.key == pygame.K_s:
                    self.keys_pressed.discard("s")


    def drawfpscounter(self):
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))
        self.screen.blit(fps_text, (10, 10))