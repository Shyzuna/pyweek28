import sys

# Check python 3
if sys.version_info < (3, 0):
    print('Need Python 3 at least to run the game !')
    sys.exit(-1)

# Check pygame
try:
    import pygame
except ImportError:
    print('Pygame 1.9 is required to run the game !')
    sys.exit(-2)

from src.__main__ import main
main()
