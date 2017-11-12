#           Rainbow morph
#           Finished 041117
#           Found a buggy sine function online and fixed it to get smooth sines
#           Creation of sine tables is a bit messy but it works and is easy to follow
#           Python 3 and Pygame


import pygame
import os
from pygame.locals import *
import random
import math

pygame.init()

winwidth = 1920
winheight = 1080
screen = pygame.display.set_mode((winwidth, winheight), FULLSCREEN | DOUBLEBUF)
screen.convert()
pygame.mouse.set_visible(False)
screen.fill((0, 0, 0))
pygame.display.update()

background = pygame.image.load("Space2.png").convert()
# background = background.convert()

''' Generate sine '''


class Cosinus:
    def __init__(self, lenght, low, high):
        '''
        :param lenght: = lenght of sinus table
        :param low: = lowest sinus value
        :param high: = highest sinus value
        '''

        self.lenght = lenght
        self.low = low
        self.high = high
        self.cos_table = []

    def rescale(X, A, B, C, D, force_float=True):
        retval = ((float(X - A) / (B - A)) * (D - C)) + C
        if not force_float and all(map(lambda x: type(x) == int, [X, A, B, C, D])):
            return int((retval))
        return retval

    def calc(self):
        ## Angles in degrees for which to calculate sine
        angles = [Cosinus.rescale(i, 0, self.lenght, 0, 360) for i in range(self.lenght)]
        self.cos_table = [int((Cosinus.rescale(s, -1, 1, self.low, self.high))) for s in
                          [math.cos(math.radians(a)) for a in angles]]
        return self.cos_table


class Sinus:
    def __init__(self, lenght, low, high):
        '''
        :param lenght: = lenght of sinus table
        :param low: = lowest sinus value
        :param high: = highest sinus value
        '''

        self.lenght = lenght
        self.low = low
        self.high = high
        self.sin_table = []

    def rescale(X, A, B, C, D, force_float=True):
        retval = ((float(X - A) / (B - A)) * (D - C)) + C
        if not force_float and all(map(lambda x: type(x) == int, [X, A, B, C, D])):
            return int((retval))
        return retval

    def calc(self):
        # Angles in degrees for which to calculate sine
        angles = [Sinus.rescale(i, 0, self.lenght, 0, 360) for i in range(self.lenght)]
        self.sin_table = [int((Sinus.rescale(s, -1, 1, self.low, self.high))) for s in
                          [math.sin(math.radians(a)) for a in angles]]
        return self.sin_table


m = Sinus(random.randint(winwidth, winwidth * 2), 0, winwidth / 2)
x1 = m.calc()

m = Sinus(random.randint(winwidth, winwidth * 2), 0, winwidth / 2)
x2 = m.calc()

m = Sinus(random.randint(winwidth, winwidth * 2), 0, winwidth / 2)
x3a = m.calc()
m = Sinus(random.randint(winwidth, winwidth * 2), 0, winwidth / 2)
x3b = m.calc()
x3 = x3a + x3b

m = Cosinus(random.randint(winheight, winheight * 2), 0, winheight / 2)
y1 = m.calc()

m = Cosinus(random.randint(winheight, winheight * 2), 0, winheight / 2)
y2 = m.calc()

m = Cosinus(random.randint(winheight, winheight * 2), 0, winheight / 2)
y3a = m.calc()
m = Cosinus(random.randint(winheight, winheight * 2), 0, winheight / 2)
y3b = m.calc()

y3 = y3a + y3b

maxx1 = len(x1)
maxx2 = len(x2)
maxx3 = len(x3)
maxy1 = len(y1)
maxy2 = len(y2)
maxy3 = len(y3)

m = Sinus(random.randint(768, 1024), 0, 255)
color1 = m.calc()

m = Sinus(random.randint(1024, 1368), 0, 255)
color2 = m.calc()

m = Sinus(random.randint(1368, 1920), 0, 255)
color3 = m.calc()

lines = 1
maxlines = 750
maxcolor1 = len(color1)
maxcolor2 = len(color2)
maxcolor3 = len(color3)
aurora = []


#         Classes

class Aurora:
    def __init__(self, x1, y1, x2, y2, x3, y3, color1, color2, color3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def move(self):

        if self.x1 == maxx1:
            self.x1 = 0
        if self.x2 == maxx2:
            self.x2 = 0
        if self.x3 == maxx3:
            self.x3 = 0
        if self.y1 == maxy1:
            self.y1 = 0
        if self.y2 == maxy2:
            self.y2 = 0
        if self.y3 == maxy3:
            self.y3 = 0
        if self.color1 == maxcolor1:
            self.color1 = 0
        if self.color2 == maxcolor2:
            self.color2 = 0
        if self.color3 == maxcolor3:
            self.color3 = 0

        pygame.draw.line(screen, (color1[self.color1], color2[self.color2], color3[self.color3]),
                         (x1[self.x1] + x3[self.x3], y1[self.y1] + y3[self.y3]),
                         (x2[self.x2] + x3[self.x3], y2[self.y2] + y3[self.y3]), 5)

        self.x1 += 1
        self.x2 += 1
        self.x3 += 1
        self.y1 += 1
        self.y2 += 1
        self.y3 += 1
        self.color1 += 1
        self.color2 += 1
        self.color3 += 1


''' Setting up variables and screen '''

for i in range(0, maxlines):
    aurora.append(Aurora(i, i, i, i, i,
                         i, i, i, i))

clock = pygame.time.Clock()

running = True

'''  Main loop '''

while running:
    clock.tick(120)
    # screen.fill((0, 0, 0))
    screen.blit((background), (0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        running = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    for line in aurora:
        line.move()

    pygame.display.update()
pygame.quit()
