import pygame

class Homework:
    def __init__(self, size, assignment_from_class, totalwork, assignment_title):
        self.size = size
        self.assignment_from_class = assignment_from_class
        self.totalwork = totalwork
        self.timespent = 0
        self.title = assignment_title