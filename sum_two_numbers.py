# Program to add two numbers

# store the numbers
number1 = input('First number: ')
number2 = input('Second number: ')

# Add the numbers
sum = float(number1) + float(number2)
sum = round(sum, 2) # round up the sum to two decimals

# Print result(sum) with specified format
print('The sum of {0} and {1} is {2}'
.format(number1, number2, sum))