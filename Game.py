import pygame
from Ball import *
from Bar import *

class WormHole():

    def __init__(self,
        pos_x=270,
        pos_y=360,
        size=75):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

class Duel():

    def __init__(self, player2='ai'):

        self.ball_num = 1
        self.balls = []
        for i in range(self.ball_num):
            self.balls.append(Ball())

        self.bars = [Bar(index=0, color=COLOR.BLUE, pos_x=80), Bar(1, color=COLOR.RED, pos_x=1000)]
        self.clock = pygame.time.Clock()

        self.score_1, self.score_2 = 0, 0
        self.scorer = None
        self.win_score = 5
        self.winner = None
        self.timeout = False

        self.time_passed_in_sec = 0

        self.is_crazybounce_on = False
        self.is_wormhole_on = True
        self.wormholes = [WormHole(270, 360), WormHole(810, 360)]

    def start_clock(self):
        self.clock.tick()

    def new_game(self):
        self.scorer = None
        self.timeout = False
        self.time_passed_in_sec = 0
        for bar in self.bars:
            bar.reset()
        for ball in self.balls:
            ball.reset()

    def loop(self):
        self.time_passed_in_sec = self.clock.tick() / 1000
        self.update()
        for bar in self.bars:
            self.check_if_bar_hit_edge(bar)
        for ball in self.balls:
            self.check_if_ball_hit_edge(ball)
            self.check_if_ball_hit_wormholes(ball)
            for bar in self.bars:
                self.check_if_ball_hit_bar(ball, bar)
        self.check_winner()
        return self.check_if_scored()

    def update(self):
        for ball in self.balls:
            ball.update(self.time_passed_in_sec)
        for bar in self.bars:
            bar.update(self.time_passed_in_sec)

    def check_if_scored(self):
        return self.scorer is not None

    def check_winner(self):
        if self.score_1 >= self.win_score:
            self.winner = 1
        elif self.score_2 >= self.win_score:
            self.winner = 2

    def check_if_ball_hit_edge(self, ball):
        # Left or Right Side
        if ball.pos_x < ball.size and ball.dir_x < 0: 
            self.scorer = 2
            self.score_2 += 1
        elif ball.pos_x > 1080-ball.size and ball.dir_x > 0:
            self.scorer = 1
            self.score_1 += 1
        # Up or Down Side
        if ball.pos_y < ball.size and ball.dir_y < 0:
            if self.is_crazybounce_on == True:
                ball.crazy_bounce_y()
            else:
                ball.normal_bounce_y()
        elif ball.pos_y > 720-ball.size and ball.dir_y > 0:
            if self.is_crazybounce_on == True:
                ball.crazy_bounce_y()
            else:
                ball.normal_bounce_y()

    def check_if_bar_hit_edge(self, bar):
        if bar.pos_y < 0.5*bar.length:
            bar.pos_y = 0.5*bar.length
        elif bar.pos_y > 720 - 0.5*bar.length:
            bar.pos_y = 720 - 0.5*bar.length

    def check_if_ball_hit_bar(self, ball, bar):
        if ball.pos_x < (bar.pos_x+ball.size+0.5*bar.width) and ball.pos_x > (bar.pos_x-ball.size-0.5*bar.width) and ball.pos_y > (bar.pos_y-0.5*bar.length-ball.size) and ball.pos_y < (bar.pos_y+0.5*bar.length+ball.size):
            if self.is_crazybounce_on == True:
                ball.crazy_bounce_x()
            else:
                ball.normal_bounce_x()

    def check_if_ball_hit_wormholes(self, ball):
        if ball.wormhole_timer != 0:
            return
        for wh in self.wormholes:
            if distance(ball, wh) < wh.size:
                print('wormhole')
                ball.wormhole_timer = 0.5

class Survival():
    pass

class CatchBall():
    pass