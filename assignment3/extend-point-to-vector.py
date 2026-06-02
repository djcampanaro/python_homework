import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f'Point ({self.x}, {self.y})'
    
    def euclidian_distance(self, other):
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f'Vector ({self.x}, {self.y})'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
point1 = Point(5, 6)
point2 = Point(7, 3)
vector1 = Vector(point1.x, point1.y)
vector2 = Vector(point2.x, point2.y)

print(point1)
print(vector2)
print(point1.euclidian_distance(point2))
print(vector1 + vector2)
