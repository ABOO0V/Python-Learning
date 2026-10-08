

# example of inheritance in python
print()

print("Inheritance in Python")

print()

class Animal:
    def Eat(self):
        print("All Animal can eat.")



class Dog(Animal):  # Dog class inherits from Animal class
    def Bark(self):
        print("Dog can bark.")


Dog_Animal = Dog()

Dog_Animal.Eat()  # Calling the inherited method from Animal class

Dog_Animal.Bark()  # Calling the method from Dog class



print()