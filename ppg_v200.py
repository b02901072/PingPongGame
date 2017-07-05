#-----PingPongGame-----#
#-------Ver 2.00-------#
import pygame, sys, math, string, random
import os
import DrawGraph
from util import *
#import pygame.freetype

from Screen import *
pygame.init()



screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#---Images Loading
images_dir = './images/'
background = pygame.image.load("./images/tech_1080.bmp").convert()
duelBackground = pygame.image.load("./images/tech_540.bmp").convert()

def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def biReturn(condition, do1, do2):
    if condition:
        return do1
    else:
        return do2

def triReturn(condition1, do1, condition2, do2, do3):
    if condition1:
        return do1
    elif condition2:
        return do2
    else:
        return do3
from enum import Enum
class GameState(Enum):
    START = 1
    HOMEPAGE = 2
    DUELMODE = 3
    OPTIONS = 4
    LOADING = 5
    GAMING = 6

    DEFAULT = 0

class Text:
    def __init__(self, size, color, posX, posY):
        self._size = size
        self._color = color
        self._posX = posX
        self._posY = posY
        self._content = ""

    def setContent(self, content):
        self._content = content

#---Color Defenition
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRAY = 150, 150, 150
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = 255, 255, 0

BORDER = 0, 0
TITLE = 30, 30

cursor = [0]

duelModeNum = 7
duelText = [0, 0, 0, 0, 0, 0, 0]
duelText[0] = [["Effect :", "Off", "On"]]
duelText[1] = [["Effect :", "Off", "On"], ["TEST2 :", "A", "B", "C"], ["WOWOW:", "A", "B"]]
duelText[2] = [["Effect :", "Off", "On"], ["TEST3 :", "A", "B", "C"]]
duelText[3] = [["Effect :", "Off", "On"], ["TEST4 :", "A", "B", "C"]]
duelText[4] = [["Effect :", "Off", "On"], ["TEST5 :", "A", "B", "C"]]
duelText[5] = [["Effect :", "Off", "On"], ["TEST6 :", "A", "B", "C"]]
duelText[6] = [["Effect :", "Off", "On"], ["TEST7 :", "A", "B", "C"]]
duelSetting = [0, 0, 0, 0, 0, 0, 0]
duelSetting[0] = [0]
duelSetting[1] = [0, 0, 0]
duelSetting[2] = [0, 0]
duelSetting[3] = [0, 0]
duelSetting[4] = [0, 0]
duelSetting[5] = [0, 0]
duelSetting[6] = [0, 0]

loadPercentage = 0
loadBarLength = 0
loadTime = 0

FONT_40 = pygame.font.Font(None, 40)
FONT_50 = pygame.font.Font(None, 50)
FONT_60 = pygame.font.Font(None, 60)
FONT_80 = pygame.font.Font(None, 80)
FONT_100 = pygame.font.Font(None, 100)
FONT_160 = pygame.font.Font(None, 160)

gameState = GameState.START

