import pygame
from maze_runner import make_adjacency_list, path_finder

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (106, 13, 173)

WIDTH = 10
HEIGHT = 10

MARGIN = 3

grid = [[0 for _ in range(50)] for _ in range(50)]


pygame.init()

WINDOW_SIZE = [653, 753]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Array Backed Grid")

done = False

clock = pygame.time.Clock()
mouse_pressed = False

input_box = pygame.Rect(200, 675, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
button_color = color_inactive
active = False
text = ''
font = pygame.font.Font(None, 32)
static_text = pygame.font.Font(None, 28).render('Enter x1, y1, x2, y2', True, GREEN)
text_rect = static_text.get_rect()
text_rect.center = (100, 690)
reset_text = pygame.font.Font(None, 28).render('Reset', True, WHITE)

while not done:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                pos = pygame.mouse.get_pos()
                try:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    grid[row][column] = 1
                except IndexError:
                    pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 400 <= mouse[0] <= 550 and 675 <= mouse[1] <= 710:
                for i in range(50):
                    for j in range(50):
                        grid[i][j] = 0
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
                mouse_pressed = True
            button_color = color_active if active else color_inactive
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    adjacency_list = make_adjacency_list(grid)
                    start = tuple(map(lambda x: int(x), text.split(',')[:2]))
                    stop = tuple(map(lambda x: int(x), text.split(',')[2:]))
                    distance, path = path_finder(adjacency_list, start, stop)
                    current_node = stop
                    while current_node != start:
                        current_node = path.get(current_node)
                        grid[current_node[0]][current_node[1]] = 2
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill(BLACK)

    for row in range(50):
        for column in range(50):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            elif grid[row][column] == 2:
                color = PURPLE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    for column in range(50):
        color = RED
        pygame.draw.rect(screen, color,
                         [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * 50 + MARGIN,
                          WIDTH, HEIGHT])


    txt_surface = font.render(text, True, button_color)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    screen.blit(static_text, text_rect)
    pygame.draw.rect(screen, button_color, input_box, 2)

    pygame.draw.rect(screen, RED, [400, 675, 150, 35])
    screen.blit(reset_text, (400, 675, 150, 35))

    clock.tick(60)

    pygame.display.flip()

pygame.quit()