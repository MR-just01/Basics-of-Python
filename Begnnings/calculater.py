operator = input("Enter the operator ('+', '-', '/', '*'): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "/":
    if num2 != 0:  # Prevent division by zero
        result = num1 / num2
        print(round(result))
    else:
        print("Error: Division by zero is not allowed!")
elif operator == "*":
    result = num1 * num2
    print(round(result))
else:
    print(f"'{operator}' is an invalid operator! Please enter a valid operator.")
 
