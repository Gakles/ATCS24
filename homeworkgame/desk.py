import pygame

def draw_desk(screen, info_zone_height, window_width, desk_zone_height):
    # Draw desk zone
    pygame.draw.rect(screen, (169, 169, 169), (0, info_zone_height, window_width, desk_zone_height))  # Dark gray desk zone
    
    # Divide the screen vertically
    fifth_width = window_width // 5
    
    # Draw left 1/5 dark brown zone called "hwk_details"
    pygame.draw.rect(screen, (139, 69, 19), (0, info_zone_height, fifth_width, desk_zone_height))  # Dark brown
    
    # Draw middle 3/5 blue zone called "click_zone"
    pygame.draw.rect(screen, (0, 0, 255), (fifth_width, info_zone_height, fifth_width * 3, desk_zone_height))  # Blue
    
    # Draw right 1/5 red zone called "teachers"
    pygame.draw.rect(screen, (255, 0, 0), (fifth_width * 4, info_zone_height, fifth_width, desk_zone_height))  # Red
