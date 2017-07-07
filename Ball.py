from util import COLOR

class Ball():
	def __init__(self, 
		index=0, size=16,
		default_color=COLOR.GREEN, accel_color=COLOR.RED,
		speed=300,
		pos_x=540, pos_y=360, 
		accel=False):

		self.index = index
		self.default_color = default_color
		self.accel_color = accel_color
		self.size = size
		self.initial_speed = speed
		self.current_speed_x = speed
		self.current_speed_y = speed
		self.pos_x = pos_x
		self.pos_y = pos_y

	def update_position(self, time_in_sec):
		self.pos_x += self.current_speed_x * time_in_sec
		self.pos_y += self.current_speed_y * time_in_sec

	
