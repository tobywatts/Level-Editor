import pygame
import button

from level_settings import *


class Renderer:
    def __init__(self):
        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Taro')

        self.scroll_x = 0
        self.scroll_y = 0

    def draw_world(self, eventManager):
        for y, row in enumerate(world_data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    eventManager.tiles[tile] = pygame.transform.scale(eventManager.tiles[tile], (TILE_SIZE, TILE_SIZE))
                    self.win.blit(eventManager.tiles[tile], (x * TILE_SIZE - self.scroll_x, y * TILE_SIZE - self.scroll_y))