import random
user = (input("Enter your move(S, P, R):"))
print("--------------------------------")
print("User move is >>>", (user))

print("--------------------------------")

x = random.choice('SPR'[0:2])
print("Computer move is >>>", (x))

print("--------------------------------")

if user == x:
    print("It is a draw!")
elif user == 'S':
    if x == 'P':
        print("User wins!")
    else:
        print("Computer wins!")

elif user == 'R':
    if x == 'P':
        print("Computer wins!")
    else:
        print("User wins!")
        
elif user == 'R':
    if x == 'S':
        print("User wins!")
    else:
        print("Computer wins!")



