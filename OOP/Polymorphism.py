
print()

print("Polymorphism in Python")

print()

class cat:
    def Sound(self):
        print("Cat can meow.")



class dog:
    def Sound(self):
        print("Dog can bark.")



class bird:
    def Sound(self):
        print("Bird can chirp.")

Cat = cat()
Dog = dog()
Bird = bird()

Cat.Sound()  # Calling the method from cat class
Dog.Sound()  # Calling the method from dog class
Bird.Sound()  # Calling the method from bird class


print()