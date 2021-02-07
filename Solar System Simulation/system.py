# name: Stephen Wang
# date: October 24, 2020
# purpose: System class

from body import Body
from math import sqrt

class System:
    def __init__(self, body_list):
        # initialize instance variables for list of bodies and constant acceleration values (for checkpoint)
        self.body_list = body_list
    
    def compute_acceleration(self, n):
        # initializing x , y distance variables and acceleration
        accel = 0
        accel_x = 0
        accel_y = 0
        x_dist = 0
        y_dist = 0
        GRAV = 6.67384E-11 # gravitational constant

        for i in range(len(self.body_list)): # num of times to calculate accelerations
            if i != n: # skipping calculation for planet itself
                x_dist = self.body_list[i].x - self.body_list[n].x
                y_dist = self.body_list[i].y - self.body_list[n].y
                r = sqrt(x_dist * x_dist + y_dist * y_dist)

                # summing up accelerations from each planet
                accel = (GRAV * self.body_list[i].mass) / (r * r)

                # return acceleration components
                accel_x += accel * (x_dist/r)
                accel_y += accel * (y_dist/r)
        
        return (accel_x, accel_y)
    
    def update(self, timestep): # update the positions and velocities for each body
        for i in range(len(self.body_list)):
            (accel_x, accel_y) = self.compute_acceleration(i)
            self.body_list[i].update_velocity(timestep, accel_x, accel_y)
            self.body_list[i].update_position(timestep)  

    def draw(self, cx, cy, pixels_per_meter):
        # draw each body + pass parameters for conversion from real world to pixels
        for bod in self.body_list:
            bod.draw(cx, cy, pixels_per_meter)
            