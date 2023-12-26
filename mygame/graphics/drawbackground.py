import pygame

class DrawBackground:
    def __init__(self, screen, window_size):
        self.screen = screen
        self.window_size = window_size
        self.position = [0,0]

    def draw(self):
        # Define colors for light and dark tan squares
        light_tan = (255, 228, 196)
        dark_tan = (210, 180, 140)

        # Calculate the size of each square
        square_size = self.window_size[0] // 20

        for row in range(20):
            for col in range(20):
                # Calculate the position of the current square
                x = self.position[0] + col * square_size
                y = self.position[1] + row * square_size

                # Alternate between light and dark tan squares
                color = light_tan if (row + col) % 2 == 0 else dark_tan

                # Draw the square
                pygame.draw.rect(self.screen, color, (x, y, square_size, square_size))