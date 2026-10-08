

# example of encapsulation in python with bank account balance
print()


print("Encapsulation in Python")

print()


class BankAccount:
    def __init__(self):
        self.__Balance = 964  # Private attribute

    def Get_Balance(self):
        return self.__Balance  # Public method to access the private attribute


Bank_Account_Chack = BankAccount()
print("Your Bank Account Balance is:", Bank_Account_Chack.Get_Balance())  # Accessing the private attribute through the public method



print()