from graphics import *


class Base(object):
    """Define Base grid and other variables."""

    BUFFER_SIZE = 20
    windowsize = 600
    squares = 3
    boxsize = windowsize / squares

    def __init__(self):
        self.TCP_IP = None
        self.TCP_PORT = None
        self.matrix = [None] * 9

    def getcenter(self, blockid):
        x = self.windowsize / 6 + (self.windowsize / 3) * (blockid % 3)
        y = self.windowsize / 6 + (self.windowsize / 3) * (blockid / 3)
        return Point(x, y)

    def draw(self):
        size = self.windowsize
        sq = self.squares
        win = GraphWin("Tic Tac Toe", size, size + 100)
        for i in range(sq - 1):
            p1 = Point(0, (size / sq) * (i + 1))
            p2 = Point(size, (size / sq) * (i + 1))
            hline = Line(p1, p2)
            hline.draw(win)
            p3 = Point((size / sq) * (i + 1), 0)
            p4 = Point((size / sq) * (i + 1), size)
            vline = Line(p3, p4)
            vline.draw(win)
        i += 1
        p1 = Point(0, (size / sq) * (i + 1))
        p2 = Point(size, (size / sq) * (i + 1))
        hline = Line(p1, p2)
        hline.draw(win)
        return win

    def draw_x(self, blockid):
        """Cross out."""
        deltax = self.windowsize / 20
        deltay = self.windowsize / 20
        x1 = (blockid % 3) * self.windowsize / 3
        y1 = (blockid / 3) * self.windowsize / 3
        x2 = x1 + self.windowsize / 3
        y2 = y1 + self.windowsize / 3
        line = Line(Point(x1 + deltax, y1 + deltay), Point(x2 - deltax, y2 - deltay))
        line.setFill('red')
        line.setWidth(5)
        line.draw(self.win)

        x3 = x1
        y3 = y1 + self.windowsize / 3
        x4 = x1 + self.windowsize / 3
        y4 = y1
        line = Line(Point(x3 + deltax, y3 - deltay), Point(x4 - deltax, y4 + deltay))
        line.setFill('red')
        line.setWidth(5)
        line.draw(self.win)

    def draw_o(self, center):
        """Circle."""
        outline_width = 5
        circle = Circle(center, self.boxsize / 3)
        circle.setOutline('blue')
        circle.setWidth(outline_width)
        circle.draw(self.win)

    def findblock(self, px, py):
        row = None
        col = None
        if px > 0 and px < self.windowsize / 3:
            col = 1
        elif px > self.windowsize / 3 and px < (self.windowsize / 3) * 2:
            col = 2
        elif px > (self.windowsize / 3) * 2 and px < self.windowsize:
            col = 3
        if py > 0 and py < self.windowsize / 3:
            row = 1
        elif py > self.windowsize / 3 and py < (self.windowsize / 3) * 2:
            row = 2
        elif py > (self.windowsize / 3) * 2 and py < self.windowsize:
            row = 3
        if row is None or col is None:
            return -1
        return (row - 1) * 3 + col - 1

    def display(self):
        for i in xrange(3):
            print self.matrix[3 * i: 3 * i + 3]

    def check(self, symbol):
        for i in xrange(3):
            if self.matrix[3 * i] is symbol and self.matrix[3 * i + 1] is symbol and self.matrix[3 * i + 2] is symbol:
                return (3 * i, 3 * i + 2), True
            if self.matrix[i] is symbol and self.matrix[i + 3] is symbol and self.matrix[i + 6] is symbol:
                return (i, i + 6), True
        if self.matrix[0] is symbol and self.matrix[4] is symbol and self.matrix[8] is symbol:
            return (0, 8), True
        if self.matrix[2] is symbol and self.matrix[4] is symbol and self.matrix[6] is symbol:
            return (2, 6), True
        return None, False

    def checkForDraw(self):
        if not self.check('O')[1] and not self.check('X')[1]:
            if None in self.matrix:
                return False
            else:
                return True
        return False
