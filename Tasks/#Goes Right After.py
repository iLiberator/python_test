#Goes Right After

def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word:
        return False
    elif word.index(first) > word.index(second):
        return False
    else:
        indx = 0
        while indx < len(word) - 1:
            if word[indx] == first:
                if word[indx + 1] == second:
                    return True
                else:
                    return False
            else:
                indx += 1
        return False


print(goes_after("pizarzdek", "z", "p"))

"""
#######v1

def goes_after(word: str, first: str, second: str) -> bool:
    for x in word:
        if x == first and word[word.index(x) + 1] == second:
            return True
        else:
            return False


#######v2

def goes_after(word: str, first: str, second: str) -> bool:
    if first not in word or second not in word:
        return False
    else:
        indx = 0
        while indx < len(word) - 1:
            if word[indx] == first and word[indx + 1] == second:
                return True
            else:
                indx += 1
        return False
"""



#assert goes_after("world", "w", "o") == True
#assert goes_after("world", "w", "r") == False
#assert goes_after("world", "l", "o") == False
#assert goes_after("panorama", "a", "n") == True
#assert goes_after("list", "l", "o") == False
#assert goes_after("", "l", "o") == False
#assert goes_after("list", "l", "l") == False
#assert goes_after("world", "d", "w") == False
#assert goes_after("Almaz", "a", "l") == False