


# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods



a = 50 #int
b = 38 # float
c = 6+7 #Complex

print(int(a))
print(float(b))
print(complex(c))


print()
print("Type conversion")
print()


x = float(a) #int to float
y = complex(b) #float to complex
z = int(c) #complex to int

print(x), print("int to float")
print()
print(y), print("float to complex")
print()
print(z), print("complxe to int")



print()

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers

print("Random number")
import random
print(random.randrange(1,10))