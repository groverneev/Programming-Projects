name = input("What is your name?")
# The with is convenient because it allows you to not have to close the file.
with open("/Users/neevgrover/Documents/Python Programs/Harvard Intro to Python/names.txt", "a") as file:
    # The "a" stands for append which means that you add stuff to the file that you already have.
    # If you instead did "w", then it would erase the previous contents of the file and then add the new contents
    file.write(name)
    file.write("\n")