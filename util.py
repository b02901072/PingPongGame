import pygame
import sys, math, random

# Definition
class COLOR():
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GRAY = 150, 150, 150
	LIGHT_GRAY = 200, 200, 200
	RED = 255, 0, 0
	GREEN = 0, 255, 0
	BLUE = 0, 0, 255
	YELLOW = 255, 255, 0

# Utility Function
def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def posi_or_nega(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return [-1, 1][random.randint(0, 1)]

def distance(a, b):
	return math.sqrt((a.pos_x-b.pos_x)**2 + (a.pos_y-b.pos_y)**2)

def random_select_another_int(start, end, i):
	# random select an interger in [start, end] which is not i
	assert i >= start and i <= end
	while True:
		j = random.randint(start, end)
		if j != i:
			return j

# Utility Class
class SelectList():

	def __init__(self, **kwargs):

		self.text = kwargs['text']
		self.len = len(self.text)
		self.pos_x = [kwargs['pos_x']] * self.len
		self.pos_y = [0] * self.len
		self.default_color = kwargs['default_color']
		self.select_color = kwargs['select_color']
		self.color = [self.default_color] * self.len
		self.text_size = [kwargs['text_size']] * self.len
		self.cursor_size = kwargs['cursor_size']
		
		for i in range(self.len):
			self.pos_y[i] = kwargs['pos_y_initial'] + i * kwargs['pos_y_spacing']
		try:
			self.pos_x[self.len-1] = kwargs['pos_x_last']
		except:
			pass
		try:
			self.pos_y[self.len-1] = kwargs['pos_y_last']
		except:
			pass

		self.cursor_index = 0
		self.color[self.cursor_index] = self.select_color

	def move_cursor(self, n):
		self.color[self.cursor_index] = self.default_color
		self.cursor_index = (self.cursor_index + n) % self.len
		self.color[self.cursor_index] = self.select_color

