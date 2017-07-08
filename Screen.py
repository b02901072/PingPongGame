import pygame
from util import *

class Screen():

    def __init__(self, scale=1.0):

        self.scale = 1.0
        self.width = int(1080*scale)
        self.height = int(720*scale)
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        # IMAGES SETTING
        self.background = pygame.image.load('images/tech_1080.bmp').convert()
        self.top_margin = pygame.image.load('images/960_60_tech.jpg').convert()
        self.wormhole_100 = pygame.image.load('images/100_blackhole_light.png').convert_alpha()
        self.wormhole_150 = pygame.transform.scale(self.wormhole_100, (150, 150))

    # DISPLAY FUNCTION
    def display_background(self):
        self.screen.blit(self.background, (0, 0))

    def display_top_margin(self):
        self.screen.blit(self.top_margin, (0, 0))

    def display_text(self, text, color, size, position):
        x = int(position[0] * self.scale)
        y = int(position[1] * self.scale)
        s = int(size * self.scale)
        self.screen.blit(pygame.font.Font(None, s).render(text, True, color), (x, y))

    def display_select_list(self, select_list):
        for i in range(select_list.len):
            text = select_list.text[i]
            pos_x = select_list.pos_x[i]
            pos_y = select_list.pos_y[i]
            color = select_list.color[i]
            text_size = select_list.text_size[i]
            self.display_text(text, color, text_size, (pos_x, pos_y))
            if i == select_list.cursor_index:
                cursor_size = select_list.cursor_size
                self.display_diamond(cursor_size, cursor_size, pos_x - 25, pos_y + 1/4*text_size, color)

    def display_game(self, game):
        
        if game.is_wormhole_on == True:
            for wh in game.wormholes:
                pos_x = int(wh.pos_x*self.scale)
                pos_y = int(wh.pos_y*self.scale)
                size = int(wh.size*self.scale)
                #pygame.draw.circle(self.screen, COLOR.WHITE, (pos_x, pos_y), 52, 0)
                self.screen.blit(self.wormhole_150, (pos_x-0.5*size, pos_y-0.5*size))

        for ball in game.balls:
            self.display_ball(ball)
        for bar in game.bars:
            self.display_bar(bar)

    def display_ball(self, ball):
        if ball.accel == True:
            color = ball.accel_color
        else:
            color = ball.default_color
        pos_x = int(ball.pos_x * self.scale)
        pos_y = int(ball.pos_y * self.scale)
        size = int(ball.size * self.scale)
        pygame.draw.circle(self.screen, color, (pos_x, pos_y), size, 0)

    def display_bar(self, bar):
        color = bar.color
        pos_x = int(bar.pos_x * self.scale)
        pos_y = int(bar.pos_y * self.scale)
        half_length = int(0.5*bar.length * self.scale)
        width = int(bar.width * self.scale)
        pygame.draw.line(self.screen, color, (pos_x, pos_y-half_length), (pos_x, pos_y+half_length), width)

    def display_left_tri(self, l, h, x, y, color):
        '''
                      x
                     /|
                    / |
                   /  |
                  /   |
                 /    |
                /     |
               /      | h
              /       |
             /        |
            /         |
           /          |
          /     l     |
         /____________|y
         \            |
          \           |
           \          |
            \         |
             \        |
              \       |
               \      | h
                \     |
                 \    |
                  \   |
                   \  |
                    \ |
                     \|
                      x
        '''
        i = x
        for i in range(x - l, x):
            k = int (h * (i - x + l) / l)
            pygame.draw.line(self.screen, color, (i, y - k), (i, y + k), 1)

    def display_right_tri(self, l, h, x, y, color):
        '''
         x  
         |\
         | \
         |  \
         |   \
         |    \
         |     \
         |      \
         | h     \
         |        \
         |         \
         |          \
         |     l     \
         |____________\ y
         |            /
         |           /
         |          /
         |         /
         |        /
         | h     /
         |      /
         |     /
         |    /
         |   /
         |  /
         | /
         |/
         x
        '''
        i = x
        for i in range(x, x + l):
            k = int (h * (x + l - i) / l)
            pygame.draw.line(self.screen, color, (i, y - k), (i, y + k), 1)

    def display_diamond(self, l, h, x, y, color):
        self.display_left_tri(l, h, x, y, color)
        self.display_right_tri(l, h, x, y, color)

def rim(screen, x1, x2, y1, y2, d, color):
    pygame.draw.line(screen, color, (x1, y1), (x2, y1), d)
    pygame.draw.line(screen, color, (x2, y1), (x2, y2 + d/2), d)
    pygame.draw.line(screen, color, (x2, y2), (x1, y2), d)
    pygame.draw.line(screen, color, (x1, y2 + d/2), (x1, y1), d)


