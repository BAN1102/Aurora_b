#
#       Aurora_b
#       This is a rework of a old project written in Euphoria around 10 years ago
#       It is mostly a learning process in how Python handle stuff
#       Python 3.6 and Pygame.
#       To do:
#               Remove all glitches without slowing the code
#               Make some sort of mutation routine when conditions are right
#               Add user input
#               Everything is working so it might stay as is....
#               Could do a rewrite in Pyglet or Kivy...
#



import math
import random
import pygame
from pygame.locals import *

''' Variables and constants '''

lines = 1           # Do not touch
maxlines = 950      # Number of lines in the object
mincolor = maxlines # Making sure we have enough colors for all lines

''' Setting up screen '''

pygame.init()
winwidth = 1920
winheight = 1080
screen = pygame.display.set_mode((winwidth, winheight), FULLSCREEN | DOUBLEBUF)
screen.convert()
pygame.mouse.set_visible(False)
screen.fill((0, 0, 0))
pygame.display.update()

background = pygame.image.load("Space2.png").convert()

''' Generate sin an cos '''


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
        # Angles in degrees for which to calculate cosinus
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
        # Angles in degrees for which to calculate sinus
        angles = [Sinus.rescale(i, 0, self.lenght, 0, 360) for i in range(self.lenght)]
        self.sin_table = [int((Sinus.rescale(s, -1, 1, self.low, self.high))) for s in
                          [math.sin(math.radians(a)) for a in angles]]
        return self.sin_table

''' Making sinus and cosinus lists '''

m = Sinus(random.randint(winwidth, winwidth * 2), 0, winwidth / 2)
x1 = m.calc()

m = Sinus(random.randint(winwidth, winwidth * 2), 0, winwidth / 2)
x2 = m.calc()

m = Sinus(random.randint(winwidth*2, winwidth * 3), 0, winwidth / 2)
x3 = m.calc()


m = Cosinus(random.randint(winheight, winheight * 2), 0, winheight / 2)
y1 = m.calc()

m = Cosinus(random.randint(winheight, winheight * 2), 0, winheight / 2)
y2 = m.calc()

m = Cosinus(random.randint(winheight*2, winheight * 3), 0, winheight / 2)
y3 = m.calc()

maxx1 = len(x1)
maxx2 = len(x2)
maxx3 = len(x3)
maxy1 = len(y1)
maxy2 = len(y2)
maxy3 = len(y3)

''' Adding colors '''

m = Sinus(random.randint(mincolor, mincolor*2), 0, 255)
color1 = m.calc()

m = Sinus(random.randint(mincolor*2, mincolor*3), 0, 255)
color2 = m.calc()

m = Sinus(random.randint(mincolor*3, mincolor*4), 0, 255)
color3 = m.calc()


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
