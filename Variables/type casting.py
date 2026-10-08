# Type casting is the process of converting a data value from one type to another (e.g., integer to float, string to integer) to ensure compatibility in expressions

print()


# start
name = "floore"
age = 21
CGPA = 3.21
student = True

type(name)
print(type(name)) #type(name) put inside print()
print(type(age))
print(type(CGPA))
print(type(student))

print()
# converting one to another

print(int(age))
print(int(CGPA))
print(float(age))

# end 

print()



# start

foods = "apple, orange, mango"
numbers= 87
flootnumbers = 12.34
complex_number= 5j #only j for complex number in python
list_number = ["list", "to", "tuple"]
tuple_number = ("tuple", "to", "list" )

print(type(foods))
print(type(numbers))
print(type(flootnumbers))
print(type(complex_number))
print(type(list_number))
print(type(tuple_number))


print()

# convering one type to another

numbers = float(numbers)
print(f"{numbers} (int to float)")

flootnumbers = int(flootnumbers) #float number name ekta variable nilam tarpor oi varaibae ke float to int a convert korlam then print korlam
print(f"{flootnumbers} (float to int)")

complex_number = str(complex_number)
print(f"{complex_number} (compx to int, can't conver in int and float)")

list_number = tuple(list_number)
print(f"{list_number} list to tuple")

tuple_number = list(tuple_number)
print(f"{tuple_number} tuple to list")

foods = list(foods)
print(f"{foods} str to list")

foods = tuple(foods)
print(f"{foods} str to tuple")


# end










print()