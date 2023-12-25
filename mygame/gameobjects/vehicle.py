import pygame
class Vehicle:
    def __init__(self, stats):
        self.stats = stats
        self.currentfuel = 10 #starter amount
        self.position = 0
        self.y_offset = 0
        self.position_in_convoy = 0