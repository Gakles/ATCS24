import pygame
import math
class Gun(pygame.sprite.Sprite):
    def __init__(self, turret):
        super().__init__()
        self.turret = turret
        if "gunimageaddress" in self.turret.vehicle.stats:
            print("bingo")
            self.image = pygame.image.load(self.turret.vehicle.stats["gunimageaddress"])
            self.image = pygame.transform.scale(self.image, (int(self.turret.vehicle.stats["gunheight"] * self.turret.vehicle.stats["metersize"]), int(self.turret.vehicle.stats["gunwidth"] * self.turret.vehicle.stats["metersize"])))
        else:
            self.image = pygame.Surface((int(self.turret.vehicle.stats["gunwidth"] * self.turret.vehicle.stats["metersize"]),
                                        int(self.turret.vehicle.stats["gunheight"] * self.turret.vehicle.stats["metersize"])))
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.turret.vehicle.position)
        self.gun_angle = 0
    
    def updategun(self):
        self.gun_angle = self.turret.turret_angle

    def update(self):
        self.image = self.image_clean.copy()
        rotated_image = pygame.transform.rotate(self.image, self.gun_angle)
        self.rect = rotated_image.get_rect(center = self.image.get_rect(center = (self.rect.centerx, self.rect.centery)).center)
        self.image = rotated_image