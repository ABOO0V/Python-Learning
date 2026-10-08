# Operators are used to perform operations on variables and values.

# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	Name	Example	
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

x = 2
y = 4


print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

# Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)


print()


# start
friends = 0

# friends = friends + 1

friends +=1 #augmented assignment
# friends -= 3 #augmented assignment
# friends *= 5 #augmented assignment
# friends /= 2 #augmented assignment

print(friends)
# end

print()

# start

A = 43.3
B= 53
C = 55

# result = round(x)
# result = abs(y)
# result = pow(3, 77)
result = max(A, B, C)
result = min(A, B, C)

print(result)

# end


print()


# start
import math

print(math.pi)
print(math.e)

Root = 64
print(math.sqrt(Root))

# end

print()

# start

radius = float(input("Enter the radius of a circle: "))
cir = 2 * math.pi * radius

