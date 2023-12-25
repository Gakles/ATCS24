class Convoy:
    def __init__(self, vehicles):
        self.vehicles = []
        for vehicle in vehicles:
            self.vehicles.append(vehicle)
        self.currentspeed = 0
        self.acceleration = self.calculatecurrentmaxacceleration()
        self.maxspeed = self.calculatecurrentmaxspeed()
        self.deceleration = self.calculatecurrentmindeceleration()
        self.reverseacc = self.calculatecurrentmaxreverseacceleration()
        self.maxreverse = self.calculatecurrentmaxreverse()

    def calculatecurrentmaxacceleration(self):
        min_vehicle = min(self.vehicles, key=lambda x: x.stats["acceleration"])
        return min_vehicle.stats["acceleration"]
    
    def calculatecurrentmaxspeed(self):
        min_vehicle = min(self.vehicles, key=lambda x: x.stats["maximumspeed"])
        return min_vehicle.stats["maximumspeed"]

    def calculatecurrentmindeceleration(self):
        min_vehicle = min(self.vehicles, key=lambda x: x.stats["deceleration"])
        return min_vehicle.stats["deceleration"]
    
    def calculatecurrentmaxreverseacceleration(self):
        min_vehicle = min(self.vehicles, key=lambda x: x.stats["reverseacceleration"])
        return min_vehicle.stats["reverseacceleration"]
    
    def calculatecurrentmaxreverse(self):
        min_vehicle = min(self.vehicles, key=lambda x: x.stats["maximumreverse"])
        return min_vehicle.stats["maximumreverse"]
    
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