import pygame
import time

from events import EventManager
from renderer import Renderer
from settings import *

eventManager = EventManager()
renderer = Renderer()

pygame.init()

start_time = time.time()
delta_time = 0


eventManager.store_tiles()
eventManager.world()
eventManager.tile_buttons()

while eventManager.running:

    new_time = time.time()

    if new_time - start_time >= 1 / FPS:
        delta_time = (new_time - start_time)
        start_time = new_time


    eventManager.checkEvents()
    eventManager.checkScroll(renderer, delta_time, FPS)

    renderer.draw_bg()
    renderer.draw_grid()


    pygame.draw.rect(renderer.win, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

        # choose a tile
    button_count = 0
    for button_count, i in enumerate(eventManager.button_list):
        if i.draw(renderer.win):
            current_tile = button_count

    pygame.display.update()
