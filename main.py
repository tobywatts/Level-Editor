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
renderer.tile_buttons(eventManager)

while eventManager.running:

    new_time = time.time()

    if new_time - start_time >= 1 / FPS:
        delta_time = (new_time - start_time)
        start_time = new_time

    eventManager.check_events()
    eventManager.check_scroll(renderer, delta_time)

    renderer.draw_bg()
    renderer.draw_grid()

    pygame.draw.rect(renderer.win, (51, 51, 51), (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    # choose a tile
    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(renderer.win):
            current_tile = button_count
            print(current_tile)

    pygame.draw.rect(renderer.win, (255, 255, 255), button_list[current_tile], 2)

    pygame.display.update()
