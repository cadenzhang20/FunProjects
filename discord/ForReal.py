import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

player = pygame.Rect(525, 0, 150, 200)
test_character = pygame.image.load("test.png").convert()
test_character = pygame.transform.scale(test_character, (player.width, player.height))
right_char = pygame.transform.flip(test_character, True, False)

g = -1
timer = 0
x_pos = 500
y_pos = 0
vel = 0
x_change = 5
jump_stop = False
di_left = True

run = True
while run:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if di_left:
        screen.blit(test_character, (player.x, player.y))
    elif not di_left:
        screen.blit(right_char, (player.x, player.y))

    if key[pygame.K_LEFT]:
        player.x -= x_change
        di_left = True
    if key[pygame.K_RIGHT]:
        player.x += x_change
        di_left = False
    if key[pygame.K_z] and not jump_stop:
        vel = 20
        jump_stop = True
    if key[pygame.K_LSHIFT]:
        x_change = 10
    else:
        x_change = 5

    vel += g
    player.y -= vel

    if player.y > 400:
        player.y = 400
        vel = 0
        jump_stop = False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()