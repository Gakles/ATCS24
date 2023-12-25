import pygame
from gameobjects.vehicle import Vehicle

class Treaded_Vehicle(Vehicle):
    def __init__(self, stats):
        super().__init__(stats)
    
    def rot_center(image, angle, x, y):    
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
        return rotated_image, new_rect