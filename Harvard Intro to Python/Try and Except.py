#Code starts with the try, if try returns an error then it goes to except
#If try does not return an error, it goes to else.
try:
    x = int(input("Enter a number."))
except:
    print("Please enter a valid number.")
    #If the user does not enter a valid number, then x remains undefined so print(x) would not work
else:
    print(x)