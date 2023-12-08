import pygame
import os
import random

class Homework:
    def __init__(self, size, assignment_from_class, totalwork, assignment_title, assigning_teacher):
        self.size = size
        self.assignment_from_class = assignment_from_class
        self.totalwork = totalwork
        self.workdone = 0
        self.timespent = 0
        self.title = assignment_title
        self.finished = False
        self.queueclickrect = None
        self.active = False
        self.teacher = assigning_teacher
        self.image = self.get_rand_image()
    def get_rand_image(self):
        script_directory = os.path.dirname(__file__)
        if self.size == "minor":
            folder_path = os.path.join(script_directory, "images/homework/minor")
        else:
            folder_path = os.path.join(script_directory, "images/homework/major")
        image_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]
        if not image_files:
            raise ValueError("No PNG images found in the specified folder.")
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
        self.image = pygame.image.load(image_path)
        return pygame.transform.scale(self.image, (128, 128))