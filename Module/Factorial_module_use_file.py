
import Factorial_module_create


user_1_factorial = Factorial_module_create.factorial(6)
#create a variable user_1_factorial and assign the value of factorial of 6 to it. we can use this variable in another python file.
print(f"The factorial of 6 is: {user_1_factorial}")
#now print the value of user_1_factorial variable. it will print the factorial of 6 which is 720.



print()

# now we take input from user for factorial

print("Give custom input for factorial calculation")
user_input = int(input("Enter a factorial number: "))

# we create a variable user_input and assign the value of input() function to it.

user_input_factorial_calculation = Factorial_module_create.factorial(user_input)

# create a variable user_input_factorial_calculation and assign the value of factorial of user_input to it.

print(f"The factorial of {user_input} is: {user_input_factorial_calculation}")


print()