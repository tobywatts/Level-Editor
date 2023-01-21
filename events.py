import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_ROWS, TILE_COLUMNS, SPRITE_WIDTH, ROWS, MAX_COLUMNS


class EventManager:
    def __init__(self):
        self.running = True

        self.x = 0
        self.y = 0
        self.tiles = []
        self.tile_set = pygame.image.load('tiles/Forest.png')

        self.world_data = []


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                pass

            if event.type == pygame.KEYUP:
                pass

    def store_tiles(self):
        for i in range(TILE_ROWS * TILE_COLUMNS):
            self.x = i % TILE_ROWS
            self.y = i // TILE_COLUMNS
            tile = self.tile_set.subsurface((self.x * SPRITE_WIDTH, self.y * SPRITE_WIDTH),
                                            (SPRITE_WIDTH, SPRITE_WIDTH))
            self.tiles.append(tile)

    def world(self):
        for row in range(ROWS):
            r = [-1] * MAX_COLUMNS
            self.world_data.append(r)

    def check_scroll(self, renderer, delta_time):
        keys = pygame.key.get_pressed()
        # scrolling background
        if keys[pygame.K_a] and renderer.scroll_x > 0:  # left
            renderer.scroll_x -= 75 * delta_time

        if keys[pygame.K_d] and renderer.scroll_x < (renderer.background_image.get_width() * 2 - SCREEN_WIDTH):
            renderer.scroll_x += 75 * delta_time

        if keys[pygame.K_w] and renderer.scroll_y > 0:
            renderer.scroll_y -= 75 * delta_time

        if keys[pygame.K_s] and renderer.scroll_y < (2 * renderer.background_image.get_height() - SCREEN_HEIGHT):
            renderer.scroll_y += 75 * delta_time
