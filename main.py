import pygame  # got up to 44:05 in the video
import button

pygame.init()

current_tile = 0
clock = pygame.time.Clock()
FPS = 60

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

win = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")

# define game variables
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

# load images
sky_img = pygame.image.load('bg_images/sky_cloud.png').convert_alpha()
mountain_img = pygame.image.load('bg_images/mountain.png').convert_alpha()
pine1_img = pygame.image.load('bg_images/pine1.png').convert_alpha()
pine2_img = pygame.image.load('bg_images/pine2.png').convert_alpha()

# store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"tile/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

# define colours
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (200, 25, 25)


# create function for drawing background
def draw_bg():
    win.fill(GREEN)
    width = sky_img.get_width()
    for x in range(4):
        win.blit(sky_img, ((x * width) - scroll * 0.5, 0))
        win.blit(mountain_img, ((x * width) - scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
        win.blit(pine1_img, ((x * width) - scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
        win.blit(pine2_img, ((x * width) - scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))


# draw grid
def draw_grid():
    # vertical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(win, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
    # horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(win, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


# create buttons
# make a button list
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0

# Game loop
running = True
while running:

    clock.tick(FPS)

    draw_bg()
    draw_grid()

    # draw side tile panel
    pygame.draw.rect(win, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    # choose a tile
    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(win):
            current_tile = button_count

    # highlight the selected
    pygame.draw.rect(win, RED, button_list[current_tile].rect, 3)

    # scrolling background
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed

    if scroll_right == True:
        scroll += 5 * scroll_speed

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False

    pygame.display.update()
