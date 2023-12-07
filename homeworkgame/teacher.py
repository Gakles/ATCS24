import pygame
import random
import os

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.image = self.get_rand_image()
        self.time_since_last_hwk = 0
        self.previoushwkgradingtime = 0
        self.previoushwkgradingtimespent = 0
        self.has_new_hwk = False
        self.currentlygrading = False
        self.randrgb = (self.rand_rgb())
        self.rgb = self.randrgb
        self.clickrect = None
        self.newassignment = True
        self.current_state = "calm"
        self.hwkpropensity = 0.5
        self.transitions = {
            ("chill", "input"): (self.transition_to_calm, "calm"),
            ("calm", "input"): (self.transition_to_out_for_blood, "out_for_blood"),
            ("out for blood", "input"): (self.transition_to_chill, "chill"),
        }

    def get_rand_image(self):
        script_directory = os.path.dirname(__file__)
        folder_path = os.path.join(script_directory, "images/teachers")
        image_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]
        if not image_files:
            raise ValueError("No PNG images found in the specified folder.")
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
        self.image = pygame.image.load(image_path)
        return pygame.transform.scale(self.image, (128, 128))
    def rand_rgb(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return r,g,b
    def transition(self, input):
        key =  (self.current_state, input)
        if key in self.transitions:
            result = self.transitions[key]
            action = result[0]
            action()
            self.current_state = result[1]
    def transition_to_calm(self):
        self.hwkpropensity = 0.5
        print("I'm teacher " + self.name + " and now I'm calm")
    def transition_to_out_for_blood(self):
        self.hwkpropensity = .80
        print("I'm teacher " + self.name + " and now I'm out for blood!")
    def transition_to_chill(self):
        self.hwkpropensity = 0.2
        print("I'm teacher " + self.name + " and now I'm chill")
    def generate_new_homework(self):
        size = ""
        if self.hwkpropensity >= round(random.uniform(0,1), 3):
            size += "minor"
        else:
            size += "major"
        totalwork = 0
        if size == "minor":
            totalwork = 300*self.hwkpropensity * random.randint(1, 3)
        else:
            totalwork = 500*self.hwkpropensity * random.randint(1, 3)
        return [size, self.subject, totalwork, "New Homework"]
    def update(self):
        self.time_since_last_hwk += 1
        if not self.currentlygrading:
            #Check if new homework should be
            if (round(random.uniform(0, 1), 3) + self.hwkpropensity) * self.time_since_last_hwk >= 1000:
                print("New homework")
                self.has_new_hwk = True
                self.time_since_last_hwk = 0
        
