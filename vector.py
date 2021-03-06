import math


class Vector:
    def __init__(self, vect):
        self.vect = vect  # vect should be an array OF LENGTH 2
        if len(vect) == 2:
            self.x = vect[0]
            self.y = vect[1]

    def __add__(self, other):
        if len(self) == len(other):
            return Vector([self[i] + other[i] for i in range(len(self))])
        else:
            return "invalid operation"

    def __sub__(self, other):
        if len(self) == len(other):
            return Vector([self[i] - other[i] for i in range(len(self))])
        else:
            return "invalid operation"

    def __mul__(self, scalar):
        return Vector([self[i] * scalar for i in range(len(self))])

    def __truediv__(self, scalar):
        return Vector([self[i] / scalar for i in range(len(self))])

    def __len__(self):
        return len(self.vect)

    def __getitem__(self, index):
        return self.vect[index]

    def __setitem__(self, key, value):
        self.vect[key] = value

    def __round__(self):
        return Vector([round(self[i]) for i in range(len(self))])

    def dist(self, other=(0, 0)):
        return math.sqrt((self[0] - other[0]) ** 2 + (self[1] - other[1]) ** 2)

    def vdist(self, other):
        return Vector((other.x - self.x, other.y - self.y))

    def norm(self):
        v = []
        for i in range(len(self)):
            v.append(self[i] / self.dist())
        return Vector(v)

    def flip(self):
        return Vector((self.y, self.x))
