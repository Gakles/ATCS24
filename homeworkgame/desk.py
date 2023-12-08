import pygame
import random
import os
from homework import Homework  #Homework class is in a file named homework.py

def draw_click_zone(screen, window_width, desk_zone_height, fifth_width, info_zone_height, homeworkQ):
    pygame.draw.rect(screen, (0, 100, 255), (fifth_width, info_zone_height, .4*fifth_width, desk_zone_height))
    hwkcount = 0
    font = pygame.font.Font(None, 16)
    for hwk in homeworkQ:
        pygame.draw.rect(screen, (0, 200, 255), (fifth_width + .025*fifth_width, info_zone_height + .025*info_zone_height + (hwkcount*(.1*info_zone_height + .025*info_zone_height)), 0.4*fifth_width - .05*fifth_width, .1*info_zone_height + .0125*info_zone_height))
        text_surface = font.render(hwk.title, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(fifth_width + .025*fifth_width + .5*( 0.4*fifth_width - .05*fifth_width), info_zone_height + .025*info_zone_height + (hwkcount*(.1*info_zone_height + .025*info_zone_height)) + .5*(.1*(info_zone_height + .0125*info_zone_height))))
        screen.blit(text_surface, text_rect)
        hwkcount += 1 

class deskdrawer:
    def __init__(self, screen, info_zone_height, window_width, desk_zone_height):
        self.screen = screen
        self.info_zone_height = info_zone_height
        self.window_width = window_width
        self.desk_zone_height = desk_zone_height
        self.fifth_width = window_width//5
    
    #Loads the main hwk image
    def load_homework_image(self, hwk, target_height):
        current_path = os.path.dirname(__file__)
        original_image = hwk.image
        original_width, original_height = original_image.get_size()
        scale_factor = target_height / original_height
        resized_image = pygame.transform.scale(original_image, (int(original_width * scale_factor), target_height))
        return resized_image
    def draw_homeworkQ_zone(self, homeworkQ):
        #base outline of the zone
        pygame.draw.rect(self.screen, (0, 100, 255), (self.fifth_width, self.info_zone_height, .4*self.fifth_width, self.desk_zone_height))
        hwkcount = 0
        font = pygame.font.Font(None, 16)
        for hwk in homeworkQ:
            clickrect = pygame.Rect(self.fifth_width + .025*self.fifth_width, 1.025*self.info_zone_height + (hwkcount*(.125*self.info_zone_height)), 0.4*self.fifth_width - .05*self.fifth_width, .1*self.info_zone_height)
            if not hwk.active:
                pygame.draw.rect(self.screen, (0, 200,255), clickrect)
            else:
                pygame.draw.rect(self.screen, (200, 0,255), clickrect)
            if hwk.finished:
                pygame.draw.rect(self.screen, (255, 200,0), clickrect)
            text_surface = font.render(hwk.title, True, (0,0,0))
            text_rect = text_surface.get_rect(center=(clickrect.center))
            self.screen.blit(text_surface, text_rect)
            hwkcount += 1
            hwk.queueclickrect = clickrect
    def draw_active_hwk(self, activehomework):
        if not activehomework == None:
            pygame.draw.rect(self.screen, (119, 39, 9), (0.025*self.fifth_width, 1.05*self.info_zone_height, .95*self.fifth_width, .95*self.desk_zone_height))
            homework_image = self.load_homework_image(activehomework, target_height=self.desk_zone_height // 2)
            #size and blit the image
            if homework_image:
                image_width, image_height = homework_image.get_size()
                image_x = (self.fifth_width - image_width) // 2
                image_y = (self.desk_zone_height // 2 - image_height) // 2 + self.info_zone_height
                self.screen.blit(homework_image, (image_x, image_y))
            #Additional information for the selected homework
            font = pygame.font.Font(None, 26)
            lines = [
                f"Title: {activehomework.title}",
                f"Size: {activehomework.size}",
                f"From Class: {activehomework.assignment_from_class}",
                f"Total Work: {activehomework.totalwork}",
                f"Time Spent: {activehomework.timespent}"
            ]
            y_offset = self.info_zone_height + self.desk_zone_height // 2 + 10  # Initial y-offset
            for line in lines:
                text_surface = font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.fifth_width // 2, y_offset))
                self.screen.blit(text_surface, text_rect)
                y_offset += 20  # Adjust this value to control the spacing between lines
    def draw_active_hwk_progess_bar(self, activehwk):
        pygame.draw.rect(self.screen, (79,79,79), (0.025*self.fifth_width, self.info_zone_height + .8*self.desk_zone_height, .95*self.fifth_width, .075*self.desk_zone_height))
        completionpercent = activehwk.workdone/activehwk.totalwork
        pygame.draw.rect(self.screen, (200,240,0), (0.025*self.fifth_width, self.info_zone_height + .8*self.desk_zone_height, completionpercent * (.95*self.fifth_width), .075*self.desk_zone_height))

    def drawteacherbar(self, teacher):
        original_rect = teacher.clickrect

        # Calculate the dimensions of the new rectangle
        new_rect_width = original_rect.width
        new_rect_height = original_rect.height / 4  # 1/4 of the original height

        # Calculate the position of the new rectangle
        new_rect_x = original_rect.x
        new_rect_y = original_rect.y + (3 / 4) * original_rect.height  # Start at 3/4 of the original height

        # Create the new rectangle
        bottom_quarter_rect = pygame.Rect(new_rect_x, new_rect_y, new_rect_width, new_rect_height)

        # Draw the bottom 1/4 rectangle
        pygame.draw.rect(self.screen, (79, 79, 79), bottom_quarter_rect)

        hwktimer = teacher.time_since_last_hwk/teacher.hwkcooldown

        # Calculate the width of the loading bar based on hwktimer
        loading_bar_width = (hwktimer / teacher.hwkcooldown) * new_rect_width

        # Create the loading bar rectangle
        loading_bar_rect = pygame.Rect(new_rect_x, new_rect_y, loading_bar_width, new_rect_height)

        # Draw the loading bar
        pygame.draw.rect(self.screen, (255, 0, 0), loading_bar_rect)

    def drawteacher_zone(self, teachers):
        pygame.draw.rect(self.screen, (220, 150, 65), (4.025 * self.fifth_width, 1.025 * self.info_zone_height, 0.95 * self.fifth_width, 0.975 * self.desk_zone_height))
        pygame.draw.rect(self.screen, (190, 140, 45), (4 * self.fifth_width, self.info_zone_height, self.fifth_width, 0.15 * self.desk_zone_height))
        teacher_count = 0
        font = pygame.font.Font(None, 16)

        for teacher in teachers:
            teacher.clickrect = pygame.Rect(4.05 * self.fifth_width + (0.4625 * self.fifth_width * (teacher_count % 2)),
                                            self.info_zone_height + 0.15 * self.desk_zone_height + (0.15 * self.desk_zone_height * (teacher_count // 2)),
                                            0.4375 * self.fifth_width, 0.15 * self.desk_zone_height)
            # Check if newassignment is True and draw a blue border  # Blue border
            if teacher.newassignment:
                pygame.draw.rect(self.screen, (0, 0, 255), teacher.clickrect, 20)
            pygame.draw.rect(self.screen, teacher.rgb, teacher.clickrect)

            # Scale teacher.image to 2/3 the size of teacher.clickrect
            scaled_width = int(2 / 3 * teacher.clickrect.width)
            scaled_height = int(2 / 3 * teacher.clickrect.height)
            scaled_image = pygame.transform.scale(teacher.image, (scaled_width, scaled_height))

            # Get the center coordinates of the clickrect
            center_x, center_y = teacher.clickrect.center

            # Draw the scaled image at the center of the clickrect
            image_rect = scaled_image.get_rect(center=(center_x, center_y))
            self.screen.blit(scaled_image, image_rect)

            # Create a text surface with teacher.name and subject
            textsubject_surface = font.render(teacher.subject, True, (255, 255, 255))  # Assuming white text
            textsubject_rect = textsubject_surface.get_rect(center=(center_x, center_y + 0.5 * scaled_height + 5))  # Adjust Y-coordinate for positioning
            textname_surface = font.render(teacher.name, True, (255, 255, 255))  # Assuming white text
            textname_rect = textname_surface.get_rect(center=(center_x, center_y - 0.5 * scaled_height - 5))

            # Draw the text surface below the top of the clickrect
            self.screen.blit(textsubject_surface, textsubject_rect)
            self.screen.blit(textname_surface, textname_rect)
            self.drawteacherbar(teacher)
            teacher_count += 1



    def draw_desk(self, activehomework, homeworkQ, teachers):
        #Left 1/5  brown rect
        pygame.draw.rect(self.screen, (139, 69, 19), (0, self.info_zone_height, self.fifth_width, self.desk_zone_height))
        #Draw the active homework
        self.draw_active_hwk(activehomework)
        #make the middle, blue zone
        pygame.draw.rect(self.screen, (0, 0, 255), (self.fifth_width, self.info_zone_height, self.fifth_width * 3, self.desk_zone_height))
        #Make the homework queue
        self.draw_homeworkQ_zone(homeworkQ)
        
        #Draw right 1/5 red zone
        pygame.draw.rect(self.screen, (255, 0, 0), (self.fifth_width * 4, self.info_zone_height, self.fifth_width, self.desk_zone_height))
        #make teachers
        self.drawteacher_zone(teachers)