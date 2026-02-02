print("SIMPLE CALCULATOR")

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first num:  "))
num2 = float(input("Enter the second num:  "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero!"
else:
    result = "Invalid operator!"

print(f"Result: {result}")
