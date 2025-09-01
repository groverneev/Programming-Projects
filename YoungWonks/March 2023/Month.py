a = input("What is your month (in 3 letters and lowercase)?")
myDictionary = {"jan" : 1, "feb" : 2, "mar" : 3, "apr" : 4, "may" : 5, "jun" : 6, "jul" : 7, "aug" : 8, "sep" : 9, "oct" : 10, "nov" : 11, "dec" : 12}
if a in myDictionary: print(myDictionary[a])
else: print("Please enter a valid month.")