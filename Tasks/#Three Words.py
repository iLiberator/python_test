#Three Words

test = "1 Hello 1 world hello"

def checkio(word):
    
    word = word.split()
    count = 0
    index = 0
    
    while index <= (len(word) - 1):
        if word[index].isalpha() == True:
            index += 1
            count += 1
            if count == 3:
                return True
        else:
            count = 0
            index += 1
    return False

print(checkio(test))

