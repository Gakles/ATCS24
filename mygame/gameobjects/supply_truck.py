# supply_truck.py
from gameobjects.vehicle import Vehicle

class Supply_Truck(Vehicle):
    def __init__(self, stats):
        super().__init__(stats)
        self.currentsupply = 0 

    def honk_horn(self):
        print("Honk! I'm a " + self.stats["class"])
