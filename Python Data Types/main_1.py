

# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:



# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType



# You can get the data type of any object by using the type() function



a = 5
print(type(a))

b = "type"
print(type(b))


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# Example	Data Type	
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType


c = 2
print(float(c))

d = 5
print(complex(d))

d1 = 2+5
print(complex(d1))

e = ["Hello-1", "Hello-2", "Hello-3"]
print(type(e))

f = ("Tuple-1", "Tuple-2", "Tuple-3")
print(type(f))

g = "Hello this is a range"
print(range(4))

h = {"Name:" : "Yeafi", "age" : "19"}
print(dict(h))
print(set(h))

i = {"Happy", "Sad", "life", "Dream", "Moment", "Money?"}
print(set(i))
