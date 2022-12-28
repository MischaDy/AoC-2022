from typing import List

from misc.point2d import Point2D


class Rock:
    """
    Represents a rock object, stored as list of points. Bottom left is (0,0).
    """
    def __init__(self, parts: List[Point2D] = None, pos=None, right_lim=None):
        if parts is None:
            parts = []
        if pos is None:
            pos = Point2D.get_origin()
        self.parts = parts
        self.pos = pos
        self.right_lim = right_lim
        self.has_landed = False

    @property
    def x(self):
        return self.pos.x

    @x.setter
    def x(self, new_x):
        self.pos.x = new_x

    @property
    def y(self):
        return self.pos.y

    @y.setter
    def y(self, new_y):
        self.pos.y = new_y

    @classmethod
    def from_shape(cls, rock_str_list, right_lim=None):
        parts = [
            Point2D(x, y)
            for y, row in enumerate(rock_str_list)
            for x, char in enumerate(row)
            if char == '#'
        ]
        return cls(parts, right_lim)

    def __iter__(self):
        return iter(self.parts)

    def fall(self, environment):
        if self.y <= 0:
            self.has_landed = True
            return
        for part in self.parts:
            if part.get_point_below() in environment:
                self.has_landed = True

    def move(self, dir_, environment, right_lim):
        delta_x = +1 if dir_ == '>' else -1
        if self.x:
            pass
