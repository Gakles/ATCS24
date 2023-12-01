import pygame
import os

def draw_static_info(screen, window_width, window_height, info_zone_height, calendar_image, static_image, pillow_image, schedule_width, box_width, box_height):
    # Draw info zone
    pygame.draw.rect(screen, (192, 192, 192), (0, 0, window_width, info_zone_height))  # Light gray info zone

    # Draw calendar subzone in the left 1/3 of the info zone
    calendar_rect = calendar_image.get_rect(left=0, top=0)
    screen.blit(calendar_image, calendar_rect)

    # Draw static-image subzone in the center vertical 1/3 of the info zone
    static_image_rect = static_image.get_rect(center=(window_width // 2, info_zone_height // 2))
    screen.blit(static_image, static_image_rect)

    # Draw daily schedule subzone in the right 1/3 of the info zone
    pygame.draw.rect(screen, (192, 192, 192), (2 * window_width // 3, 0, schedule_width, info_zone_height))  # Light gray schedule zone

    # Draw hourly boxes in the daily schedule subzone
    for i in range(4):
        box_count = 7 if i < 3 else 3
        for j in range(box_count):
            # Change color based on position
            color_value = (
                max(0, min(255, (j * 255 // (box_count - 1)))),
                max(0, min(255, (i * 255 // 3))),
                max(0, min(255, ((6 - j) * 255 // (box_count - 1)))),
            )
            pygame.draw.rect(screen, color_value, (2 * window_width // 3 + j * box_width, i * box_height, box_width, box_height))

            # Display time in 12-hour format
            hour = i * box_count + j + 1
            am_pm = "AM" if hour < 12 else "PM"
            hour = hour % 12 if hour % 12 != 0 else 12
            time_label = f"{hour}:00 {am_pm}"

            font = pygame.font.Font(None, 16)
            text = font.render(time_label, True, (0, 0, 0))  # Black text
            text_rect = text.get_rect(center=(2 * window_width // 3 + j * box_width + box_width // 2, i * box_height + box_height // 2))
            screen.blit(text, text_rect)

    # Draw pillow image to fill the empty space between the 3 boxes on the 4th row and the bottom of the info zone
    pillow_rect = pillow_image.get_rect(left=2 * window_width // 3 + 3 * box_width - 4, top=info_zone_height - pillow_image.get_height() - 2)
    screen.blit(pillow_image, pillow_rect)

def draw_dynamic_info(screen, window_width, window_height, info_zone_height, time_of_day):
    # Convert minutes to hours and minutes
    hours = time_of_day // 60
    minutes = time_of_day % 60
    
    # Convert to 12-hour time format
    am_pm = "AM" if hours < 12 else "PM"
    hours = hours % 12 or 12  # Make 0 or 12 display as 12
    
    # Create a string in the format "hh:mm AM/PM"
    time_string = f"{hours:02d}:{minutes:02d} {am_pm}"
    font = pygame.font.Font(None, 36)
    text = font.render(time_string, True, (200, 100, 200))
    text_rect = text.get_rect(center=(window_width // 2, info_zone_height // 4))
    pygame.draw.rect(screen, (192, 192, 192), text_rect)
    
    screen.blit(text, text_rect)

