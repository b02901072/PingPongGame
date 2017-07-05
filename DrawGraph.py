import pygame

def leftTri(screen, l, h, x, y, color):
#             /|
#            / |
#           /  |
#          /   |
#         /    |
#        /     |
#       /      | h
#      /       |
#     /        |
#    /         |
#   /          |
#  /     l     |
# /____________|y
# \            |
#  \           |
#   \          |
#    \         |
#     \        |
#      \       |
#       \      | h
#        \     |
#         \    |
#          \   |
#           \  |
#            \ |
#             \|
#              x
#
    i = x
    for i in range(x - l, x):
        k = int (h * (i - x + l) / l)
        pygame.draw.line(screen, color, (i, y - k), (i, y + k), 1)

def rightTri(screen, l, h, x, y, color):
# |\
# | \
# |  \
# |   \
# |    \
# |     \
# |      \
# | h     \
# |        \
# |         \
# |          \
# |     l     \
# |____________\ y
# |            /
# |           /
# |          /
# |         /
# |        /
# | h     /
# |      /
# |     /
# |    /
# |   /
# |  /
# | /
# |/
# x
#
    i = x
    for i in range(x, x + l):
        k = int (h * (x + l - i) / l)
        pygame.draw.line(screen, color, (i, y - k), (i, y + k), 1)

def diamond(screen, l, h, x, y, color):
    leftTri(screen, l, h, x, y, color)
    rightTri(screen, l, h, x, y, color)

def rim(screen, x1, x2, y1, y2, d, color):
    pygame.draw.line(screen, color, (x1, y1), (x2, y1), d)
    pygame.draw.line(screen, color, (x2, y1), (x2, y2 + d/2), d)
    pygame.draw.line(screen, color, (x2, y2), (x1, y2), d)
    pygame.draw.line(screen, color, (x1, y2 + d/2), (x1, y1), d)
