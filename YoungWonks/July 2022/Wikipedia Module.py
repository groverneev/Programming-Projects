import wikipedia
a = input("What do you want to know about?")
b = int(input("How many sentences do you want?"))
c = input("What language do you want?")
wikipedia.set_lang(c)
print(wikipedia.summary(a, sentences = b))
