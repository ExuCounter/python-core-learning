class Point3D:
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x},y={self.y},z={self.z})"


class ColoredPoint(Point3D):
    __slots__ = ('color')

    def __init__(self, x, y, z, color="black"):
        super().__init__(x, y, z)
        self.color = color


class ShapedPoint(Point3D):
    __slots__ = ('shape')

    def __init__(self, x, y, z, shape="sphere"):
        super().__init__(x, y, z)
        self.shape = shape


p = Point3D(5,5,5)
cp = ColoredPoint(5,5,5)
sp = ShapedPoint(5,5,5)
print(p)
print(cp)
print(sp)
sp.__setattr__('shape', 'square')
print(sp.__getattribute__('shape'))
