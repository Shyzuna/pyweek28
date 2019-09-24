import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
        screen.fill((255, 255, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
