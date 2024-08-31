#  print error while using try except.
try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /) ")
    num2 = float(input("Enter second number: "))
    # Using conditional statements to perform the operation
    if operator == '+':
        result = (num1 + num2)
    elif operator == '-':
        result = (num1- num2)
    elif operator == '*':
        result = (num1* num2)
    elif operator == '/':
        result = (num1/ num2)
    else:
        print("Invalid operator!")

    # Printing the result
    print(f"{num1} {operator} {num2} = {result:.2f}")
except Exception as e:
        print("An error occured:",e)
