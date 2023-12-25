import pygame
class Convoy:
    def __init__(self, vehicles):
        self.vehicles = []
        for vehicle in vehicles:
            self.vehicles.append(vehicle)
        self.update_convoy_order()
        self.currentspeed = 0
        self.acceleration = self.calculate_current_min_attribute("acceleration")
        self.maxspeed = self.calculate_current_min_attribute("maximumspeed")
        self.deceleration = self.calculate_current_min_attribute("deceleration")
        self.reverseacc = self.calculate_current_min_attribute("reverseacceleration")
        self.maxreverse = self.calculate_current_min_attribute("maximumreverse")


    def calculate_current_min_attribute(self, attribute):
        min_vehicle = min(self.vehicles, key=lambda x: x.stats[attribute])
        return min_vehicle.stats[attribute]
    
    def accelerate(self):
        self.currentspeed += self.acceleration
        if self.currentspeed >= self.maxspeed:
            self.currentspeed = self.maxspeed

    def decelerate(self):
        if self.currentspeed > 0:
            self.currentspeed -= self.deceleration
        else:
            self.currentspeed -= self.reverseacc
        if self.currentspeed < -self.maxreverse:
            self.currentspeed = -self.maxreverse
    
    def passivedecelerate(self):
        if self.currentspeed > 0:
            if self.currentspeed // (self.deceleration/4) > 0:
                self.currentspeed -= self.deceleration/4
            else:
                self.currentspeed = 0
        if self.currentspeed < 0:
            if self.currentspeed // (self.acceleration/8) < 0:
                self.currentspeed += self.acceleration/8
            else:
                self.currentspeed = 0

    def update(self, keys_pressed):
        if "right" in keys_pressed and not "left" in keys_pressed:
            self.accelerate()
        elif "left" in keys_pressed and not "right" in keys_pressed:
            self.decelerate()
        else:
            self.passivedecelerate()

    def update_convoy_order(self):
        i = 1
        for vehicle in self.vehicles:
            vehicle.position_in_convoy = i
            i+=1
            if vehicle.is_lead:
                vehicle.is_lead = False
        self.vehicles[0].is_lead = True