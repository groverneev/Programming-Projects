import calendar
d = int(input("Enter a day."))
m = int(input("Enter a month."))
y = int(input("Enter a year."))
a = (calendar.weekday(y, m, d))
if a == 0:
    print("Monday")
elif a == 1:
    print("Tuesday")
elif a == 2:
    print("Wednesday")
elif a == 3:
    print("Thursday")
elif a == 4:
    print("Friday")
elif a == 5:
    print("Saturday")
elif a == 6:
    print("Sunday")
