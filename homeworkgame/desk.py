import pygame
import os
from homework import Homework  # Assuming Homework class is in a file named homework.py

def load_homework_image(size, target_height):
    current_path = os.path.dirname(__file__)
    if size == "minor":
        image_path = os.path.join(current_path, "images", "minorhwk.png")
    elif size == "major":
        image_path = os.path.join(current_path, "images", "majorhwk.png")
    else:
        return None  # Handle unsupported size
    
    original_image = pygame.image.load(image_path)
    original_width, original_height = original_image.get_size()
    
    # Calculate the scaling factor to fit the image in the target height
    scale_factor = target_height / original_height
    
    # Resize the image
    resized_image = pygame.transform.scale(original_image, (int(original_width * scale_factor), target_height))
    
    return resized_image

def draw_desk(screen, info_zone_height, window_width, desk_zone_height, homework):
    # Draw desk zone
    pygame.draw.rect(screen, (169, 169, 169), (0, info_zone_height, window_width, desk_zone_height))  # Dark gray desk zone
    
    # Divide the screen vertically
    fifth_width = window_width // 5
    
    # Draw left 1/5 dark brown zone called "hwk_details"
    pygame.draw.rect(screen, (139, 69, 19), (0, info_zone_height, fifth_width, desk_zone_height))  # Dark brown
    
    # Load and resize homework image based on size
    homework_image = load_homework_image(homework.size, target_height=desk_zone_height // 2)
    
    if homework_image:
        # Get the size of the loaded image
        image_width, image_height = homework_image.get_size()
        
        # Calculate position to center the image in the top half of the left zone
        image_x = (fifth_width - image_width) // 2
        image_y = (desk_zone_height // 2 - image_height) // 2 + info_zone_height
        
        # Draw the resized homework image
        screen.blit(homework_image, (image_x, image_y))
    
    # Draw middle 3/5 blue zone called "click_zone"
    pygame.draw.rect(screen, (0, 0, 255), (fifth_width, info_zone_height, fifth_width * 3, desk_zone_height))  # Blue
    
    # Draw right 1/5 red zone called "teachers"
    pygame.draw.rect(screen, (255, 0, 0), (fifth_width * 4, info_zone_height, fifth_width, desk_zone_height))  # Red
    
    # Draw additional information in the bottom half of the leftmost zone
    font = pygame.font.Font(None, 36)
    
    # Display each piece of information on a new line
    lines = [
        f"Size: {homework.size}",
        f"From Class: {homework.assignment_from_class}",
        f"Total Work: {homework.totalwork}",
        f"Time Spent: {homework.timespent}",
        f"Title: {homework.title}"
    ]
    
    y_offset = info_zone_height + desk_zone_height // 2 + 10  # Initial y-offset
    
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(fifth_width // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 40  # Adjust this value to control the spacing between lines
