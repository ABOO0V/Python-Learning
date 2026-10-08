
# factorial ---> factorial is a mathematical function that multiplies a number by every number below it. For example, the factorial of 5 is 5*4*3*2*1 = 120. The factorial of 0 is 1.

# how to use factorial function in python?
# ---> we can use factorial function in python by importing math module. The math module provides a factorial() function that can be used to calculate the factorial of a number.

# import math
# factorial = math.factorial(5)
# print(f"The factorial of 5 is: {factorial}")

# but we want to create our own factorial function in python. so we can create a module for factorial function and use it in another python file.

def factorial(number):
    if number ==0 or number == 1:
        return 1
    
    else:
        return number * factorial(number-1)
    
# 0! = 1
# 1! = 1
# that's why we have to check if number is 0 or 1, then return 1. otherwise, we will return number * factorial(number-1) which is the recursive function for factorial.