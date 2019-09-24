import pygame


class DisplayManager:
    def __init__(self):
        self._screen = None

    def init(self):
        self._screen = pygame.display.set_mode((1200, 800))

    def update(self):
        self._screen.fill((255, 255, 255))
        pygame.display.flip()


DisplayManager = DisplayManager()
