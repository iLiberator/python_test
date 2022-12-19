def checkio(words: str) -> bool:
    words_list = words.split()
    
    index = 0
    str_count = 0
    while index < len(words_list):
        if type(int(words_list[index])) == True:
            str_count = 0
        else:
            str_count += 1
            if str_count == 3:
                return True
        index += 1
        return False 

#________________________________________________

def checkio_test(words: str) -> bool:
    words_list = words.split()
    
    if type(str()) == type(words_list[0]):
        end = True
    else:
        end = False
    return end


wordsss = "Hello hello hello"
#wordsss = wordsss.split()

print(checkio_test(wordsss))


#print(checkio(wordsss))


#assert checkio("Hello World hello") == True
#assert checkio("He is 123 man") == False
#assert checkio("1 2 3 4") == False
#assert checkio("bla bla bla bla") == True
#assert checkio("Hi") == False