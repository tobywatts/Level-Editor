import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
SIDE_MARGIN = 300

GREEN = (144, 201, 120)

win = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor')

# define game variables
ROWS = 16
MAX_COLUMNS = 65
TILE_SIZE = SCREEN_HEIGHT // ROWS

scroll_left = False
scroll_right = False
scroll_up = False
scroll_down = False
scroll_x = 0
scroll_y = 0

# load images
sky_img = pygame.image.load('bg_images/temp_bg.png').convert_alpha()
sky_img = pygame.transform.scale(sky_img, (SCREEN_WIDTH + SIDE_MARGIN - scroll_x, SCREEN_HEIGHT - scroll_y))


def draw_bg():
    win.fill(GREEN)
    width = sky_img.get_width()
    height = sky_img.get_height()
    for i in range(2):
        win.blit(sky_img, (i * width - scroll_x, 0 - scroll_y))
        # will draw images above creating an extra layer above to the background
        win.blit(sky_img, (i * width - scroll_x, -height - scroll_y))


def draw_grid():
    for i in range(MAX_COLUMNS + 1):
        pygame.draw.line(win, (255, 255, 255), (i * TILE_SIZE - scroll_x, 0), (i * TILE_SIZE - scroll_x, SCREEN_HEIGHT))

    for i in range(ROWS + 1):
        pygame.draw.line(win, (255, 255, 255), (0, -i * TILE_SIZE - scroll_y),
                         (SCREEN_WIDTH, -i * TILE_SIZE - scroll_y))
        pygame.draw.line(win, (255, 255, 255), (0, i * TILE_SIZE - scroll_y), (SCREEN_WIDTH, i * TILE_SIZE - scroll_y))


running = True
while running:

    # scrolling background
    if scroll_left and scroll_x > 0:
        scroll_x -= 5

    if scroll_right and scroll_x < (sky_img.get_width() * 2 - SCREEN_WIDTH):  # could use '(MAX_COLUMNS * TILE_SIZE) - SCREEN_WIDTH'
        scroll_x += 5

    if scroll_up and scroll_y > -sky_img.get_height():
        scroll_y -= 5

    if scroll_down and scroll_y < (sky_img.get_height() - SCREEN_HEIGHT):
        scroll_y += 5

    clock.tick(FPS)

    draw_bg()
    draw_grid()

    pygame.draw.rect(win, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_UP:
                scroll_up = True
            if event.key == pygame.K_DOWN:
                scroll_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_UP:
                scroll_up = False
            if event.key == pygame.K_DOWN:
                scroll_down = False
    pygame.display.update()
