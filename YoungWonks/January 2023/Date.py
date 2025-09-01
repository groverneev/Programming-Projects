dateStr = input("Enter the date in numerical form seperated by a space.")
Month, Day, Year = dateStr.split(" ")
z =[Month, Day, Year]
a = "/".join(z)
print(a)