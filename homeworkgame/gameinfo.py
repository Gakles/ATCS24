import pygame

class Game:
    def __init__(self, homeworkQ, teachers):
        self.homeworkQ = homeworkQ
        self.activehwk = None
        self.teachers = teachers
    
    def update(self, timepassed):
        
