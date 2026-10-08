
# 1.try 
# je code a error hoyer shombabona thake, sakhane try use kora hoy. jodi error hoy tahole except block e chole jabe.

# 2.except
# jodi try block e error hoy tahole except block e chole jabe. except block e error handle kora hoy.

# 3.try use holy except user korteii hobe. jodi try block e error na hoy tahole except block e chole jabe na.

# 4.else 
# jodi try block e kono error na hoy tahole else block e chole jabe. else block e kono error handle kora hoy na.

# 5.finally
# jodi try block e error hoy tahole finally block e chole jabe. jodi try block e kono error na hoy taholeo finally block e chole jabe. finally block e kono error handle kora hoy na.

# try
# except
# else
# finally
# raise
# assert



# standard example of try-except-else-finally in Python
print("standard example of try-except-else-finally in Python")

print()

#'This is try block'
try: #find out if user input is a valid integer or not
    number = int(input("Enter a number: "))

#'This is except block'

except ValueError: #execute if ValueError occurs in try block
    print("Invalid input! Please enter a valid integer.")

#'This is else block'
else: #execute if no exception in try block
    print(f"Your number is: {number}")

#'This is finally block'

finally: #always execute
    print("Execution completed.")




# example-1
try:
    a =  int(input("Enter a number (a): "))
    b =  int(input("Enter another number (b): "))
    result = a / b
    print(f"The result is: {result}")

except ValueError:
    print("Invalid input! Please enter valid integers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print(f"The division of {a} by {b} is: {result}")

finally:
    print("Execution completed.")