num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

action = input("Please enter the action (+, -, *, /): ")

if action == '+':
    result = num1 + num2
elif action == '-':
    result = num1 - num2
elif action == '*':
    result = num1 * num2
elif action == '/':
    if num2 == 0:
        print("You can't divide by 0")
    else:
        result = num1 / num2
else:
    print("Invalid action. Please enter one of the following: +, -, *, /")

print("Your result is", result)