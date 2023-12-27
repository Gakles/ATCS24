import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, stats):
        super().__init__()
        self.stats = stats
        if "hullimageaddress" in self.stats:
            self.image = pygame.image.load(self.stats["hullimageaddress"])
            self.image = pygame.transform.scale(self.image, (int(self.stats["length"] * self.stats["metersize"]), int(self.stats["width"] * self.stats["metersize"])))
        else:
            self.image = pygame.Surface((int(self.stats["width"] * self.stats["metersize"]),
                                                    int(self.stats["length"] * self.stats["metersize"])))
            self.image.fill((200, 200, 20))
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = ((self.stats["window_width"]/2)-self.rect.width/2,(self.stats["window_height"]/2) - self.rect.height/2)
        self.currentfuel = 10  # starter amount
        self.angle = 0
        self.position = self.rect.center
        self.reload_img_counter = 0

    def update(self):
        self.image = self.image_clean.copy()
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = rotated_image.get_rect(center = self.image.get_rect(center = (self.rect.centerx, self.rect.centery)).center)
        self.image = rotated_image


