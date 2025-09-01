num_people = int(input())
people = []
for a in range(num_people):
    people.append(int(input()))
final = 9999999999999999999999999999999999999999999
counter = 0
for a in range(num_people):
    for b in range(num_people):
        counter = counter + (people[b]*b)
    if counter < final:
        final = counter
    counter = 0
    d = people[0]
    del people[0]
    people.append(d)
print(final)