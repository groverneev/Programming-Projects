import sys
number = int(input("What is your number?"))
if number == 0:
    sys.exit()
number_sum = number
mean = number
mean_counter = 1
largest_num = number
smallest_num = number
while number != 0:
    number = int(input("What is your next number?"))
    number_sum = number_sum + number
    mean = mean + number
    mean_counter = mean_counter + 1
    if number > largest_num:
        largest_num = number
    if number < smallest_num:
        smallest_num = number
print("Here is the sum of your numbers:", number_sum)
print("Here is the largest number you entered:", largest_num)
print("Here is the smallest number you entered:", smallest_num)
final_mean = mean/mean_counter
print("Here is the mean of your values:", final_mean)
