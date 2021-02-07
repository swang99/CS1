# author: Stephen Wang
# date: September 30, 2020
# purpose: A two-player pong game.

from cs1lib import *

# window size
WINDOW_X = 400
WINDOW_Y = 400

# height and width of paddles
HEIGHT = WINDOW_X * 0.2
WIDTH = WINDOW_Y * 0.05

# x coordinate of paddles
LX_POSITION = 0  
RX_POSITION = WINDOW_X - WIDTH

# paddle movement speed
MOVE = WINDOW_Y * 0.03

# movement/action keys
LEFT_UP = "a" 
LEFT_DOWN = "z" 
RIGHT_UP = "k"
RIGHT_DOWN = "m"
QUIT = "q"
NEW_GAME = " "

# radius of ball
R = WINDOW_X * 0.025

# y coordinate of paddles
ly_position = (WINDOW_Y - HEIGHT)/2
ry_position = (WINDOW_Y - HEIGHT)/2

# ball x and y coordinates, x and y movement speeds
ball_x = WINDOW_X / 2
ball_y = WINDOW_Y / 2
ball_speed_x = MOVE * 0.5
ball_speed_y = MOVE * 0.4

# movement key press booleans
apressed = False
zpressed = False
kpressed = False
mpressed = False
spacepressed = False

def left_paddle(): # drawing left paddle
    set_fill_color(1, 1, 0)
    disable_stroke()
    draw_rectangle(LX_POSITION, ly_position, WIDTH, HEIGHT)

def right_paddle(): # drawing right paddle
    set_fill_color(1, 1, 0)
    disable_stroke()
    draw_rectangle(RX_POSITION, ry_position, WIDTH, HEIGHT)

def ball(): # drawing ball
    set_fill_color(1, 1, 1)
    disable_stroke()
    draw_circle(ball_x, ball_y, R)
    ball_move()

# movement of the paddles
def paddle_move():
    global ly_position, ry_position
    # moving left paddle up
    if apressed and ly_position > 0:
        ly_position = max(0, ly_position - MOVE)
    # moving left paddle down
    if zpressed and ly_position < WINDOW_Y - HEIGHT:
        ly_position = min((WINDOW_Y - HEIGHT), ly_position + MOVE)
    # moving right paddle up
    if kpressed and ry_position > 0:
        ry_position = max(0, ry_position - MOVE)
    # moving right paddle down
    if mpressed and ry_position < WINDOW_Y - HEIGHT:
        ry_position = min((WINDOW_Y - HEIGHT), ry_position + MOVE)

def before_game(): # draw starting instructions
    if not spacepressed:
        enable_stroke()
        set_stroke_color(0,0,0)
        set_font("Arial")
        set_font_size(WINDOW_X * 0.0375)
        draw_text("Welcome to Pong!", WINDOW_X/3.5, WINDOW_Y * 0.45)
        draw_text("Press space to start.", WINDOW_X/3.5, WINDOW_Y * 0.55)

def ball_move(): # movement of the ball
    global ball_x, ball_y, ball_speed_x, ball_speed_y, spacepressed
    
    # initializing ball speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collisions 1A: Side of either paddle, reverse x-component speed
    # Checking to see if the the ball's top/bottom (y) and right/left (x) is in range to hit the paddle face-on
    if (ball_y >= ry_position and ball_y <= ry_position + HEIGHT) and (ball_x >= RX_POSITION - R) \
    or (ball_y >= ly_position and ball_y <= ly_position + HEIGHT)  and (ball_x <= LX_POSITION + WIDTH + R):
        ball_speed_x *= -1 
        # Collision 1B: Top or bottom of either paddle, end game
        if (ball_x + R > RX_POSITION + abs(ball_speed_x)) or (ball_x - R < LX_POSITION + WIDTH - abs(ball_speed_x)):
            game_ends()
            
    # Collisions 2: Vertical wall, end game
    if (ball_x - R <= 0) or (ball_x + R >= WINDOW_X): 
        game_ends()

    # Collisions 3: Horizontal wall, reverse y-component speed
    if (ball_y - R <= 0) or (ball_y + R >= WINDOW_Y): 
        ball_speed_y *= -1

def game_ends():
    global ball_x, ball_y, ball_speed_y, spacepressed
    # re-show starting message
    enable_stroke()
    # reset ball position and speed
    ball_x = WINDOW_X / 2
    ball_y = WINDOW_Y / 2
    ball_speed_y = MOVE * 0.4
    spacepressed = False

def my_key_press(value): # key press tracking
    global apressed, zpressed, kpressed, mpressed, spacepressed
    if value == LEFT_UP:
        apressed = True
    if value == LEFT_DOWN:
        zpressed = True
    if value == RIGHT_UP:
        kpressed = True
    if value == RIGHT_DOWN:
        mpressed = True
    if value == NEW_GAME:
        spacepressed = True
    elif value == QUIT:
        cs1_quit()

def my_key_release(value): # key release tracking
    global apressed, zpressed, kpressed, mpressed
    if value == LEFT_UP:
        apressed = False
    if value == LEFT_DOWN:
        zpressed = False
    if value == RIGHT_UP:
        kpressed = False
    if value == RIGHT_DOWN:
        mpressed = False

def draw():
    # setting gray background
    clear()
    set_clear_color(0.6, 0.6, 0.6)

    # drawing the paddles and their movements
    left_paddle()
    right_paddle()
    paddle_move()

    # starting instructions
    before_game()

    # start the game and draw the ball
    if spacepressed:
        ball()

start_graphics(draw, width=WINDOW_X, height=WINDOW_Y, key_press=my_key_press, key_release=my_key_release)