import os
import time
from termcolor import colored
import math 


class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsVerticalWall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x

    def hitsHorizontalWall(self, point):
        return round(point[1]) < 0 or round(point[1]) >= self._y

    def hitsWall(self, point):
        return self.hitsVerticalWall(point) or self.hitsHorizontalWall(point)

    def getReflection(self, point):
        return [-1 if self.hitsVerticalWall(point) else 1, -1 if self.hitsHorizontalWall(point) else 1]

    def setPos(self, pos, mark):
        self._canvas[round(pos[0])][round(pos[1])] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class Scribe:
    def __init__(self, canvas, framerate=0.05, startPosition=[0,0], trailColour='white', markColour = 'red'):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = framerate
        self.pos = startPosition
        self.trailColour = trailColour
        self.markColour = markColour
        self.direction = [0, 1]

    def setPosition(self, pos):
        self.pos = pos

    def setDegrees(self, degrees):
        radians = (degrees/180) * math.pi 
        self.direction = [math.sin(radians), -math.cos(radians)]

    def bounce(self, pos):
        reflection = self.canvas.getReflection(pos)
        self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

    def forward(self, distance):
        for i in range(distance):
            pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            if self.canvas.hitsWall(pos):
                self.bounce(pos)
                pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, colored(self.trail, self.trailColour))
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, self.markColour))
        #print(self.pos)
        self.canvas.print()
        time.sleep(self.framerate)
    
class DirectionScribe(Scribe):
    def __init__(self, canvas, framerate=0.05, startPosition=[0,0], trailColour='white', markColour='red'):
        super().__init__(canvas, framerate, startPosition, trailColour, markColour)
    
    def up(self):
        self.direction = [0, -1]
        self.forward(1)

    def down(self):
        self.direction = [0, 1]
        self.forward(1)

    def right(self):
        self.direction = [1, 0]
        self.forward(1)

    def left(self):
        self.direction = [-1, 0]
        self.forward(1)
    
    def drawSquare(self, size):
        for i in range(size):
            self.right()
        for i in range(size):
            self.down()
        for i in range(size):
            self.left()
        for i in range(size):
            self.up()


class GraphScribe(Scribe):
    def __init__(self, canvas, function, framerate=0.05, startPosition=[0,0], trailColour='white', markColour='red'):
        super().__init__(canvas, framerate, startPosition, trailColour, markColour)
        self.graphFunction = function
    
    def plotX(self):
        for x in range(self.canvas._x):
            pos = [x, self.graphFunction(x)]
            if pos[1] and not self.canvas.hitsWall(pos):
                self.draw(pos)


def sine(x):
    return 5*math.sin(x/4) + 15

def cosine(x):
    return 5*math.cos(x/4) + 15

def circleTop(x):
    radius = 10
    center = 20
    if x > center - radius and x < center + radius:
        return center-math.sqrt(radius**2 - (x-center)**2)

def circleBottom(x):
    radius = 10
    center = 20
    if x > center - radius and x < center + radius:
        return center+math.sqrt(radius**2 - (x-center)**2)


canvas = Canvas(30, 30)

squareScribe = DirectionScribe(canvas)
squareScribe.drawSquare(15)

sineScribe = GraphScribe(canvas, sine, trailColour='light_blue', markColour='green', framerate=0.01)
sineScribe.plotX()

cosineScribe = GraphScribe(canvas, cosine, trailColour='light_magenta', markColour='light_yellow', framerate=0.02)
cosineScribe.plotX()

topCircleScribe = GraphScribe(canvas, circleTop, markColour='cyan', framerate=0.03)
topCircleScribe.plotX()

bottomCircleScribe = GraphScribe(canvas, circleBottom, trailColour='light_red', framerate=0.04)
bottomCircleScribe.plotX()


# ORIGINAL CLASS WITH NO SUBCLASSES AND INHERITANCE

# class TerminalScribe:
#     def __init__(self, canvas):
#         self.canvas = canvas
#         self.trail = '.'
#         self.mark = '*'
#         self.framerate = 0.05
#         self.pos = [0, 0]

#         self.direction = [0, 1]

#     def setPosition(self, pos):
#         self.pos = pos

#     def setDegrees(self, degrees):
#         radians = (degrees/180) * math.pi 
#         self.direction = [math.sin(radians), -math.cos(radians)]

#     def up(self):
#         self.direction = [0, -1]
#         self.forward(1)

#     def down(self):
#         self.direction = [0, 1]
#         self.forward(1)

#     def right(self):
#         self.direction = [1, 0]
#         self.forward(1)

#     def left(self):
#         self.direction = [-1, 0]
#         self.forward(1)

#     def bounce(self, pos):
#         reflection = self.canvas.getReflection(pos)
#         self.direction = [self.direction[0] * reflection[0], self.direction[1] * reflection[1]]

#     def forward(self, distance):
#         for i in range(distance):
#             pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
#             if self.canvas.hitsWall(pos):
#                 self.bounce(pos)
#                 pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
#             self.draw(pos)

#     def plotX(self, function):
#         for x in range(self.canvas._x):
#             pos = [x, function(x)]
#             if pos[1] and not self.canvas.hitsWall(pos):
#                 self.draw(pos)

#     def drawSquare(self, size):
#         for i in range(size):
#             self.right()
#         for i in range(size):
#             self.down()
#         for i in range(size):
#             self.left()
#         for i in range(size):
#             self.up()

#     def draw(self, pos):
#         self.canvas.setPos(self.pos, self.trail)
#         self.pos = pos
#         self.canvas.setPos(self.pos, colored(self.mark, 'red'))
#         #print(self.pos)
#         self.canvas.print()
#         time.sleep(self.framerate)

