def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error : cannot divide by zero"
    return a/b

def calculator():
    print("=== CLI CALCULATOR ===")
    print("Operations - + - * /")
    print("Type 'quit' to exit/n")


while True:

    user_input = input("Enter expression (e.g 5 + 3) : ").strip()

    if user_input.lower == "quit":
        print("Goodbye!")
        break

    parts = user_input.split()

    if len(parts) != 3:
        print("Invalid format : Use - number operator number")
        continue

    num1_str, operator, num2_str = parts

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)

    except ValueError:
        print("Invalid numbers. Try again. \n")
        continue

    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)

    else:
        print("Unknown operator '{operator}'. Use +, -, *, /\n")
        continue
    
    print(f"Result: {num1} {operator} {num2} = {result}\n")

calculator()
   