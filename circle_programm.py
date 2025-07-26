import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi *self.radius * self.radius
    def perimeter(self):
        return 2*math.pi * self.radius
try:
    r= float(input("Enter the radius of the circle:"))
    c=Circle(r)
    print("Area of the circle is:",c.area())
    print("Perimeter of the cricle :",c.perimeter())
except ValueError:
        print("Invalid input")