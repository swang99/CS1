# name: Stephen Wang
# date: November 16, 2020
# purpose: Vertex class

from cs1lib import *

class Vertex:
    def __init__(self, name, x, y, adj):
        self.name = name
        self.x = x
        self.y = y
        self.adj = adj
    
    def __str__(self):
        new_adj = []
        for vert in self.adj:
            new_adj.append(vert.name)
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + ", ".join(new_adj)
    
    def init_draw(self, r, g, b,radius):
        # draw initial point
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, radius)

        # draw initial connections
        set_stroke_width(3)
        set_stroke_color(r, g, b)
        for adj in self.adj:
            draw_line(self.x, self.y, adj.x, adj.y)
    
    # highlight BFS path
    def draw_bfs(self, path, r, g, b, radius): 
        for i in range(len(path) - 1):
            set_stroke_color(r, g, b)
            draw_line(path[i].x, path[i].y, path[i+1].x, path[i+1].y)
        for point in path:
            set_fill_color(r, g, b)
            draw_circle(point.x, point.y, radius)
    
    # is mouse on a vertex?
    def mouse_on(self, radius): 
        if abs(mouse_x() - self.x) <= radius and abs(mouse_y() - self.y) <= radius:
            return True
    
    # set starting vertex
    def set_start(self, r, g, b, radius): 
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, radius)

    # is mouse hovering over a goal vertex?
    def detect_goal(self, r, g, b, radius): 
        if self.mouse_on(radius): 
            set_stroke_color(r, g, b)
            set_fill_color(r, g, b)
            draw_circle(self.x, self.y, radius)
            return True