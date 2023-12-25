import pygame

class DrawConvoy:
    def __init__(self, screen, screen_size, convoy):
        self.screen = screen
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.convoy = convoy
        self.bar_width = self.screen_width/20
        self.meter_mult = .2 * self.bar_width
    
    def drawvehicles(self):
        for vehicle in self.convoy.vehicles:
            print(self.meter_mult * vehicle.stats["length"])
            #pygame.draw.rect(self.screen, (0,100,0), ((self.screen_width/2) - vehicle.position_in_convoy*20, (self.screen_height/2)+vehicle.y_offset), self.meter_mult * vehicle.stats["length"], self.meter_mult * vehicle.stats["width"])
            pygame.draw.rect(self.screen, (0,100,0), ((self.screen_width/2) - (vehicle.position_in_convoy*200),((self.screen_height/2)+vehicle.y_offset),self.meter_mult * vehicle.stats["length"],self.meter_mult * vehicle.stats["width"]))