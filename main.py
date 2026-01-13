fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
for fruit in fruits:
    print(fruit)

user = input("What is your fav fruit?")

if user in fruits:
    print("Great choice!")
else:
    print("Nice, I haven't tried that one.")