import random

print("-------------------------------------------------")
passlen = int(input("\nEnter the lenght of the password: "))
print("\n-----------------------------------------------")

s = "qwertyuiopasdfghj@!#$%^&*()-+klzxbcnvm<>?'',[]{|}.:"

x = "".join(random.sample(s, passlen))
print("Your new password is:" +str(x))