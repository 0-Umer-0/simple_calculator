num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))

print("choose operation: +,-,*,/")
operation = input("enter your operation: ")

if operation == "+":
    result = num1 + num2
    print("result: ", result)
elif operation == "-":
    result = num1 - num2
    print("result", result)
elif operation == "*":
    result = num1 * num2
    print("result", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("result", result)
    else:
        print("ZeroDivisionError: Cannot divide by zero")
else:
    print("invalid operation")     