import pygame

# Cellular Automata
# Started on Wednesday, February 28th, 2024
# First copy completed Thursday, February 29th, 2024
# by Caden Zhang

# Just a fun little project
# TODO:
#   - Make it run faster
#   - Make adding in rules better
#   - Make setting up the default state better

# constants
cst_screen_width = 700
cst_screen_height = 700

cst_pixel_length = 10  # best results if it can evenly divide width and length
cst_width = cst_screen_width // cst_pixel_length  # 140
cst_height = cst_screen_height // cst_pixel_length

# game array
arr_game_grid = [[0 for _ in range(cst_width)] for _ in range(cst_height)]

# ---------------------------------------------
# FILES
# using a file for the rules of the game
txt_file_rules = open("pygame_projects/Cellular_Automata/rules.txt", "r")
obj_input_rules = txt_file_rules.readlines()
txt_file_rules.close()

obj_input_rules = [line.strip("\n") for line in obj_input_rules]

rule_count = (len(obj_input_rules) + 1) // 7  # at least with the current format
rules = [[], [], [], [], []]

loc_counter = 0
loc_rule_num = 0
loc_rules = []
for li in range(len(obj_input_rules)):
    if li == len(obj_input_rules):
        break

    line = obj_input_rules[li].strip()
    if len(line) == 0:
        continue
    elif not (line[0].isdigit() or line[0] in ">="):
        continue

    # adding rules from file
    if loc_counter == 0:
        loc_rule_num = int(line.split()[1])
    elif 1 <= loc_counter <= 3:
        loc_rules.append([int(s) for s in line.split()[:3]])
    elif loc_counter == 4:
        rules[loc_rule_num].append([loc_rules, int(line.split()[1])])

        loc_rule_num = 0
        loc_rules = []
        loc_counter = -1

    loc_counter += 1

# ---------------------------------------------
# GAME CONTENT

# starting values

# arr_game_grid[cst_height // 2][cst_width // 2] = 1

for y in range(1, cst_height):
    arr_game_grid[y][-1] = 1


# primary computation function
def find_neighbors(loc_x, loc_y):
    global cst_width
    global cst_height

    ret_offsets = [[0, 0], [0, 0]]

    if loc_x - 1 == -1:
        ret_offsets[0][0] = cst_width - 1
        ret_offsets[0][1] = loc_x + 1
    elif loc_x + 1 == cst_width:
        ret_offsets[0][0] = loc_x - 1
        ret_offsets[0][1] = 0
    else:
        ret_offsets[0][0] = loc_x - 1
        ret_offsets[0][1] = loc_x + 1

    if loc_y - 1 == -1:
        ret_offsets[1][0] = cst_height - 1
        ret_offsets[1][1] = loc_y + 1
    elif loc_y + 1 == cst_width:
        ret_offsets[1][0] = loc_y - 1
        ret_offsets[1][1] = 0
    else:
        ret_offsets[1][0] = loc_y - 1
        ret_offsets[1][1] = loc_y + 1

    ret_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pointer = [0, 0]
    for y_pos in [ret_offsets[1][0], loc_y, ret_offsets[1][1]]:
        for x_pos in [ret_offsets[0][0], loc_x, ret_offsets[0][1]]:
            ret_grid[pointer[1]][pointer[0]] = arr_game_grid[y_pos][x_pos]
            pointer[0] += 1
        pointer[1] += 1
        pointer[0] = 0

    return ret_grid


def calc_rules(cell_x, cell_y):
    loc_x, loc_y, loc_state = cell_x, cell_y, arr_game_grid[cell_y][cell_x]

    arr_neighbors = find_neighbors(loc_x, loc_y)
    for rule in rules[loc_state]:
        if arr_neighbors == rule[0]:
            return rule[1]

    return loc_state


def compute_game_grid():
    arr_new_game_grid = [line[:] for line in arr_game_grid]

    for y in range(cst_height):
        for x in range(cst_width):
            arr_new_game_grid[y][x] = calc_rules(x, y)

    return arr_new_game_grid


# ---------------------------------------------

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


# draws the out the board
def draw_game_grid(brush, size):
    brush.x, brush.y = 0, 0
    for y in range(cst_height):
        for x in range(cst_width):
            cur_pixel = arr_game_grid[y][x]
            pygame.draw.rect(screen, lst_colors[cur_pixel], brush)
            brush.move_ip(size, 0)
        brush.move_ip(0, size)
        brush.x = 0


obj_pixel_brush = pygame.Rect(0, 0, cst_pixel_length, cst_pixel_length)

# begin the pygame display
pygame.init()

screen = pygame.display.set_mode((cst_width * cst_pixel_length, cst_height * cst_pixel_length))
pygame.display.set_caption("Cellular Automata")
pygame.display.update()

# delta time?
dt = pygame.time.Clock()
cst_frames_per_display = 1

# game loop
loc_frame_count = 0
bol_game_running = True
while bol_game_running:
    # check to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bol_game_running = False

    # match set speed
    if loc_frame_count == cst_frames_per_display:
        loc_frame_count = -1

        arr_game_grid = compute_game_grid()
        draw_game_grid(obj_pixel_brush, cst_pixel_length)

        # update screen
        pygame.display.update()

    # update the clock
    loc_frame_count += 1
    dt.tick(30)

# quit game
pygame.quit()
