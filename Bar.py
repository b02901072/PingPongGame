from util import COLOR

class Bar():
	def __init__(self, 
		index=0, half_length=50, width=12,
		color=COLOR.BLUE,
		speed=400,
		pos_x=20,
		pos_y=360):

		self.index = index
		self.color = color
		self.half_length = half_length
		self.width = width
		self.dir_x = 0
		self.dir_y = 0
		self.speed_x = 0
		self.speed_y = speed
		self.pos_x = pos_x
		self.pos_y = pos_y

	def update_position(self, time_in_sec):
		self.pos_x += self.speed_x * time_in_sec * self.dir_x
		self.pos_y += self.speed_y * time_in_sec * self.dir_y
		if self.pos_y < self.half_length:
			self.pos_y = self.half_length
		elif self.pos_y > 720 - self.half_length:
			self.pos_y = 720 - self.half_length
