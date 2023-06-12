import os
import time
from termcolor import colored
import math 


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.05
        self.pos = [0, 0]

        self.direction = [0, 1]

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]
    
    def setPosition(self, position):
        self.pos = position

    def up(self):
        self.direction = [0, -1]
        self.forward()

    def down(self):
        self.direction = [0, 1]
        self.forward()

    def right(self):
        self.direction = [1, 0]
        self.forward()

    def left(self):
        self.direction = [-1, 0]
        self.forward()

    def forward(self):
        pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)

canvas = Canvas(50, 50)

scribeDicts = [{'degrees': 12, 'position': [5, 5], 'instructions': [('forward', 5), ('right', 3)]},
               {'degrees': 45, 'position': [1, 1], 'instructions': [('down', 2), ('right', 2)]},
               {'degrees': 90, 'position': [10, 10], 'instructions': [('left', 9), ('right', 3)]}]

for dict in scribeDicts:
    dict['scribe'] = TerminalScribe(canvas)
    dict['scribe'].setDegrees(dict['degrees'])
    dict['scribe'].setPosition(dict['position'])
    
    instructions = dict['instructions']
    for pair in instructions:
        if pair[0] == 'forward':
            for i in range(pair[1]):
                dict['scribe'].forward()
        elif pair[0] == 'up':
            for i in range(pair[1]):
                dict['scribe'].up()
        elif pair[0] == 'down':
            for i in range(pair[1]):
                dict['scribe'].down()
        elif pair[0] == 'left':
            for i in range(pair[1]):
                dict['scribe'].left()
        elif pair[0] == 'right':
            for i in range(pair[1]):
                dict['scribe'].right()


scribe = TerminalScribe(canvas)
scribe.setDegrees(135)
for i in range(25):
    scribe.forward()
    
scribe = TerminalScribe(canvas)
scribe.drawSquare(15)

