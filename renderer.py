import pygame
import button

from settings import *


class Renderer:
    def __init__(self):

        self.win = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))
        pygame.display.set_caption('Level Editor')

        # load images
        self.background_image = pygame.image.load('bg_images/temp_bg.png').convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))

        self.scroll_x = 0
        self.scroll_y = 0

        self.button_column = 0
        self.button_row = 0
        self.tile_button = None

    def draw_bg(self):
        self.win.fill((51, 51, 51))
        width = self.background_image.get_width()
        height = self.background_image.get_height()
        for i in range(2):
            self.win.blit(self.background_image, (i * width - self.scroll_x, 0 - self.scroll_y))
            # will draw images below creating an extra layer below to the background
            self.win.blit(self.background_image, (i * width - self.scroll_x, height - self.scroll_y))

    def draw_grid(self):
        for i in range(MAX_COLUMNS + 1):
            pygame.draw.line(self.win, (255, 255, 255), (i * TILE_SIZE - self.scroll_x, 0),
                             (i * TILE_SIZE - self.scroll_x, SCREEN_HEIGHT))

        for i in range(ROWS + 1):
            pygame.draw.line(self.win, (255, 255, 255), (0, i * TILE_SIZE - self.scroll_y),
                             (SCREEN_WIDTH, i * TILE_SIZE - self.scroll_y))
            pygame.draw.line(self.win, (255, 255, 255), (0, i * TILE_SIZE - self.scroll_y + SCREEN_HEIGHT),
                             (SCREEN_WIDTH, i * TILE_SIZE - self.scroll_y + SCREEN_HEIGHT))

    def tile_buttons(self, eventManager):
        for i in range(len(eventManager.tiles)):
            self.tile_button = button.Button(SCREEN_WIDTH + (60 * self.button_column) + 45,
                                             60 * self.button_row + 30,
                                             eventManager.tiles[i], 4)
            button_list.append(self.tile_button)

            self.button_column += 1

            if self.button_column == 4:
                self.button_row += 1
                self.button_column = 0
