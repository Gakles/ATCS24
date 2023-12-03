import pygame
import random
import os

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.image = self.get_rand_image()
        self.time_since_last_hwk = 0

    def get_rand_image(self):
        script_directory = os.path.dirname(__file__)
        folder_path = os.path.join(script_directory, "images/teachers")
        image_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]
        if not image_files:
            raise ValueError("No PNG images found in the specified folder.")
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
        self.image = pygame.image.load(image_path)
        return pygame.transform.scale(self.image, (128, 128))