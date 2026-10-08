

# calculate factorial of a number using function

print()
print("Factorial of a number using function")

print()
# start

def Factorial(Number):
  result = 1
  for i in range(1, Number+1):
    result = result * i

  return result

Input_Number = int(input("Enter the factorial number: "))
print("Your", Input_Number, "number factorial is = ", Factorial(Input_Number))

# end

print()