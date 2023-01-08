class Point2D:
    def __init__(self, *args):
        if len(args) == 1:
            x, y = args[0]
        else:
            x, y = args
        self.x = x
        self.y = y

    def __getitem__(self, item):
        return [self.x, self.y][item]

    @classmethod
    def get_origin(cls) -> "Point2D":
        return cls(0, 0)

    def get_point_below(self) -> "Point2D":
        cls = type(self)
        return cls(self.x, self.y-1)
