import random

number = random.randint(1, 10)

for i in range(0,3):
    user = int(input("Enter your first guess:"))
    if user == number:
        print("Your guess is correct")
        break
if user!=number:
    print(f"The correct number was {number}")
