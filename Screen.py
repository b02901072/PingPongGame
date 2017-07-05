import pygame
from util import *

class Screen():

	def __init__(self, width=1080, height=720):

		self.width = width
		self.height = height

		self.screen = pygame.display.set_mode((self.width, self.height))

		self.background = None

	# IMAGES SETTING
	def set_background(self, image_filename):
		self.background = pygame.image.load(image_filename).convert()

	# DISPLAY FUNCTION
	def display_background(self):
		if self.background is None:
			raise
		self.screen.blit(self.background, POSITION.BORDER)

