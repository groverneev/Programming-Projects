students, num_resp, num_q = map(int, input().split())
responses = []
for f in range(students):
    test = input().split()
    for s in range(len(test)):
        test[s] = int(test[s])
    responses.append(test)
questions = []
correct_stu = []
for t in range(students):
    correct_stu.append(1)
for i in range(num_q):
    a, b = map(int, input().split())
    for student in range(students):
        if responses[student][a - 1] != b:
            correct_stu[student] = 0
final = 0
for a in range(len(correct_stu)):
    if correct_stu[a] == 1:
        final = final + 1
print(final)