a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count


number = int(input())
words = []
for test in range(number):
    xx, yy = input().split()
    aray = []
    aray.append(xx)
    aray.append(yy)
    words.append(aray)
for counter in range(number):
    test = "a"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        a = a + count_letter(words[counter][0], test)
    else:
        a = a + count_letter(words[counter][1], test)
    test = "b"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        b = b + count_letter(words[counter][0], test)
    else:
        b = b + count_letter(words[counter][1], test)
    test = "c"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        c = c + count_letter(words[counter][0], test)
    else:
        c = c + count_letter(words[counter][1], test)
    test = "d"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        d = d + count_letter(words[counter][0], test)
    else:
        d = d + count_letter(words[counter][1], test)
    test = "e"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        e = e + count_letter(words[counter][0], test)
    else:
        e = e + count_letter(words[counter][1], test)
    test = "f"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        f = f + count_letter(words[counter][0], test)
    else:
        f = f + count_letter(words[counter][1], test)
    test = "g"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        g = g + count_letter(words[counter][0], test)
    else:
        g = g + count_letter(words[counter][1], test)

    test = "h"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        h = h + count_letter(words[counter][0], test)
    else:
        h = h + count_letter(words[counter][1], test)

    test = "i"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        i = i + count_letter(words[counter][0], test)
    else:
        i = i + count_letter(words[counter][1], test)

    test = "j"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        j = j + count_letter(words[counter][0], test)
    else:
        j = j + count_letter(words[counter][1], test)
    test = "k"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        k = k + count_letter(words[counter][0], test)
    else:
        k = k + count_letter(words[counter][1], test)

    test = "l"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        l = l + count_letter(words[counter][0], test)
    else:
        l = l + count_letter(words[counter][1], test)

    test = "m"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        m = m + count_letter(words[counter][0], test)
    else:
        m = m + count_letter(words[counter][1], test)

    test = "n"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        n = n + count_letter(words[counter][0], test)
    else:
        n = n + count_letter(words[counter][1], test)

    test = "o"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        o = o + count_letter(words[counter][0], test)
    else:
        o = o + count_letter(words[counter][1], test)

        
    test = "p"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        p = p + count_letter(words[counter][0], test)
    else:
        p = p + count_letter(words[counter][1], test)

    test = "q"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        q = q + count_letter(words[counter][0], test)
    else:
        q = q + count_letter(words[counter][1], test)

    test = "r"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        r = r + count_letter(words[counter][0], test)
    else:
        r = r + count_letter(words[counter][1], test)

    test = "s"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        s = s + count_letter(words[counter][0], test)
    else:
        s = s + count_letter(words[counter][1], test)

    test = "t"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        t = t + count_letter(words[counter][0], test)
    else:
        t = t + count_letter(words[counter][1], test)

    test = "u"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        u = u + count_letter(words[counter][0], test)
    else:
        u = u + count_letter(words[counter][1], test)

    test = "v"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        v = v + count_letter(words[counter][0], test)
    else:
        v = v + count_letter(words[counter][1], test)

    test = "w"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        w = w + count_letter(words[counter][0], test)
    else:
        w = w + count_letter(words[counter][1], test)

    test = "x"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        x = x + count_letter(words[counter][0], test)
    else:
        x = x + count_letter(words[counter][1], test)

    test = "y"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        y = y + count_letter(words[counter][0], test)
    else:
        y = y + count_letter(words[counter][1], test)

    test = "z"
    if count_letter(words[counter][0], test) >= count_letter(words[counter][1], test):
        z = z + count_letter(words[counter][0], test)
    else:
        z = z + count_letter(words[counter][1], test)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)
print(r)
print(s)
print(t)
print(u)
print(v)
print(w)
print(x)
print(y)
print(z)