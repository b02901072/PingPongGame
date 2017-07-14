import random
import math
from util import *

class Ball():
    def __init__(self, 
        index=0, size=16,
        default_color=COLOR.GREEN, accel_color=COLOR.RED,
        speed_x=300, speed_y=300,
        pos_x=540, pos_y=360):

        self.index = index
        self.default_color = default_color
        self.accel_color = accel_color
        self.size = size
        self.initial_speed_x = speed_x
        self.initial_speed_y = speed_y
        self.current_speed_x = speed_x
        self.current_speed_y = speed_y
        self.dir_x = 0
        self.dir_y = 0
        self.random_direction()
        self.initial_pos_x = pos_x
        self.initial_pos_y = pos_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self.accel = False

        self.invisible = False

        self.bounce_timer = 0
        self.bounce_timeout = 0.1

        self.wormhole_timer = 0
        self.wormhole_timeout = 0.3

    def update(self, time_in_sec):
        self.pos_x += self.current_speed_x * time_in_sec * self.dir_x
        self.pos_y += self.current_speed_y * time_in_sec * self.dir_y
        self.bounce_timer -= time_in_sec
        self.wormhole_timer -= time_in_sec
        if self.bounce_timer < 0:
            self.bounce_timer = 0
        if self.wormhole_timer < 0:
            self.wormhole_timer = 0
        '''
        if self.pos_x > 0.3*1080 and self.pos_x < 0.7*1080:
            self.invisible = True
        else:
            self.invisible = False
        '''

    def reset(self):
        self.pos_x = self.initial_pos_x
        self.pos_y = self.initial_pos_y
        self.dir_x = 1
        self.dir_y = 1
        self.bounce_timer = 0

    def random_direction(self, start=30, end=60):
        angle = random.randint(30, 60)
        dx = posi_or_nega(self.dir_x)
        dy = posi_or_nega(self.dir_y)
        self.dir_x = math.sqrt(2)*math.cos(angle*math.pi/180.0) * dx
        self.dir_y = math.sqrt(2)*math.sin(angle*math.pi/180.0) * dy

    def normal_bounce_x(self):
        if self.bounce_timer == 0:
            self.dir_x *= -1
            if self.accel == True:
                self.accel = False
            self.set_bounce_timer()

    def crazy_bounce_x(self):
        if self.bounce_timer == 0:
            self.dir_x *= -1
            r = random.randint(1,2)
            if r == 1:
                self.dir_y *= -1
            self.random_direction()
            if self.accel == True:
                self.accel = False
            self.set_bounce_timer()

    def normal_bounce_y(self):
        if self.bounce_timer == 0:
            self.dir_y *= -1
            if self.accel == True:
                self.accel = False
            self.set_bounce_timer()

    def crazy_bounce_y(self):
        if self.bounce_timer == 0:
            self.dir_y *= -1
            r = random.randint(1,2)
            if r == 1:
                self.dir_x *= -1
            self.random_direction()
            if self.accel == True:
                self.accel = False
            self.set_bounce_timer()

    def set_bounce_timer(self):
        self.bounce_timer = self.bounce_timeout

    def set_wormhole_timer(self):
        self.wormhole_timer = self.wormhole_timeout
    
