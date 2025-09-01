z = input().split()
num_cow = int(z[0])
num_ques = int(z[1])
time = []
question = []
final_cow = []
for y in range(num_cow):
    time.append(int(input()))
for y in range(num_ques):
    question.append(int(input()))
for x in range(len(time)):
    for q in range(time[x]):
        final_cow.append(x+1)
for y in range(len(question)):
    print(final_cow[question[y]])