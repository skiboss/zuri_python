# Program to get number of words in specified file

fname = input("What is your file name: ")

#initialize word count
words_number = 0

with open(fname, 'r') as f: #open specified file in read mode
    for line in f: #do this for every line in the file
        words = line.split() #split the words by white space
        words_number += len(words) #add the word count to the initial word value

print("Number of words: ")
print(words_number)