while True:
    screen.blit(background, BORDER)
    if gameState == GameState.START:
        screen.blit(FONT_160.render("Ping Pong Game", True, WHITE), (100, 250))
        screen.blit(FONT_100.render("Ver 2.00", True, WHITE), (400, 400))
        screen.blit(FONT_40.render("Press any button to START", True, WHITE), (350, 500))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                else:
                    gameState = GameState.HOMEPAGE
                    cursor[0] = 0
    if gameState == GameState.HOMEPAGE:
        screen.blit(FONT_100.render("PingPongGame", True, WHITE), TITLE)
        homePageText = ["Duel 1P", "Duel 2P", "Survival 1P", "Survival 2P", "CatchBall 1P", "CatchBall 2P"]
        textYPos, textColor = [], []
        for i in range(0, 6):
            textYPos.append(150 + 80 * i)
            textColor.append(WHITE)
        textColor[cursor[0]] = YELLOW
        for i in range(0, 6):
            screen.blit(FONT_50.render(homePageText[i], True, textColor[i]), (80, textYPos[i]))
        DrawGraph.diamond(screen, 15, 15, 80 - 25, textYPos[cursor[0]] + 15, YELLOW)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_BACKSPACE:
                    gameState = GameState.START
                elif events.key == pygame.K_UP or events.key == pygame.K_s:
                    cursor[0] = (cursor[0] - 1) % 6
                elif events.key == pygame.K_DOWN or events.key == pygame.K_w:
                    cursor[0] = (cursor[0] + 1) % 6
                elif events.key == pygame.K_RETURN or events.key == pygame.K_SPACE:
                    if cursor[0] == 0 or cursor[0] == 1:
                        gameState = GameState.DUELMODE
                        cursor = [0, 0, 0]
    if gameState == GameState.DUELMODE:
        screen.blit(duelBackground, (400, 50))
        screen.blit(FONT_100.render("Duel", True, WHITE), TITLE)
        duelModeText = ["Laser", "Acceleration", "Invisbility", "CrazyBounce", "Gravity", "Vibration", "WormHole"]
        textYPos, textColor = [], []
        for i in range(0, duelModeNum):
            textYPos.append(120 + 60 * i)
            textColor.append(WHITE)
        textColor.append(WHITE)
        if cursor[0] == 0:
            if cursor[2] == 0:
                textColor[cursor[1]] = YELLOW
            DrawGraph.diamond(screen, 15, 15, 80 - 25, textYPos[cursor[1]] + 10, YELLOW)
        else:
            textColor[duelModeNum] = YELLOW
            DrawGraph.diamond(screen, 15, 15, 900 - 25, 660 + 10, YELLOW)
        for i in range(0, duelModeNum):
            color = biReturn(duelSetting[i][0] == 1, GREEN, textColor[i])
            screen.blit(FONT_40.render(duelModeText[i], True, color), (80, textYPos[i]))
        screen.blit(FONT_40.render("Continue", True, textColor[duelModeNum]), (900, 660))
        for i in range(0, len(duelText[cursor[1]])):
            textColor1 = biReturn(duelSetting[cursor[1]][0] == 0, GRAY, WHITE)
            text1 = FONT_60.render(duelText[cursor[1]][i][0], True, textColor1)
            screen.blit(text1, (460, 440 + 60 * i))
            textColor2 = triReturn(cursor[2] == i + 1 and cursor[0] == 0, YELLOW, duelSetting[cursor[1]][0] == 0, GRAY, WHITE)
            text2 = FONT_60.render(duelText[cursor[1]][i][duelSetting[cursor[1]][i] + 1], True, textColor2)
            screen.blit(text2, (740, 440 + 60 * i))
        if cursor[0] == 0 and cursor[2] != 0:
            DrawGraph.leftTri(screen, 15, 20, 700, 400 + 60 * cursor[2], YELLOW)
            DrawGraph.rightTri(screen, 15, 20, 900, 400 + 60 * cursor[2], YELLOW)
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_BACKSPACE:
                    if cursor[0] == 1:
                        cursor[0] = 0 
                    elif cursor[2] == 0:
                        gameState = GameState.HOMEPAGE
                        cursor = [0]
                    else:
                        cursor[2] = 0
                elif events.key == pygame.K_RETURN: 
                    if cursor[0] == 1:
                        gameState = GameState.OPTIONS
                        cursor = [1, 0, 0]
                    elif cursor[2] == 0:
                        cursor[2] = 1
                    else:
                        cursor[0] = 1
                elif events.key == pygame.K_UP or events.key == pygame.K_w:
                    if cursor[0] == 0:
                        if cursor[2] == 0:                        
                            cursor[1] = (cursor[1] - 1) % duelModeNum
                        elif duelSetting[cursor[1]][0] == 1:
                            cursor[2] = ((cursor[2] - 1 - 1) % len(duelText[cursor[1]])) + 1
                elif events.key == pygame.K_DOWN or events.key == pygame.K_s:
                    if cursor[0] == 0:                    
                        if cursor[2] == 0:                        
                            cursor[1] = (cursor[1] + 1) % duelModeNum
                        elif duelSetting[cursor[1]][0] == 1:
                            cursor[2] = ((cursor[2] - 1 + 1) % len(duelText[cursor[1]])) + 1
                elif events.key == pygame.K_LEFT or events.key == pygame.K_a:
                    if cursor[0] == 0:
                        if cursor[2] > 0:                    
                            duelSetting[cursor[1]][cursor[2] - 1] -= 1
                            duelSetting[cursor[1]][cursor[2] - 1] %= len(duelText[cursor[1]][cursor[2] - 1]) - 1
                    else:
                        cursor[0] = 0
                        cursor[2] = 0
                elif events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                    if cursor[0] == 0:
                        if cursor[2] > 0:
                            duelSetting[cursor[1]][cursor[2] - 1] += 1
                            duelSetting[cursor[1]][cursor[2] - 1] %= len(duelText[cursor[1]][cursor[2] - 1]) - 1
                        else:
                            cursor[0] = 1
                
    if gameState == GameState.OPTIONS:
        screen.blit(FONT_100.render("Options", True, WHITE), TITLE)
        optionsText = ["Ball", "Bar", "Control", "Difficulty", "Start"]
        textYos, textColor = [], []
        for i in range(0, 4):
            textYPos.append(240 + 60 * i)
            textColor.append(WHITE)
        textColor.append(WHITE)
        if cursor[0] == 0:
            textColor[cursor[1]] = YELLOW
            DrawGraph.diamond(screen, 15, 15, 80 - 25, textYPos[cursor[1]] + 10, YELLOW)
        else:
            textColor[4] = YELLOW
            DrawGraph.diamond(screen, 15, 15, 900 - 30, 660 + 10, YELLOW)
        for i in range(0, 4):
            screen.blit(FONT_40.render(optionsText[i], True, textColor[i]), (80, textYPos[i]))
        screen.blit(FONT_60.render("Start", True, textColor[4]), (900, 650))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_BACKSPACE:
                    gameState = GameState.DUELMODE
                elif events.key == pygame.K_RETURN:
                    if cursor[0] == 1:
                        gameState = GameState.LOADING
                        loadTime = 0
                        loadBarLength = 0
                        loadPercentage = 0
                        loadTimer = pygame.time.Clock()
                elif events.key == pygame.K_UP or events.key == pygame.K_w:
                    if cursor[0] == 0:
                        cursor[1] = (cursor[1] - 1) % 4
                elif events.key == pygame.K_DOWN or events.key == pygame.K_s:
                    if cursor[0] == 0:
                        cursor[1] = (cursor[1] + 1) % 4
                elif events.key == pygame.K_LEFT or events.key == pygame.K_a:
                    cursor[0] = 0
                elif events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                    cursor[0] = 1
    if gameState == GameState.LOADING:
        r = random.random() * 7
        t = loadTimer.tick()
        loadTime += t
        if r < 3:
            loadPercentage += t
        elif r < 4:
            loadPercentage += 2 * t
        elif r < 4.5:
            loadPercentage += 20 * t
        elif r < 4.6:
            loadPercentage += 100 * t
        loadText = ["Loading.", "Loading..", "Loading...", "Loading"]
        if loadBarLength < 800:
            loadBarLength = (8 * loadPercentage) / 500
            DrawGraph.rim(screen, 132 - 2, 932 + 2, 400, 500, 4, WHITE)
            pygame.draw.line(screen, BLUE, (132 + 2, 450), (132 + loadBarLength, 450), 100 - 4)
            screen.blit(FONT_80.render("%d"%(loadBarLength/8), True, WHITE), (500, 420))
            screen.blit(FONT_100.render(loadText[(loadTime / 1000) % 4], True, WHITE), (390, 300))
        else:
            screen.blit(FONT_50.render("Press any button to Start", True, WHITE), (400 , 350))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
                elif events.key == pygame.K_l or loadBarLength >= 800:
                    gameState = GameState.GAMING
    if gameState == GameState.GAMING:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    quit_game()
    pygame.display.update()
