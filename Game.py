import pygame
from Ball import *
from Bar import *

class Duel():

	def __init__(self):

		self.ball_num = 1
		self.balls = [Ball()]
		self.bars = [Bar(index=0, color=COLOR.BLUE, pos_x=20), Bar(1, color=COLOR.RED, pos_x=1060)]
		self.clock = pygame.time.Clock()

		self.time_passed_in_sec = 0

	def loop(self):
        self.time_passed_in_sec = self.clock.tick() / 1000.0
        self.update_all_position()
        for ball in balls:
        	self.check_if_ball_hit_edge(ball)
        	for bar in bars:
        		self.check_if_ball_hit_bar(bar)

    def update_all_position(self):
    	for ball in self.balls:
    		ball.update_position(self.time_passed_in_sec)
    	for bar in self.bars:
			bar.update_position(self.time_passed_in_sec)

	def check_if_ball_hit_edge(self, ball):
		# Left or Right Side
		if ball.current_pos_x < ball.size and ball.current_speed_x < 0: 
			ball.current_speed_x *= -1
		elif ball.current_pos_x > 1080-ball.size and ball.current_speed_x > 0:
			ball.current_speed_x *= -1
		# Up or Down Side
		if ball.current_pos_y < ball.size and ball.current_speed_y < 0
			ball.current_speed_y *= -1
		if ball.current_pos_y > 720-ball.size and ball.current_speed_y > 0:
			ball.current_speed_y *= -1

	def check_if_ball_hit_bar(self, ball, bar):
		if ball.pos_x < bar.pos_x + ball.size and ball.pos_x > bar.pos_x - bar_width and ball.pos_y > bar.pos_y - (bar.half_length + ball.size) and ball.pos_y < bar.pos_y + (bar.half_length + ball.size):
			if ball.current_speed_x < 0:
				ball.current_speed_x *= -1
			if ball.accel == True:
				ball.accel = False
		elif ball.pos_x > bar.pos_x - ball.size and ball.pos_x < bar.pos_x + bar.width and ball.pos_y > bar.pos_y - (bar.half_length + ball.size) and ball.pos_y < bar.pos_y + (bar.half_length + ball.size):
			if ball.current_speed_x > 0:
				ball.current_speed_x *= -1
			if ball.accel == True:
				ball.accel = False

class Survival():
	pass

class CatchBall():
	pass