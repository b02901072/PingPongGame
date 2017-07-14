import random

class WormHole():

    def __init__(self,
        pos_x=270, pos_y=360,
        size=75):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def random_pos_y(self):
        self.pos_y = random.randint(0+self.size, 720-self.size)        

class Laser():

    def __init__(self,
        pos_y=360):
        
        self.pos_y = pos_y
        self.phase = 0
        self.timer = 0

    def random_pos_y(self):
        r = random.randint(0, 1)
        self.pos_y = random.randint(100, 620)

    def update(self, time_in_sec):
        self.timer -= time_in_sec
        if self.timer < 0:
            self.timer = 0
        if self.timer == 0:
            if self.phase == 0:
                self.random_pos_y()
                self.phase = 1
                self.timer = 3
            elif self.phase == 1:
                self.phase = 2
                self.timer = 0.5
            elif self.phase == 2:
                self.phase = 0
                self.timer = 4

def Fog():

    def __init__(self,
        pos_x=0, pos_y=0,
        width=0, height=0,):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height