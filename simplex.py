import math

class Point(object):

    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def __eq__(self, other):

        return ((self.X == other.X) and (self.Y == other.Y) and (self.Z == other.Z))

    def __str__(self):
        return '(' + str(self.X) + ', ' + str(self.Y) + ', ' + str(self.Z) + ')'

    def to(self, other):
        return Vector(other.X - self.X, other.Y - self.Y, other.Z - self.Z)


class Line(object):

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def __str__(self):
        return '['+str(self.A)+' ==> '+str(self.B)+']'

    def direction(self):
        return (self.A.to(self.B)).unit()

    def inrange(self, z0):
        if (self.A.Z < z0 and z0 <= self.B.Z) or (self.B.Z < z0 and z0 < self.A.Z):
            return True
        else:
            return False

    def lp_int(self, z0):
        if (self.A.Z < z0 and z0 < self.B.Z) or (self.B.Z <= z0 and z0 < self.A.Z):
            t = (z0 - self.A.Z) / (self.B.Z - self.A.Z)
            return Point(self.A.X + t * (self.B.X - self.A.X), self.A.Y + t * (self.B.Y - self.A.Y), z0)


class Triangle(object):

    def __init__(self, p1, p2, p3):

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):

        return '[' + str(self.p1) + ', ' + str(self.p2) + ', ' + str(self.p3) + ']'

    def inrange(self, z0):

        if self.min() < z0 and z0 < self.max():

            return True

        else:

            return False

    def min(self):

        return min(self.p1.Z, self.p2.Z, self.p3.Z)

    def max(self):

        return max(self.p1.Z, self.p2.Z, self.p3.Z)

    def tp_int(self, z0):

        q1 = Point(0,0,0)
        L12 = Line(self.p1, self.p2)
        L23 = Line(self.p2, self.p3)
        L31 = Line(self.p3, self.p1)

        if type(q1) == type(L12.lp_int(z0)) and type(q1) == type(L23.lp_int(z0)):
            return Line(L12.lp_int(z0), L23.lp_int(z0))

        if type(q1) == type(L23.lp_int(z0)) and type(q1) == type(L31.lp_int(z0)):
            return Line(L23.lp_int(z0), L31.lp_int(z0))

        if type(q1) == type(L31.lp_int(z0)) and type(q1) == type(L12.lp_int(z0)):
            return Line(L31.lp_int(z0), L12.lp_int(z0))


class Vector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == type(self):

            return self.x * other.x + self.y * other.y + self.z * other.z

        else:
            return Vector(other * self.x, other * self.y, other * self.z)

    def __xor__(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __pos__(self):
        return self

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def __eq__(self, other):

        return ((self.x == other.x) and (self.y == other.y) and (self.z == other.z))

    def __str__(self):

        return ('(' + str(self.x) + ' ,' + str(self.y) + ' ' + str(self.z) + ')')

    def unit(self):

        l = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return Vector(self.x / l, self.y / l, self.z / l)

