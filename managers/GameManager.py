import pygame
from managers.DisplayManager import DisplayManager
from managers.InputManager import InputManager


class GameManager:
    def __init__(self):
        pass

    def init(self):
        pygame.init()
        DisplayManager.init()
        InputManager.init()
        self.loop()

    def loop(self):
        while True:
            InputManager.update()
            DisplayManager.update()


GameManager = GameManager()
