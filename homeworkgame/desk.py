import pygame
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
    def load_homework_image(self, size, target_height):
        current_path = os.path.dirname(__file__)
        if size == "minor":
            image_path = os.path.join(current_path, "images", "minorhwk.png")
        elif size == "major":
            image_path = os.path.join(current_path, "images", "majorhwk.png")
        else:
            return None
        original_image = pygame.image.load(image_path)
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
            text_surface = font.render(hwk.title, True, (0,0,0))
            text_rect = text_surface.get_rect(center=(clickrect.center))
            self.screen.blit(text_surface, text_rect)
            hwkcount += 1
            hwk.queueclickrect = clickrect
    def drawteacher_zone(self, teachers):
        pygame.draw.rect(self.screen, (220,150,65), (4.025*self.fifth_width, 1.025*self.info_zone_height, .95*self.fifth_width, 0.975*self.desk_zone_height))
        pygame.draw.rect(self.screen, (190,140,45), (4*self.fifth_width, self.info_zone_height, self.fifth_width, .15*self.desk_zone_height))
        teacher_count = 0
        font = pygame.font.Font(None, 16)
        for teacher in teachers:
            clickrect = pygame.Rect(4*self.fifth_width, )
        
    def draw_desk(self, activehomework, homeworkQ, teachers):
        #Left 1/5  brown rect
        pygame.draw.rect(self.screen, (139, 69, 19), (0, self.info_zone_height, self.fifth_width, self.desk_zone_height))
        #load correct wk image
        homework_image = self.load_homework_image(activehomework.size, target_height=self.desk_zone_height // 2)
        #size and blit the image
        if homework_image:
            image_width, image_height = homework_image.get_size()
            image_x = (self.fifth_width - image_width) // 2
            image_y = (self.desk_zone_height // 2 - image_height) // 2 + self.info_zone_height
            self.screen.blit(homework_image, (image_x, image_y))
        #Additional information for the selected homework
        font = pygame.font.Font(None, 36)
        lines = [
            f"Size: {activehomework.size}",
            f"From Class: {activehomework.assignment_from_class}",
            f"Total Work: {activehomework.totalwork}",
            f"Time Spent: {activehomework.timespent}",
            f"Title: {activehomework.title}"
        ]
        y_offset = self.info_zone_height + self.desk_zone_height // 2 + 10  # Initial y-offset
        for line in lines:
            text_surface = font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.fifth_width // 2, y_offset))
            self.screen.blit(text_surface, text_rect)
            y_offset += 40  # Adjust this value to control the spacing between lines
        #make the middle, blue zone
        pygame.draw.rect(self.screen, (0, 0, 255), (self.fifth_width, self.info_zone_height, self.fifth_width * 3, self.desk_zone_height))
        #Make the homework queue
        self.draw_homeworkQ_zone(homeworkQ)
        
        #Draw right 1/5 red zone
        pygame.draw.rect(self.screen, (255, 0, 0), (self.fifth_width * 4, self.info_zone_height, self.fifth_width, self.desk_zone_height))
        #make teachers
        self.drawteacher_zone(teachers)