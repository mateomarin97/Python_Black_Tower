from math import hypot
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        #We denfine our vector to bew false if its length is zero.
        #return bool(abs(self))
        
        #A faster way to check if the vector is zero-length
        return bool(self.x or self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
A = Vector(3, 4)
B = Vector(5, 12)
C = A + B
D = A * 3
Z = A * 0
print(f"A: {A}, B: {B}, C: {C}, D: {D}, Z: {Z}, bool(Z): {bool(Z)}, abs(A): {abs(A)}, abs(B): {abs(B)}")