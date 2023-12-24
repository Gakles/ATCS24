import pygame

class DrawBackground:
    def __init__(self, screen, window_size):
        self.screen = screen
        self.window_size = window_size
        self.bars = []
        self.bar_width = self.window_size[0] // 20
        self.colors = [(210, 180, 140), (222, 184, 135)]
        self.aggregatedistance = 0
        for i in range(20):
            color_index = i  % 2
            self.bars.append([self.colors[color_index], i*self.bar_width, 0, self.bar_width, self.window_size[1]])

    def update(self, move_distance):
        self.aggregatedistance += move_distance
        if self.aggregatedistance > 2*self.bar_width:
            self.aggregatedistance = self.aggregatedistance % (2*self.bar_width)
        for barinfo in self.bars:
            pos = barinfo[1] + self.aggregatedistance
            if pos >= self.window_size[0] - self.bar_width:
                rectinfo = (pos, barinfo[2], barinfo[3], barinfo[4])
                pygame.draw.rect(self.screen, barinfo[0],rectinfo)
                pos = pos - self.window_size[0]
            rectinfo = (pos, barinfo[2], barinfo[3], barinfo[4])
            pygame.draw.rect(self.screen, barinfo[0],rectinfo)
