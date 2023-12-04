import pygame

class Game:
    def __init__(self, homeworkQ, teachers, player):
        self.homeworkQ = homeworkQ
        self.activehwk = None
        self.teachers = teachers
        self.player = player
        self.redrawhomework = False
    
    def changeactivehwk(self, newhwk):
        self.activehwk.active = False
        self.activehwk = newhwk
        self.activehwk.active = True

    def update(self):
        #do work
        self.activehwk.workdone += self.player.workingspeed * self.player.workpertime
        #add to the activehwks timespent
        self.activehwk.timespent += 10
        #check if the hwk is finished
        if self.activehwk.workdone >= self.activehwk.totalwork:
            self.activehwk.finished = True
            next_unfinished_hwk = None
            for hwk in self.homeworkQ:
                if not hwk.finished:
                    next_unfinished_hwk = hwk
                    break
            if next_unfinished_hwk is not None:
                self.homeworkQ.remove(next_unfinished_hwk)
                self.homeworkQ.insert(0, self.activehwk)
                self.activehwk = next_unfinished_hwk
                self.changeactivehwk(next_unfinished_hwk)
        self.redrawhomework = True
