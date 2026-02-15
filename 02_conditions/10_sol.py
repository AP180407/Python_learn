# import string

animal = input("Enter your animal's species Dog or cat: ")
age = int(input("Enter your animal's age: "))

if animal == "Dog": 
    if age < 2:
        print("consider Puppy food ")

    

elif animal == "Cat":
    if age > 5:
        print("consider Senior cat food ")