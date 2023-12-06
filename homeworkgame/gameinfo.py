import pygame

class Game:
    def __init__(self, homeworkQ, teachers, player):
        self.homeworkQ = homeworkQ
        self.activehwk = None
        self.teachers = teachers
        self.player = player
        self.redrawhomework = False
    
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
                    print(titlestring)
        #this could cause performance issues
        self.redrawhomework = True
