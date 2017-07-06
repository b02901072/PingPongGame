import pygame
from util import *

class Screen():

	def __init__(self, scale=1.0):

		self.scale = 1.0
		self.width = int(1080*scale)
		self.height = int(720*scale)

		self.screen = pygame.display.set_mode((self.width, self.height))

		self.background = None

	# IMAGES SETTING
	def set_background(self, image_filename):
		self.background = pygame.image.load(image_filename).convert()

	# DISPLAY FUNCTION
	def display_background(self):
		if self.background is None:
			raise
		self.screen.blit(self.background, (0, 0))

	def display_text(self, text, color, size, position):
		x = int(position[0] * self.scale)
		y = int(position[1] * self.scale)
		s = int(size * self.scale)
		self.screen.blit(pygame.font.Font(None, s).render(text, True, color), (x, y))

