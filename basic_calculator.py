# Program to make a simple CLI calculator

# Addition function
def add(a, b):
    return a + b

# Subtraction function
def subtract(a, b):
    return a - b

# Multiplication function
def multiply(a, b):
    return a * b

# Division function
def divide(a, b):
    return a / b

# Modulus function
def modulus(a, b):
    return a % b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        if choice == '1':
            print(number1, '+', number2, "=", add(number1, number2))

        elif choice == '2':
            print(number1, '-', number2, "=", subtract(number1, number2))

        elif choice == '3':
            print(number1, '*', number2, "=", multiply(number1, number2))

        elif choice == '4':
            print(number1, '/', number2, "=", divide(number1, number2))

        elif choice == '5':
            print(number1, '%', number2, "=", modulus(number1, number2))

        another_calculation = input("Do you still want to calculate? (yes/no): ")
        if another_calculation == 'no':
            break

    else:
        print("Invalid Input!")