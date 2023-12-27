import pygame
from gameobjects.vehicle import Vehicle
from gameobjects.turret import Turret

class Treaded_Vehicle(Vehicle):
    def __init__(self, stats):
        super().__init__(stats)
        if self.stats["turret"]:
            self.turret = Turret(self)