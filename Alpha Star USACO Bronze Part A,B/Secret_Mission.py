#First Try!
name = input()
code = input()
name_num = 0
code_num = 0
for a in range(len(name)):
    name_num = name_num + ord(name[a]) - 64
for b in range(len(code)):
    code_num = code_num + ord(name[b]) - 64
if a == b:
    print("GO")
else:
    print("STAY")