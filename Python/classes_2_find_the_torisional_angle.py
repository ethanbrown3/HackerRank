# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        '''
        subtraction operation
        '''
        return Points(self.x-no.x, self.y-no.y, self.z-no.z)

    def dot(self, no):
        '''
        dot product operation
        '''
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        '''
        cross product operation
        '''
        a = [self.x, self.y, self.z]
        b = [no.x, no.y, no.z]
        return Points(a[1]*b[2] - a[2]*b[1],
                      a[2]*b[0] - a[0]*b[2],
                      a[0]*b[1] - a[1]*b[0])

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = map(float, raw_input().split())
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print "%.2f" % math.degrees(angle)