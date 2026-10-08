
# Take two number from user and add, sub, multiply, and divid

# import number from user
# Start

# Md.Arafat bhuiyan, Roll-909, CST-2nd

User_input_1st_Number = input("Enter you first number: ")
User_input_2st_Number = input("Enter you secound number: ")


# string to integer
User_input_1st_Number = int(User_input_1st_Number)
User_input_2st_Number = int(User_input_2st_Number)

# add two numbers 
Sum_User_input_Number = User_input_1st_Number + User_input_2st_Number
# print the sum
print("The first number is", User_input_1st_Number, "and secound number is ",  User_input_2st_Number,",", "The total sum is ", Sum_User_input_Number)

# Print sub
Sub_User_input_Number = User_input_1st_Number - User_input_2st_Number
print("The first number is", User_input_1st_Number, "and secound number is ",  User_input_2st_Number,",", "The total sub is ", Sub_User_input_Number)

# Print multiply
Multiply_User_input_Number = User_input_1st_Number * User_input_2st_Number
print("The first number is", User_input_1st_Number, "and secound number is ",  User_input_2st_Number,",", "The total sum is ", Multiply_User_input_Number)

# print divide
Divide_User_input_Number = User_input_1st_Number / User_input_2st_Number
print("The first number is", User_input_1st_Number, "and secound number is ",  User_input_2st_Number,",", "The total sum is ", Divide_User_input_Number)

# End

print()


# start
print("Farenhite to Centigrade:")
F = float(input("Enter you Farenhite:"))
C = ((F - 32)*5)/9
print("Centigrade is :", C)
# end


print()


# start 
print("Centigrade to farenhite")
C1 = float(input("Enter Centigrade:"))
F1 = (C1 * 1.8)+32
print("Farenheit is :", F1) 
# end 

print()

# start

first_name = "Ali Hassan"
print(f"Your name is {first_name}")

secound_name = "Hassan"
print(f"Your secound name is {secound_name}")

age = 20
print(f"You age is {age}")

email = "abc@fake email.com"
print(f"Your email is {email}")

print(f"In total information about you is, Your name {first_name}, your age {age}. and your email is {email}")

# end

print()


# start

name = input("What's your name?: ")
age = input("What's your age?: ")

print(f"So, Your name is '{name}', and you are '{age}' old")

# end

print()

# start
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width
print(f"The area is: {area} cm²/inch²/m²") #numlock alt 0178

# end

print()


# start
# shopping cart program
shopping_item = input("What item you want to buy?: ")
item_price = float(input("What price range you want to buy?: "))
item_quantity = int(input("How many item you want to buy?: "))

total_item_price = item_price * item_quantity

print(f"You want to buy {item_quantity} x {shopping_item} and you total cost is: '${total_item_price}'")

# end

print()


 