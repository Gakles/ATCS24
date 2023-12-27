import pygame
import math

class Turret(pygame.sprite.Sprite):
    def __init__(self, vehicle):
        super().__init__()
        self.vehicle = vehicle
        if "turretimageaddress" in self.vehicle.stats:
            self.image = pygame.image.load(self.vehicle.stats["turretimageaddress"])
            self.image = pygame.transform.scale(self.image, (int(self.vehicle.stats["length"] * self.vehicle.stats["metersize"]), int(self.vehicle.stats["width"] * self.vehicle.stats["metersize"])))
        else:
            self.image = pygame.Surface((int(self.vehicle.stats["width"] * self.vehicle.stats["metersize"]),
                                        int(self.vehicle.stats["length"] * self.vehicle.stats["metersize"])))
        self.image_clean = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (self.vehicle.position)
        self.turret_angle = 0
        
    def updateturret(self, mouse_angle, hull_rotation):
        self.turret_angle_adjusted = self.turret_angle % 360
        if mouse_angle < 0:
            mouse_angle = mouse_angle * -1
        else:
            mouse_angle = 360 - mouse_angle
        
        angle_difference = (mouse_angle - self.turret_angle_adjusted + 180) % 360 - 180

        # Adjust for the shortest path
        if angle_difference > 180:
            angle_difference -= 360
        elif angle_difference < -180:
            angle_difference += 360

        # Determine the direction to rotate
        if angle_difference > 0:
            self.turret_angle += min(angle_difference, self.vehicle.stats["turretrotation"]/60)
        elif angle_difference < 0:
            self.turret_angle -= min(abs(angle_difference), self.vehicle.stats["turretrotation"]/60)

        # Ensure the turret angle is within [0, 360)
        self.turret_angle -= hull_rotation
        self.turret_angle = self.turret_angle % 360

        if abs(mouse_angle - self.turret_angle_adjusted) < self.vehicle.stats["turretrotation"]/60:
            self.turret_angle = mouse_angle

    def update(self):
        self.image = self.image_clean.copy()
        rotated_image = pygame.transform.rotate(self.image, self.turret_angle)
        self.rect = rotated_image.get_rect(center = self.image.get_rect(center = (self.rect.centerx, self.rect.centery)).center)
        self.image = rotated_image
    