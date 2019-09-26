import pygame
import sys
import settings.settings as settings
from data.constants import Color, Information
from src.scenes.gameScene import GameScene

screen = None
currentScene = None
allScenes = None


def init():
    global screen, currentScene, allScenes
    pygame.init()
    screen = pygame.display.set_mode(settings.RESOLUTION, pygame.DOUBLEBUF)
    pygame.display.set_caption('{} - {}'.format(Information['title'], Information['version']))
    allScenes = {
        'menu': None,
        'game': GameScene()
    }
    changeScene(settings.DEFAULT_SCENE)

def loop():
    time = pygame.time.Clock()
    while True:
        # 60 fps
        deltaTime = time.tick(60)
        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
        # Update
        currentScene.update(deltaTime)
        # Redraw
        screen.fill(Color.Black.value)
        currentScene.display(screen)
        pygame.display.flip()


def changeScene(sceneName):
    global currentScene
    currentScene = allScenes[sceneName]
    currentScene.load()
    pygame.display.set_caption('{} - {} - {}'.format(Information['title'], currentScene.getName(), Information['version']))
