def is_all_upper(text: str) -> bool:
    if text.isupper() == True or text == '' or text.isdigit() == True:
        return True
    
    else:
        for i in text:
            if i.isdigit() != True or i != ' ':
                return False

print(is_all_upper('4 4'))

#assert is_all_upper("ALL UPPER") == True
#assert is_all_upper("all lower") == False
#assert is_all_upper("mixed UPPER and lower") == False
#assert is_all_upper("") == True
#assert is_all_upper("444") == True
#assert is_all_upper("55 55 5 ") == True