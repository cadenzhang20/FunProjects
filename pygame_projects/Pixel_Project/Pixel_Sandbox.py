import pygame

# Pixel Sandbox
# Started on Friday, March 1st, 2024
# by Caden Zhang

# Kinda copied code from my other project

# constants
cst_screen_width = 700
cst_screen_height = 700

arr_particles = []


# vectors
class Vector2:
    def __init__(self, change_x=0, change_y=0):
        self.x = change_x
        self.y = change_y

    def __add__(self, other):
        pass


# particles
class Particle:
    def __init__(self, x_pos, y_pos, vector):
        pass




# colors and other variables
class Colors:
    white = 255, 255, 255
    black = 0, 0, 0

    red = 255, 0, 0
    green = 0, 255, 0
    blue = 0, 0, 255

    nice_red = 222, 80, 80
    nice_green = 62, 200, 18
    nice_blue = 19, 138, 219


lst_colors = [Colors.black,         # 0
              Colors.white,         # 1
              Colors.nice_green,    # 2
              Colors.nice_blue,     # 3
              Colors.nice_red       # 4
              ]

pygame.init()

screen = pygame.display.set_mode((cst_screen_width, cst_screen_height))
pygame.display.set_caption("Pixel Sandbox")

# delta time?
dt = pygame.time.Clock()
cst_frames_per_display = 1


loc_frame_count = 0
bol_game_running = True
while bol_game_running:
    # check to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bol_game_running = False

    # match set speed
    if loc_frame_count == cst_frames_per_display:
        pass

    # update the clock
    loc_frame_count += 1
    dt.tick(30)

# quit game
pygame.quit()
