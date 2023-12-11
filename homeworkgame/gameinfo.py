import pygame
import sys
import os
import time
import info as Info
import desk
import homework
from helpers import*
import teacher
import character

class Game:
    def __init__(self, homeworkQ, teachers):
        self.homeworkQ = homeworkQ
        self.activehwk = None
        self.teachers = teachers
        self.player = character.Character("Johnathan")
        self.redrawhomework = False
        self.mouse_clicks = []
        self.keys_pressed = set()

        #Time variables
        self.time = 0
        self.last_time  = 0
        self.day = 0
        self.clock = pygame.time.Clock()

        #Graphics Variables
        self.window_width = 1400
        self.window_height = 750
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Pygame Game Loop")
        self.info_zone_height = self.window_height // 3
        self.desk_zone_height = self.window_height - self.info_zone_height
        self.calendar_width = self.window_width // 3
        self.calendar_height = self.info_zone_height
        self.static_image_width = self.window_width // 3
        self.static_image_height = self.info_zone_height
        self.schedule_width = self.window_width // 3
        self.schedule_height = self.info_zone_height
        self.button_width = self.window_width // 24
        self.button_height = 30
        self.empty_space_width = self.window_width - (2 * self.window_width // 3 + 3 * self.schedule_width // 7)
        self.box_width = self.schedule_width // 7
        self.box_height = self.info_zone_height // 4
        self.x_width = self.window_width // 60
        self.x_height = self.info_zone_height // 10

        # Boolean flags for drawing stuff
        self.static_info_drawn = False
        self.button_drawn = False
        self.wholedeskdrawn = False

        #Font
        self.font = pygame.font.Font(None, 36)

        #Images
        current_path = os.path.dirname(__file__)
        self.calendar_image = Image(os.path.join(current_path, "images", "calendar.png"), self.calendar_width, self.calendar_height, (0, 0))
        self.static_image = Image(os.path.join(current_path, "images", "desk.png"), self.static_image_width, self.static_image_height, (self.calendar_width, 0))
        self.pillow_image = Image(os.path.join(current_path, "images", "pillow.png"), self.empty_space_width, self.info_zone_height // 4, (2 * self.window_width // 3 + 3 * self.schedule_width // 7, .75*self.info_zone_height))
        self.button_image = Image(os.path.join(current_path, "images", "button.png"), self.button_width, self.button_height, (.554*self.window_width, self.info_zone_height-self.button_height))
        self.x_image = pygame.image.load(os.path.join(current_path, "images", "x.png"))
        self.images = {"calendar" : self.calendar_image, "static" : self.static_image, "pillow" : self.pillow_image, "button" : self.button_image, "x" : self.x_image}

        #Important game objects
        self.Info = Info
        self.deskobj = desk.deskdrawer(self.screen, self.info_zone_height, self.window_width, self.window_height-self.info_zone_height)

    def changeactivehwk(self, newhwk):
        if self.activehwk is not None:
            self.activehwk.active = False
        self.activehwk = newhwk
        self.activehwk.active = True

    def update(self):
        #do work
        if self.activehwk is not None:
            self.activehwk.workdone += self.player.workingspeed * self.player.workpertime
        #add to the activehwks timespent
            self.activehwk.timespent += 1
        #check if the hwk is finished
            if self.activehwk.workdone >= self.activehwk.totalwork:
                self.activehwk.finished = True
                self.activehwk = None
                next_unfinished_hwk = None
                for hwk in self.homeworkQ:
                    if not hwk.finished:
                        next_unfinished_hwk = hwk
                        break
                if next_unfinished_hwk is not None:
                    self.changeactivehwk(next_unfinished_hwk)
                    titlestring = ""
                    for hwk in self.homeworkQ:
                        titlestring += hwk.title
        #probably doesn't cause fps issues
        self.redrawhomework = True
    
    def handle_mouse_click(self, event):
        self.mouse_clicks.append(event.pos)
        for click in self.mouse_clicks:
            for hwk in self.homeworkQ:
                if hwk.queueclickrect.collidepoint(click):
                        if not hwk.finished and not hwk.active:
                            self.changeactivehwk(hwk)
                            self.wholedeskdrawn = False
                        elif hwk.finished:
                            #submitting the hwk
                            hwk.teacher.startgrading()
                            self.homeworkQ.remove(hwk)
                            self.wholedeskdrawn = False
                for teacher in self.teachers:
                    if teacher.clickrect.collidepoint(click):
                        teacher.rgb = (100,100,100)
                        self.wholedeskdrawn = False
    def teacherupdates(self):
        for teacher in self.teachers:
            teacher.update()
            self.deskobj.drawteacherassignmentbar(teacher)
            if teacher.has_new_hwk:
                newhwkstats = teacher.generate_new_homework()
                new_hwk = homework.Homework(newhwkstats[0], newhwkstats[1], newhwkstats[2], newhwkstats[3], teacher)
                self.homeworkQ.append(new_hwk)
                self.redrawhomework = True
                teacher.has_new_hwk = False

    def run(self):
        while True:
            self.mouse_clicks = []
            self.keys_pressed = set()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Log key presses and releases
                elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    key = pygame.key.name(event.key)
                    action = "pressed" if event.type == pygame.KEYDOWN else "released"
                    self.keys_pressed.add((key, action))

                # Log mouse clicks
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    appendstr = ""
                    for hwk in self.homeworkQ:
                        appendstr += hwk.title + " "
                    self.handle_mouse_click(event)

            # Draw static info if it hasn't been drawn
            if not self.static_info_drawn:
                Info.draw_static_info(self.screen, self.window_width, self.window_height, self.info_zone_height, self.images["calendar"], self.images["static"], self.images["pillow"], self.schedule_width, self.box_width, self.box_height)
                self.crossmarks = Info.daycrossmarks(self.screen, self.images["x"], self.window_width, self.info_zone_height)
                self.crossmarks.drawnewx()
                self.static_info_drawn = True
            if not self.button_drawn:
                Info.draw_dynamic_info("drawbutton", self.screen, self.window_width, self.window_height, self.info_zone_height, self.time, self.images["button"])
                self.button_drawn = True
            if not self.wholedeskdrawn:
                self.deskobj.draw_desk(self.activehwk, self.homeworkQ, self.teachers, self.player)
                self.wholedeskdrawn = True
            current_time = pygame.time.get_ticks()
            #This checks if it's time for a "game tick" to happen
            if current_time - self.last_time >= 33.3:
                self.time += 1
                self.last_time = current_time
                if self.time > 1440:
                    self.crossmarks.drawnewx()
                    self.day += 1
                    self.time = 0
                Info.draw_dynamic_info("timeupdate", self.screen, self.window_width, self.window_height, self.info_zone_height, self.time, self.images["button"])
                self.update()
                self.teacherupdates()
                if self.redrawhomework:
                    self.deskobj.draw_homeworkQ_zone(self.homeworkQ)
                    self.deskobj.draw_active_hwk(self.activehwk)
                    self.redrawhomework = False
                if self.activehwk is not None:
                    self.deskobj.draw_active_hwk_progess_bar(self.activehwk)
            # Render FPS counter
            fps = self.clock.get_fps()
            fps_text = self.font.render(f"FPS: {int(fps)}", True, (0, 0, 0))  # Black color
            pygame.draw.rect(self.screen, (129,129,129), fps_text.get_rect(topleft =(self.window_width - 120, 20)))
            self.screen.blit(fps_text, (self.window_width - 120, 20))  # Position the FPS counter in the top right corner

            # Update the display
            pygame.display.flip()

            # Cap the frame rate to 60 fps
            self.clock.tick(60)
