# Program to check if an input is positive

number = input("Enter a number: ") # enter number

# Validation
try:
    # Runs if input is valid
    number = float(number)
    print("Hooray, you entered a number")

    if number >= 0:
        print("True")

    else:
        print("False")

except:
    # Runs if input is invalid
    print("User input is not a number. Please enter a number")
