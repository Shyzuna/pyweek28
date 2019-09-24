import pygame
import sys


class InputManager:
    def __init__(self):
        pass

    def init(self):
        pass

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)


InputManager = InputManager()