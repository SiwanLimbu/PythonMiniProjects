first = input("Enter the first number:")
operator = input("Enter Operator (+, -, *, /):")
second = input("Enter the second number:")

first = int(first)
second = int(second)

if operator == '+' :
    print("The result is :" + str(first + second))
elif operator == '-':
    print ("The result is: "+ str(first - second))
elif operator == '*':
    print("The result is: " + str(first * second))
elif operator == '/':
    print("The result is: " + str(first / second))

else:
    print("invalid operation")