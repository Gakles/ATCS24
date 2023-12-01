import pygame
import os
import homework

def load_homework_image(size):
    if size == "minor":
        return pygame.image.load(os.path.join("images", "minorhwk.png"))
    elif size == "major":
        return pygame.image.load(os.path.join("images", "majorhwk.png"))
    else:
        return None  # Handle unsupported size

def draw_desk(screen, info_zone_height, window_width, desk_zone_height, homework):
    # Draw desk zone
    pygame.draw.rect(screen, (169, 169, 169), (0, info_zone_height, window_width, desk_zone_height))  # Dark gray desk zone
    
    # Divide the screen vertically
    fifth_width = window_width // 5
    
    # Draw left 1/5 dark brown zone called "hwk_details"
    pygame.draw.rect(screen, (139, 69, 19), (0, info_zone_height, fifth_width, desk_zone_height))  # Dark brown
    
    # Load homework image based on size
    homework_image = load_homework_image(homework.size)
    
    if homework_image:
        # Get the size of the loaded image
        image_width, image_height = homework_image.get_size()
        
        # Calculate position to center the image in the left zone
        image_x = (fifth_width - image_width) // 2
        image_y = (desk_zone_height - image_height) // 2 + info_zone_height
        
        # Draw the homework image
        screen.blit(homework_image, (image_x, image_y))
    
    # Draw middle 3/5 blue zone called "click_zone"
    pygame.draw.rect(screen, (0, 0, 255), (fifth_width, info_zone_height, fifth_width * 3, desk_zone_height))  # Blue
    
    # Draw right 1/5 red zone called "teachers"
    pygame.draw.rect(screen, (255, 0, 0), (fifth_width * 4, info_zone_height, fifth_width, desk_zone_height))  # Red
