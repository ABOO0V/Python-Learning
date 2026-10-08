
# this is a program to calculate the area of a circle using class


print()
print("Area of a circle using class")
print()

import math

# pi * r^2

class Circle:
  def __init__ (self, radius):
    self.radius = radius

  def get_radius(self):
    area = math.pi * self.radius * self.radius

    return area

R = float(input("Enter the radius: "))
C = Circle(R)

print("Your circle radius is = ", C.get_radius())