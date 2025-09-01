counter = 0
first_name = ['black', 'black', 'captain', 'doctor', 'drax', 'falcon', 'gamora', 'groot', 'hulk', 'iron', 'loki', 'mantis', 'nebula', 'rocket', 'scarlet', 'spider', 'star', 'thanos', 'thor', 'vision', 'war', 'winter']
last_name = ['soldier', 'machine', 'vision', 'thor', 'thanos', 'lord', 'man', 'witch', 'rocket', 'nebula', 'mantis', 'loki', 'man', 'hulk', 'groot', 'gamora', 'falcon', 'drax', 'strange', 'america', 'widow', 'panther']
for a in range(len(first_name)):
    for b in range(len(last_name)):
        c = first_name[a]
        d = last_name[b]
        if a == b:
            counter = counter + 1
        print(c, d)
print("I got", counter, "names right.")
