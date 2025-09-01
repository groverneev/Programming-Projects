a, b = input().split()
num_card = int(a)
play = int(b)
cards = []
greatest = 0
index_ = 0
for a in range(num_card):
    cards.append(int(input()))
for a in range(play):
    greatest = 0
    index_ = 0
    for a in range(num_card):
        if cards[a] > greatest:
            greatest = cards[a]
            index_ = a
    print(index_ + 1)
    b = int(greatest/(num_card-1))
    c = greatest%(num_card-1)
    count = 0
    for z in range(num_card):
        if z != index_:
            cards[z] = cards[z] + b
            if count < c:
                cards[z] = cards[z] + 1
                count = count + 1
    cards[index_] = 0