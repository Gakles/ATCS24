class Convoy:
    def __init__(self, vehicles):
        self.vehicles = []
        for vehicle in vehicles:
            self.vehicles.append(vehicle)
        self.currentspeed = 0
        self.acceleration = self.calculatecurrentmaxacceleration()

    def calculatecurrentmaxacceleration(self):
        min_object = min(self.vehicles, key=lambda x: x.stats["acceleration"])
        return min_object.stats["acceleration"]