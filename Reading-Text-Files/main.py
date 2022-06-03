# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename,'r') as file:
        doc = file.read()
    
    return (doc)


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    
    words = text.split()
    dic = dict()
    for word in words:
        word_count = words.count(word)
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
        #result = {word:word_count}
    for key in list(dic.keys()):
        print(key, ":", dic[key])
        #print (result)

    return dic

count_words()