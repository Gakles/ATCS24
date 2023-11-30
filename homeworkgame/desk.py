import pygame

def draw_desk(screen, info_zone_height, window_width, desk_zone_height):
    # Draw desk zone
    pygame.draw.rect(screen, (169, 169, 169), (0, info_zone_height, window_width, desk_zone_height))  # Dark gray desk zone
