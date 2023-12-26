import math
class Player:
    def __init__(self, currentvehicle, drawbackground):
        self.currentvehicle = currentvehicle
        self.drawbackground = drawbackground
        self.vehiclecurrent_angle = 0
        self.move_speed = 1
        self.rotation_speed = 15
        self.x = 0
        self.y = 0

    def movevehicle(self, keys_pressed):
        for key in keys_pressed:
            if key == 'w':
                # Move forward
                self.drawbackground.position[0] += self.move_speed * math.cos(self.vehiclecurrent_angle)
                self.drawbackground.position[1] += self.move_speed * math.sin(self.vehiclecurrent_angle)
            elif key == 's':
                # Move backward
                self.drawbackground.position[0] -= self.move_speed * math.cos(self.vehiclecurrent_angle)
                self.drawbackground.position[1] -= self.move_speed * math.sin(self.vehiclecurrent_angle)
            elif key == 'a':
                # Turn left
                self.vehiclecurrent_angle  += self.rotation_speed
            elif key == 'd':
                # Turn right
                self.vehiclecurrent_angle  -= self.rotation_speed