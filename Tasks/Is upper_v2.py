def is_all_upper(text: str) -> bool:
    if text.isupper() or text == '':
        return True
    elif text.isdigit():
        return True
    else:
        for i in text:
            if i.isdigit() == True or i == ' ':
                return True
        return False

test = '5 5'

def def_test(text: str) -> bool:
    if text.isupper() or text == '' or text == ' ':
        return True
    elif text.isdigit():
        return True
    for i in text:
        if i.isalpha() and i.islower():
            return False
        elif i.isdigit() or i == ' ':
            return True

print(def_test(test))



#assert is_all_upper("ALL UPPER") == True
#assert is_all_upper("all lower") == False
#assert is_all_upper("mixed UPPER and lower") == False
#assert is_all_upper("") == True
#assert is_all_upper("444") == True
#assert is_all_upper("55 55 5 ") == True