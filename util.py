import pygame
import sys

# COLOR DEFINITION
class COLOR():
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GRAY = 150, 150, 150
	RED = 255, 0, 0
	GREEN = 0, 255, 0
	BLUE = 0, 0, 255
	YELLOW = 255, 255, 0

def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()