import pygame
from gameobjects.treaded_vehicle import Treaded_Vehicle

class Tank(Treaded_Vehicle):
    def __init__(self,stats):
        super().__init__(stats)
        self.turret_rotation = 0
        
    