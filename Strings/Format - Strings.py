# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this
# But we can combine strings and numbers by using f-strings or the format() method!


# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

# F-Strings

print("Using 'f-string' method")
age = 20
text = f"My name is johan and i am {age}"
print(text)

print()

print("Using 'format' method")
print(format(text))

print()


price = 59
txt = f"The price is {price} dollars"
print(txt)