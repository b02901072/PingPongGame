from util import *

class Bar():
	def __init__(self, 
		index=0, length=100, width=12,
		color=COLOR.BLUE,
		speed=600,
		pos_x=20,
		pos_y=360):

		self.index = index
		self.color = color
		self.length = length
		self.width = width
		self.dir_x = 0
		self.dir_y = 0
		self.speed_x = 0
		self.speed_y = speed
		self.initial_pos_x = pos_x
		self.initial_pos_y = pos_y
		self.pos_x = pos_x
		self.pos_y = pos_y

	def update(self, time_in_sec):
		self.pos_x += self.speed_x * time_in_sec * self.dir_x
		self.pos_y += self.speed_y * time_in_sec * self.dir_y

	def reset(self):
		self.pos_x = self.initial_pos_x
		self.pos_y = self.initial_pos_y
		self.dir_x = 0
		self.dir_y = 0

	def auto_move(self, ball):
		pass
		