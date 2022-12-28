class Point3D:
    def __init__(self, *args):
        if len(args) == 1:
            x, y, z = args[0]
        else:
            x, y, z = args
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, item):
        return [self.x, self.y, self.z][item]

    @classmethod
    def get_origin(cls) -> "Point3D":
        return cls(0, 0, 0)

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def __repr__(self):
        return f'<{type(self)} object; x={self.x}, y={self.y}, z={self.z}>'
