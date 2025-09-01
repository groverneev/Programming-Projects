my_list = ["a", "c", "b", "z", "k"]
my_list.sort()
print(my_list)
duplicate = []
counter = 0
for a in range(4, -1, -1):
    duplicate.append(my_list[a])
print(duplicate)
#my_list = my_list[::-1]
#This is another method to reverse the list
