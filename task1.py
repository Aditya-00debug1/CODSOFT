def calculator():
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print("Result:", result)
        elif operation == '-':
            result = num1 - num2
            print("Result:", result)
        elif operation == '*':
            result = num1 * num2
            print("Result:", result)
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print("Result:", result)
        else:
            print("Invalid operation selected.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


calculator()