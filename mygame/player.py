import math
class Player:
    def __init__(self, currentvehicle, drawbackground):
        self.currentvehicle = currentvehicle
        self.drawbackground = drawbackground
        self.vehiclecurrent_angle = math.radians(-90)
        self.move_speed = 1
        self.rotation_speed = math.radians(30/60)
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
                    self.vehiclecurrent_angle += self.rotation_speed/2
                else:
                    # Turn left
                    if 'w' not in keys_pressed:
                        self.vehiclecurrent_angle -= self.rotation_speed
                    else:
                        self.vehiclecurrent_angle -= self.rotation_speed/2
            elif key == 'd':
                if 's' in keys_pressed:
                    # Turn left while reversing
                    self.vehiclecurrent_angle -= self.rotation_speed/2
                else:
                    # Turn right
                    if 'w' not in keys_pressed:
                        self.vehiclecurrent_angle += self.rotation_speed
                    else:
                        self.vehiclecurrent_angle += self.rotation_speed/2
        self.currentvehicle.angle = -math.degrees(self.vehiclecurrent_angle)

    def moveturret(self, mousepos):
        if self.currentvehicle.stats["turret"]:
            #print(self.currentvehicle.position, mousepos)
            angle_radians = math.atan2(mousepos[1] - self.currentvehicle.position[1], mousepos[0] - self.currentvehicle.position[0])
            angle_degrees = math.degrees(angle_radians)
            self.currentvehicle.turret.updateturret(angle_degrees)
        