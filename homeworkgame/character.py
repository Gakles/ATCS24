import pygame

class Character:
    def __init__(self, name):
        self.workingspeed  = 1
        self.workpertime = 10
        self.morale = 100
        self.xp = 0
        self.level = 1
        self.name = name
    