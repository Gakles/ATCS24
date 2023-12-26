import pygame
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, stats):
        super().__init__()
        self.stats = stats
        self.hitbox = pygame.Surface((self.stats["width"]*self.stats["metersize"], self.stats["length"]*self.stats["metersize"]))
        self.hitbox.fill((200,200,20))
        self.image = self.hitbox.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)
        self.currentfuel = 10 #starter amount
        self.angle = 0
        self.position = self.rect.center
    
    

    
        
