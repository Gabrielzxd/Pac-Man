import math

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.thresh = 0.0000001

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mult__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            return None
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __eq__(self, other) -> bool:
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitude_squared(self):
        return self.x**2 + self.y**2

    def distance_between_two_points(self, point):
        return (self.x - point.x) ** 2 + (self.y - point.y) ** 2

    def copy(self):
        return Vector(self.x, self.y)

    def as_tuple(self):
        return self.x, self.y

    def as_int(self):
        return int(self.x), int(self.y)

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"