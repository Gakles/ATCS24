import math
class Player:
    def __init__(self, currentvehicle, drawbackground):
        self.currentvehicle = currentvehicle
        self.drawbackground = drawbackground
        self.vehiclecurrent_angle = math.radians(-90)
        self.move_speed = 1
        self.rotation_speed = math.radians(15/60)
        self.x = 0
        self.y = 0

    def movevehicle(self, keys_pressed):
        for key in keys_pressed:
            if key == 'w':
                # Move backward
                self.drawbackground.position[0] -= self.move_speed * math.cos(self.vehiclecurrent_angle)
                self.drawbackground.position[1] -= self.move_speed * math.sin(self.vehiclecurrent_angle)
            elif key == 's':
                # Move forward
                self.drawbackground.position[0] += self.move_speed * math.cos(self.vehiclecurrent_angle)
                self.drawbackground.position[1] += self.move_speed * math.sin(self.vehiclecurrent_angle)
            elif key == 'a':
                if 's' in keys_pressed:
                    # Turn right while reversing
                    self.vehiclecurrent_angle += self.rotation_speed
                else:
                    # Turn left
                    self.vehiclecurrent_angle -= self.rotation_speed
            elif key == 'd':
                if 's' in keys_pressed:
                    # Turn left while reversing
                    self.vehiclecurrent_angle -= self.rotation_speed
                else:
                    # Turn right
                    self.vehiclecurrent_angle += self.rotation_speed
        self.currentvehicle.angle = -math.degrees(self.vehiclecurrent_angle)