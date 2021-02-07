# name: Stephen Wang
# date: October 24, 2020
# purpose: Body class

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        # physical properties of body
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        # radius of body
        self.pixel_radius = pixel_radius
        
        # RGB values for body
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        # updating position using updated speed
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    def update_velocity(self, timestep, ax, ay):
        # update velocity comps. using acceleration comps. and timestep
        self.vx += ax * timestep
        self.vy += ay * timestep
        
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)

        # draw the body in its current position (how far it has moved away from its initial center)
        draw_circle(cx + (self.x * pixels_per_meter), cy + (self.y * pixels_per_meter), self.pixel_radius)