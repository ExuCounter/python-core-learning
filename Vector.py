import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def eq(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return False

        new_vector = Vector(x=self.x + other.x, y=self.x + other.y, z=self.z + other.z)
        return new_vector

    def __radd__(self, other):
        if not isinstance(other, Vector):
            return False

        return self + other

    def __mul__(self, num):
        if not isinstance(num, int):
            return False

        new_vector = Vector(x=self.x * num, y=self.x * num, z=self.z * num)
        return new_vector

    def __rmul__(self, num):
        if not isinstance(num, int):
            return False

        return self + num

    def __bool__(self):
        return self.magnitude() > 0

    def __hash__(self):
        return hash(self.x, self.y, self.z)

    def __gt__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError

        return self.magnitude() > other.magnitude()

    def __getitem__(self, item):
        if isinstance(item, str):
            if item == "y" or "Y":
                return item.y
            if item == "x" or "X":
                return item.x
            if item == "z" or "Z":
                return item.z

        raise NotImplementedError
