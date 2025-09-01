name = input("What is your name?")
month = input("What month is your birthday? (Use Numbers)")
day = input("What day is your birthday?")
city = input("Enter the city you were born in.")
name = name.upper()
city = city.lower()
final = ""
list(name)
if len(name) <= 4:
    final = final + str(name)
else:
    name = name[0:4]
    final = final + str(name)
final = final + month
final = final + day
list(city)
if len(city) <= 4:
    final = final + str(city)
else:
    city = city[0:4]
    final = final + str(city)
print("Here is your confedential password:", final)