import pygame
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, stats):
        super().__init__()
        self.stats = stats
        self.ogimage = pygame.Surface((50,50))
        self.image = self.ogimage.fill((200,200,20))
        self.rect = self.image #.get_rect()
        self.rect.center = (200,200)
        self.currentfuel = 10 #starter amount
        self.position = 0
        self.y_offset = 0
        self.position_in_convoy = 0
        self.angle = 0
        self.is_lead = False
