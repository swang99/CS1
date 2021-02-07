# name: Stephen Wang
# date: November 16, 2020
# purpose: Display graph + select start/goal vertices

from cs1lib import *
from load_graph import load_graph 
from bfs import bfs

WINDOW_X = 1012
WINDOW_Y = 811
PT_RADIUS = 6 # vertex radius

mpressed = False # mouse pressed?
start = None # start vertex
goal = None # goal vertex

def draw():
    global mpressed, start, goal
    
    # load map
    img = load_image("dartmouth_map.png")
    draw_image(img, 0, 0)

    for v in vertex_dict: 
        vertex = vertex_dict[v] # key value of vertex
        vertex.init_draw(0, 0, 1, PT_RADIUS)
    
    for v in vertex_dict:
        vertex = vertex_dict[v]
        
        # set start vertex
        if mpressed and vertex.mouse_on(PT_RADIUS): 
            start = vertex
        if vertex == start:
            start.set_start(1, 0, 0, PT_RADIUS)

        # set goal vertex
        if vertex.mouse_on(PT_RADIUS) and (start is not None) and (vertex != start): 
            goal = vertex
            goal.detect_goal(1, 0, 0, PT_RADIUS)
            trace = bfs(start, goal)
            vertex.draw_bfs(trace, 1, 0, 0, PT_RADIUS)
        else:
            goal = None
        
def my_mouse_press(mx, my):
    global mpressed
    mpressed = True

def my_mouse_release(mx, my):
    global mpressed
    mpressed = False
   
vertex_dict = load_graph("dartmouth_graph.txt")
start_graphics(draw, width=WINDOW_X, height=WINDOW_Y, mouse_press=my_mouse_press, mouse_release=my_mouse_release)