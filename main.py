# Ping Pong Game

import pygame
import sys
import DrawGraph
from Screen import *
from util import quit_game

class GameState():
    START = 1
    HOMEPAGE = 2
    DUELMODE = 3
    OPTIONS = 4
    LOADING = 5
    GAMING = 6

    DEFAULT = 0

pygame.init()

screen = Screen()
screen.set_background('./images/tech_1080.bmp')

gamestate = GameState.START

while True:
    screen.display_background()
    if gamestate == GameState.START:
        screen.display_text("Ping Pong Game", COLOR.WHITE, 160, (100, 250))
        screen.display_text("Ver 2.00", COLOR.WHITE, 100, (400, 400))
        screen.display_text("Press any button to START", COLOR.WHITE, 40, (350, 500))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                else:
                    quit_game()
                    #gameState = GameState.HOMEPAGE
                    #cursor[0] = 0
    elif gamestate == GameState.HOMEPAGE:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                else:
                    quit_game()
                    #gameState = GameState.HOMEPAGE
                    #cursor[0] = 0
    pygame.display.update()

