# Guessing game Program
ourFavNumber = 25 # store the number to guess

userGuess = int(input("Guess the number: ")) # take the guessed input

# < == > >= <=

if userGuess == ourFavNumber:
    print('Hurray! you guessed the number! Our favourite is: ' 
        + str(ourFavNumber))

if userGuess < ourFavNumber:
    print('Oops! A low guess. Try something higher')

if userGuess > ourFavNumber:
    print('Oops! A high guess. Try something lower')

# try and except