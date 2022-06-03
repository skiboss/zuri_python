# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    result = sorted(word) == sorted(anagram)
    print(result)
        
    return result

find_anagram("hey there", "eey hethr")

