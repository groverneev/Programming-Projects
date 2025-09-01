import csv
name = input("What is your name?")
person = input("Are you an adult, child, or teen?")
with open("/Users/neevgrover/Documents/Python Programs/Harvard Intro to Python/names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "person"])
    writer.writerow({"name": name, "person": person})