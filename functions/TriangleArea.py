

# calculate the area of a triangle given its base and height

def TriangleArea(Base, Height):
  Area = 0.5 * Base * Height
  return Area


Input_Base = float(input("Enter the base number: "))
Input_Height = float(input("Enter the Height number: "))

print("The Triangle Area is = ", TriangleArea(Input_Base, Input_Height))