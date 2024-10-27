# https://quera.org/problemset/239083

import math

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_angle(self):
        is_in_domain = True if self.x >= 0 else False
        angle = math.atan(self.y / self.x)
        if not is_in_domain:
            angle += 180
        return angle

class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.i = Coords(x1, y1)
        self.f = Coords(x2, y2)

        if self.i.get_angle() >= self.f.get_angle:
            self.i, self.f = self.f, self.i

    def __and__(self, other):
        p = self.i.get_angle() <= other.i.get_angle() and self.f.get_angle() >= other.i.get_angle()
        q = self.i.get_angle() <= other.f.get_angle() and self.f.get_angle() >= other.f.get_angle()
        
        return True if p or q else False



inputCount = int(input())

targets = []

for i in range(inputCount):
    target = [int(i) for i in input().split()]
    targets.append(target)

targets = [Line(*target) for target in targets]
    

# Arctangent only works on the first area of coordinate plane!
# Must find the area related to the spot and calculate the currect angle.