
# if = do some code only if some conditon is true
#  else do something else

print()

# start
age_verify = int(input("Enter your age: "))
if age_verify >= 18:
    print("You are elegible to open a bank account")

else:
    print("Your are not elegible to open a bank account")


# end

print()

# start
age_verify = int(input("Enter your age: "))

if age_verify >= 70:
    print("You are tooo old, you havent open a new account")
    
elif age_verify >= 18:
    print("You are elegible to open a bank account")
    
elif age_verify <0:
    print("You havent been born yet")

else:
    print("Your are not elegible to open a bank account")
    
# end 

print()

# start
response = input("Would you like food?(Y/N): ")
if response == "Y" :
    print("Have some food")

else :
    print("No food for you")
    
# end

print()


# start
online_offilne = True

if online_offilne:
    print("The user is online")

else:
    print("The user is offile")

# end

