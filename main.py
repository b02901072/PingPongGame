# Ping Pong Game

import pygame
from Screen import *
from Game import *
from util import *

class GameState():
    START = 1
    GAMEMODE = 2
    DUEL_SETTING = 3
    OPTIONS = 4
    LOADING = 5
    PREPARATION = 6
    INGAME = 7

    DEFAULT = 0

pygame.init()

screen = Screen()
screen.set_background('./images/tech_1080.bmp')
screen.set_top_margin('./images/960_60_tech.jpg')

gamestate = GameState.START

gamemode_select_list = SelectList(
    text=['Duel 1P', 'Duel 2P', 'Survival 1P', 'Survival 2P', 'CatchBall 1P', 'CatchBall 2P'],
    text_size=50,
    pos_x=80,
    pos_y_initial=150,
    pos_y_spacing=80,
    default_color=COLOR.WHITE,
    select_color=COLOR.YELLOW,
    cursor_icon='diamond',
    cursor_size=15,
)

duel_select_list = SelectList(
    text=['Laser', 'Acceleration', 'Invisibility', 'CrazyBounce', 'Gravity', 'Vibration', 'WormHole', 'Continue'],
    text_size=40,
    pos_x=80,
    pos_y_initial=120,
    pos_y_spacing=60,
    default_color=COLOR.WHITE,
    select_color=COLOR.YELLOW,
    cursor_icon='diamond',
    cursor_size=15,
    pos_x_last=900,
    pos_y_last=660,
)

while True:
    # 顯示背景
    screen.display_background()
    
    # 遊戲首頁
    if gamestate == GameState.START:
        screen.display_text('Ping Pong Game', COLOR.WHITE, 160, (100, 250))
        screen.display_text('Ver 2.00', COLOR.WHITE, 100, (400, 400))
        screen.display_text('Press any button to START', COLOR.WHITE, 40, (350, 500))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                else:
                    gamestate = GameState.GAMEMODE
    
    # 遊戲模式選擇：[Duel, Survival, CatchBall] [1P, 2P]
    elif gamestate == GameState.GAMEMODE:
        screen.display_text("Game Mode", COLOR.WHITE, 100, (30, 30))
        screen.display_select_list(gamemode_select_list)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_BACKSPACE:
                    gamestate = GameState.START
                elif events.key == pygame.K_UP or events.key == pygame.K_w:
                    gamemode_select_list.move_cursor(-1)
                elif events.key == pygame.K_DOWN or events.key == pygame.K_s:
                    gamemode_select_list.move_cursor(1)
                elif events.key == pygame.K_RETURN or events.key == pygame.K_SPACE:
                    cursor = gamemode_select_list.cursor_index
                    if cursor == 0:
                        gamemode = 'duel'
                        gamestate = GameState.DUEL_SETTING
    
    # DUEL模式遊戲設定
    elif gamestate == GameState.DUEL_SETTING:
        screen.display_text('Duel', COLOR.WHITE, 100, (30, 30))
        screen.display_select_list(duel_select_list)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_BACKSPACE:
                    gamestate = GameState.GAMEMODE
                elif events.key == pygame.K_UP or events.key == pygame.K_w:
                    duel_select_list.move_cursor(-1)
                elif events.key == pygame.K_DOWN or events.key == pygame.K_s:
                    duel_select_list.move_cursor(1)
                elif events.key == pygame.K_RETURN or events.key == pygame.K_SPACE:
                    cursor = duel_select_list.cursor_index
                    if cursor == duel_select_list.len-1:
                        gamestate = GameState.PREPARATION
    
    # 準備階段
    elif gamestate == GameState.PREPARATION:
        screen.display_text('Press SPACE to start the game.', COLOR.WHITE, 50, (300, 400))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_SPACE:
                    gamestate = GameState.INGAME
                    game = Duel()
    
    # 正式遊戲
    elif gamestate == GameState.INGAME:
        #screen.display_top_margin()
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                if events.key == pygame.K_w:
                    bars[0].dir_y = -1
                elif events.key == pygame.K_s:
                    bars[0].dir_y = 1
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_w or events.key == pygame.K_s:
                    bars[0].dir_y = 0

        game.loop()
        screen.display_game(game)

    # 更新遊戲畫面
    pygame.display.update()

