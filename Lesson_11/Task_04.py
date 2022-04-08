# Реализовать проект «Операции с комплексными числами»


class ComplexNumber():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x = self.x+other.x
        self.y = self.y+other.y
        if self.y > 0:
            return f'{self.x} + {self.y}j'
        else:
            return f'{self.x} + ({self.y})j'
    def __sub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y
        if self.y > 0:
            return f'{self.x} + {self.y}j'
        else:
            return f'{self.x} + ({self.y})j'
    def __mul__(self, other):
        self.x = (self.x*other.x) - (self.y*other.y)
        self.y = (self.x*other.y) + (other.x*self.y)
        if self.y > 0:
            return f'{self.x} + {self.y}j'
        else:
            return f'{self.x} + ({self.y})j'
    def __str__(self):
        if self.y > 0:
            return self.x + self.y+'j'
        else:
            return f'{self.x} + ({self.y})j'
c1 = ComplexNumber(1,3)
c2 = ComplexNumber(2,1)
c3 = ComplexNumber(1,-2)
c4 = c1 + c2
c5 = c1 + c3
c6 = c1 - c2
c7 = c2 * c3
print(c4)
print(c5)
print(c6)
print(c7)