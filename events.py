import pygame
import csv

from settings import *

class EventManager():
    def __init__(self):
        self.running = True

        self.x = 0
        self.y = 0
        self.tiles = []
        self.tile_set = pygame.image.load('tiles/Forest.png')
        self.current_tile = 0

    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def store_tiles(self):
        for i in range(TILE_ROWS * TILE_COLUMNS):
            self.x = i % TILE_ROWS
            self.y = i // TILE_COLUMNS
            tile = self.tile_set.subsurface((self.x * SPRITE_WIDTH, self.y * SPRITE_WIDTH),
                                            (SPRITE_WIDTH, SPRITE_WIDTH))
            self.tiles.append(tile)

    def check_scroll(self, renderer, delta_time):
        keys = pygame.key.get_pressed()
        # scrolling background
        if keys[pygame.K_a] and renderer.scroll_x > 0:  # left
            renderer.scroll_x -= 500 * delta_time

        if keys[pygame.K_d] and renderer.scroll_x < (renderer.background_image.get_width() * 2 - SCREEN_WIDTH):
            renderer.scroll_x += 500 * delta_time

        if keys[pygame.K_w] and renderer.scroll_y > 0:
            renderer.scroll_y -= 500 * delta_time

        if keys[pygame.K_s] and renderer.scroll_y < (2 * renderer.background_image.get_height() - SCREEN_HEIGHT):
            renderer.scroll_y += 500 * delta_time

    def load_level(self, renderer):
        renderer.scroll_x = 0 
        with open('level_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x,row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)