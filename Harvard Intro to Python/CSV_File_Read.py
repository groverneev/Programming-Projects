#CSV files are useful so that you can have multiple things in one single line
people = []
with open("/Users/neevgrover/Documents/Python Programs/Harvard Intro to Python/names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        #The rstrip method removes the stuff at the end of the thing
        #The split method splits the csv file through the commas.
        people.append([row[0], "is a", row[1]])
for person in sorted(people):
    for i in range(len(person)):
        print(person[i], end = " ")
    print()