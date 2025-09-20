# Calculator (Using match-case)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Enter choice (1/2/3/4/5): ")

if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error! Division by zero.")
        case '5':
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
else:
    print("Invalid input. Please select a valid operation.")