#Vector
#Vector.py
#From the Pygame Wiki
#11/9/2014

import math

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("This "+str(key)+" key is not a vector key!")

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y)

    def length(self):
        return math.sqrt((self.x**2 + self.y**2))

    def normalize(self):
        length = self.length()
        if length != 0:
            return (self.x / length, self.y / length)
        return None
