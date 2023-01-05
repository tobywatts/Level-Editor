import pygame  # got up to 16:00 in the video

pygame.init()

# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

win = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")

# load images
sky_img = pygame.image.load('bg_images/sky_cloud.png').convert_alpha()
mountain_img = pygame.image.load('bg_images/mountain.png').convert_alpha()
pine1_img = pygame.image.load('bg_images/pine1.png').convert_alpha()
pine2_img = pygame.image.load('bg_images/pine2.png').convert_alpha()

# define game variables
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


def draw_bg():
    win.blit(sky_img, (scroll, 0))
    win.blit(mountain_img, (scroll, SCREEN_HEIGHT - mountain_img.get_height() - 300))
    win.blit(pine1_img, (scroll, SCREEN_HEIGHT - pine1_img.get_height() - 150))
    win.blit(pine2_img, (scroll, SCREEN_HEIGHT - pine2_img.get_height()))


# Game loop
running = True
while running:

    # scrolling background
    if scroll_left:
        scroll += 5

    if scroll_right:
        scroll -= 5

    draw_bg()

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False

    pygame.display.update()
