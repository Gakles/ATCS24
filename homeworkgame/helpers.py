import pygame
class Image:
    def __init__(self, path, width, height, position):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.width = width
        self.height = height
        self.position = position

    def draw(self, screen):
        screen.blit(self.image, self.position)