import Area_Function
a = input("Do you want to find the area of a rectangle, triangle, or circle?")
if a == "r":
    Area_Function.rectangle(int(input("What is your length?")), int(input("What is your width?")))
elif a == "t":
    Area_Function.triangle(int(input("What is the length of your base?")), int(input("What is your height?")))
else:
    Area_Function.circle(int(input("What is the radius of your circle?")))
