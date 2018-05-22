import math
import random

import pygame

import utils
from gameengine import GameEngine
from gamestate import GameState

class Snake(GameState):

    def __init__(self):
        super(Snake, self).__init__()

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEngine.quit()
        keypresses = pygame.key.get_pressed()

    def update(self):
        super().update(50)

    def draw(self):
        GameEngine.game_display.fill((0, 0, 0))
        super().draw()
