x = int(input("Enter a number "))
y = int(input("Enter a second number "))
operation = input("Enter an operation (+, -, *, /) ")
sum = 0

if (operation == "+"):
    sum = x + y
elif (operation == "-"):
    sum = x - y
elif (operation == "*"):
    sum = x * y
elif (operation == "/"):
    sum = x / y

print("The sum is " + str(sum)) 