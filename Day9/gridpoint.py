# from collections import Iterable
from cmath import sqrt


class GridPoint:  # (Iterable):
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    @property
    def coords(self):
        return self.x, self.y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise ValueError('only index 0 and 1 supported')

    def __iadd__(self, other):
        self.x += int(other[0])
        self.y += int(other[1])
        return self

    def __add__(self, other):
        return self.__class__(self.x + int(other[0]), self.y + int(other[1]))

    def __sub__(self, other):
        return self.__class__(self.x - int(other[0]), self.y - int(other[1]))

    def __mul__(self, other):
        other = int(other)
        return self.__class__(other * self.x, other * self.y)

    def __str__(self):
        return f'<GridPoint: ({self.x}, {self.y})>'

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter((self.x, self.y))
