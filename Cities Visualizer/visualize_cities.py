# name: Stephen Wang
# date: November 7, 2020
# purpose: Visualizing the 50 most populous cities on a map

from cs1lib import *
from city import City

WINDOW_X = 720
WINDOW_Y = WINDOW_X / 2
CENTER_X = WINDOW_X / 2
CENTER_Y = WINDOW_Y / 2
TOP = 50 # top 50 cities in population

loaded = False # has the map loaded?
count = 0 # how many pts. have been drawn?
frames = 0 # count number of frames

def get_coordinates(): 
    # read into cities_population.txt
    r_file = open("cities_population.txt", "r")
    city_coor = []
    
    # add coordinates of top cities as tuples into city_coor list
    for i in range(TOP):
        line = r_file.readline()
        city2 = line.strip().split(",")
        city_coor.append((float(city2[3]), float(city2[2])))
    
    r_file.close()
    
    return city_coor

def draw():
    global count, frames, loaded
    # load map
    if not loaded:
        img = load_image("world.png")
        draw_image(img, CENTER_X, CENTER_Y, 360, 180) # center the image
        loaded = True
    else:
        # if less than TOP pts. drawn, draw a pt. every 10 frames
        if (count < TOP) and (frames % 10 == 0):
            # get city coordinates
            city_coor = get_coordinates()
            
            # draw point of city
            enable_stroke()
            set_stroke_color(1, 0.6, 0)
            set_stroke_width(8)
            draw_point(CENTER_X + 2*(city_coor[count][0]), CENTER_Y - 2*(city_coor[count][1]))
            
            # increase number of pts. drawn
            count += 1
    frames += 1

start_graphics(draw, width=WINDOW_X, height=WINDOW_Y)